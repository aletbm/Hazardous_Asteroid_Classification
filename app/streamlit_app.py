import streamlit as st
import cloudpickle

path = "/mount/src/Hazardous_Asteroid_Classification/"
path="./"

with open(path+'model/HAP_model.bin', 'rb') as f_in:
    pipe, le, sfs, rf = cloudpickle.load(f_in)
    
st.write("# ☄️ Hazardous Asteroid Classification - NASA JPL Asteroid by [Alexander D. Rios](https://linktr.ee/aletbm)")