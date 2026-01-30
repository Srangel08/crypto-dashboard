# GLANCE TERMINAL - Crypto Dashboard

GLANCE es una plataforma de análisis financiero desarrollada en Python utilizando el framework Streamlit. El sistema permite el monitoreo de activos digitales en tiempo real y la visualización de indicadores técnicos avanzados mediante una interfaz optimizada para entornos de trading.

## Características Principales

* Monitoreo de Mercado: Seguimiento de precios para BTC, ETH, SOL y BNB utilizando la API de Yahoo Finance.
* Visualización Avanzada: Implementación de gráficos de velas japonesas, flujo de volumen y oscilador RSI (Relative Strength Index).
* Modos de Análisis: Soporte para consultas históricas mensuales y análisis detallado de 24 horas (intradía).
* Interfaz Profesional: Diseño basado en CSS personalizado con tipografía Inter y esquema de colores de alto contraste para terminales.

## Estructura del Sistema

La arquitectura del proyecto se divide en los siguientes módulos:

* main.py: Punto de entrada de la aplicación y monitor de precios en vivo.
* data_fetcher.py: Módulo encargado de la extracción, limpieza y normalización de datos.
* visualizer.py: Motor de renderizado de gráficos basado en la librería Plotly.
* pages/01_Dashboard.py: Interfaz principal de análisis técnico.

## Requisitos de Instalación

1. Clonar el repositorio:
   git clone https://github.com/Srangel08/crypto-dashboard.git
   cd crypto-dashboard

2. Instalar las dependencias necesarias:
   pip install streamlit yfinance pandas plotly

3. Ejecutar la plataforma:
   python -m streamlit run main.py

## Metodología de Indicadores

* Acción de Precio: Representación precisa mediante Candlesticks de alta fidelidad.
* Flujo de Volumen: Identificación visual de la relación entre apertura y cierre por periodo.
* Momento RSI: Cálculo del Índice de Fuerza Relativa con periodo de 14 sesiones para identificar niveles de sobrecompra y sobreventa.

## Especificaciones Técnicas
* Python 3.9+
* Integración con Yahoo Finance API
* Renderizado dinámico vía Streamlit Cloud

---
<img width="1365" height="743" alt="Screenshot 2026-01-22 203503" src="https://github.com/user-attachments/assets/05035f3b-c4f3-4cc9-aa35-289aac5aad4d" />

