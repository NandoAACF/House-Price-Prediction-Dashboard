import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(
    page_title="More Insights",
    page_icon="📋"
)

@st.cache_data
def load_data():
    df = pd.read_csv('housing.csv')
    df.dropna(inplace=True)
    return df

df = load_data()

st.title('📋 California Housing Extra Insights')

st.write('### **Bagaimana distribusi harga rumah berdasarkan tipe lingkungannya?**')
plt.figure(figsize=(8, 5))
sns.boxplot(x='ocean_proximity', y='median_house_value', data=df, palette='rainbow')
plt.title('House Price by Ocean Proximity')
plt.xlabel('Ocean Proximity')
plt.ylabel('House Price')
plt.xticks(rotation=45)
st.pyplot(plt)
with st.expander('📋 Analisis Insights', expanded=True):
    st.info('Tampak bahwa rumah yang berada di Pulau Avalon memiliki distribusi harga yang jauh lebih mahal dibandingkan dengan lokasi lainnya.')
    st.info('Hal tersebut masuk akal karena teori high demand dan low supply. Jumlah rumah yang berada di Pulau Avalon sedikit, padahal peminatnya banyak sehingga harga rumah-rumah tersebut menjadi mahal.')
    st.info('Rumah di tengah pulau memiliki distribusi harga yang paling murah, tetapi ada juga beberapa rumah di tengah pulau yang memiliki harga mahal. Hal tersebut karena jumlah rumah yang cukup banyak sehingga harga harus bersaing dan tidak memiliki sesuatu yang spesial, seperti view laut.')
    st.info('Di sisi lain, rumah yang berada di dekat laut memiliki distribusi harga yang cukup bervariasi, tetapi cenderung berada di antara kedua lokasi sebelumnya.')

st.write('### **Bagaimana distribusi umur rumah berdasarkan tipe lingkungannya?**')
plt.figure(figsize=(8, 5))
sns.boxplot(x='ocean_proximity', y='housing_median_age', data=df, palette='Set1')
plt.title('Median House Age by Ocean Proximity')
plt.xlabel('Ocean Proximity')
plt.ylabel('Median House Age')
plt.xticks(rotation=45)
st.pyplot(plt)
with st.expander('📋 Analisis Insights', expanded=True):
    st.info('Tampak bahwa rumah yang berada di Pulau Avalon memiliki distribusi umur rumah yang paling tua dibandingkan dengan lokasi lainnya, hampir semuanya berada di antara 30-50 tahun.')
    st.info('Hal tersebut karena Pulau Avalon merupakan lokasi yang sudah berkembang sejak lama dan sangat minim lahan kosong untuk membangun rumah baru.')
    st.info('Rumah yang berada di dekat teluk juga memiliki distribusi umur rumah yang cukup tua, tetapi ada juga beberapa rumah yang berumur muda. Hal tersebut karena lokasi tersebut memiliki beberapa daerah yang sudah berkembang dan beberapa daerah yang masih berkembang.')
    st.info('Rumah di lokasi lainnya memiliki harga yang cukup bervariasi, namun mayoritas cenderung lebih muda dari kedua lokasi sebelumnya.')

st.write('### **Bagaimana korelasi antara jumlah populasi dengan harga rumah?**')
plt.figure(figsize=(8, 5))
sns.scatterplot(x='median_house_value', y='population', data=df, color='red')
plt.title('Population vs House Price')
plt.xlabel('House Price')
plt.ylabel('Population')
st.pyplot(plt)
with st.expander('📋 Analisis Insights', expanded=True):
    st.info('Tampak bahwa tidak ada korelasi yang jelas antara jumlah populasi dengan harga rumah.')
    st.info('Hal tersebut masuk akal karena ada banyak faktor yang lebih mempengaruhi tinggi rendahnya harga rumah, seperti lokasi dan demand rumah.')


st.write('### Bagaimana korelasi antara harga rumah dengan pendapatan warganya?')
plt.figure(figsize=(18, 6))

plt.subplot(1, 2, 1)
plt.scatter(df['longitude'], df['latitude'], c=df['median_house_value'], cmap='jet', alpha=0.4)
plt.colorbar(label='House Price')
plt.title('Geographic Distribution of House Price')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.subplot(1, 2, 2)
plt.scatter(df['longitude'], df['latitude'], c=df['median_income'], cmap='jet', alpha=0.4)
plt.colorbar(label='Income (in thousand USD)')
plt.title('Geographic Distribution of Income')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.tight_layout()
st.pyplot(plt)
with st.expander('📋 Analisis Insights', expanded=True):
    st.info('Tampak jelas bahwa para warga yang tinggal di lokasi dengan harga rumah yang tinggi memiliki pendapatan yang tinggi pula, begitu pula sebaliknya.')
    st.info('Hal tersebut masuk akal karena harga rumah yang tinggi cenderung dibeli oleh orang yang memiliki pendapatan tinggi juga.')
    st.info('Dalam kasus ini, harga rumah yang tinggi berada di dekat laut. Kemungkinan besar lapangan pekerjaan di daerah tersebut cenderung lebih baik dibandingkan dengan daerah lainnya.')

# st.write("### **Apakah pendapatan berbanding lurus dengan harga rumah?**")
# df['income_category'] = pd.cut(df['median_income'],
#                                 bins=[0, 3, 6, np.inf],
#                                 labels=['Low', 'Medium', 'High'])
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='income_category', y='median_house_value', data=df, palette='rainbow')
# plt.title('Median House Value by Income Category')
# plt.xlabel('Income Category')
# plt.ylabel('Median House Value')
# st.pyplot(plt)

st.write('### **Apakah ada korelasi antara usia rumah dengan total ruangan?**')
df['age_category'] = pd.cut(df['housing_median_age'],
                            bins=[0, 10, 20, 30, 40, 50, np.inf],
                            labels=['0-10', '11-20', '21-30', '31-40', '41-50', '50+'])

plt.figure(figsize=(12, 6))
sns.boxplot(x='age_category', y='total_rooms', data=df, palette='nipy_spectral')
plt.title('Total Rooms by Age Category')
plt.xlabel('Age Category')
plt.ylabel('Total Rooms')
st.pyplot(plt)
with st.expander('📋 Analisis Insights', expanded=True):
    st.info('Tampak bahwa rumah yang berumur lebih muda memiliki distribusi total ruangan yang lebih banyak dibandingkan dengan rumah yang berumur lebih tua.')
    st.info('Hal tersebut kemungkinan terjadi karena rumah yang berumur lebih tua biasanya memiliki ukuran ruangan yang lebih besar sehingga jumlah ruangan yang ada lebih sedikit, sedangkan rumah jaman sekarang cenderung memiliki jumlah ruangan yang lebih banyak, tetapi ukuran setiap ruangnya lebih kecil.')


