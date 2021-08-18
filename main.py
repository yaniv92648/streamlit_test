import streamlit as st

st.title('File upload app!')

fp = st.sidebar.file_uploader("Upload File")
st.text(fp)
