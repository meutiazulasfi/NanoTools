import streamlit as st

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="NanoFood Tools",
    page_icon="🧬",
    layout="centered"
)

# =============================
# CSS CUSTOM THEME
# =============================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #360185, #8F0177, #DE1A58, #F4B342);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.card {
    background: rgba(255,255,255,0.93);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}

h1, h2, h3 {
    color: #360185;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =============================
# JUDUL
# =============================
st.markdown("<h1>🧬 NanoFood Tools</h1>", unsafe_allow_html=True)
st.markdown("<h3>Website Perhitungan Nanoteknologi & Pangan</h3>", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Nanoteknologi", "Pangan"]
)

# =============================
# NANOTEKNOLOGI
# =============================
if menu == "Nanoteknologi":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔬 Kalkulator Konversi Penimbangan")

    konsentrasi = st.number_input("Konsentrasi larutan (g/L)", 0.0)
    volume = st.number_input("Volume larutan (L)", 0.0)

    if st.button("Hitung Massa"):
        massa = konsentrasi * volume
        st.success(f"Massa yang harus ditimbang: **{massa:.4f} gram**")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📏 Perhitungan Kalibrasi Instrumen")

    nilai_standar = st.number_input("Nilai standar", 0.0)
    nilai_terbaca = st.number_input("Nilai terbaca alat", 0.0)

    if st.button("Hitung Error"):
        if nilai_standar != 0:
            error = ((nilai_terbaca - nilai_standar) / nilai_standar) * 100
            st.info(f"Persentase error: **{error:.2f}%**")
        else:
            st.error("Nilai standar tidak boleh nol")

    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# PANGAN
# =============================
elif menu == "Pangan":
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🍽 Program Diet (Kalori Harian)")

    berat = st.number_input("Berat badan (kg)", 0.0)
    aktivitas = st.selectbox(
        "Tingkat aktivitas",
        ["Ringan", "Sedang", "Berat"]
    )

    faktor = {"Ringan": 25, "Sedang": 30, "Berat": 35}

    if st.button("Hitung Kalori"):
        kalori = berat * faktor[aktivitas]
        st.success(f"Kebutuhan kalori harian: **{kalori:.0f} kkal/hari**")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🥗 Perhitungan Gizi (Makronutrien)")

    kalori_total = st.number_input("Total kalori harian (kkal)", 0.0)

    if st.button("Hitung Gizi"):
        karbo = 0.55 * kalori_total / 4
        protein = 0.15 * kalori_total / 4
        lemak = 0.30 * kalori_total / 9

        st.write(f"🍚 Karbohidrat: **{karbo:.1f} g**")
        st.write(f"🥩 Protein: **{protein:.1f} g**")
        st.write(f"🥑 Lemak: **{lemak:.1f} g**")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("👤 Kebutuhan Pangan per Orang")

    bb = st.number_input("Berat badan individu (kg)", 0.0)

    if st.button("Hitung Kebutuhan Pangan"):
        kalori_orang = bb * 30
        st.success(f"Kebutuhan energi individu: **{kalori_orang:.0f} kkal/hari**")

    st.markdown("</div>", unsafe_allow_html=True)
