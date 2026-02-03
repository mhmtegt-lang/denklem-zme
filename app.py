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
    p, label, div { color: #FFFFFF !important; font-size: 18px; }
    
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
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* PORTAL BUTONU */
    div.stButton > button {
        background-color: #533483 !important;
        color: white !important;
        border-radius: 10px;
        font-size: 20px;
        width: 100%;
        border: 2px solid #E94560;
        margin-top: 10px;
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
        margin-bottom: 10px;
    }
    
    .success-text { color: #00FF00 !important; font-weight: bold; }
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

# Sekmelerle Aşamalı Öğretim (4. Sekme Eklendi)
tab1, tab2, tab3, tab4 = st.tabs(["1. Portal Eğitimi 🌀", "2. Rehberli Çözüm 🧭", "3. Antrenman Sahası 🏋️", "4. Bilgi Köşesi 📚"])

# --- TAB 1: PORTAL SİMÜLASYONU ---
with tab1:
    st.header("🌀 Portalın Kuralı: İşaret Değişimi")
    st.write("Aşağıdaki denkleme bak. $+4$ sayısı portaldan (eşittir) karşıya geçerse ne olur?")
    
    if 'portal_step' not in st.session_state: st.session_state.portal_step = 0
    
    if st.session_state.portal_step == 0:
        st.markdown("<div class='equation-box'>x + 4 = 10</div>", unsafe_allow_html=True)
        st.info("Görev: x'i yalnız bırakmak için +4'ü karşıya at!")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Karşıya +4 olarak geçir", key="p_err"):
                st.error("HATA! Portaldan geçen sayı aynen kalamaz! Terazi bozulur.")
        with col2:
            if st.button("Karşıya -4 olarak geçir (SİHİR!) ✨", key="p_cor"):
                st.session_state.portal_step = 1
                st.rerun()
                
    elif st.session_state.portal_step == 1:
        st.markdown("<div class='equation-box'>x = 10 - 4</div>", unsafe_allow_html=True)
        st.success("HARİKA! Toplama (+), portaldan geçince Çıkarma (-) oldu.")
        
        if st.button("Sonucu Hesapla", key="p_calc"):
            st.session_state.portal_step = 2
            st.rerun()
            
    elif st.session_state.portal_step == 2:
        st.markdown("<div class='equation-box'>x = 6</div>", unsafe_allow_html=True)
        st.balloons()
        st.markdown("<div class='info-box'>Tebrikler! Denklem Kökünü Buldun.</div>", unsafe_allow_html=True)
        if st.button("🔄 Tekrar Başla", key="p_res"):
            st.session_state.portal_step = 0
            st.rerun()

# --- TAB 2: ADIM ADIM REHBERLİ ÇÖZÜM ---
with tab2:
    st.header("🧭 Büyük Sınav: 3x + 2 = 20")
    
    if 'solve_step' not in st.session_state: st.session_state.solve_step = 0
    
    if st.session_state.solve_step == 0:
        st.markdown("<div class='equation-box'>3x + 2 = 20</div>", unsafe_allow_html=True)
        st.write("Adım 1: Bilinenleri bir tarafa topla. +2 fazlalık yapıyor.")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("2'yi karşıya -2 olarak at", key="s_step1"):
                st.session_state.solve_step = 1
                st.rerun()
        with c2:
            if st.button("3x'i karşıya at", key="s_err1"):
                st.warning("Hayır! x yerinde kalmalı.")

    elif st.session_state.solve_step == 1:
        st.markdown("<div class='equation-box'>3x = 20 - 2</div>", unsafe_allow_html=True)
        st.info("Doğru! +2 portaldan geçti ve -2'ye dönüştü.")
        if st.button("İşlemi Yap (20 - 2)", key="s_step2"):
            st.session_state.solve_step = 2
            st.rerun()

    elif st.session_state.solve_step == 2:
        st.markdown("<div class='equation-box'>3x = 18</div>", unsafe_allow_html=True)
        st.write("Adım 2: x'in başındaki 3 (katsayı) çarpım durumunda.")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Her iki tarafı 3'e BÖL (/)", key="s_step3"):
                st.session_state.solve_step = 3
                st.rerun()
        with c2:
            if st.button("Her iki taraftan 3 ÇIKAR (-)", key="s_err2"):
                st.error("Çarpma işlemi çıkarma ile yok edilemez. Bölmelisin!")

    elif st.session_state.solve_step == 3:
        st.markdown("<div class='equation-box'>x = 6</div>", unsafe_allow_html=True)
        st.balloons()
        st.success("MÜKEMMEL! x özgürlüğüne kavuştu.")
        if st.button("🔄 Başa Dön", key="s_res"):
            st.session_state.solve_step = 0
            st.rerun()

# --- TAB 3: ANTRENMAN SAHASI (YENİ VE SONSUZ SORU) ---
with tab3:
    st.header("🏋️ Antrenman Sahası: Kendini Dene!")
    st.write("Burada karşına rastgele denklemler çıkacak. Kuralları uygula!")

    # Rastgele Soru Değişkenleri
    if 'q_a' not in st.session_state:
        st.session_state.q_a = random.randint(2, 9) # Katsayı (örn: 4x)
        st.session_state.q_x = random.randint(2, 10) # Cevap (x)
        st.session_state.q_b = random.randint(1, 20) # Sabit sayı (örn: +4)
        # Denklem Türü: 0 -> Toplama (ax + b = c), 1 -> Çıkarma (ax - b = c)
        st.session_state.q_type = random.randint(0, 1) 
        
        # Sonuç (c) hesapla
        if st.session_state.q_type == 0: # ax + b = c
            st.session_state.q_c = (st.session_state.q_a * st.session_state.q_x) + st.session_state.q_b
        else: # ax - b = c
            st.session_state.q_c = (st.session_state.q_a * st.session_state.q_x) - st.session_state.q_b
            
    if 'train_step' not in st.session_state: st.session_state.train_step = 0

    # 1. Aşama: Denklemi Göster
    a, b, c = st.session_state.q_a, st.session_state.q_b, st.session_state.q_c
    
    if st.session_state.train_step == 0:
        # Denklem metnini oluştur
        sign = "+" if st.session_state.q_type == 0 else "-"
        eq_text = f"{a}x {sign} {b} = {c}"
        
        st.markdown(f"<div class='equation-box'>{eq_text}</div>", unsafe_allow_html=True)
        st.write(f"**Soru:** Bilinen sayıyı ({sign}{b}) karşıya nasıl atarsın?")
        
        col_t1, col_t2 = st.columns(2)
        
        # Seçenekleri Mantıklı Hazırla
        op_text = "Çıkarma (-)" if st.session_state.q_type == 0 else "Toplama (+)"
        wrong_op_text = "Toplama (+)" if st.session_state.q_type == 0 else "Çıkarma (-)"
        
        with col_t1:
            if st.button(f"Karşıya {op_text} olarak geçer", key="t_cor1"):
                st.session_state.train_step = 1
                st.rerun()
        with col_t2:
            if st.button(f"Karşıya {wrong_op_text} olarak geçer", key="t_err1"):
                st.error(f"Hata! {sign} işaretinin tersi {wrong_op_text} değildir.")

    # 2. Aşama: Sadeleştirme ve Bölme
    elif st.session_state.train_step == 1:
        # Ara işlemi hesapla
        if st.session_state.q_type == 0: # + idi - geçti
            new_c = c - b
            step_text = f"{a}x = {c} - {b}"
        else: # - idi + geçti
            new_c = c + b
            step_text = f"{a}x = {c} + {b}"
            
        st.markdown(f"<div class='equation-box'>{a}x = {new_c}</div>", unsafe_allow_html=True)
        st.info("Harika! Sabit sayıdan kurtulduk. Şimdi x'i yalnız bırakmak için son vuruşu yap.")
        
        if st.button(f"Her iki tarafı {a}'e BÖL (/)", key="t_cor2"):
            st.session_state.train_step = 2
            st.rerun()

    # 3. Aşama: Sonuç ve Kutlama
    elif st.session_state.train_step == 2:
        st.markdown(f"<div class='equation-box'>x = {st.session_state.q_x}</div>", unsafe_allow_html=True)
        st.balloons()
        st.success("Tebrikler Dedektif! Bir denklemi daha çözdün.")
        
        if st.button("🎲 Yeni Soru Getir", key="new_q"):
            # Değişkenleri silip rerun yaparak yeni soru üretilmesini sağla
            del st.session_state.q_a
            del st.session_state.train_step
            st.rerun()

# --- TAB 4: BİLGİ KÖŞESİ ---
with tab4:
    st.header("📚 Sihir Kitabı (Kurallar)")
    st.info("Denklem çözerken bu tabloyu unutma:")
    st.table({
        "Mevcut İşlem": ["Toplama (+)", "Çıkarma (-)", "Çarpma (x)", "Bölme (/)"],
        "Karşıya Geçince": ["Çıkarma (-)", "Toplama (+)", "Bölme (/)", "Çarpma (x)"]
    })
    st.markdown("*Kaynak: Adım Adım Denklem Çözme Rehberi*")
