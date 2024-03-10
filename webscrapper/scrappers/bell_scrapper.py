import requests
import json

def scrape_website(url):
    # Function to scrape a website and return the JSON response
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Convert the response content to JSON
            json_data = response.json()
            return json_data
        else:
            print(f"Failed to fetch URL: {url}. Status code: {response.status_code}")
            return {"error": f"Failed to fetch URL: {url}. Status code: {response.status_code}"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": f"An error occurred: {e}"}

# Example usage
if __name__ == "__main__":
    # Replace 'example.com/api/data' with the URL that returns JSON
    scraped_data = scrape_website("https://ws1-bell.sbeglobalcare.com/gc-ws-connect-1.9/rest/gcWsConnect/findCatalogModels?session_id=8a331dc7-2cca-4cbe-8458-f04e48927e3c&category_code=TRADEIN&manufacturer_code=AP&cache=true")
    print(scraped_data)
