import streamlit as st

st.title('File upload app!')

file = st.sidebar.file_uploader("Upload File")
st.write([line for line in file])
