from typing import cast
import streamlit as st
from streamlit_option_menu import option_menu
from PIL  import Image 

#1. as sidebar menu 
with st.sidebar:
    choose=option_menu("Menu Utama", ["House", "Tentor", "Registrasi", "Contact", "Payment"],
        icons=["Star", "Moon", "", ""],
    )
if choose == "House": 
    col1, col2, col3 = st.columns(3)  
    with col1: 
        st.title("King Teach Tutor📚📝")
        st.caption("Website kursus online dengan tutor-tutor yang terpercaya, yang dapat mengajarkan tentang berbagai macam pengetahuan tentang ekonomi, akuntansi sampai ke bahasa inggris. Terumata bagi yang Soshum") 

    with col2:
        st.write(" ")
    with col3:
        st.image("logo.jpeg")
        st.write(" ")  
    def garis():
        st.write("------------------------------------------------------------------------------------------")
    garis()

    st.title('List Mata Pelajaran')
    st.image('matematika.jpeg')

    st.header('Matematika')
    st.subheader('Rp50.000')
    st.text('Kode id: 001')


    st.image('akuntansi.jpeg')

    st.header('Akuntansi')
    st.subheader('Rp50.000')
    st.text('Kode Id: 002')


    st.image('ekonomi.jpeg')

    st.header('Ekonomi')
    st.subheader('Rp45.000')
    st.text('Kode Id: 003')


    st.image('sosiologi.jpeg')

    st.header('Sosiologi')
    st.subheader('Rp45.000')
    st.text('Kode Id: 004')


    st.image('geografi.jpeg')

    st.header('Geografi')
    st.subheader('Rp45.000')
    st.text('Kode Id: 005')


    st.image('inggris.jpeg')

    st.header('Bahasa Inggris')
    st.subheader('Rp45.000')
    st.text('Kode Id: 006')

if choose == "Tentor":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.title('👩🏻‍🏫List     Nama    Tentor👨🏻‍🏫')          
        ("----------------------------------------------------------------------------------------------------")
    with col3:
        st.write(" ")


    st.header('Matematika')
    st.subheader('Edisanto Siburian')
        
    st.image('edi.jpg')

    st.header('Akuntansi')
    st.subheader('Widia Sari Hutabarat')

    st.image('widia.jpg')

    st.header('Ekonomi')
    st.subheader('Ikmalia Askaa')

    st.image('lia.jpeg')

    st.header('Sosiologi')
    st.subheader('rizki Septian')

    st.image('rizki.jpg')

    st.header('Geografi')
    st.subheader('Luthfi Ardiansyah')

    st.image('lutfi.jpg')

    st.header('Bahasa Inggris')
    st.subheader('Amelia Sola Gracia Tobing')

    st.image('sola.jpeg')

if choose == "Registrasi":
    st.subheader("Masukan Data Diri Anda")
        
    Nama =st.text_input("Nama Pelajar : ")
    Nomor =st.text_input("Nomor Telepon : ")
    Jumlah =st.number_input("Jumlah jam yang diambil : ",0)
    Kode =st.text_input("Kode Id : ")
    Mapel = []
    Harga = []
    while Kode : 
        if Kode=="001": 
            Mapel.append("Matematika")
            Harga = int(50000)
            break
        elif Kode=="002": 
            Mapel.append("Akuntansi")
            Harga = int(50000)
            break
        elif Kode=="003": 
            Mapel.append("Ekonomi")
            Harga = int(45000)
            break
        elif Kode=="004": 
            Mapel.append("Sosiologi")
            Harga = int(45000)
            break
        elif Kode=="005": 
            Mapel.append("Geografi")
            Harga = int(45000)
            break
        elif Kode=="006": 
            Mapel.append("Bahasa Inggris")
            Harga = int(45000)
            break
        else : 
            Kode=st.text_input("Nomor Id Salah, Masukan Ulang Id Mata Pelajaran : ")
        
    Total = (Jumlah*Harga)

    Pembayaran = st.button("Total Pembayaran")
    if Pembayaran:
        st.write("Nama Pelajar :", Nama)
        st.write("Nomor Telepon :", Nomor)
        st.write("Kode Id:", Kode)
        st.write("Jumlah Pembayaran Kursus Online")
        st.write("Jumlah Pembayaran : Rp",round(Total))

if choose == "Payment":
    st.title("Pembayaran Dapat Dilakukan Melalui💵")

    st.write("BNI           :   1338491475    📝 Luthfi Ardiansyah")
    st.write("Dana          :   081263304592  📝 amelia sola gracia tobing")
    st.write("Shoppe Pay    :   081263304592  📝 amelia sola gracia tobing")

    st.image("payment.jpeg")
    st.subheader("https://docs.google.com/forms/d/15neY96-5uoilRIcHA9h9BgaGGwlkdli47X8tJ5_xsKk/edit")



if choose == "Contact":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        st.title("Informasi Lebih Lanjut⬇️")

    st.image("kontak.png")
    
    st.title("THANK YOU❣️")
    st.title("Hope You Like It ^-^")
