import streamlit as st

st.title('File upload app!')

file = st.sidebar.file_uploader(encoding = 'utf-8')
st.write(file.readlines())
