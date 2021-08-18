import streamlit as st
import pandas as pd

st.title('File upload app!')
file = st.file_uploader('')
print(file.read().decode("utf-8"))
