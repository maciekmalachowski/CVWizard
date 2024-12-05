import streamlit as st
import tempfile
import os
from llama_index.llms.openai import OpenAI
from scrapper import get_data
from cv_reader import read_cv


def uploader_callback():
    st.session_state.button_clicked = False

def button_callback():
    st.session_state.button_clicked = True

def main():
    st.set_page_config(
        page_title="CVWizard",
        page_icon="🧙‍♂️", 
        layout="centered",
        initial_sidebar_state="collapsed",
        )

    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    st.header("Paste your CV 📜")
    uploaded_file = st.file_uploader("Upload your file", type=(["pdf"]), on_change=uploader_callback)
    if uploaded_file:
        if st.button("Process", use_container_width=True, on_click=button_callback, disabled=st.session_state.button_clicked):
            with st.spinner("Processing your CV..."):
                temp_dir = tempfile.mkdtemp()
                path = os.path.join(temp_dir, uploaded_file.name)
                with open(path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                    pdf_engine = read_cv(f.name)

    if st.session_state.button_clicked:
        offer_link = st.text_input("Job offer link")
        if st.button("Search", use_container_width=True):
            with st.spinner("Searching for offer..."):
                get_data(offer_link)

if __name__ == "__main__":
    main()