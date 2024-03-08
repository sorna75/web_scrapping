from PIL import Image
import streamlit as st

def display_images(image_paths):
    for path in image_paths:
        image = Image.open(path)
        st.image(image, caption=f"Image: {path}", use_column_width=True)

if __name__ == "__main__":
    image_paths = [
        r'D:\work space\web_scraping\images\img1.jpg',
        r'D:\work space\web_scraping\images\img2.jpg',
        r'D:\work space\web_scraping\images\img3.jpg',
        r'D:\work space\web_scraping\images\img4.jpg',
        r'D:\work space\web_scraping\images\img5.jpg',
        r'D:\work space\web_scraping\images\img6.jpg',
        r'D:\work space\web_scraping\images\img7.jpg',
        r'D:\work space\web_scraping\images\img8.jpg',
        r'D:\work space\web_scraping\images\img9.jpg',
        r'D:\work space\web_scraping\images\img10.jpg',
        r'D:\work space\web_scraping\images\img11.jpg',
        r'D:\work space\web_scraping\images\img13.jpg',
        r'D:\work space\web_scraping\images\img14.jpg',
        r'D:\work space\web_scraping\images\img15.jpg',
        r'D:\work space\web_scraping\images\img16.jpg',
        r'D:\work space\web_scraping\images\img17.jpg',
        r'D:\work space\web_scraping\images\img18.jpg',
        r'D:\work space\web_scraping\images\img19.jpg',
        r'D:\work space\web_scraping\images\img20.jpg',
        r'D:\work space\web_scraping\images\img21.jpg',
        r'D:\work space\web_scraping\images\img22.jpg',
        r'D:\work space\web_scraping\images\img23.jpg',
        r'D:\work space\web_scraping\images\img24.jpg',
        r'D:\work space\web_scraping\images\img25.jpg',
        r'D:\work space\web_scraping\images\img26.jpg'
        # Add more image paths as needed
    ]

    display_images(image_paths)
