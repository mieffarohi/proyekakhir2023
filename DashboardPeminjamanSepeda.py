import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from altair import Chart

# Membaca dataset
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Menampilkan judul dashboard
st.title('Bike Sharing Dashboard')

# Convert kolom 'dteday' ke tipe data datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Menambahkan input tanggal untuk memilih rentang waktu
date_range = st.date_input('Pilih Rentang Tanggal', [day_df['dteday'].min(), day_df['dteday'].max()])

# Filter dataset berdasarkan rentang waktu yang dipilih
filtered_day_df = day_df[(day_df['dteday'] >= str(date_range[0])) & (day_df['dteday'] <= str(date_range[1]))]
filtered_hour_df = hour_df[(hour_df['dteday'] >= str(date_range[0])) & (hour_df['dteday'] <= str(date_range[1]))]

# Menampilkan dataset jika diinginkan
if st.checkbox('Tampilkan Data Harian'):
    st.dataframe(filtered_day_df)
if st.checkbox('Tampilkan Data Jam'):
    st.dataframe(filtered_hour_df)

# Visualisasi Waktu dengan Jumlah Peminjaman Terbanyak dan Paling Sedikit (Harian)
fig_day, axes_day = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

# Barplot untuk jumlah peminjaman terbanyak (Harian)
sns.barplot(x='dteday', y='cnt', data=filtered_day_df, ax=axes_day[0], color='lightblue')
axes_day[0].set_xlabel('Tanggal (Harian)')
axes_day[0].set_ylabel('Jumlah Peminjaman Sepeda')
axes_day[0].set_title('Peminjaman Terbanyak (Harian)', fontsize=15)
axes_day[0].tick_params(axis='x', rotation=45)

# Barplot untuk jumlah peminjaman paling sedikit (Harian)
sns.barplot(x='dteday', y='cnt', data=filtered_day_df, ax=axes_day[1], color='lightblue')
axes_day[1].set_xlabel('Tanggal (Harian)')
axes_day[1].set_ylabel('Jumlah Peminjaman Sepeda')
axes_day[1].set_title('Peminjaman Paling Sedikit (Harian)', fontsize=15)
axes_day[1].tick_params(axis='x', rotation=45)

# Menambahkan judul keseluruhan visualisasi (Harian)
st.write("## Visualisasi Harian")
st.pyplot(fig_day)

# Visualisasi Distribusi Peminjaman Sepeda pada Jam-jam Sibuk (Jam)
hourly_distribution = filtered_hour_df.groupby(by="hr").agg({
    "cnt": "sum"
}).reset_index()

fig_hour, ax_hour = plt.subplots(figsize=(12, 6))

# Barplot untuk distribusi peminjaman sepeda pada jam-jam sibuk (Jam)
sns.barplot(x='hr', y='cnt', data=hourly_distribution, color='lightgreen', ax=ax_hour)
ax_hour.set_xlabel('Jam dalam Sehari')
ax_hour.set_ylabel('Jumlah Peminjaman Sepeda')
ax_hour.set_title('Distribusi Peminjaman Sepeda pada Jam-jam Sibuk (Jam)', fontsize=15)

# Menambahkan judul visualisasi (Jam)
st.write("## Distribusi Jam-jam Sibuk")
st.pyplot(fig_hour)
