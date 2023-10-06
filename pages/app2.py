import streamlit as st

st.set_page_config(layout="wide", page_title="BMI Calculator", page_icon=":health:")

# Fungsi Untuk Kalkulasi BMI
def calculate_bmi(height, weight):
    try:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        return bmi
    except ZeroDivisionError:
        return "Tinggi badan tidak boleh nol!"
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

# Judul
st.title("Aplikasi Penghitung BMI")

# Input widget untuk tinggi badan (dalam cm)
height = st.number_input("Masukkan tinggi badan (cm):", 0, 300, 170)

# Input widget untuk berat badan (dalam kg)
weight = st.number_input("Masukkan berat badan (kg):", 0, 300, 70)

# Tombol untuk menghitung BMI
if st.button("Hitung BMI"):
    bmi_result = calculate_bmi(height, weight)
    if isinstance(bmi_result, float):
        st.success(f"Indeks Massa Tubuh (BMI): {bmi_result:.2f}")
        st.write("Interpretasi BMI:")
        if bmi_result < 18.5:
            st.warning(f"Kurang berat badan")
        elif 18.5 <= bmi_result < 24.9:
            st.success(f"Berat badan normal")
        elif 25 <= bmi_result < 29.9:
            st.warning(f"Kelebihan berat badan")
        else:
            st.warning(f"Obesitas")
            st.write("Obesitas")
    else:
        st.error(bmi_result)
