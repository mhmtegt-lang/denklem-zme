

import streamlit as st
import time
import random

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Denklem Sihirbazı", layout="centered")

# --- TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #1A1A2E; color: #E94560; }
    h1 { color: #E94560 !important; text-align: center; font-family: 'Courier New', monospace; }
    p, label, div { color: #FFFFFF !important; font-size: 18px; }
    
    /* Temel Denklem Kutusu */
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
        font-family: 'Courier New', monospace;
        min-height: 100px; /* Animasyon sırasında kutu küçülmesin diye */
    }

    /* ANİMASYON İÇİN ÖZEL STİLLER */
    .moving-part {
        color: #FFD700; /* Altın sarısı vurgu */
        text-shadow: 0 0 10px #FFD700;
        transition: all 0.5s ease;
        display: inline-block;
    }
    .portal-active {
        font-size: 50px;
        animation: spin 2s linear infinite;
    }
    @keyframes spin { 100% { transform: rotate(360deg); } }

    /* BUTONLAR */
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

# --- YARDIMCI FONKSİYON: PORTAL ANİMASYONU ---
def animate_portal_transfer(placeholder, start_html, moving_part_html, end_html, final_html):
    """
    Bir sayının karşıya geçişini kare kare canlandırır.
    placeholder: Denklemin gösterildiği st.empty() alanı.
    """
    # Adım 1: Parçayı Vurgula (Havalanma Efekti)
    placeholder.markdown(f"<div class='equation-box'>{start_html} <span class='moving-part'>[{moving_part_html}]</span> = {end_html}</div>", unsafe_allow_html=True)
    time.sleep(0.7)
    
    # Adım 2: Portal Aktif (Yok olma ve geçiş)
    placeholder.markdown(f"<div class='equation-box'>{start_html} <span class='portal-active'>🌀</span> = {end_html}</div>", unsafe_allow_html=True)
    time.sleep(0.7)
    
    # Adım 3: Karşıda Belirme (İşaret Değişmiş Halde)
    # Burada basitlik için final_html'i doğrudan gösteriyoruz ama vurgulu da yapabiliriz.
    placeholder.markdown(f"<div class='equation-box'>{final_html}</div>", unsafe_allow_html=True)
    time.sleep(0.5)

st.title("🔮 Denklem Sihirbazı: Portal Kapısı")

tab1, tab2, tab3 = st.tabs(["1. Portal Eğitimi 🌀", "2. Rehberli Çözüm 🧭", "3. Antrenman Sahası 🏋️ (Animasyonlu)"])

# --- TAB 3: ANTRENMAN SAHASI (ANİMASYONLU) ---
with tab3:
    st.header("🏋️ Antrenman Sahası")
    
    # Soru Üretme
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
    target_sign = "-" if sign == "+" else "+"

    # Animasyon için yer tutucu
    eq_placeholder = st.empty()

    # ADIM 0: SABİT SAYIYI KARŞIYA ATMA (Toplama/Çıkarma)
    if st.session_state.train_step == 0:
        # Başlangıç durumunu göster
        eq_placeholder.markdown(f"<div class='equation-box'>{a}x {sign} {b} = {c}</div>", unsafe_allow_html=True)
        st.write(f"**Soru:** Bilinen sayıyı ({sign}{b}) portaldan karşıya nasıl atarsın?")
        
        col1, col2 = st.columns(2)
        with col1:
            # DOĞRU CEVAP BUTONU (Animasyonu Tetikler)
            if st.button(f"Karşıya {target_sign}{b} olarak geçer (SİHİR!) ✨"):
                # --- ANİMASYON BAŞLIYOR ---
                moving_part = f"{sign} {b}"
                start_part = f"{a}x"
                end_part = f"{c}"
                final_state = f"{a}x = {c} {target_sign} {b}"
                
                animate_portal_transfer(eq_placeholder, start_part, moving_part, end_part, final_state)
                # --- ANİMASYON BİTTİ ---
                
                st.session_state.train_step = 1
                st.rerun()
        with col2:
            if st.button(f"İşareti değişmeden ({sign}{b}) geçer"):
                st.error("Portal Kuralı: Karşıya geçerken işaret mutlaka zıtlaşır!")

    # ADIM 1: BEKLEME VE HESAPLAMA
    elif st.session_state.train_step == 1:
        eq_placeholder.markdown(f"<div class='equation-box'>{a}x = {c} {target_sign} {b}</div>", unsafe_allow_html=True)
        st.info(f"Sayı başarıyla geçti! Şimdi sağ tarafı hesapla.")
        
        if st.button(f"İşlemi yap"):
            st.session_state.train_step = 2
            st.rerun()

    # ADIM 2: KATSAYIDAN KURTULMA (Çarpma -> Bölme Animasyonu)
    elif st.session_state.train_step == 2:
        new_c = c - b if sign == "+" else c + b
        eq_placeholder.markdown(f"<div class='equation-box'>{a}x = {new_c}</div>", unsafe_allow_html=True)
        st.write(f"x'i yalnız bırakmak için katsayıyı ({a}) karşıya atmalıyız. Çarpma nasıl geçer?")
        
        col1, col2 = st.columns(2)
        with col1:
            # DOĞRU CEVAP (Bölme Animasyonu)
            if st.button(f"Bölme (/) olarak geçer ✨"):
                 # --- ANİMASYON BAŞLIYOR ---
                moving_part = f"• {a}" # Çarpı a
                start_part = f"x"
                end_part = f"{new_c}"
                # Bölme gösterimi: new_c / a
                final_state = f"x = {new_c} / {a}"
                
                animate_portal_transfer(eq_placeholder, start_part, moving_part, end_part, final_state)
                # --- ANİMASYON BİTTİ ---

                st.session_state.train_step = 3
                st.rerun()
        with col2:
            if st.button("Çıkarma (-) olarak geçer"):
                 st.error("Yapışık sayılar (çarpım) çıkarma ile ayrılamaz! Bölmelisin.")

    # ADIM 3: SONUÇ
    elif st.session_state.train_step == 3:
        eq_placeholder.markdown(f"<div class='equation-box'>x = {st.session_state.q_x}</div>", unsafe_allow_html=True)
        st.balloons()
        st.success("Tebrikler! Denklem kökünü buldun.")
        if st.button("🎲 Yeni Soru"):
            for key in ['q_a', 'train_step']: del st.session_state[key]
            st.rerun()
