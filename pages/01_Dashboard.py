import streamlit as st
from datetime import datetime
from data_fetcher import get_crypto_data
from visualizer import plot_crypto

st.set_page_config(page_title="CRYPTO DASHBOARD", layout="wide")

# CSS REFINADO
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* BANNER DE CONSULTA REFINADO */
    .query-banner {
        background-color: #161a1e;
        border: 1px solid #1f2228;
        padding: 8px 20px;
        border-radius: 8px;
        display: flex;
        justify-content: space-between;
        margin-bottom: 25px;
    }
    
    .query-label { color: #808495; font-size: 13px; text-transform: uppercase; }
    .query-value { color: white; font-weight: 700; margin-left: 5px; }

    /* CUADROS DE MÉTRICAS CENTRADOS */
    div[data-testid="stMetric"] {
        background-color: #161a1e !important;
        border: 1px solid #1f2228 !important;
        border-radius: 12px !important;
        height: 130px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; /* CENTRADO HORIZONTAL */
        justify-content: center !important; /* CENTRADO VERTICAL */
        text-align: center !important;
    }

    /* Ajuste para que el valor y el delta también se centren */
    div[data-testid="stMetricValue"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    
    div[data-testid="stMetricDelta"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    div[data-testid="stMetricValue"] > div {
        font-size: 28px !important;
        font-weight: 700 !important;
        color: white !important;
    }

    div[data-testid="stMetricLabel"] > div > p {
        font-size: 12px !important;
        color: #00ffbb !important;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        width: 100%;
        text-align: center !important;
    }
    
    /* TERMINAL EN COLOR BLANCO */
    .terminal-title {
        color: white !important;
        font-size: 25px;
        font-weight: 800;
        margin-top: 0;
    }

    .block-container { max-width: 95% !important; padding-top: 1.5rem !important; }
    
    /* Borde del menú lateral */
    [data-testid="stSidebar"] { border-right: 2px solid #00ffbb; }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    # Título TERMINAL en Blanco
    st.markdown("<h2 class='terminal-title'>TERMINAL</h2>", unsafe_allow_html=True)
    st.divider()
    asset = st.selectbox("SELECT ASSET", ["Bitcoin", "Ethereum", "Solana"])
    mode = st.radio("TIMEFRAME", ["Monthly", "Detailed 24h"])
    q_date = st.date_input("START DATE", datetime(2025, 6, 1))
    st.divider()
    btn = st.button("RUN ANALYSIS", use_container_width=True)

st.markdown("<h1 style='text-align: center; color: white; margin-bottom:0;'>CRYPTO DASHBOARD</h1>", unsafe_allow_html=True)

if btn:
    tickers = {"Bitcoin": "BTC-USD", "Ethereum": "ETH-USD", "Solana": "SOL-USD"}
    df = get_crypto_data(tickers[asset], q_date, "monthly" if mode == "Monthly" else "intraday")
    
    if not df.empty:
        # Fecha de la consulta (último dato disponible)
        query_day = df.index[-1].strftime('%Y-%m-%d')
        
        st.markdown(f"""
            <div class="query-banner">
                <div><span class="query-label">ASSET:</span><span class="query-value">{asset.upper()}</span></div>
                <div><span class="query-label">CONSULTED DAY:</span><span class="query-value">{query_day}</span></div>
                <div><span class="query-label">MODE:</span><span class="query-value">{mode.upper()}</span></div>
            </div>
        """, unsafe_allow_html=True)

        m1, m2, m3 = st.columns(3)
        perf = ((df['Close'].iloc[-1] - df['Open'].iloc[0]) / df['Open'].iloc[0]) * 100
        
        # Las métricas ahora aparecerán centradas gracias al CSS
        m1.metric("LAST PRICE", f"${df['Close'].iloc[-1]:,.2f}")
        m2.metric("VOLATILITY", f"{(df['Close'].pct_change().std()*100):.2f}%")
        m3.metric("SENTIMENT", "BULLISH" if perf > 0 else "BEARISH", delta=f"{perf:.2f}%")
        
        st.markdown("<br>", unsafe_allow_html=True)
        fig = plot_crypto(df, {}, q_date, mode)
        st.plotly_chart(fig, use_container_width=True)