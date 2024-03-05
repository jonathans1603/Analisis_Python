import streamlit as st
import pandas as pd
from PIL import Image

# Set judul dashboard
st.title('Visualisasi Data E-commerce')

dataset = pd.read_csv('Datasetalldata.csv')

#Tabel data
st.text("data customer product order")
st.dataframe(dataset)

#Visualisasi Pertanyaan 1
st.header('1.Visualisasi Barang Dibeli Per bulan')
st.subheader('Chart jumlah penjualan product E-commerce Per Bulan')
st.image('Revenue.png')

#Visualisasi Pertanyaan 2
st.header('2. Visualisasi Kategori product berdasarkan Performa Penjualan')
st.subheader('Chart perfoma kategori product terbaik dan terburuk berdasarkan jumlah pembelian')
st.image('Bestworst.png')
