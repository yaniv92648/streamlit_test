import streamlit as st

st.text('Hello world')
x = st.slider('Select a value: ')
st.write(f'{x} + 2 = {x+2}')
