import streamlit as st 
import pandas as pd
import streamlit_extras.dataframe_explorer as dataframe_explorer
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv(r'C:\Users\acer\Bike-sharing-data11\day.csv')
st.table(day_df.head())

# Mapping the nomor season ke nama musim aktual agar lebih mudah dibaca
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
day_df['season_name'] = day_df['season'].map(season_mapping)

# Menggabungkan jumlah total penyewaan sepeda per musim
seasonal_data = day_df.groupby('season_name')['cnt'].sum().reset_index()

# Menyortir musim untuk the plot
seasonal_data['season_name'] = pd.Categorical(seasonal_data['season_name'], categories=['Spring', 'Summer', 'Fall', 'Winter'])
seasonal_data = seasonal_data.sort_values('season_name')


plt.figure(figsize=(10, 6))
sns.barplot(x='season_name', y='cnt', data=seasonal_data, palette='coolwarm')
plt.title('Total Number of Bike Rentals per Season')
plt.xlabel('Season')
plt.ylabel('Total Bike Rentals')
plt.grid(axis='y')
st.pyplot(plt)


#Pertanyaan 2:
#- Lebih banyak terjadi transaksi saat holiday atau non holiday?

# Menggabungkan jumlah total penyewaan sepeda untuk holiday dan non-holiday
holiday_data = day_df.groupby('holiday')['cnt'].sum().reset_index()

# Me mapping holiday ke nilai yang lebih mudah dibaca
holiday_data['holiday'] = holiday_data['holiday'].map({0: 'Non-Holiday', 1: 'Holiday'})

# Membuat bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x='holiday', y='cnt', data=holiday_data, palette='viridis')
plt.title('Total Number of Bike Rentals: Holiday vs Non-Holiday')
plt.xlabel('Day Type')
plt.ylabel('Total Bike Rentals')
plt.grid(axis='y')
st.pyplot(plt)


# def data_frame_hour(dataframe):
    
#     st.markdown("## :green[Data Frame Hour ]")
#     filtered_df = dataframe_explorer(dataframe, case=False)
#     st.dataframe(filtered_df, use_container_width=True)
    
# data_frame_hour(day_df)