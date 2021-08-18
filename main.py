import streamlit as st
import pandas as pd

st.title('File upload app!')

def get_total_chat():
  file = st.file_uploader('').readlines()
  return [line.decode("utf-8") for line in file]

st.write(get_total_chat())
