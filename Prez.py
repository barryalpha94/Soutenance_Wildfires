import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
st.title("Analyse des feux de forêts aux USA")
st.sidebar.title("Feux de forêts aux USA")
st.sidebar.header("Déroulé du projet")
pages=["Présentation du jeu de données", "Préparation des données", "Data Visualisation", "Modélisation", "Time Series"]
page=st.sidebar.radio("Allez vers", pages)
if page == pages[0] :
    st.write("## Présentation du jeu de données : première exploration")
    st.divider()
    st.write("https://www.fs.usda.gov/rds/archive/catalog/RDS-2013-0009.6")
    st.divider()
    st.image("https://www.fs.usda.gov/sites/default/files/users/user3824/Photos/CWDG/SweetCrk-Milepost2Fire-Marcus-Kauffman.jpg")
if page == pages[1] :
    st.write("## Préparation des données : complétude des données")
if page==pages[4]:
    st.write("## Modélisation temporelle avec Prophet")
st.sidebar.header("L'équipe")

