import streamlit as st
import pandas as pd

st.title('File upload app!')
file = st.file_uploader('')
full_text = file.read().decode("utf-8")
st.write(full_text)
