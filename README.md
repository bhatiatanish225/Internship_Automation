# Internship Application Automation

A powerful tool to automate the process of applying for internships. This project allows users to upload resumes and professor data (in CSV format), automatically scrape professor profiles, generate personalized internship application emails, and send them via SMTP or Gmail API.

## Features

- **CSV Upload**: Upload professor data (Name, Email, Profile URL) in CSV format.
- **Resume Upload**: Upload multiple resumes (PDF/DOCX).
- **Profile Scraping**: Automatically scrape professor profile data from provided URLs (research areas, projects, etc.).
- **Email Generation**: Use AI to generate personalized emails using resume details and professor profiles.
- **Email Sending**: Send the generated email to professors with an optional resume attachment.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.8 or higher
- `streamlit`: For building the UI
- `pandas`: For handling CSV data
- `google-generativeai`: For generating personalized emails
- `smtplib`: For sending emails via SMTP
- `PyPDF2` and `python-docx`: For parsing PDF and DOCX files

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/internship-application-automation.git
    cd internship-application-automation
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables for API keys and SMTP configuration:
    - Store your **GEMINI_API_KEY** (for Google Gemini) and **SMTP credentials** in a `config.py` file.

    Example `config.py`:
    ```python
    GEMINI_API_KEY = 'your-api-key'
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    EMAIL_SENDER = 'your-email@gmail.com'
    EMAIL_PASSWORD = 'your-app-password'
    ```

## Usage

1. Run the application:

    ```bash
    streamlit run app.py
    ```

2. The Streamlit app will open in your browser.

3. Upload the professor data CSV file, then upload one or more resumes (PDF or DOCX format).

4. Select the resume you want to send from the dropdown.

5. The professor's profile will be scraped, and a personalized email will be generated.

6. You can review the subject and body of the email, and click on "Send Email" to send it.

## Example CSV Format

Your CSV file should contain the following columns:

```csv
Professor Name,Email,Profile URL
Prof. Gupta,profgupta@example.com,http://professor-profile.com
Prof. Sharma,profsharma@example.com,http://profsharma-profile.com
