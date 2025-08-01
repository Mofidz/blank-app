import streamlit as st
import matplotlib.pyplot as plt

# Data Nabi dan Umur
nabi = [
    "Adam", "Idris", "Nuh", "Hud", "Shaleh", "Ibrahim", "Luth", "Ismail", "Ishaq", "Ya'qub",
    "Yusuf", "Syu'aib", "Ayyub", "Dzulkifli", "Musa", "Harun", "Dawud", "Sulaiman", "Ilyas",
    "Ilyasa’", "Yunus", "Zakaria", "Yahya", "Isa", "Muhammad"
]

umur = [
    930, 865, 950, 464, 280, 175, 100, 137, 180, 147,
    110, 242, 93, 85, 120, 123, 100, 85, 105,
    90, 110, 120, 35, 33, 63
]

# Judul
st.title("Visualisasi Umur 25 Nabi dalam Islam")

# Buat grafik
fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.barh(nabi[::-1], umur[::-1], color='teal')
ax.set_xlabel("Umur (tahun)")
ax.set_title("Umur Para Nabi (Perkiraan Sejarah Islam)")

# Tampilkan nilai umur
for bar in bars:
    width = bar.get_width()
    ax.text(width + 5, bar.get_y() + bar.get_height()/2, str(width), va='center')

ax.grid(axis='x', linestyle='--', alpha=0.7)
st.pyplot(fig)
