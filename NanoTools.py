import streamlit as st
import streamlit.components.v1 as components
import py3Dmol
import pandas as pd

# =============================
# 1. KONFIGURASI & CSS (FIXED)
# =============================
st.set_page_config(page_title="Atomic Module 4K", layout="wide")

st.markdown("""
<style>
    .stApp { background: #000814; color: #E0E0E0; }
    .card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #00D2FF;
        backdrop-filter: blur(10px);
    }
    .card-header {
        color: #00D2FF;
        font-size: 2rem;
        font-weight: bold;
        border-bottom: 2px solid #00D2FF;
        margin-bottom: 20px;
    }
    .label-accent { color: #00D2FF; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# =============================
# 2. DATASET 118 UNSUR
# =============================
DATA_URL = "https://raw.githubusercontent.com/dataprotocols/periodic-table/master/data/periodic-table.csv"

@st.cache_data
def load_data():
    # Memuat data tabel periodik 118 unsur
    df = pd.read_csv(DATA_URL)
    return df

df = load_data()

# =============================
# 3. FUNGSI RENDER 3D
# =============================
def render_atomic_3d(symbol):
    # Membuat model unit sel sederhana (FCC) untuk visualisasi atom
    xyz = f"4\n\n{symbol} 0 0 0\n{symbol} 2 2 0\n{symbol} 2 0 2\n{symbol} 0 2 2"
    view = py3Dmol.view(width=700, height=500)
    view.addModel(xyz, 'xyz')
    view.setStyle({
        'sphere': {'colorscheme': 'Jmol', 'scale': 0.5},
        'stick': {'radius': 0.15}
    })
    view.zoomTo()
    view.setBackgroundColor('rgba(0,0,0,0)')
    view.spin(True, 0.4)
    return view.render()

# =============================
# 4. ANTARMUKA UTAMA
# =============================
st.markdown("<h1 style='text-align: center;'>⚛️ Modul Atom & Struktur Materi</h1>", unsafe_allow_html=True)
st.write("---")

# Pencarian Unsur (Dropdown dengan 118 Nama)
search_options = [f"{row['atomicnumber']}. {row['name']} ({row['symbol']})" for _, row in df.iterrows()]
selected_element = st.selectbox("🔍 Cari Unsur (Nomor Atom atau Nama):", search_options)

# Ambil data spesifik unsur
target_idx = int(selected_search.split('.')[0]) - 1 if 'selected_search' in locals() else int(selected_element.split('.')[0]) - 1
el = df.iloc[target_idx]

col_viz, col_data = st.columns([1.5, 1])

with col_data:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='card-header'>{el['symbol']} - {el['name']}</div>", unsafe_allow_html=True)
    
    # Grid Data Unsur
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"<p><span class='label-accent'>Nomor Atom:</span><br>{el['atomicnumber']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><span class='label-accent'>Massa Atom:</span><br>{el['atomicmass']} u</p>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<p><span class='label-accent'>Golongan:</span><br>{el['group']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><span class='label-accent'>Periode:</span><br>{el['period']}</p>", unsafe_allow_html=True)
    
    st.markdown(f"<p><span class='label-accent'>Konfigurasi:</span><br><code>{el['electronicconfiguration']}</code></p>", unsafe_allow_html=True)
    
    st.write("---")
    # Link Google Drive / Literatur Dinamis
    drive_url = f"https://www.google.com/search?q=journal+nanotechnology+{el['name']}"
    st.link_button(f"📚 Buka Literatur {el['name']}", url=drive_url, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_viz:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    # Tampilkan Viewer 3D
    obj_3d = render_atomic_3d(el['symbol'])
    components.html(obj_3d, height=520)
    st.markdown(f"<p style='text-align:center;'>Visualisasi Struktur Kisi Atom {el['name']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =============================
# 5. MATERI TEORI (FOOTER)
# =============================
st.write("---")
st.markdown("### 📘 Pendalaman Materi Atom")



[Image of the periodic table of elements]


tab_teori, tab_tren = st.tabs(["Struktur Dasar", "Tren Periodik"])

with tab_teori:
    st.write(f"""
    Unsur **{el['name']}** memiliki konfigurasi elektron `{el['electronicconfiguration']}`. 
    Dalam nanoteknologi, posisi elektron pada orbital terluar menentukan bagaimana atom ini 
    akan membentuk ikatan kovalen atau logam pada nanopartikel.
    """)
    

[Image of electron shells and energy levels]


with tab_tren:
    st.info(f"Unsur ini berada pada Periode {el['period']} dan Golongan {el['group']}. Hal ini memengaruhi energi ionisasi dan jari-jari atomnya.")
