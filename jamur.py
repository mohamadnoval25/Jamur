import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('mushrooms.sav','rb'))

st.title('Prediksi Jamur Beracun')
col1, col2 = st.columns(2)

with col1:
   cap_shape = st.number_input('Bentuk tudung')
   cap_surface = st.number_input('Permukaan Tudung')
   cap_color = st.number_input('Warna Tudung')
   bruises = st.number_input('Memar')
   odor = st.number_input('Bau')
   gill_attachment = st.number_input('Sisik')
   gill_spacing = st.number_input('Jarak Sisik')
   gill_size = st.number_input('Ukuran Sisik')
   gill_color = st.number_input('Warna Sisik')
   stalk_shape = st.number_input('Bentuk Batang')
   stalk_root = st.number_input('Akar batang')
   
with col2:
    stalk_surface_above_ring = st.number_input('Permukaan batang di Atas lingkaran')
    stalk_surface_below_ring = st.number_input('Permukaan batang di Bawah lingkaran')
    stalk_color_above_ring = st.number_input('Warna batang di Atas cincin')
    stalk_color_below_ring = st.number_input('Warna batang di Bawah cincin')
    veil_type = st.number_input('Tipe Tudung')
    veil_color = st.number_input('Warna Topi')
    ring_number = st.number_input('Ukuran cincin')
    ring_type = st.number_input('Tipe cincin')
    spore_print_color = st.number_input('warna Spora')
    population = st.number_input('Populasi')
    habitat = st.number_input('Habitat')
   
predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[cap_shape,cap_surface,cap_color,bruises,odor,gill_attachment,gill_spacing,gill_size,gill_color,stalk_shape,stalk_root,stalk_surface_above_ring,stalk_surface_below_ring,stalk_color_above_ring,stalk_color_below_ring,veil_type,veil_color,ring_number,ring_type,spore_print_color,population,habitat]])
    if(predik[0] == 1):
        predik = 'Kemungkinan Jamur Beracun'
    else:
        predik = 'Kemungkinan Jamur Tidak Beracun'
st.success(predik)