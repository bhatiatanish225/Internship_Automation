import google.generativeai as genai
from config import GEMINI_API_KEY  # Store API key in config.py

# Set API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate email using Google Gemini
def generate_email(resume_details, profile_data):
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    You are an AI specializing in writing **high-impact internship application emails**. 
    Your goal is to **impress the professor** and get a response.

    #### **Instructions:**
    1. **Personalization:** Use the professor’s name, research areas, and projects to tailor the email.
    2. **Strong Opening:** Start with something unique that grabs attention.
    3. **Clear Value Proposition:** Show how the applicant's skills and projects align with the professor’s work.
    4. **Call-to-Action:** End with a compelling reason to respond.
    5. **Out-of-the-box Subject Line:** Make it **concise, creative, and intriguing.**
    
    #### **Applicant's Resume Details:**
    {resume_details}

    #### **Professor’s Profile Data:**
    {profile_data}

    ### **Expected Output:**
    - **Subject:** A unique, attention-grabbing subject line.
    - **Email Body:** A well-structured, engaging email.
    
    **Now, generate the email.**
    """

    response = model.generate_content(prompt)
    
    return response.text if response else "Failed to generate email."
