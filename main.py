import streamlit as st
import pandas as pd

st.title('File upload app!')
filename = st.file_uploader('')
df = pd.read_csv(filename, encoding='utf-8')
st.write(df)
