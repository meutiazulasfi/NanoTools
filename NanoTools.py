import streamlit as st
import math
import pandas as pd # Perlu import pandas untuk grafik dummy
import numpy as np  # Perlu import numpy untuk grafik dummy

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="NanoTools",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =============================
# CSS CUSTOM THEME & BACKGROUND
# =============================
st.markdown("""
<style>
/* Background & Animasi */
.stApp {
    background: linear-gradient(-45deg, #360185, #8F0177, #DE1A58, #F4B342);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
/* Card Style */
div.css-1r6slb0.e1tzin5v2 {
    background-color: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}
.card {
    background: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    margin-bottom: 25px;
}
.card-header {
    color: #360185;
    font-weight: bold;
    font-size: 1.3rem;
    margin-bottom: 15px;
    border-bottom: 2px solid #DE1A58;
    padding-bottom: 5px;
}
/* Typography */
h1, h2, h3 {
    color: #ffffff !important;
    text-shadow: 2px 2px 4px #000000;
    text-align: center;
}
/* Button */
.stButton>button {
    background-color: #360185;
    color: white;
    border-radius: 10px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HEADER APLIKASI
# =============================
st.markdown("<h1>🧬 NanoTools <span style='color:#F4B342'>Pro</span></h1>", unsafe_allow_html=True)
st.markdown("<h3>Integrated System for Nanotech</h3>", unsafe_allow_html=True)
st.markdown("---")

# =============================
# FUNGSI UTILITAS
# =============================
def make_card_start():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

def make_card_end():
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# SIDEBAR (NAVIGASI DIPERBAIKI)
# =============================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3053/3053984.png", width=100)
    st.title("Menu NanoTools")
    
    # PERBAIKAN 1: Menambahkan semua opsi menu ke dalam list ini
    menu = st.radio(
        "Pilih Menu:",
        [
            "📈 Insight",
            "🔬 Lab Nanoteknologi", 
            "🛠 Tools",  
            "👤 About"
        ]
    )
    
    st.markdown("---")
    st.info("Aplikasi formulasi nanoteknologi.")

# =============================
# LOGIKA HALAMAN (IF - ELIF)
# =============================

# 1. MODUL NANOTEKNOLOGI
if menu == "🔬 Lab Nanoteknologi":
    st.markdown("## 🧪 Perhitungan Laboratorium")
    
    # Kalkulator Molaritas
    make_card_start()
    st.markdown("<div class='card-header'>⚖️ Kalkulator Molaritas</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        molaritas = st.number_input("Molaritas (M)", 0.0, step=0.1)
        volume_l = st.number_input("Volume (Liter)", 0.0, step=0.1)
    with col2:
        mr = st.number_input("Berat Molekul (MR)", 0.0, step=0.1)
    if st.button("Hitung Massa"):
        st.success(f"Massa: **{molaritas * volume_l * mr:.4f} gram**")
    make_card_end()


# ==========================================
# PERBAIKAN 2: Menggunakan variabel 'menu' 
# dan string biasa, bukan 'selected_menu' 
# atau 't["..."]' yang error.
# ==========================================

# 1. MENU INSIGHT
elif menu == "📈 Insight":
    st.title("🔬 Nanoparticle Insight")
    st.write("Data tren penelitian nanoteknologi terkini.")
    # Contoh grafik dummy
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
    st.line_chart(chart_data)

# 2. LAB NANOTEKNOLOGI
elif menu == "🛠 Tools":
    st.title("🛠 Extra Tools")
    tab1, tab2 = st.tabs(["🧬 Nano Tools", "🍽️ Food Tools"])
    with tab1:
        make_card_start()
        st.write("Kalkulator tambahan Nanoteknologi akan muncul di sini.")
        make_card_end()
    with tab2:
        make_card_start()
        st.write("Konverter unit pangan akan muncul di sini.")
        make_card_end()


# 3. TOOLS
elif menu == "📚 Tools":
    st.title("📚 Pusat Belajar")
    tabs = st.tabs(["⚗️ Kimia Dasar", "🌿 Organik", "💎 Anorganik"])
    
    with tabs[0]:
        make_card_start()
        st.markdown("### Stoikiometri\nIlmu yang mempelajari hubungan kuantitatif zat.")
        make_card_end()
    with tabs[1]:
        make_card_start()
        st.markdown("### Gugus Fungsi\nAlkohol, Aldehid, Keton, dll.")
        make_card_end()


# 4. MENU ABOUT
elif menu == "👤 About":
    st.title("👤 Tentang Aplikasi")
    make_card_start()
    st.write("**NanoTools Pro v1.0**")
    st.write("Dikembangkan untuk membantu mahasiswa dan praktisi pangan.")
    make_card_end()

# =============================
# FOOTER
# =============================
st.markdown("---")
st.markdown("<p style='text-align: center; color: white;'>Developed with ❤️ using NanoTools 2025</p>", unsafe_allow_html=True)
