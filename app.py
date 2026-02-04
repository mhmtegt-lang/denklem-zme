

import streamlit as st
import time
import random

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Denklem Ustası", layout="centered")

# --- TASARIM (CSS: HAVALANMA VE RENK DEĞİŞİMİ) ---
st.markdown("""
    <style>
    .stApp { background-color: #0F172A; color: #F8FAFC; }
    h1 { color: #38BDF8 !important; text-align: center; font-family: 'Trebuchet MS', sans-serif; }
    
    /* DENKLEM KUTUSU */
    .equation-box {
        background-color: #1E293B;
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #334155;
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #F8FAFC;
        margin-bottom: 20px;
        font-family: 'Monaco', monospace;
        min-height: 200px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }

    /* HAVALANMA EFEKTİ */
    .levitate {
        display: inline-block;
        color: #FACC15 !important; /* Altın Sarısı Parlama */
        transform: translateY(-60px); /* Havaya kalkış yüksekliği */
        transition: all 0.5s ease-in-out;
        text-shadow: 0 0 20px #FACC15;
    }

    /* HAVADA DÖNÜŞÜM EFEKTİ */
    .mid-air {
        color: #FB7185 !important; /* Pembe/Kırmızı Dönüşüm */
        transform: translateY(-60px) scale(1.2);
        opacity: 0.8;
    }

    /* BUTONLAR: SARI ZEMİN SİYAH YAZI */
    div.stButton > button {
        background-color: #FFD700 !important;
        border: none !important;
        border-radius: 12px !important;
        height: 60px !important;
        width: 100% !important;
    }
    div.stButton > button * {
        color: #000000 !important; 
        font-weight: 900 !important;
        font-size: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

class AnimationEngine:
    """Sayının havadaki yolculuğunu yöneten motor."""
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def play_move_animation(self, left, moving, right, result_val):
        """Toplama/Çıkarma için havalanma animasyonu."""
        # 1. Aşama: Sayı Havalanır (Sarı parlar)
        self.placeholder.markdown(f"<div class='equation-box'>{left} <span class='levitate'>{moving}</span> = {right}</div>", unsafe_allow_html=True)
        time.sleep(0.8)
        
        # 2. Aşama: Havada Dönüşüm (İşaret değişir, renk değişir)
        new_moving = moving.replace('+', '-').replace('-', '+') if '+' in moving or '-' in moving else moving
        self.placeholder.markdown(f"<div class='equation-box'>{left} &nbsp;&nbsp; <span class='mid-air'>{new_moving}</span> &nbsp;&nbsp; {right}</div>", unsafe_allow_html=True)
        time.sleep(0.8)
        
        # 3. Aşama: Karşıya Konuş
        self.placeholder.markdown(f"<div class='equation-box'>{left} = {right} {new_moving}</div>", unsafe_allow_html=True)

# --- OYUN MANTIĞI ---
st.title("⚖️ Denklem Ustası: Havalanan Sayılar")

if 'step' not in st.session_state: st.session_state.step = 0
if 'q' not in st.session_state:
    st.session_state.q = {"a": 3, "x": 6, "b": 2, "c": 20} # Örnek: 3x + 2 = 20

q = st.session_state.q
display = st.empty()
engine = AnimationEngine(display)

# --- ADIMLAR ---
if st.session_state.step == 0:
    display.markdown(f"<div class='equation-box'>{q['a']}x + {q['b']} = {q['c']}</div>", unsafe_allow_html=True)
    st.write("Bilinenleri bir tarafa toplamak için $+{}$ sayısını havalandırıp karşıya gönderelim!".format(q['b']))
    
    if st.button("SAYIYI UÇUR! 🚀"):
        engine.play_move_animation(f"{q['a']}x", f"+{q['b']}", f"{q['c']}", q['c'] - q['b'])
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    display.markdown(f"<div class='equation-box'>{q['a']}x = {q['c']} - {q['b']}</div>", unsafe_allow_html=True)
    st.success("Sayı havada işaret değiştirdi ve $-{}$ olarak kondu!".format(q['b']))
    
    if st.button("İşlemi Sonuçlandır"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    new_c = q['c'] - q['b']
    display.markdown(f"<div class='equation-box'>{q['a']}x = {new_c}</div>", unsafe_allow_html=True)
    st.write("$x$'in başındaki ${}$ katsayısından kurtulmak için onu bölme olarak uçurmalıyız.".format(q['a']))
    
    if st.button("Katsayıyı Havalandır! 🚀"):
        # Katsayı havalanma animasyonu
        display.markdown(f"<div class='equation-box'><span class='levitate'>{q['a']}</span>x = {new_c}</div>", unsafe_allow_html=True)
        time.sleep(0.8)
        # Karşıya geçiş ve kesir gösterimi
        display.markdown(f"<div class='equation-box'>x = \\frac{{{new_c}}}{{{q['a']}}}</div>", unsafe_allow_html=True)
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    new_c = q['c'] - q['b']
    display.markdown(f"<div class='equation-box'>x = \\frac{{{new_c}}}{{{q['a']}}}</div>", unsafe_allow_html=True)
    if st.button("x'i Özgür Bırak (Sonuç)"):
        display.markdown(f"<div class='equation-box'>x = {q['x']}</div>", unsafe_allow_html=True)
        st.balloons()
        st.success("Tebrikler! Denklem kökünü başarıyla buldun.")
        if st.button("Yeni Soru 🔄"):
            st.session_state.step = 0
            st.rerun()
