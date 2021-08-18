import streamlit as st
import pandas as pd

st.title('File upload app!')
file = st.file_uploader('')
with open('chat.txt', encoding="utf-8") as file:
  total_chat = file.readlines()
# df = pd.read_csv('chat.txt', delimiter = "\t", encoding='utf-8')
# display(df)
