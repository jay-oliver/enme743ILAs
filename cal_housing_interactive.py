from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import seaborn as sns
cal_housing = fetch_california_housing(data_home='.')
X = cal_housing.data
avg_price = cal_housing.target
feature_names = cal_housing.feature_names
df=pd.DataFrame(np.hstack([X,avg_price[:,np.newaxis]]),columns=np.hstack([feature_names,'price']))
print(df.head())
#Plots each data point on a Longitude Latitude map of California with price indicated in some fashion according to what
# you think is best (e.g., annotations, coloring, alpha values, marker size, surfaces, parallel plots, etc. the choice is yours).
x = df.Latitude
y = df.Longitude
color = df.price

scatter = plt.scatter(x, y, c=color, cmap='turbo', s=10)
colorbar = plt.colorbar(scatter, label='Value')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('California Home Prices')
plt.show()
#Allow users to interact with this map by enabling interactive filtering on other features like minimums and maximums
# of HouseAge, AveRooms, AveBedrms, AveOccup, etc. such that the dataset being plotted can be
# manipulated or reduced interactively.
min_price = df['price'].min()
max_price = df['price'].max()
min_medinc = df['MedInc'].min()
max_medinc = df['MedInc'].max()
min_house_age = df['HouseAge'].min()
max_house_age = df['HouseAge'].max()
min_averooms = df['AveRooms'].min()
max_averooms = df['AveRooms'].max()
min_avebedrooms = df['AveBedrms'].min()
max_avebedrooms = df['AveBedrms'].max()
min_occup = df['AveOccup'].min()
max_occup = df['AveOccup'].max()
min_pop = df['Population'].min()
max_pop = df['Population'].max()
# Define the range slider
price_range = st.slider('Select Price Range:', min_price, max_price, (min_price, max_price), step=0.1)
house_age_range = st.slider('Select House Age Range:', min_house_age, max_house_age, (min_house_age, max_house_age), step=1.0)
rooms_range = st.slider('Select Average Rooms Range:', min_averooms, max_averooms, (min_averooms, max_averooms), step=0.1)
bedrooms_range= st.slider('Select Average Bedrooms Range:', min_avebedrooms, max_avebedrooms, (min_avebedrooms, max_avebedrooms), step=0.05)
occup_range= st.slider('Select Average Occupants Range:', min_occup, max_occup, (min_occup, max_occup), step=0.5)
medinc_range= st.slider('Select Median Income Range:', min_medinc, max_medinc, (min_medinc, max_medinc), step=0.05)
pop_range= st.slider('Select Population Range:', min_pop, max_pop, (min_pop, max_pop), step=0.05)

# Filter data based on slider
filtered_df = df[
    (df['price'] >= price_range[0]) & (df['price'] <= price_range[1]) &
    (df['HouseAge'] >= house_age_range[0]) & (df['HouseAge'] <= house_age_range[1]) &
    (df['AveRooms'] >= rooms_range[0]) & (df['AveRooms'] <= rooms_range[1]) &
    (df['AveBedrms'] >= bedrooms_range[0]) & (df['AveBedrms'] <= bedrooms_range[1]) &
    (df['AveOccup'] >= occup_range[0]) & (df['AveOccup'] <= occup_range[1]) &
    (df['MedInc'] >= medinc_range[0]) & (df['MedInc'] <= medinc_range[1]) &
    (df['Population'] >= pop_range[0]) & (df['Population'] <= pop_range[1])
]

# Create the scatter plot
fig = px.scatter(filtered_df, x='Latitude', y='Longitude', color='price', color_continuous_scale='plasma', title='Interactive Scatter Plot with Slider')

# Display the plot
st.plotly_chart(fig)
