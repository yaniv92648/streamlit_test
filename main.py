import streamlit as st
import pandas as pd

st.title('File upload app!')
filename = st.file_uploader('').name()
with open(filename, encoding="utf-8") as file:
  total_chat = file.readlines()
st.write(total_chat)
