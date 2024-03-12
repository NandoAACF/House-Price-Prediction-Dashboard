import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv('housing.csv')
    df.dropna(inplace=True)
    return df

df = load_data()

st.title('🏠 California Housing Dashboard')

st.sidebar.title('Filter 📌')

min_price = st.sidebar.slider('Min Price', int(df['median_house_value'].min()), int(df['median_house_value'].max()), int(df['median_house_value'].min()))

max_price = st.sidebar.slider('Max Price', int(df['median_house_value'].min()), int(df['median_house_value'].max()), int(df['median_house_value'].max()))

filtered_df = df[(df['median_house_value'] >= min_price) & (df['median_house_value'] <= max_price)]

ocean_proximity = st.sidebar.selectbox('Ocean Proximity', list(filtered_df['ocean_proximity'].unique()), index=None)
ocean_proximity = [ocean_proximity] if ocean_proximity else None

if ocean_proximity:
    filtered_df = filtered_df[filtered_df['ocean_proximity'].isin(ocean_proximity)]

col1, col2, col3, col4 = st.columns(4)

col1.metric('Total Blocks', value=filtered_df.shape[0])
col2.metric('Average House Price', value=int(filtered_df['median_house_value'].mean()))
col3.metric('Average Income', value=(int(filtered_df['median_income'].mean())*10000))
col4.metric('Average House Age', value=int(filtered_df['housing_median_age'].mean()))

col1.metric('Average Population', value=int(filtered_df['population'].mean()))
col2.metric('Average Households', value=int(filtered_df['households'].mean()))
col3.metric('Average Rooms', value=int(filtered_df['total_rooms'].mean()))
col4.metric('Average Bedrooms', value=int(filtered_df['total_bedrooms'].mean()))


st.subheader('🗺️ Map Distribution of Median House Price')
fig = px.scatter_mapbox(filtered_df, lat='latitude', lon='longitude',
                        hover_name='ocean_proximity',
                        color='median_house_value',
                        size='population',
                        zoom=4.3, height=550, color_continuous_scale=px.colors.sequential.Magma_r)

fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(title='Map Distribution of Median House Price')

st.plotly_chart(fig, theme='streamlit')


st.subheader('💵 Median House Price & Median Income')
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(filtered_df['median_house_value'], kde=True, bins=30)
plt.title('Distribution of Median House Price')
plt.xlabel('Median House Price')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.histplot(filtered_df['median_income'], kde=True, bins=30, color='orange')
plt.title('Distribution of Median Income')
plt.xlabel('Median Income')
plt.ylabel('Frequency')

plt.tight_layout()
st.pyplot(plt)

st.subheader('📊 Median House Price by Age Category')

filtered_df['age_category'] = pd.cut(filtered_df['housing_median_age'],
                            bins=[0, 10, 20, 30, 40, 50, np.inf],
                            labels=['0-10', '11-20', '21-30', '31-40', '41-50', '50+'])

median_values_by_age = filtered_df.groupby('age_category')['median_house_value'].median().sort_index()

plt.figure(figsize=(10, 5))

palette = sns.color_palette('magma_r')

sns.barplot(x=median_values_by_age.index, y=median_values_by_age.values, palette="magma_r")

plt.title('Median House Price by Age Category')
plt.xlabel('Age Category')
plt.ylabel('Median House Price')
plt.xticks(rotation=0)

st.pyplot(plt)

st.subheader('🛌 Total Bedrooms vs Population')

plt.figure(figsize=(10, 5))
scatter = plt.scatter(x='total_bedrooms', y='population', data=filtered_df, c=filtered_df['median_house_value'], cmap='magma_r')

plt.title('Total Bedrooms vs. Population')
plt.xlabel('Total Bedrooms')
plt.ylabel('Population')
plt.colorbar(scatter, label='Median House Value')

st.pyplot(plt)