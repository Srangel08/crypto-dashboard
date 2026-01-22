import yfinance as yf
import pandas as pd
from datetime import timedelta, datetime

def get_crypto_data(symbol, start_date, mode="monthly"):
    try:
        if mode == "monthly":
            next_month = start_date.replace(day=28) + timedelta(days=4)
            end_date = next_month.replace(day=1) - timedelta(days=1)
            interval = '1d'
        else:
            end_date = start_date + timedelta(days=1)
            days_diff = (datetime.now().date() - start_date).days
            # Ajuste de intervalo según antigüedad para evitar errores de Yahoo
            interval = '15m' if days_diff < 50 else '1h'
        
        # Bajamos datos con margen para que los indicadores (RSI/MA) no salgan vacíos al inicio
        df = yf.download(symbol, start=start_date - timedelta(days=20), end=end_date, interval=interval, progress=False)
        
        if df.empty: return pd.DataFrame()
        if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
        
        df.index = df.index.tz_localize(None)
        df.columns = [str(col).capitalize() for col in df.columns]
        
        # Recorte exacto para cumplir con el requerimiento visual
        mask = (df.index >= pd.Timestamp(start_date)) & (df.index <= pd.Timestamp(end_date))
        return df.loc[mask].dropna()
    except:
        return pd.DataFrame()