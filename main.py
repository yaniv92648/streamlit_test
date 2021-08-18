import streamlit as st


def get_total_chat():
  lines = st.file_uploader('').readlines()
  return [line.decode("utf-8") for line in lines]
  

total_chat = get_total_chat()
st.write(total_chat)
