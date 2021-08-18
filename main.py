import streamlit as st
import pandas as pd

st.title('File upload app!')
filename = st.file_uploader('').name
df = pd.read_csv(filename, delimiter = "\t", encoding='utf-8')
display(df)
