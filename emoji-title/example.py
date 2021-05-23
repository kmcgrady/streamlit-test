import streamlit as st

btn_menu = st.sidebar.radio("", ["page1", "page2"])

def pageOne():
    st.title(":smile:")

if btn_menu == "page1":
    pageOne()

