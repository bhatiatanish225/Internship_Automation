import streamlit as st
import pandas as pd
from scraper.scraper import scrape_profile
from email_generator.email_gen import generate_email
from utils.resume_parser import extract_resume_details
from utils.email_sender import send_email  # SMTP function

st.set_page_config(page_title="Internship Application Automation", layout="wide")

st.title("📩 Internship Application Automation")

# Upload CSV (Professor Data)
uploaded_csv = st.file_uploader("📂 Upload CSV (Professor Data)", type=['csv'])

# Upload Resumes (multiple files)
uploaded_resumes = st.file_uploader("📄 Upload Resumes (PDF/DOCX)", type=['pdf', 'docx'], accept_multiple_files=True)

if uploaded_csv and uploaded_resumes:
    # Read CSV with Professor info
    df = pd.read_csv(uploaded_csv)

    # Create a dictionary to store extracted resume details
    resume_details_dict = {}

    # Extract details from each uploaded resume
    for resume in uploaded_resumes:
        resume_details = extract_resume_details(resume)
        resume_details_dict[resume.name] = resume_details

    # Let the user select which resume to send
    selected_resume = st.selectbox("Select Resume to Send", list(resume_details_dict.keys()))

    # Get the selected resume details
    selected_resume_details = resume_details_dict[selected_resume]

    for index, row in df.iterrows():
        with st.expander(f"📌 {row['Professor Name']} - {row['Email']}"):
            # Scrape Professor's Profile Data
            profile_data = scrape_profile(row["Profile URL"])
            st.write(profile_data)

            # Generate Email Content based on profile match
            email_content = generate_email(selected_resume_details, profile_data)
            st.text_area("📧 Generated Email", email_content, height=200)

            # Email Sending Form
            with st.form(f"send_email_form_{index}"):
                submit_button = st.form_submit_button("✉️ Send Email")

                if submit_button:
                    # Get the selected resume file
                    selected_resume_file = next((resume for resume in uploaded_resumes if resume.name == selected_resume), None)

                    if selected_resume_file:
                        # Send email with attachment
                        success = send_email(row["Email"], "Internship Application", email_content, resume_file=selected_resume_file)
                    else:
                        success = send_email(row["Email"], "Internship Application", email_content)

                    if success:
                        st.success(f"✅ Email sent to {row['Email']}")
                    else:
                        st.error("❌ Failed to send email.")
