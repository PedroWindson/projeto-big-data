import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Main Page",
)

conn = st.connection('matriz_db', type=sql)

def load_data():
    uploaded_file = st.file_uploader("Insira um arquivo:", ".xlsx")
    notas = pd.read_excel(uploaded_file, skiprows=[1])
    notas = notas.round(1)
    notas.to_sql("notas_alunos", conn, if_exists="append")
    return notas

st.write("# Bem-vindos as suas estatisticas")

st.sidebar.info("Selecione o que deseja ver")

notas = load_data()

st.dataframe(notas, hide_index=True)
