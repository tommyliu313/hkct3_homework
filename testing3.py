from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def google_search(query):
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Start maximized
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors

    # Initialize the driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Find the search box using the name attribute value
        search_box = driver.find_element(By.NAME, "q")
        
        # Input query and submit the form
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results to load
        time.sleep(2)
        
        # Scrape the search results
        results = driver.find_elements(By.CSS_SELECTOR, 'div.g')  # 'div.g' is a common class for search results
        
        # Extract titles and URLs from the results
        for result in results:
            title = result.find_element(By.TAG_NAME, 'h3').text
            url = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
            print(f"Title: {title}")
            print(f"URL: {url}\n")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    google_search(search_query)