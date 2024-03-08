import streamlit as st
import pandas as pd

# Load your JSON file into a Pandas DataFrame
json_file_path = "data.json"  # Replace with your file path
df = pd.read_json(json_file_path)

# Simple top menu bar for login/logout
menu = ["Home", "Login", "Logout"]
choice = st.sidebar.selectbox("Menu", menu)

# Add animation
if choice == "Home":
    st.title("JSON Data Display with Streamlit")
    st.table(df)
elif choice == "Login":
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Add your login logic here
        st.success("Logged in as {}".format(username))
elif choice == "Logout":
    st.title("Logout Page")
    # Add your logout logic here
    st.info("Logged out successfully")
