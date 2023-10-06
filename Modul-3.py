import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(layout="wide", page_title="Main Page", page_icon=":helmet_with_white_cross:")

def home():
    st.write("# Aplikasi Web - Modul 3")
    st.markdown(
        """
        Dalam Modul 3 ini terdapat 4 materi utama yang akan dilatih,
        yakni:
        1. Progress Bar Widget
        2. Caching
        3. Multipages
        4. Session & Callback
        """
    )

    st.write("# Aplikasi Web - Modul 4")
    st.markdown(
        """
        Dalam Modul 4 ini mahasiswa diminta untuk dapat membuat
        sebuah aplikasi menggunakan Streamlit
        """
    )
    with st.expander("Informasi Lebih Lanjut"):
        st.markdown(
            '''
            - Nama: [Muhammad Hanif Annafi](https://annafikk.my.id)
            - NIM: 21537141009
            - Kelas: I.1 S1 - Teknologi Informasi
            '''
        )

def stats_con():
    st.header('Status Container')
    with st.expander("Apa itu Status Container?"):
        st.markdown(
            '''
            Dalam Streamlit, "container" biasanya merujuk pada widget 
            yang digunakan untuk mengelompokkan elemen-elemen dalam 
            aplikasi web. Ada beberapa jenis widget yang berfungsi 
            sebagai container yang memungkinkan pengguna untuk dapat 
            mengatur tata letak dan tampilan elemen-elemen di dalamnya.
            '''
        )

    # ------------------------------------------------------------------
    # All Functions
    # ------------------------------------------------------------------

    def iterasi1():
        'Memulai Komputasi'
        st.toast('Memulai Komputasi')
        
        # Menambahkan Placeholder
        iterasi = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update Bar
            iterasi.text(f'Iterasi {i+1}')
            bar.progress(i+1)
            time.sleep(0.1) 
        
        'Komputasi Selesai'
        st.toast('Komputasi Selesai')

    
    def iterasi2():
        st.toast('Memulai Pengunduhan')
        with st.spinner("Downloading Data ..."):
            st.write("Searching Data ...")
            time.sleep(2)
            st.write("Found URL.")
            time.sleep(1)

            iterasi = st.empty()
            bar = st.progress(0)

            for i in range(100):
                iterasi.text(f'Downloading Data ... {i+1}%')
                bar.progress(i+1)
                time.sleep(0.1)
        st.toast('Pengunduhan Selesai')

    # ------------------------------------------------------------------
    # Progress Bar
    # ------------------------------------------------------------------
    
    st.subheader("Progress Bar")
    with st.expander("Apa itu Progress Bar?"):
        st.markdown(
            '''
            Progres bar adalah elemen grafis yang digunakan untuk 
            mengindikasikan kemajuan suatu tugas atau proses yang 
            sedang berlangsung. Ini berguna ketika pengguna memiliki 
            tugas yang memakan waktu lama, seperti pengolahan 
            data besar atau pembaruan database.
            '''
        )
    
    with st.expander("Contoh Implementasi Progress Bar :"):
        on1 = st.toggle(('On / Off'), key= "b1")
        if on1:
            iterasi1()

    # ------------------------------------------------------------------
    # Status Widget
    # ------------------------------------------------------------------

    st.subheader("Status Widget")
    with st.expander("Apa itu Progress Bar?"):
        st.markdown(
            '''
            Widget status adalah elemen yang digunakan untuk 
            menampilkan status atau pesan kepada pengguna. 
            Ini dapat berupa pesan sukses, pesan error, atau 
            informasi lainnya.
            '''
        )
    
    with st.expander("Contoh Implementasi Status Widget :"):
        on2 = st.toggle(('On / Off'), key= "2")
        if on2:
            iterasi2()

