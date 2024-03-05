import streamlit as st
from PIL import Image
st.title("Visualisasi Data E-commerce")

st.subheader("Halaman Image")
st.write(
    "Visualisasi Data Revenue product E-commerce per Bulan"
)
image_file = st.file_uploader("upload image", type=['png', 'jpeg', 'jpg'])
 