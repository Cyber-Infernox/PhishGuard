# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 00:26:43 2024

@author: sayon
"""

import streamlit as st
from streamlit_option_menu import option_menu
from About import about_page
from Report import report_page
from Contact import contact_us_page
from Prediction import main
from Footer import generate_footer

# ------------------------------------------------------
page_title = "PhishGuard"
layout = "centered"
#  page_icon=page_icon,
st.set_page_config(page_title=page_title, layout=layout)
#  + " " + page_icon
st.title(page_title)
# ------------------------------------------------------

selected = option_menu(
    menu_title=None,
    options=["Prediction", "About", "Report", "Contact"],
    default_index=0,
    orientation="horizontal"
    )

st.markdown('<hr style="border: 2px dashed #999; margin-top: 0px; margin-bottom: 0px;">', unsafe_allow_html=True)

if selected == "Prediction":
    main()
if selected == "About":
    about_page()
elif selected == "Report":
    report_page()
elif selected == "Contact":
    contact_us_page()
    
generate_footer()