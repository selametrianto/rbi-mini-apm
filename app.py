import streamlit as st
import pandas as pd

st.set_page_config(page_title="RBI Mini APM", layout="wide")

# ⚠️ PASTIKAN NAMA FILE SAMA PERSIS
EXCEL_FILE = "Patuha_RBI_Mini_APM_GE_Like_Software_View.xlsx"

st.title("RBI Mini APM System")
st.caption("Connected to Excel")

try:
    excel_file = pd.ExcelFile(EXCEL_FILE)
st.write("Available Sheets:", excel_file.sheet_names)

target_sheet = "01_ASSET_INPUT_FULL"

if target_sheet in excel_file.sheet_names:
    df = pd.read_excel(EXCEL_FILE, sheet_name=target_sheet)
else:
    st.warning(f"Sheet '{target_sheet}' tidak ditemukan. Pakai sheet pertama.")
    df = pd.read_excel(EXCEL_FILE, sheet_name=0)
except Exception as e:
    st.error("Gagal baca Excel")
    st.write(e)
