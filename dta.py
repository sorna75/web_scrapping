import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract data from the HTML using BeautifulSoup

    # Example: Extracting titles from an HTML page
    titles = soup.find_all('h2')
    return [title.text for title in titles]

def main():
    st.title('Web Scraping with Streamlit')

    # Input URL
    url = st.text_input('Enter URL:', 'https://finance.yahoo.com/quote/%5ENSEI/history/')

    if st.button('Scrape Data'):
        # Perform web scraping
        scraped_data = scrape_data(url)

        # Display the scraped data
        st.write('Scraped Data:')
        st.write(scraped_data)

if __name__ == '__main__':
    main()
