import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

bike_df=pd.read_csv("bike_df.csv")
datetime_columns=["dteday"]
bike_df.sort_values(by="dteday", inplace=True)
bike_df.reset_index(inplace=True)

for column in datetime_columns:
    bike_df[column] = pd.to_datetime(bike_df[column])

# Membuat komponen filter
min_date = bike_df["dteday"].min()
max_date = bike_df["dteday"].max()
with st.sidebar :
    # Menambahkan logo 
    st.image("https://raw.githubusercontent.com/NurShofiatun/ProyekAnalisis/main/istockphoto-1180641993-1024x1024.jpg")

    # Mengambil start_date dan end_date dari date_input
    start_date, end_date = st.date_input(
        label = "Rentang Waktu", 
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = bike_df[(bike_df["dteday"] >= str(start_date)) &
                  (bike_df["dteday"] <= str(end_date))]

# Menambahkan Header Dashboard
st.header("Bike Sharing :sparkles:")

# Menampilkan Frekuensi Peminjaman Sepeda 
st.subheader("Jumlah Peminjaman Sepeda")

col1, col2, col3 = st.columns(3)
with col1 :
    total_loan = main_df.cnt.sum()
    st.metric("Total Peminjaman Sepeda : ", value = total_loan)

with col2 : 
    total_regis = main_df.registered.sum()
    st.metric("Total Peminjaman Sepeda (Registered) : ", value=total_regis)

with col3 :
    total_casual = main_df.casual.sum()
    st.metric("Total Peminjaman Sepeda (Casual) : ", value=total_casual)

fig, ax = plt.subplots(figsize=(16,8))
ax.plot(
    main_df["dteday"],
    main_df["cnt"],
    marker = "o",
    color = "#90CAF9"
)
ax.set_ylabel("Jumlah Peminjaman", fontsize=22)
ax.set_xlabel("Tanggal Peminjaman", fontsize=17)
ax.tick_params(axis="y", labelsize = 20)
ax.tick_params(axis="x", labelsize = 15)

st.pyplot(fig)

# Menampilkan proporsi peminjaman sepeda berdasarkan cuaca
st.subheader("Proporsi Peminjaman Sepeda berdasarkan Cuaca")

fig, ax = plt.subplots(figsize=(20,10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="cnt",
    x="weathersit",
    data=main_df.sort_values(by="cnt", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_ylabel("Jumlah Peminjaman", fontsize=33)
ax.set_xlabel("Cuaca", fontsize=38)
ax.tick_params(axis="x", labelsize=35)
ax.tick_params(axis="y", labelsize=30)
st.pyplot(fig)

# Menampilkan proporsi peminjaman sepeda untuk hari kerja dan hari libur
st.subheader("Proporsi Peminjaman Sepeda untuk Workingday dan Weekend")

fig, ax = plt.subplots(figsize=(20,10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="cnt",
    x="workingday",
    data=main_df.sort_values(by="cnt", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_ylabel("Jumlah Peminjaman", fontsize=33)
ax.set_xlabel(None)
ax.tick_params(axis="x", labelsize=35)
ax.tick_params(axis="y", labelsize=30)
st.pyplot(fig)

# Menampilkan proporsi peminjaman sepeda berdasarkan musim
st.subheader("Proporsi Peminjaman Sepeda berdasarkan Musim")

fig, ax = plt.subplots(figsize=(20,10))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y="cnt",
    x="season",
    data=main_df.sort_values(by="cnt", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_ylabel("Jumlah Peminjaman", fontsize=33)
ax.set_xlabel("Musim", fontsize=33)
ax.tick_params(axis="x", labelsize=35)
ax.tick_params(axis="y", labelsize=30)
st.pyplot(fig)


# Menampilkan korelasi atau hubungan suhu dan kecepatan angin terhadap peminjaman sepeda
st.subheader("Korelasi antara Suhu, Kecepatan Angin, dan Jumlah Peminjaman Sepeda")

# Menghitung korelasi
correlation_matrix = main_df[["temp", "windspeed", "cnt"]].corr()

# Membuat Heatmap
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(correlation_matrix, annot = True, cmap  = "coolwarm", fmt = ".2f")
st.pyplot(fig)