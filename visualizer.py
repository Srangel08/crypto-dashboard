import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_crypto(df, info, date_obj, mode):
    # Indicadores
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    df['RSI'] = 100 - (100 / (1 + (gain / loss)))

    # Aumentamos vertical_spacing para mayor claridad entre secciones
    fig = make_subplots(
        rows=3, cols=1, 
        shared_xaxes=True,
        vertical_spacing=0.1, 
        row_heights=[0.55, 0.15, 0.3],
        subplot_titles=('<b>PRICE ACTION (USD)</b>', '<b>VOLUME FLOW</b>', '<b>RSI MOMENTUM</b>')
    )

    # 1. Velas
    fig.add_trace(go.Candlestick(
        x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
        increasing_line_color='#00ffbb', decreasing_line_color='#ff3333'
    ), row=1, col=1)
    
    # 2. Volumen
    colors = ['#00ffbb' if c >= o else '#ff3333' for o, c in zip(df['Open'], df['Close'])]
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], marker_color=colors, opacity=0.8), row=2, col=1)

    # 3. RSI
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='#00d4ff', width=2),
                             fill='tozeroy', fillcolor='rgba(0, 212, 255, 0.1)'), row=3, col=1)

    fig.update_layout(
        template='plotly_dark',
        xaxis_rangeslider_visible=False,
        height=900,
        paper_bgcolor='#0e1117',
        plot_bgcolor='#0e1117',
        showlegend=False,
        margin=dict(t=50, b=20, l=10, r=10) # Márgenes externos de la gráfica
    )

    fig.update_yaxes(tickprefix="$", tickformat=",", gridcolor='#1f2228', row=1, col=1)
    fig.update_yaxes(gridcolor='#1f2228', row=2, col=1)
    fig.update_yaxes(range=[0, 100], gridcolor='#1f2228', row=3, col=1)

    return fig