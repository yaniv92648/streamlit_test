import streamlit as st
import pandas as pd

st.title('File upload app!')
file = st.file_uploader('')
st.write(file.read().decode("utf-8"))
