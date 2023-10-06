# Introduction-to-Streamlit

Mata Kuliah Aplikasi Web
Modul 3 & 4 - Introduction to Streamlit

Yang diperlukan :
1. Integrated Development Environment (IDE)
2. Anaconda
3. Streamlit
4. Enable PowerShell Execution Policy
5. Virtual Environment (Via Anaconda / Visual Code Studio)

Membuat Virtual Environment:
1. Via Anaconda
   - Launch Anaconda
   - Klik Environment > Create
   - Isi nama & package > Klik Create
   - Buka Anaconda Prompt
   - Masukkan perintah:
     **conda activate aplikasi_web**
   - Install Streamlit
     **pip install streamlit**
   - Tes Streamlit
     **streamlit hello**

2. Via Visual Code Studio
   - Launch VCS
   - Buat folder baru dengan nama **Streamlit**
   - Buka terminal, masukkan perintah:
     **python -m venv env_aplikasi_web**
   - Jalankan virtual environment
     **env_aplikasi_web\Scripts\activate**
   - Install Streamlit
     **pip install streamlit**
   - Tes Streamlit
     **streamlit hello**

Halaman yang Tersedia:
1. NYC Uber Ridesharing Data [Source Here](https://github.com/streamlit/demo-uber-nyc-pickups)
2. Kalkulator BMI

Atribut Streamlit yang Digunakan:
1. st.write()
2. st.markdown()
3. st.title()
4. st.header()
5. st.subheader()
6. st.caption()
7. st.text()
8. st.toast()

Fungsi yang Digunakan:
1. home()
2. stats_con()
3. caching()
4. session()
5. callback()
6. Pages
7. Nav
