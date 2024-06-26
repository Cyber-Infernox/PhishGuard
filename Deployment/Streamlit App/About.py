# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:08:15 2024

@author: sayon
"""
import streamlit as st

def about_page():
    # ------------------------------------------------------
    page_title = "About - Us"
    st.title(page_title)
    # ------------------------------------------------------
    
    st.markdown(
        """
        PhishGuard is a web application designed to help users identify and 
        avoid phishing websites, which are fraudulent sites created to deceive users into 
        providing sensitive information such as passwords, credit card numbers, and personal 
        details. Our mission is to empower individuals and organizations to protect themselves 
        from cyber threats by providing a simple and effective tool for detecting potential 
        phishing URLs.

        ### How It Works

        Our website utilizes state-of-the-art machine learning algorithms and data analysis 
        techniques to analyze URLs and assess their likelihood of being phishing websites. 
        When a user submits a URL for analysis, our system evaluates various features of 
        the URL, including its domain, subdomain, path, and characteristics of the web page 
        content. Based on this analysis, the system provides a risk score indicating the 
        probability that the URL is a phishing site.

        ### Our Team

        PhishGuard is developed and maintained by a team of undergrad students with inconsiderable experience in threat detection, machine learning, and web 
        security. Our dedicated team is committed to continuously improving the accuracy 
        and effectiveness of our detection system to stay ahead of emerging threats and 
        protect our users from cyber attacks.

        ### Privacy Policy

        We take your privacy seriously. Our privacy policy outlines how we collect, use, 
        and protect your personal information when you use our website. We are committed to 
        ensuring the confidentiality and security of your data and complying with applicable 
        privacy laws and regulations.

        Thank you for using PhishGuard and joining us in the fight against 
        online fraud!
        """
    )