import streamlit as st
import time
import random

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Denklem Sihirbazı", layout="centered")

# --- TASARIM (CSS: SİHİRLİ PORTAL TEMASI) ---
st.markdown("""
    <style>
    .stApp { background-color: #1A1A2E; color: #E94560; }
    
    h1 { color: #E94560 !important; text-align: center; font-family: 'Courier New', monospace; }
    h2, h3 { color: #0F3460 !important; }
    p, label { color: #FFFFFF !important; font-size: 18px; }
    
    /* DENKLEM KUTUSU */
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
    }
    
    /* PORTAL BUTONU */
    div.stButton > button {
        background-color: #533483 !important;
        color: white !important;
        border-radius: 10px;
        font-size: 20px;
        width: 100%;
        border: 2px solid #E94560;
    }
    div.stButton > button:hover {
        background-color: #E94560 !important;
        color: white !important;
    }
    
    .info-box {
        background-color: #0F3460;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #E94560;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BAŞLIK VE GİRİŞ ---
st.title("🔮 Denklem Sihirbazı & Portal Kapısı")
st.markdown("""
<div class='info-box'>
    <b>Hoş Geldin Çırak!</b><br>
    Matematikte "Eşittir" (=) işareti sıradan bir çizgi değil, sihirli bir <b>PORTALDIR</b>.
    Bu portaldan geçen sayılar değişime uğrar! Amacımız "Bilinmeyeni" (x) yalnız bırakıp özgürlüğüne kavuşturmaktır.
</div>
""", unsafe_allow_html=True)

# Sekmelerle Aşamalı Öğretim
tab1, tab2, tab3 = st.tabs(["1. Portal Eğitimi 🌀", "2. Rehberli Çözüm 🧭", "3. Bilgi Köşesi 📚"])

# --- TAB 1: PORTAL SİMÜLASYONU (Kavram Öğretimi) ---
with tab1:
    st.header("🌀 Portalın Kuralı: İşaret Değişimi")
    st.write("Aşağıdaki denkleme bak. $+4$ sayısı portaldan (eşittir) karşıya geçerse ne olur?")
    
    # Durum Yönetimi
    if 'portal_step' not in st.session_state: st.session_state.portal_step = 0
    
    # Görsel Denklem
    if st.session_state.portal_step == 0:
        st.markdown("<div class='equation-box'>x + 4 = 10</div>", unsafe_allow_html=True)
        st.info("Görev: x'i yalnız bırakmak için +4'ü karşıya at!")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Karşıya +4 olarak geçir"):
                st.error("HATA! Portaldan geçen sayı aynen kalamaz! Terazi bozulur.")
        with col2:
            if st.button("Karşıya -4 olarak geçir (SİHİR!) ✨"):
                st.session_state.portal_step = 1
                st.rerun()
                
    elif st.session_state.portal_step == 1:
        st.markdown("<div class='equation-box'>x = 10 - 4</div>", unsafe_allow_html=True)
        st.success("HARİKA! Toplama (+), portaldan geçince Çıkarma (-) oldu.")
        st.write("Şimdi sonucu bulalım:")
        
        if st.button("Sonucu Hesapla"):
            st.session_state.portal_step = 2
            st.rerun()
            
    elif st.session_state.portal_step == 2:
        st.markdown("<div class='equation-box'>x = 6</div>", unsafe_allow_html=True)
        st.balloons()
        st.markdown("""
        <div class='info-box'>
        <b>Tebrikler! Denklem Kökünü Buldun.</b><br>
        x = 6 değeri teraziyi dengede tutan tek sayıdır.
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔄 Tekrar Başla"):
            st.session_state.portal_step = 0
            st.rerun()

# --- TAB 2: ADIM ADIM REHBERLİ ÇÖZÜM (3x + 2 = 20) ---
with tab2:
    st.header("🧭 Büyük Sınav: 3x + 2 = 20")
    st.write("Rehberdeki örneği birlikte çözelim. Adım adım ilerleyeceğiz.")
    
    if 'solve_step' not in st.session_state: st.session_state.solve_step = 0
    
    # Adım 0: Soru
    if st.session_state.solve_step == 0:
        st.markdown("<div class='equation-box'>3x + 2 = 20</div>", unsafe_allow_html=True)
        st.write("Adım 1: Bilinenleri bir tarafa topla. +2 fazlalık yapıyor.")
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("2'yi karşıya -2 olarak at"):
                st.session_state.solve_step = 1
                st.rerun()
        with col_b:
            if st.button("3x'i karşıya at"):
                st.warning("Hayır! Amacımız x'i yalnız bırakmak, onu göndermek değil.")

    # Adım 1: Karşıya Atma
    elif st.session_state.solve_step == 1:
        st.markdown("<div class='equation-box'>3x = 20 - 2</div>", unsafe_allow_html=True)
        st.info("Doğru! +2 portaldan geçti ve -2'ye dönüştü. Şimdi sağ tarafı hesapla.")
        
        if st.button("İşlemi Yap (20 - 2)"):
            st.session_state.solve_step = 2
            st.rerun()

    # Adım 2: Sadeleştirme
    elif st.session_state.solve_step == 2:
        st.markdown("<div class='equation-box'>3x = 18</div>", unsafe_allow_html=True)
        st.write("Adım 2: Katsayıdan kurtulma. x'in başında çarpım durumunda 3 var.")
        st.write("Çarpmanın tersi nedir?")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Her iki tarafı 3'e BÖL (/)"):
                st.session_state.solve_step = 3
                st.rerun()
        with c2:
            if st.button("Her iki taraftan 3 ÇIKAR (-)"):
                st.error("Dikkat! 3 ile x çarpışıyor (yapışık). Çıkarma işlemi onları ayıramaz. Bölmelisin!")

    # Adım 3: Sonuç
    elif st.session_state.solve_step == 3:
        st.markdown("<div class='equation-box'>x = 6</div>", unsafe_allow_html=True)
        st.balloons()
        st.success("MÜKEMMEL! x özgürlüğüne kavuştu.")
        st.markdown("""
        **Özet Rapor:**
        1. $+2$ karşıya $-2$ olarak geçti.
        2. $20-2$ işlemi $18$ oldu.
        3. Çarpım durumundaki $3$, karşıya bölme olarak geçti.
        4. $18 / 3 = 6$.
        """)
        if st.button("🔄 Başa Dön"):
            st.session_state.solve_step = 0
            st.rerun()

# --- TAB 3: BİLGİ KÖŞESİ (KAVRAMSAL ÖZET) ---
with tab3:
    st.header("📚 Sihir Kitabı (Kurallar)")
    
    st.markdown("### 1. Denklem Kökü Nedir?")
    st.info("Bir denklemde eşitliğin her iki tarafını birbirine tam olarak eşitleyen, bilinmeyen (genellikle x) değerine denir.")
    
    st.markdown("### 2. Terazi Dengesi")
    st.warning("Eşitliğin bir tarafına ne yapıyorsak, dengenin bozulmaması için diğer tarafına da tam olarak aynısını yapmalıyız.")
    
    st.markdown("### 3. Portal Kuralları (İşaret Değişimi)")
    st.table({
        "Mevcut İşlem": ["Toplama (+)", "Çıkarma (-)", "Çarpma (x)", "Bölme (/)"],
        "Karşıya Geçince": ["Çıkarma (-)", "Toplama (+)", "Bölme (/)", "Çarpma (x)"]
    })
    st.markdown("*Kaynak: Adım Adım Denklem Çözme Rehberi*")
