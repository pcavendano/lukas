import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    # Function to scrape a website and extract relevant information
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the website
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract relevant information from the HTML
            # Example: Scraping the titles of all <h1> tags
            # Return the scraped data in JSON format
            return json.dumps({"devices": devices})
        else:
            print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
            return json.dumps({"error": f"Failed to fetch URL: {url}. Status code: {response.status_code}"})
    except Exception as e:
        print(f"An error occurred: {e}")
        return json.dumps({"error": f"An error occurred: {e}"})

# Example usage
if __name__ == "__main__":
    # Replace 'example.com' with the URL you want to scrape
    scraped_data = scrape_website("https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/findCatalogModels?session_id=8a331dc7-2cca-4cbe-8458-f04e48927e3c&category_code=TRADEIN&manufacturer_code=AP&cache=true")
    print(scraped_data)
