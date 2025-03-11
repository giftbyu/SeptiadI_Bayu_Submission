import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_data = pd.read_csv('day.csv')
hour_data = pd.read_csv('hour.csv')

st.title("🚲 Bike Rental Dashboard")

st.header("📊 Dataset Information")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Informasi Dataset Day")
    st.write(day_data.head())
with col2:
    st.subheader("Informasi Dataset Hour")
    st.write(hour_data.head())

st.header("❌ Missing Values Check")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Missing Values in 'day' Dataset")
    st.write(day_data.isnull().sum())
with col2:
    st.subheader("Missing Values in 'hour' Dataset")
    st.write(hour_data.isnull().sum())

st.header("📑 Duplicate Check")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Duplicate Rows in 'day' Dataset")
    st.write(day_data.duplicated().sum())
with col2:
    st.subheader("Duplicate Rows in 'hour' Dataset")
    st.write(hour_data.duplicated().sum())

st.header("📈 Descriptive Statistics")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Descriptive Statistics for 'day' Dataset")
    st.write(day_data.describe())
with col2:
    st.subheader("Descriptive Statistics for 'hour' Dataset")
    st.write(hour_data.describe())

st.header("🔍 Insight dari Data")
st.markdown("""
1. **Tidak ada nilai yang hilang (missing values)**, yang berarti dataset sudah lengkap dan siap digunakan untuk analisis lebih lanjut.
2. **Dataset tidak mengandung duplikasi**, sehingga setiap baris data adalah unik dan dapat digunakan untuk analisis tanpa pengaruh duplikasi.
3. Kolom **cnt (jumlah penyewaan sepeda)** memiliki rentang yang luas, yang menunjukkan adanya fluktuasi tinggi dalam penyewaan sepeda di waktu yang berbeda.
""")

st.header("📅 Penyewaan Berdasarkan Hari")
weekday_rentals = day_data.groupby('weekday')['cnt'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=weekday_rentals, x='weekday', y='cnt', palette='coolwarm')
plt.title("Total Penyewaan Sepeda Berdasarkan Hari dalam Seminggu", fontsize=16)
plt.xlabel("Hari dalam Minggu", fontsize=12)
plt.ylabel("Jumlah Penyewaan", fontsize=12)
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'])
st.pyplot(plt)
st.markdown("""
Penyewaan sepeda bervariasi setiap hari dalam seminggu. Grafik ini menunjukkan jumlah penyewaan sepeda berdasarkan hari dalam seminggu.
""")

st.header("🌤️ Penyewaan Berdasarkan Cuaca")
weather_rentals = day_data.groupby('weathersit')['cnt'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=weather_rentals, x='weathersit', y='cnt', palette='muted')
plt.title("Total Penyewaan Sepeda Berdasarkan Cuaca", fontsize=16)
plt.xlabel("Situasi Cuaca", fontsize=12)
plt.ylabel("Jumlah Penyewaan", fontsize=12)
plt.xticks([0, 1, 2], ['Cerah', 'Berawan', 'Hujan'])
st.pyplot(plt)
st.markdown("""
Grafik ini menunjukkan jumlah penyewaan sepeda berdasarkan kondisi cuaca. Terdapat tiga kategori cuaca: cerah, berawan, dan hujan.
""")

st.header("🌸 Penyewaan Berdasarkan Musim")
seasonal_rentals = day_data.groupby('season')['cnt'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=seasonal_rentals, x='season', y='cnt', palette='viridis')
plt.title("Total Penyewaan Sepeda Berdasarkan Musim", fontsize=16)
plt.xlabel("Musim", fontsize=12)
plt.ylabel("Jumlah Penyewaan", fontsize=12)
plt.xticks([0, 1, 2, 3], ['Musim Dingin', 'Panas', 'Gugur', 'Semi'])
st.pyplot(plt)
st.markdown("""
Penyewaan sepeda di setiap musim menunjukkan tren berbeda. Grafik ini membandingkan jumlah penyewaan pada setiap musim.
""")

st.header("📈 Tren Penyewaan Harian")
daily_rentals = day_data.groupby('dteday')['cnt'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.scatterplot(data=daily_rentals, x='dteday', y='cnt', color='b', marker='o')
plt.title("Total Penyewaan Sepeda Per Hari", fontsize=16)
plt.xlabel("Tanggal", fontsize=12)
plt.ylabel("Jumlah Penyewaan", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(plt)
st.markdown("""
Tren penyewaan sepeda setiap hari dapat dilihat di grafik ini. Penyewaan bervariasi tergantung pada banyak faktor, termasuk cuaca dan musim.
""")

st.header("📊 Tren Penyewaan Bulanan")
monthly_rentals = day_data.groupby('mnth')['cnt'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=monthly_rentals, x='mnth', y='cnt', palette='coolwarm')
plt.title("Total Penyewaan Sepeda Berdasarkan Bulan", fontsize=16)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Jumlah Penyewaan", fontsize=12)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(plt)
st.markdown("""
Grafik ini menunjukkan total jumlah penyewaan sepeda untuk setiap bulan, memungkinkan analisis tren bulanan.
""")
