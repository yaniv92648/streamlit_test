import streamlit as st

st.title('File upload app!')

uploaded_file = st.sidebar.file_uploader("Upload File")
for line in uploaded_file:
  st.write(line)