def caching():
    st.subheader('Caching')
    with st.expander("Apa itu Progress Bar?"):
        st.markdown(
            '''
            Dalam Streamlit, "caching" merujuk pada proses penyimpanan hasil 
            komputasi atau perhitungan sehingga hasil tersebut dapat digunakan 
            kembali tanpa perlu menghitung ulang setiap kali pengguna 
            berinteraksi dengan aplikasi web. Caching adalah teknik yang 
            berguna untuk meningkatkan kinerja aplikasi web, terutama ketika 
            ada perhitungan yang memakan waktu atau pengambilan data yang 
            intensif.
            '''
        )
    
    with st.expander("Contoh Implementasi Caching :"):
        @st.cache_data
        def komputasi(input_nilai):
            hasil = input_nilai ** 2
            return hasil

        # Input widget to get a user's input
        input_nilai = st.slider("Pilih Nilai dari 1-100", 1, 100, 1)

        # Call the cached function
        hasil = komputasi(input_nilai)

        # Display the result
        st.write(f"Hasil Komputasi Kuadrat : {hasil}")


def session():
    st.subheader('Session')
    with st.expander("Apa itu Session?"):
        st.markdown(
            '''
            Session mengacu pada interaksi atau sesi yang dimiliki oleh 
            pengguna individu dengan aplikasi Streamlit. Setiap kali 
            pengguna membuka aplikasi Streamlit maka hal tersebut dapat 
            disebut sebagai satu sesi. Session menyimpan informasi tentang 
            interaksi pengguna selama waktu mereka berinteraksi dengan aplikasi.
            
            Dalam Streamlit, session umumnya adalah sesi stateless 
            yang berarti aplikasi tidak secara otomatis menyimpan informasi 
            atau status pengguna antara dua sesi berbeda. Namun pengembang 
            dapat menggunakan teknik seperti st.session_state untuk menyimpan 
            data yang spesifik untuk sesi tersebut dan digunakan dalam 
            interaksi selanjutnya.
            '''
        )

    with st.expander("Contoh Implementasi Session :"):
        input_var = st.text_input('Masukkan Nama Anda :')

        st.write(f"Halo, {input_var}!")

        if ('name' not in st.session_state) and (input_var != ''):
            st.session_state['name'] = input_var

        st.write('Nama Pertama yang Anda Masukkan :')
        if 'name' in st.session_state:
            st.write(st.session_state['name'])

        st.write(st.session_state)


def callback():
    st.subheader('Callback')
    with st.expander("Apa itu Callback?"):
        st.markdown(
            '''
            Callback biasanya mengacu pada penggunaan fungsi yang 
            dieksekusi sebagai respons terhadap peristiwa atau 
            interaksi pengguna dalam aplikasi web. Fungsi-fungsi ini 
            disebut "callback functions" atau "callbacks." Callbacks 
            digunakan untuk membuat aplikasi Streamlit yang 
            lebih dinamis dengan merespons perubahan yang dibuat 
            oleh pengguna dalam widget atau antarmuka aplikasi.

            Callback dalam Streamlit adalah konsep yang terkait 
            erat dengan widget dan interaktivitas. Pengguna dapat 
            mengaitkan fungsi tertentu dengan perubahan nilai 
            dalam widget, sehingga ketika pengguna berinteraksi 
            dengan widget tersebut, fungsi callback akan dipanggil 
            dan dapat melakukan tindakan tertentu, seperti 
            memperbarui tampilan, menghitung ulang data, 
            atau melakukan tugas lainnya.
            '''
        )

    def calc_area():
        st.session_state['area'] = st.session_state['side'] ** 2
        st.session_state['slider_side'] = st.session_state['side'] 

    def calc_side():
        st.session_state['side'] = st.session_state['area'] ** (1/2)
        st.session_state['slider_side'] = st.session_state['side']
    
    with st.expander("Contoh Implementasi Callback : "):
        st.write('Area Kalkulasi Kuadratik')
        side = st.number_input("Panjang :", key='side', on_change = calc_area)
        area = st.number_input("Luas Area :", key='area', on_change = calc_side)

        st.write(st.session_state)

pages = {
    "Beranda": home,
    "Status Container": stats_con,
    "Caching": caching,
    "Session": session,
    "Callback": callback
}

nav = st.sidebar.selectbox('Silakan Pilih Fungsi Modul 3', pages.keys())
pages[nav]()
