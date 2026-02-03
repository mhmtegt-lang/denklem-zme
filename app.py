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
    p, label, div { color: #CBD5E1 !important; font-size: 18px; }
    
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
        min-height: 180px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }

    /* HAVALANMA EFEKTİ */
    .levitate {
        display: inline-block;
        color: #FACC15 !important; /* Altın Sarısı */
        transform: translateY(-40px); /* Havaya kalkma */
        transition: all 0.4s ease-in-out;
        text-shadow: 0 0 20px #FACC15;
    }

    /* KARŞI TARAFTA BELİRME (YENİ KİMLİK) */
    .transformed {
        color: #F87171 !important; /* Kırmızımsı vurgu */
        font-weight: 800;
        animation: pulse 1s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }

    /* BUTONLAR */
    div.stButton > button {
        background-color: #38BDF8 !important;
        border: none !important;
        border-radius: 12px !important;
        height: 60px !important;
        width: 100% !important;
    }
    div.stButton > button * {
        color: #0F172A !important; 
        font-weight: bold !important;
        font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

class EquationEngine:
    """Animasyonlu denklem motoru."""
    def __init__(self, placeholder):
        self.placeholder = placeholder

    def show_levitation(self, left_part, moving_val, right_part):
        """Sayıyı havaya kaldırır ve karşıya süzülmesini sağlar."""
        # 1. Aşama: Sayı Havalanır
        self.placeholder.markdown(f"""
            <div class='equation-box'>
                {left_part} <span class='levitate'>{moving_val}</span> = {right_part}
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.8)

        # 2. Aşama: Sayı Ortada Kaybolur (Uçuş hissi)
        self.placeholder.markdown(f"""
            <div class='equation-box'>
                {left_part} &nbsp;&nbsp;&nbsp; = &nbsp;&nbsp;&nbsp; {right_part}
            </div>
        """, unsafe_allow_html=True)
        time.sleep(0.5)

    def show_landing(self, left_part, final_right_part):
        """Sayı karşıya yeni haliyle konar."""
        self.placeholder.markdown(f"""
            <div class='equation-box'>
                {left_part} = <span class='transformed'>{final_right_part}</span>
            </div>
        """, unsafe_allow_html=True)

# --- OYUN MANTIĞI ---
st.title("⚖️ Denklem Ustası: Havalanan Sayılar")

if 'step' not in st.session_state: st.session_state.step = 0
if 'q' not in st.session_state:
    # Rehberdeki 3x + 2 = 20 örneği baz alınmıştır
    st.session_state.q = {"a": 3, "x": 6, "b": 2, "c": 20}

q = st.session_state.q
display = st.empty()
engine = EquationEngine(display)

# ADIM 0: BAŞLANGIÇ
if st.session_state.step == 0:
    display.markdown(f"<div class='equation-box'>{q['a']}x + {q['b']} = {q['c']}</div>", unsafe_allow_html=True)
    st.write("Teraziyi dengede tutmak için $+{}$ değerini karşıya göndermeliyiz.".format(q['b']))
    
    if st.button("Sayıyı Havalandır ve Gönder! 🚀"):
        # Animasyon Silsilesi
        engine.show_levitation(f"{q['a']}x", f"+{q['b']}", f"{q['c']}")
        engine.show_landing(f"{q['a']}x", f"{q['c']} - {q['b']}")
        st.session_state.step = 1
        st.rerun()

# ADIM 1: HESAPLAMA
elif st.session_state.step == 1:
    engine.show_landing(f"{q['a']}x", f"{q['c']} - {q['b']}")
    st.info("Sayı karşıya geçerken kimlik değiştirdi ve $-{}$ oldu!".format(q['b']))
    
    if st.button("İşlemi Sonuçlandır"):
        st.session_state.step = 2
        st.rerun()

# ADIM 2: KATSAYI HAVALANIR (Çarpma -> Bölme)
elif st.session_state.step == 2:
    new_c = q['c'] - q['b']
    display.markdown(f"<div class='equation-box'>{q['a']}x = {new_c}</div>", unsafe_allow_html=True)
    st.write("$x$'in başındaki ${}$ katsayısı çarpım durumundadır. Onu karşıya bölme olarak uçuralım!".format(q['a']))
    
    if st.button("Katsayıyı Havaya Kaldır! 🚀"):
        # Çarpma katsayısının havalanması
        engine.show_levitation("x", f"{q['a']} \cdot", f"{new_c}")
        # Bölme olarak konması (LaTeX formatı)
        engine.show_landing("x", f"\\frac{{{new_c}}}{{{q['a']}}}")
        st.session_state.step = 3
        st.rerun()

# ADIM 3: SONUÇ
elif st.session_state.step == 3:
    new_c = q['c'] - q['b']
    display.markdown(f"<div class='equation-box'>x = \\frac{{{new_c}}}{{{q['a']}}}</div>", unsafe_allow_html=True)
    if st.button("Bilinmeyeni Özgür Bırak (Sonuç)"):
        display.markdown(f"<div class='equation-box'>x = {q['x']}</div>", unsafe_allow_html=True)
        st.balloons()
        st.success("Tebrikler! Denklem kökünü başarıyla buldun.")
        if st.button("Yeni Sınav 🔄"):
            st.session_state.step = 0
            st.rerun()
