import streamlit as st
#from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import pandas as pd
import os


def main():


    

    df = pd.read_csv("src/edu_pad/static/csv/data_extractora.csv")
    columnas = ["Productos","Precios","Calificaciones"]
    df_2 = df[columnas]
    profile = ProfileReport(df_2, title="Dashboard Indicador Dolar")
    st.title("Análisis de Datos")
    #st.write(profile.to_html(),unsafe_allow_html=True)
    st.components.v1.html(profile.to_html(), height=600, scrolling=True)


if __name__ == "__main__":
    main()