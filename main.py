import streamlit as st
import yfinance as yf

st.set_page_config(page_title="CRYPTO DASHBOARD", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* CABECERA LIMPIA */
    .main-header {
        font-size: 75px;
        font-weight: 900;
        color: white;
        text-align: center;
        margin-top: -50px;
        letter-spacing: -3px;
    }
    
    /* CUADROS LIVE - SIMETRÍA TOTAL */
    .live-card {
        background-color: #161a1e;
        border: 1px solid #1f2228;
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: all 0.3s ease;
    }
    .live-card:hover { border-color: #00ffbb; box-shadow: 0px 0px 20px rgba(0, 255, 187, 0.1); }
    
    .price-text { font-size: 38px; font-weight: 800; color: white; margin: 10px 0; }
    .asset-label { color: #808495; font-size: 14px; letter-spacing: 4px; font-weight: 700; }
    
    /* NAVEGACIÓN LATERAL MEJORADA */
    [data-testid="stSidebar"] {
        background-color: #111418 !important;
        border-right: 1px solid #1f2228;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-header">CRYPTO DASHBOARD</h1>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("MARKET LIVE FEED")
cols = st.columns(4)
assets = {"BTC-USD": "BITCOIN", "ETH-USD": "ETHEREUM", "SOL-USD": "SOLANA", "BNB-USD": "BINANCE"}

for col, (ticker, name) in zip(cols, assets.items()):
    t = yf.Ticker(ticker)
    price = t.fast_info['last_price']
    change = ((price - t.fast_info['open']) / t.fast_info['open']) * 100
    with col:
        st.markdown(f"""
            <div class="live-card">
                <p class="asset-label">{name}</p>
                <p class="price-text">${price:,.2f}</p>
                <p style="color:{'#00ffbb' if change > 0 else '#ff3333'}; font-weight:bold; font-size:22px;">
                    {'▲' if change > 0 else '▼'} {abs(change):.2f}%
                </p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button(" OPEN ANALYSIS TERMINAL", use_container_width=True):
        st.switch_page("pages/01_Dashboard.py")