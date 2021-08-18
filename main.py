import streamlit as st

st.title('File upload app!')

file = st.sidebar.file_uploader()
# text_io = io.TextIOWrapper(file,encoding='UTF-8')
# st.write(list(text_io.readlines()))
