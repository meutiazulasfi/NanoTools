import streamlit as st
import math

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="NanoFood Tools Pro",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =============================
# CSS CUSTOM THEME & BACKGROUND
# =============================
# Palet Warna: #360185, #8F0177, #DE1A58, #F4B342
st.markdown("""
<style>
/* Mengatur Background Utama Aplikasi */
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

/* Mengatur Tampilan Kartu (Glassmorphism) */
div.css-1r6slb0.e1tzin5v2 {
    background-color: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    margin-bottom: 25px;
}

/* Judul dan Teks */
h1, h2, h3 {
    color: #ffffff;
    text-shadow: 2px 2px 4px #000000;
    text-align: center;
    font-family: 'Helvetica', sans-serif;
}

.card-header {
    color: #360185;
    font-weight: bold;
    font-size: 1.3rem;
    margin-bottom: 15px;
    border-bottom: 2px solid #DE1A58;
    padding-bottom: 5px;
}

.stButton>button {
    background-color: #360185;
    color: white;
    border-radius: 10px;
    border: none;
    width: 100%;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background-color: #DE1A58;
    color: white;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# =============================
# HEADER APLIKASI
# =============================
st.markdown("<h1>🧬 NanoFood Tools <span style='color:#F4B342'>Pro</span></h1>", unsafe_allow_html=True)
st.markdown("<h3>Integrated System for Nanotech & Food Science</h3>", unsafe_allow_html=True)
st.markdown("---")

# =============================
# SIDEBAR
# =============================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3053/3053984.png", width=100)
    st.title("Navigasi")
    menu = st.radio(
        "Pilih Modul:",
        ["🔬 Lab Nanoteknologi", "🍽 Gizi & Pangan", "🏭 Food Engineering"]
    )
    
    st.markdown("---")
    st.info("Aplikasi ini membantu perhitungan cepat untuk formulasi nano-emulsi dan estimasi gizi pangan.")

# =============================
# FUNGSI UTILITAS (CARD WRAPPER)
# =============================
def make_card_start():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

def make_card_end():
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# 1. MODUL NANOTEKNOLOGI
# =============================
if menu == "🔬 Lab Nanoteknologi":
    st.markdown("## 🧪 Perhitungan Laboratorium")

    # --- Kalkulator 1: Molaritas & Penimbangan ---
    make_card_start()
    st.markdown("<div class='card-header'>⚖️ Kalkulator Molaritas & Massa</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        molaritas = st.number_input("Molaritas (M)", 0.0, step=0.1)
        volume_l = st.number_input("Volume Akhir (Liter)", 0.0, step=0.1)
    with col2:
        mr = st.number_input("Berat Molekul (MR) zat (g/mol)", 0.0, step=0.1)
    
    if st.button("Hitung Massa Zat"):
        massa_zat = molaritas * volume_l * mr
        st.success(f"Massa yang harus ditimbang: **{massa_zat:.4f} gram**")
    make_card_end()

    # --- Kalkulator 2: Pengenceran (Dilution) ---
    make_card_start()
    st.markdown("<div class='card-header'>💧 Kalkulator Pengenceran ($M_1V_1 = M_2V_2$)</div>", unsafe_allow_html=True)
    st.write("Hitung berapa volume larutan stok yang dibutuhkan.")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        m1 = st.number_input("Konsentrasi Stok (M1/%)", 0.0, step=0.1)
        m2 = st.number_input("Konsentrasi Target (M2/%)", 0.0, step=0.1)
    with col_d2:
        v2 = st.number_input("Volume Target (ml)", 0.0, step=1.0)
    
    if st.button("Hitung Volume Stok"):
        if m1 > 0:
            v1 = (m2 * v2) / m1
            st.info(f"Ambil **{v1:.2f} ml** larutan stok, tambahkan pelarut hingga **{v2} ml**.")
        else:
            st.error("Konsentrasi stok tidak boleh 0.")
    make_card_end()

    # --- Kalkulator 3: Rasio Luas Permukaan (Nano Concept) ---
    make_card_start()
    st.markdown("<div class='card-header'>⚛️ Rasio Luas Permukaan vs Volume</div>", unsafe_allow_html=True)
    st.write("Semakin kecil partikel, semakin besar reaktivitasnya.")
    
    radius_nm = st.slider("Jari-jari partikel (nanometer)", 1, 1000, 50)
    
    if st.button("Analisis Karakteristik Nano"):
        # Asumsi bentuk bola
        surface_area = 4 * math.pi * (radius_nm**2)
        volume_nano = (4/3) * math.pi * (radius_nm**3)
        ratio = surface_area / volume_nano
        
        st.write(f"Luas Permukaan: {surface_area:.2e} nm²")
        st.write(f"Volume: {volume_nano:.2e} nm³")
        st.warning(f"Rasio SA/V: **{ratio:.4f}**")
        
        if radius_nm < 100:
            st.success("✅ Masuk kategori Nanomaterial (sangat reaktif)")
        else:
            st.info("⚠️ Masuk kategori Material Bulk/Mikro")
    make_card_end()


# =============================
# 2. MODUL GIZI & PANGAN
# =============================
elif menu == "🍽 Gizi & Pangan":
    st.markdown("## 🥗 Manajemen Diet & Nutrisi")

    # --- Kalkulator 1: TDEE & BMR ---
    make_card_start()
    st.markdown("<div class='card-header'>🔥 Kalkulator Kebutuhan Kalori (Mifflin-St Jeor)</div>", unsafe_allow_html=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        gender = st.selectbox("Jenis Kelamin", ["Pria", "Wanita"])
        usia = st.number_input("Usia (tahun)", 10, 100, 25)
    with col_g2:
        bb_diet = st.number_input("Berat Badan (kg)", 30.0, 200.0, 60.0)
        tb_diet = st.number_input("Tinggi Badan (cm)", 100.0, 250.0, 165.0)
    
    aktivitas_dict = {
        "Sangat Jarang (Sedenter)": 1.2,
        "Jarang (1-3 hari/minggu)": 1.375,
        "Normal (3-5 hari/minggu)": 1.55,
        "Sering (6-7 hari/minggu)": 1.725
    }
    level_aktivitas = st.selectbox("Tingkat Aktivitas Fisik", list(aktivitas_dict.keys()))
    
    if st.button("Hitung TDEE"):
        # Rumus Mifflin-St Jeor
        if gender == "Pria":
            bmr = (10 * bb_diet) + (6.25 * tb_diet) - (5 * usia) + 5
        else:
            bmr = (10 * bb_diet) + (6.25 * tb_diet) - (5 * usia) - 161
            
        tdee = bmr * aktivitas_dict[level_aktivitas]
        
        st.write(f"BMR (Energi dasar): **{bmr:.0f} kkal**")
        st.success(f"Total Kebutuhan Harian (TDEE): **{tdee:.0f} kkal**")
        
        # Breakdown Makro
        st.markdown("---")
        st.markdown("**Rekomendasi Makronutrien (Balanced Diet):**")
        c1, c2, c3 = st.columns(3)
        c1.metric("Karbohidrat (50%)", f"{(0.5*tdee/4):.0f} g")
        c2.metric("Protein (20%)", f"{(0.2*tdee/4):.0f} g")
        c3.metric("Lemak (30%)", f"{(0.3*tdee/9):.0f} g")
    make_card_end()

    # --- Kalkulator 2: BMI ---
    make_card_start()
    st.markdown("<div class='card-header'>⚖️ Indeks Massa Tubuh (BMI)</div>", unsafe_allow_html=True)
    
    if st.button("Cek Status Gizi"):
        bmi = bb_diet / ((tb_diet/100)**2)
        st.write(f"Skor BMI Anda: **{bmi:.2f}**")
        
        if bmi < 18.5:
            st.warning("Kategori: Kekurangan Berat Badan")
        elif 18.5 <= bmi < 24.9:
            st.success("Kategori: Normal (Ideal)")
        elif 25 <= bmi < 29.9:
            st.warning("Kategori: Kelebihan Berat Badan")
        else:
            st.error("Kategori: Obesitas")
    make_card_end()


# =============================
# 3. MODUL FOOD ENGINEERING
# =============================
elif menu == "🏭 Food Engineering":
    st.markdown("## 🏭 Rekayasa Pangan")

    # --- Prediksi Umur Simpan (Q10) ---
    make_card_start()
    st.markdown("<div class='card-header'>📅 Prediksi Umur Simpan (Metode Q10)</div>", unsafe_allow_html=True)
    st.write("Estimasi perubahan umur simpan produk berdasarkan perubahan suhu penyimpanan.")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        shelf_life_ref = st.number_input("Umur simpan pada suhu referensi (hari)", 1)
        temp_ref = st.number_input("Suhu referensi (°C)", 25.0)
    with col_e2:
        q10 = st.number_input("Nilai Q10 Produk", 2.0, help="Biasanya bernilai 2.0 untuk reaksi kimia umum")
        temp_target = st.number_input("Suhu penyimpanan baru (°C)", 35.0)
    
    if st.button("Prediksi Umur Simpan Baru"):
        delta_t = temp_target - temp_ref
        # Rumus: t2 = t1 / (Q10 ^ (DeltaT / 10))
        shelf_life_new = shelf_life_ref / (q10 ** (delta_t / 10))
        
        st.metric(label="Umur Simpan Baru", value=f"{shelf_life_new:.1f} hari", delta=f"{shelf_life_new - shelf_life_ref:.1f} hari")
        
        if shelf_life_new < shelf_life_ref:
            st.warning("Suhu lebih panas mempercepat kerusakan produk!")
        else:
            st.success("Suhu lebih dingin memperpanjang umur simpan produk.")
    make_card_end()
    
    # --- Konversi Unit Tekanan ---
    make_card_start()
    st.markdown("<div class='card-header'>⏲️ Konversi Tekanan (Processing)</div>", unsafe_allow_html=True)
    psi = st.number_input("Tekanan (PSI)", 0.0)
    if st.button("Konversi"):
        bar = psi * 0.0689476
        pascal = psi * 6894.76
        st.write(f"**{bar:.2f} Bar**")
        st.write(f"**{pascal:.0f} Pascal**")
    make_card_end()

# =============================
# FOOTER
# =============================
st.markdown("---")
st.markdown("<p style='text-align: center; color: white;'>Developed with ❤️ using Streamlit | NanoFood Tools 2025</p>", unsafe_allow_html=True)
