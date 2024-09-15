from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from itertools import cycle, islice
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import random

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

import warnings
warnings.filterwarnings("ignore")


@st.cache_data
def load_data(path: str):
	data = pd.read_excel(path)
	return data


data = load_data("lib/hhh.xlsx")




st.sampled_df = data[(data['id1'] % 10) == 0]
st.write("shape of sample data set")
st.sampled_df.shape


st.sampled_df.describe().transpose()




rows_before = st.sampled_df.shape[0]
sampled_df = st.sampled_df.dropna()
rows_after = sampled_df.shape[0]

st.write("head of data set")
sampled_df.columns

features1 = ['temprature1', 'temprature2']
features2 = ['water_level1', 'water_level2']

select_df1 = sampled_df[features1]
select_df2 = sampled_df[features2]
st.write("head of Temprature")
select_df1.columns
st.write("head of Water_level")
select_df2.columns
st.write("Data of Temprature")
select_df1
st.write("Data of Water_level")
select_df2
X = StandardScaler().fit_transform(select_df1)
st.write("StandardScaler Data of Temprature")
X
Y = StandardScaler().fit_transform(select_df2)
st.write("StandardScaler Data of Water_level")
Y
kmeans = KMeans(n_clusters=12)
model = kmeans.fit(X)
print("model\n", model)

st.write("StandardScaler Data after kmeans of Temprature")
centers1 = model.cluster_centers_
centers1

def pd_centers(featuresUsed, centers1):
	colNames = list(featuresUsed)
	colNames.append('prediction')

	Z = [np.append(A, index) for index, A in enumerate(centers1)]

	P = pd.DataFrame(Z, columns=colNames)
	P['prediction'] = P['prediction'].astype(int)
	return P



def parallel_plot(data):
	my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
	plt.figure(figsize=(6,6)).gca().axes.set_ylim([-3,+3])
	parallel_coordinates(data, 'prediction', color = my_colors, marker='o')

      

P = pd_centers(features1, centers1)
st.write("prediction of Temprature")
P

st.write("StandardScaler Data after kmeans of Water_level")
centers2 = model.cluster_centers_
centers2

def pd_centers1(featuresUsed, centers2):
	colNames = list(featuresUsed)
	colNames.append('prediction')

	Z = [np.append(A, index) for index, A in enumerate(centers1)]

	P1 = pd.DataFrame(Z, columns=colNames)
	P1['prediction'] = P1['prediction'].astype(int)
	return P1



def parallel_plot1(data):
	my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
	plt.figure(figsize=(6,6)).gca().axes.set_ylim([-3,+3])
	parallel_coordinates(data, 'prediction', color = my_colors, marker='o')

P1 = pd_centers1(features2, centers2)
st.write("prediction of Water_level1")
P1

st.write("Parallel_plot of Temprature")
st.pyplot(parallel_plot(P[P['temprature2'] < 0.5]))

st.write("Parallel_plot of Water_level")
st.pyplot(parallel_plot(P1[P1['water_level1'] > 0.5]))
