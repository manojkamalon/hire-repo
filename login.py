import streamlit as st
import pandas  as pd


# Sidebar menu
menu = st.sidebar.radio(
    "Menu",
    ["Home", "Login", "Register", "Dashboard", "CV Upload"]
)

# Display content based on the selected menu option
if menu == "Home":
    st.title("Welcome to the App")
    st.write("This is the home page of the app.")

elif menu == "Login":
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.write(f"Attempting login for user: {username}")

elif menu == "Register":
    st.title("Register")
    with st.form("registration_form"):
        username = st.text_input("Username")
        name = st.text_input("Full Name")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Register")

        if submitted:
            if password != confirm_password:
                st.error("Passwords do not match!")
            elif not username or not name or not password:
                st.error("All fields are required!")
            else:
                st.success("User registered successfully!")

elif menu == "Dashboard":
    st.title("Dashboard")
    st.write("Welcome to the dashboard!")
    # Add dashboard functionalities here

elif menu == "CV Upload":
    st.title("Candidate Details")
    st.subheader("Upload CV")
    upload_file = st.file_uploader("Choose a PDF file", type="pdf" )
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
