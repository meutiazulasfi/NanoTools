import streamlit as st
import pandas as pd
import numpy as np
import time

# =============================
# 1. KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="NanoFood Ecosystem",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================
# 2. CSS & TEMA
# =============================
st.markdown("""
<style>
/* Background Animasi Gradient */
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
/* Glassmorphism */
.glass-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 25px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    margin-bottom: 20px;
    color: white;
}
h1, h2, h3, h4, .stMarkdown, p, div { color: white !important; }
[data-testid="stSidebar"] { background-color: rgba(54, 1, 133, 0.9); }
.stButton>button {
    background-color: #F4B342; color: #360185; font-weight: bold; border-radius: 12px; border: none;
}
.stButton>button:hover { background-color: #DE1A58; color: white; transform: scale(1.05); }
</style>
""", unsafe_allow_html=True)

# =============================
# 3. KAMUS BAHASA (TRANSLATION)
# =============================
# Ini mengatur teks tombol dan judul
txt = {
    "ID": {
        "nav_title": "Menu Utama",
        "menu_opts": ["🏠 Tools & Calc", "📊 Insight (Nano)", "📚 Learning", "🤖 Ask Copilot", "👤 About"],
        "tools_h1": "🛠️ Laboratorium Digital",
        "tools_sub": "Kumpulan alat hitung untuk Nanoteknologi dan Rekayasa Pangan.",
        "calc_dilution": "🧪 Kalkulator Pengenceran",
        "calc_shelf": "📅 Prediksi Umur Simpan (Q10)",
        "learn_h1": "📚 Pusat Pembelajaran",
        "learn_sub": "Pilih modul pembelajaran kimia di bawah ini:",
        "tabs_learn": ["⚗️ Kimia Dasar", "🌿 Kimia Organik", "💎 Kimia Anorganik", "🍞 Kimia Pangan"]
    },
    "EN": {
        "nav_title": "Main Menu",
        "menu_opts": ["🏠 Tools & Calc", "📊 Insight (Nano)", "📚 Learning", "🤖 Ask Copilot", "👤 About"],
        "tools_h1": "🛠️ Digital Laboratory",
        "tools_sub": "Calculation tools for Nanotechnology and Food Engineering.",
        "calc_dilution": "🧪 Dilution Calculator",
        "calc_shelf": "📅 Shelf Life Prediction (Q10)",
        "learn_h1": "📚 Learning Center",
        "learn_sub": "Select chemistry learning modules below:",
        "tabs_learn": ["⚗️ Basic Chem", "🌿 Organic Chem", "💎 Inorganic Chem", "🍞 Food Chem"]
    }
}

# =============================
# 4. SIDEBAR & BAHASA
# =============================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2021/2021652.png", width=80)
    
    # --- PILIH BAHASA ---
    lang_choice = st.selectbox("🌐 Language / Bahasa", ["Indonesia", "English"])
    lang_code = "ID" if lang_choice == "Indonesia" else "EN"
    t = txt[lang_code] # Memuat kamus berdasarkan bahasa yang dipilih
    
    st.markdown("---")
    st.write(f"**NanoFood Hub** ({lang_code})")
    
    selected_menu = st.radio(
        t["nav_title"],
        t["menu_opts"],
        index=0
    )
    st.markdown("---")

# Helper Function
def make_glass_card(content_func):
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    content_func()
    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# MENU 1: TOOLS
# =============================
if selected_menu == t["menu_opts"][0]: # Tools
    st.title(t["tools_h1"])
    st.write(t["tools_sub"])
    
    tab1, tab2 = st.tabs(["🧬 Nano", "🍽️ Food"])
    
    with tab1:
        make_glass_card(lambda: st.write("Content Nano Calculator here... (Logic retained)"))
    with tab2:
        make_glass_card(lambda: st.write("Content Food Calculator here... (Logic retained)"))

# =============================
# MENU 2: INSIGHT
# =============================
elif selected_menu == t["menu_opts"][1]: # Insight
    st.title("🔬 Nanoparticle Insight")
    # (Kode grafik sama seperti sebelumnya, dipersingkat untuk fokus ke Learning)
    st.line_chart(pd.DataFrame(np.random.randn(20, 3), columns=['A','B','C']))

# =============================
# MENU 3: LEARNING (UPDATE)
# =============================
elif selected_menu == t["menu_opts"][2]: # Learning
    st.title(t["learn_h1"])
    st.write(t["learn_sub"])

    # Membuat Tabs sesuai bahasa
    tabs = st.tabs(t["tabs_learn"])

    # -----------------------------------------------------------
    # [AREA EDIT MATERI]
    # Di bawah ini adalah tempat Anda menyisipkan materi pelajaran.
    # Gunakan format Markdown.
    # -----------------------------------------------------------

    # TAB 1: KIMIA DASAR
    with tabs[0]:
        make_glass_card(lambda: st.markdown(
            """
            ### ⚗️ Materi Kimia Dasar
            
            **Bahasa Indonesia:**
            * **Stoikiometri:** Perhitungan kuantitas zat dalam reaksi kimia.
            * **Hukum Lavoisier:** Massa zat sebelum dan sesudah reaksi adalah tetap.
            
            ---
            **English:**
            * **Stoichiometry:** Calculating quantities in chemical reactions.
            * **Lavoisier's Law:** Mass is neither created nor destroyed.
            """ if lang_code == "ID" or lang_code == "EN" else "" 
            # Tips: Anda bisa memisahkan if/else total jika teksnya sangat panjang
        ))
        
        # Contoh jika ingin membedakan total teks berdasarkan bahasa:
        if lang_code == "ID":
            st.info("💡 Tips: Pahami konsep Mol sebelum melanjut ke Molaritas.")
        else:
            st.info("💡 Tip: Understand the Mole concept before proceeding to Molarity.")

    # TAB 2: KIMIA ORGANIK
    with tabs[1]:
        make_glass_card(lambda: st.markdown("""
        ### 🌿 Gugus Fungsi (Functional Groups)
        
        1. **Alkohol (-OH)**: Methanol, Ethanol.
        2. **Aldehid (-COH)**: Formalin.
        3. **Asam Karboksilat (-COOH)**: Asam cuka.
        """))

    # TAB 3: KIMIA ANORGANIK
    with tabs[2]:
        make_glass_card(lambda: st.markdown("""
        ### 💎 Logam Transisi
        Logam transisi sering digunakan sebagai katalis dalam sintesis nanopartikel.
        Contoh: **Emas (Au)**, **Perak (Ag)**, **Seng (Zn)**.
        """))

    # TAB 4: KIMIA PANGAN
    with tabs[3]:
        # -----------------------------------------------
        # ANDA BISA MENYISIPKAN MATERI BARU DI SINI
        # -----------------------------------------------
        make_glass_card(lambda: st.markdown("""
        ### 🍞 Reaksi Kimia pada Pangan
        
        * **Reaksi Maillard:** Reaksi pencoklatan antara gula pereduksi dan asam amino (memberi rasa enak pada roti/daging bakar).
        * **Karamelisasi:** Oksidasi gula pada suhu tinggi.
        * **Emulsi:** Campuran dua cairan yang tidak saling larut (contoh: Santan, Mayones).
        """))

# =============================
# MENU 4: COPILOT
# =============================
elif selected_menu == t["menu_opts"][3]:
    st.title("🤖 Ask Copilot")
    st.write("Current Language: " + lang_choice)
    # (Logika chat sama seperti sebelumnya)

# =============================
# MENU 5: ABOUT
# =============================
elif selected_menu == t["menu_opts"][4]:
    st.title("👤 About")
    st.write("Developed by Food Technologist.")
