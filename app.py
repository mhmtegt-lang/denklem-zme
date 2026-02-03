import streamlit as st
import time
import random

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Denklem Sihirbazı", layout="centered")

# --- TASARIM (CSS: SİYAH YAZILI SARI BUTONLAR) ---
st.markdown("""
    <style>
    .stApp { background-color: #1A1A2E; color: #E94560; }
    h1 { color: #E94560 !important; text-align: center; font-family: 'Courier New', monospace; }
    p, label, div { color: #FFFFFF !important; font-size: 18px; }
    
    .equation-box {
        background-color: #16213E;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #0F3460;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #E94560;
        margin-bottom: 20px;
    }

    /* BUTONLAR: SARI ZEMİN, SİYAH YAZI */
    div.stButton > button {
        background-color: #FFD700 !important;
        border: 2px solid #E94560 !important;
        border-radius: 10px !important;
        height: 55px !important;
    }
    div.stButton > button * {
        color: #000000 !important; 
        font-weight: 900 !important;
        font-size: 18px !important;
    }
    
    .info-box {
        background-color: #0F3460;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #E94560;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 Denklem Sihirbazı: Portal Kapısı")

tab1, tab2, tab3 = st.tabs(["1. Portal Eğitimi 🌀", "2. Rehberli Çözüm 🧭", "3. Antrenman Sahası 🏋️"])

# --- TAB 3: ANTRENMAN SAHASI (GELİŞTİRİLMİŞ AKIŞ) ---
with tab3:
    st.header("🏋️ Antrenman Sahası")
    
    if 'q_a' not in st.session_state:
        st.session_state.q_a = random.randint(2, 6) # Katsayı
        st.session_state.q_x = random.randint(2, 8) # Sonuç (x)
        st.session_state.q_b = random.randint(1, 15) # Sabit sayı
        st.session_state.q_type = random.randint(0, 1) # 0: +, 1: -
        if st.session_state.q_type == 0:
            st.session_state.q_c = (st.session_state.q_a * st.session_state.q_x) + st.session_state.q_b
        else:
            st.session_state.q_c = (st.session_state.q_a * st.session_state.q_x) - st.session_state.q_b
        st.session_state.train_step = 0

    a, b, c = st.session_state.q_a, st.session_state.q_b, st.session_state.q_c
    sign = "+" if st.session_state.q_type == 0 else "-"

    # ADIM 0: DENKLEMİ GÖSTER VE PORTAL KURALINI SOR
    if st.session_state.train_step == 0:
        st.markdown(f"<div class='equation-box'>{a}x {sign} {b} = {c}</div>", unsafe_allow_html=True)
        st.write(f"**Soru:** Bilinen sayıyı ({sign}{b}) portaldan karşıya nasıl atarsın?")
        
        target_sign = "-" if sign == "+" else "+"
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Karşıya {target_sign}{b} olarak geçer"):
                st.session_state.train_step = 1
                st.rerun()
        with col2:
            if st.button(f"İşareti değişmeden ({sign}{b}) geçer"):
                st.error("Portal Kuralı: Karşıya geçerken işaret mutlaka zıtlaşır!")

    # ADIM 1: PORTALDAN GEÇTİ AMA HESAPLANMADI (BEKLEME)
    elif st.session_state.train_step == 1:
        target_sign = "-" if sign == "+" else "+"
        st.markdown(f"<div class='equation-box'>{a}x = {c} {target_sign} {b}</div>", unsafe_allow_html=True)
        st.info(f"**Sihir Gerçekleşti!** Sayı portaldan geçti ve **{target_sign}{b}** oldu. Şimdi sağ tarafı hesapla.")
        
        if st.button(f"İşlemi yap ({c} {target_sign} {b})"):
            st.session_state.train_step = 2
            st.rerun()

    # ADIM 2: HESAPLANDI, KATSAYIYA BÖLME ZAMANI
    elif st.session_state.train_step == 2:
        new_c = c - b if sign == "+" else c + b
        st.markdown(f"<div class='equation-box'>{a}x = {new_c}</div>", unsafe_allow_html=True)
        st.write(f"Şimdi x'i tamamen özgür bırakmak için her iki tarafı katsayıya ({a}) bölmeliyiz.")
        
        if st.button(f"Her iki tarafı {a}'e böl"):
            st.session_state.train_step = 3
            st.rerun()

    # ADIM 3: SONUÇ
    elif st.session_state.train_step == 3:
        st.markdown(f"<div class='equation-box'>x = {st.session_state.q_x}</div>", unsafe_allow_html=True)
        st.balloons()
        st.success("Tebrikler! Denklem kökünü başarıyla buldun.")
        if st.button("🎲 Yeni Soru"):
            for key in ['q_a', 'train_step']: del st.session_state[key]
            st.rerun()
