# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:11:52 2024

@author: sayon
"""
import streamlit as st
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv("C:/Users/sayon/Downloads/ML Projects/Malicious URL Detection/hosting/Jojo-URL-Detection/deployment/.env")
#load_dotenv(".env")

# Connect to MongoDB
try:
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("MONGO_REPORT_DB")]
    collection = db[os.getenv("MONGO_REPORT_COLLECTION")]
    connection_status = True
except Exception as e:
    st.error(f"Failed to connect to MongoDB: {e}")
    connection_status = False

# Function to add report to the database
def add_report(url, details, observations):
    if not connection_status:
        return False
    
    try:
        collection.insert_one({"url": url, "details": details, "observations": observations})
        return True
    except Exception as e:
        st.error(f"Failed to add report to database: {e}")
        return False

def report_form():
    # Form inputs
    url = st.text_input("URL of the suspected phishing website:")
    details = st.text_area("Additional details:")
    observations = st.text_area("Observations:")
    
    result = ''

    # Submit button
    if st.button("Submit Report"):
        if url:
            if add_report(url, details, observations):
                result = "Report submitted successfully!"
            else:
                result = "Failed to submit report. Please try again later."
                
            # Reset form inputs after submission
        else:
            result = "Please enter the URL of the suspected phishing website."
            
    st.success(result)

def report_page():
    # ------------------------------------------------------
    page_title = "Report - Phish"
    st.title(page_title)
    # ------------------------------------------------------
    
    st.markdown(
        """
        If you have encountered a suspected phishing website, we encourage you to report it 
        to help protect others from falling victim to online scams. Please provide as much 
        information as possible about the suspicious URL, including:

        - The URL of the suspected phishing website
        - Any additional details about the website
        - Observations (if available)

        You can report the phishing website by sending an email to report@phishguard.com 
        or by filling out the form below:

        Thank you for your vigilance in helping us combat online fraud!
        """
    )
        
    st.markdown('<hr style="border: 2px dashed #999; margin-top: 0px; margin-bottom: 35px;">', unsafe_allow_html=True)

    report_form()