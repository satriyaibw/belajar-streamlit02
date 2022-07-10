from ast import If
from datetime import datetime
import streamlit as st
import pandas as pd
from PIL import Image

def main():
    st.title("Selamat Datang")
    st.write('Ini merupakan aplikasi khusus jomblo yang ingin mencari jodoh. Silahkan lengkapi data diri di bawah ini untuk melanjutkan.')

    with st.form(key='form', clear_on_submit=True):
        st.header("Isi Biodata Kamu")
        nama_tamu = st.text_input('Masukkan Nama Lengkap (Wajib)')
        tgl_lahir_tamu = st.date_input('Pilih Tanggal Lahir', min_value=datetime(1945,12,12), max_value=datetime(2022,12,12))
        alamat_tamu = st.text_input('Alamat')
        gambar_tamu = st.camera_input('Foto Kamu')
        submit_button = st.form_submit_button('Cari Jodohmu!')
    if submit_button:    
            if nama_tamu == 'ida ayu praba iswari dewi':
                st.header('Jodoh Kamu Adalah:')
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader('Nama :')
                    st.write('Ida Bagus Satriya Wibawa')
                    st.subheader('Tanggal Lahir :')
                    st.write('25 Januari 2001 (21th)')
                    st.subheader('Alamat :')
                    st.write('Karangasem')
                with col2:
                    image = Image.open('photo.jpg')
                    st.image(image, width=400)
            elif nama_tamu == '':
                st.warning('Data tidak boleh kosong')
            elif tgl_lahir_tamu == '':
                st.warning('Data tidak boleh kosong')
            elif alamat_tamu == '':
                st.warning('Data tidak boleh kosong')
            elif gambar_tamu == '':
                st.warning('Data tidak boleh kosong')
            else:
                st.header('Jodoh Kamu Adalah:')
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader('Nama :')
                    st.write('Monyet')
                    st.subheader('Tanggal Lahir :')
                    st.write('tidak diketahui')
                    st.subheader('Alamat :')
                    st.write('Hutan')
                with col2:
                    image = Image.open('monkey.jpg')
                    st.image(image, width=400)    

if __name__ == '__main__':
    main()

