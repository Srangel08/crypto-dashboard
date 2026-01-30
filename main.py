import streamlit as st
import yfinance as yf
import os

# 1. Configuración de página
st.set_page_config(page_title="GLANCE TERMINAL", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&display=swap');

    .stApp { background-color: #0c0e12; font-family: 'Inter', sans-serif; }
    .block-container { padding-top: 0rem !important; padding-bottom: 2rem !important; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); height: 0px; }

    /* LOGO: Mantenemos tu ajuste de equilibrio */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
    [data-testid="stImage"] img {
        max-width: 350px !important; 
        height: auto;
        margin-left: 80px !important; 
    }

    /* SUBTÍTULO ALINEADO A LA IZQUIERDA */
    .left-aligned-subtitle {
        text-align: left !important;
        color: #808495;
        font-size: 12px;
        letter-spacing: 4px;
        font-weight: 700;
        margin-top: -15px;
        margin-bottom: 45px;
        padding-left: 0px; /* Pegado al borde del contenedor */
    }

    /* TICKER DE NOTICIAS */
    .news-ticker {
        background-color: #111418; border-bottom: 1px solid #1f2228; border-top: 1px solid #1f2228;
        color: #63677a; padding: 15px 0; font-size: 13px; letter-spacing: 0.5px;
        overflow: hidden; white-space: nowrap; width: 100vw; margin-left: calc(-50vw + 50%);
    }
    .ticker-content { display: inline-block; padding-left: 100%; animation: ticker 50s linear infinite; }
    @keyframes ticker { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }

    /* CARDS DE MERCADO */
    .live-card {
        background-color: #161a1e; border: 1px solid #1f2228;
        padding: 30px 20px; border-radius: 12px; text-align: center;
    }
    .price-text { font-size: 38px; font-weight: 800; color: #ffffff; letter-spacing: -1.5px; margin: 5px 0; }
    .asset-label { color: #808495; font-size: 13px; letter-spacing: 2px; font-weight: 700; text-transform: uppercase; }

    /* BOTONES */
    .main-btn-container { display: flex; justify-content: center; width: 100%; padding: 40px 0; }
    .main-btn-container div.stButton > button {
        height: 75px !important; width: 480px !important; font-size: 22px !important; font-weight: 900 !important;
        background: linear-gradient(135deg, #ffffff 0%, #333333 100%) !important; color: #0c0e12 !important;
        border: none !important; border-radius: 10px !important;
    }

    .status-box { background-color: #161a1e; border-left: 4px solid #ffffff; padding: 30px; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. TICKER ---
st.markdown("""<div class="news-ticker"><div class="ticker-content"><b>MARKET UPDATE:</b> Institutional accumulation detected in Bitcoin spot ETFs | <b>FED WATCH:</b> Rates held steady | <b>ON-CHAIN:</b> Ethereum network activity reaches new scalability milestones</div></div>""", unsafe_allow_html=True)

# --- 2. LOGO ---
st.markdown("<br>", unsafe_allow_html=True)
col_l, col_c, col_r = st.columns([1, 1.4, 1]) 
with col_c:
    if os.path.exists("2-Photoroom.png"):
        st.image("2-Photoroom.png", use_container_width=False)
    else:
        st.markdown("<h1 style='text-align:center; color:white;'>GLANCE</h1>", unsafe_allow_html=True)

# --- SUBTÍTULO PEGADO A LA IZQUIERDA ---
st.markdown('<p class="left-aligned-subtitle">REAL-TIME FINANCIAL TERMINAL</p>', unsafe_allow_html=True)

# --- 3. MONITOR DE MERCADO ---
cols = st.columns(4)
assets = {"BTC-USD": "BITCOIN", "ETH-USD": "ETHEREUM", "SOL-USD": "SOLANA", "BNB-USD": "BINANCE"}

for col, (ticker, name) in zip(cols, assets.items()):
    try:
        t = yf.Ticker(ticker)
        data = t.fast_info
        price, op = data['last_price'], data['open']
        change = ((price - op) / op) * 100
        color = "#00ffbb" if change > 0 else "#ff3333"
        symbol = "▲" if change > 0 else "▼"
        with col:
            st.markdown(f"""<div class="live-card"><div class="asset-label">{name}</div><div class="price-text">${price:,.2f}</div><div style="color: {color}; font-weight: 700;">{symbol} {abs(change):.2f}%</div></div>""", unsafe_allow_html=True)
    except: col.error("DATA ERR")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- 4. SECCIÓN INFERIOR ---
cl, cr = st.columns([2, 1])
with cl:
    st.markdown("""<div class="status-box"><h4 style='color:white; margin:0; font-weight:800;'>CORE ENGINE STATUS</h4><p style='color:#808495; font-size:15px; margin: 10px 0;'>Terminal operational. High-speed data sync verified.</p><span style='color:#ffffff; font-weight:800; font-size:11px;'>● SYSTEM ONLINE</span></div>""", unsafe_allow_html=True)
with cr:
    st.markdown("<p style='color:#808495; font-weight:800; font-size:11px; margin-bottom:10px;'>RESOURCES</p>", unsafe_allow_html=True)
    st.button("Technical Documentation", use_container_width=True, key="d")
    st.button("Indicator Methodology", use_container_width=True, key="m")

# --- 5. BOTÓN INITIALIZE ---
st.markdown('<div class="main-btn-container">', unsafe_allow_html=True)
if st.button("INITIALIZE GLANCE TERMINAL", key="init"):
    st.switch_page("pages/01_Dashboard.py")
st.markdown('</div>', unsafe_allow_html=True)