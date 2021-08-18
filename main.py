import streamlit as st

st.title('File upload app!')

file = st.sidebar.file_uploader(type="txt", encoding = 'utf8')
st.write(file.readlines())
