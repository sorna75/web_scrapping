from bs4 import BeautifulSoup
import requests

# Step 1: Fetch HTML content
url = "https://paperswithcode.com/method/densenet"
response = requests.get(url)
html_content = response.content

# Step 2: Create a Beautiful Soup object
soup = BeautifulSoup(html_content, "html.parser")

# Step 3: Find all occurrences of the title tag
titles = soup.find_all("div")

# Step 4: Extract and print the titles
for title in titles:
    print(title.text)
