# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:15:31 2024

@author: sayon
"""
import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def contact_us_page():
    # ------------------------------------------------------
    page_title = "Contact - Us"
    st.title(page_title)
    # ------------------------------------------------------
    
    st.markdown(
        """
        If you have any questions, feedback, or concerns, we would love to hear from you! 
        Please feel free to reach out to us using any of the following methods:

        **Email:** contact@phishguard.com  
        **Phone:** +91 (123) 456-7890  
        **Address:** 123 Cybersecurity Street, City, Country

        Our team is dedicated to providing the best possible support and assistance to 
        our users. We strive to respond to all inquiries promptly and address any issues 
        or questions you may have.

        Thank you for using PhishGuard and helping us in the fight against online fraud!
        """
    )

    contact_form = """
    <form action="https://formsubmit.co/sayonkar@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your name..." required>
         <input type="email" name="email" placeholder="Your email..." required>
         <textarea name="message" placeholder="Your message..."></textarea>
         <button type="submit">Send</button>
     </form>
     """
     
    st.markdown(contact_form, unsafe_allow_html=True)
     
    local_css("C:/Users/sayon/Downloads/ML Projects/Malicious URL Detection/hosting/Jojo-URL-Detection/deployment/style/style.css")
    #local_css("style/style.css")