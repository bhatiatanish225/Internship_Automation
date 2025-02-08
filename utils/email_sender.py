import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import SMTP_SERVER, SMTP_PORT, EMAIL_SENDER, EMAIL_PASSWORD

def send_email(receiver_email, email_subject, email_content, resume_file=None):
    server = None  # Define server outside try block

    try:
        # Set up the SMTP server and login
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Encrypts the connection
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        # Create the email message
        message = MIMEMultipart()
        message["From"] = EMAIL_SENDER
        message["To"] = receiver_email
        message["Subject"] = email_subject  # Use the separate subject here
        message.attach(MIMEText(email_content, "plain"))

        # Attach the resume file if provided
        if resume_file:
            part = MIMEBase("application", "octet-stream")

            if isinstance(resume_file, str) and os.path.exists(resume_file):
                # If `resume_file` is a **file path**
                filename = os.path.basename(resume_file)
                with open(resume_file, "rb") as attachment:
                    file_data = attachment.read()
            elif hasattr(resume_file, "read"):  
                # If `resume_file` is a **Streamlit uploaded file**
                filename = resume_file.name
                file_data = resume_file.getvalue()  # Read bytes from UploadedFile
            else:
                print("⚠️ Invalid resume file format. Skipping attachment.")
                file_data = None

            # Attach file properly if file data is valid
            if file_data:
                part.set_payload(file_data)
                encoders.encode_base64(part)  # Encode in base64
                part.add_header(
                    "Content-Disposition", f'attachment; filename="{filename}"'
                )
                message.attach(part)

        # Send the email
        server.sendmail(EMAIL_SENDER, receiver_email, message.as_string())
        print(f"✅ Email sent successfully to {receiver_email}")
        return True

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed: Check email/password or enable 'App Password' in Gmail settings.")
    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {e}")
    except Exception as e:
        print(f"❌ General error sending email: {e}")

    finally:
        if server:
            server.quit()  # Ensure SMTP connection is always closed

    return False
