import requests
from bs4 import BeautifulSoup

def scrape_profile(url):
    try:
        # Bypass SSL certificate verification (for testing purposes)
        response = requests.get(url, verify=False)  # Disable SSL verification
        response.raise_for_status()  # Check if request was successful

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the professor's name (assuming it's in an <h1> tag)
        name = soup.find("h1").text if soup.find("h1") else "Unknown"
        
        # Extract the research interests (assuming they're in <li> tags with a class of "research-area")
        research_interests = [tag.text for tag in soup.find_all("li", class_="research-area")]
        
        # Extract the projects (assuming they're in <p> tags with a class of "project-description")
        projects = [p.text for p in soup.find_all("p", class_="project-description")]

        # Return extracted information as a dictionary
        return {
            "name": name,
            "research_interests": research_interests,
            "projects": projects
        }

    except requests.exceptions.RequestException as e:
        print(f"Error while scraping {url}: {e}")
        return None
