from bs4 import BeautifulSoup
import requests
import streamlit as st

def get_data(link):
    try:
        response = requests.get(link)
    except:
        st.write("Something is wrong")