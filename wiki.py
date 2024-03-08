import os
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
from urllib.parse import urljoin

def scrape_and_save_images(url):
    # Make a request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags
        img_tags = soup.find_all('img')
        
        # Create a directory to save the images
        os.makedirs('images', exist_ok=True)
        
        # Save each image to the "images" folder
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            
            # If the image URL is relative, convert it to an absolute URL
            img_url = urljoin(url, img_url)
            
            # Get the image content
            img_content = requests.get(img_url).content
            print(type(img_content))
            
            try:
                # Try to open the image using PIL (Python Imaging Library)
                img = Image.open(BytesIO(img_content))
                
                # Generate a unique filename based on the image URL
                img_filename = os.path.join('images', os.path.basename(img_url))
                
                # Save the image to the "images" folder
                img.save(img_filename)
                
                print(f"Image saved: {img_filename}")
                
                # Optionally, you can perform further processing on the image data without saving it
                
            except Exception as e:
                # Handle the case when the content is not a valid image
                print(f"Error processing image at {img_url}: {e}")
            
    else:
        print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")

# Example usage
url_to_scrape = "https://en.wikipedia.org/wiki/Subramania_Bharati"
scrape_and_save_images(url_to_scrape)
