import streamlit as st
import pandas as pd

st.set_page_config(page_title="RBI Mini APM", layout="wide")

# ⚠️ PASTIKAN NAMA FILE SAMA PERSIS
EXCEL_FILE = "Patuha_RBI_Mini_APM_GE_Like_Software_View.xlsx"

st.title("RBI Mini APM System")
st.caption("Connected to Excel")

try:
    df = pd.read_excel(EXCEL_FILE)

    st.success("Excel berhasil dibaca")

    col1, col2 = st.columns(2)
    col1.metric("Total Rows", len(df))
    col2.metric("Total Columns", len(df.columns))

    st.subheader("Preview Data")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("Gagal baca Excel")
    st.write(e)
