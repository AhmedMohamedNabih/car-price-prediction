import streamlit as st
import pandas as pd 
import pickle
import gzip

with gzip.open("Cars_prediction.sav.gz", "rb") as f:
    model = pickle.load(f)
st.title('Car Price_prediction')
st.sidebar.header('Feature Selecting')
st.sidebar.info('Easy Application For Predicting Cars_price')
st.image("car.jpg")
# --------------------------------------------------------------------
m1 = ['LEXUS','CHEVROLET','HONDA','FORD','HYUNDAI','TOYOTA','MERCEDES-BENZ',
      'OPEL','PORSCHE','BMW','JEEP','VOLKSWAGEN','AUDI','RENAULT','NISSAN',
      'SUBARU','DAEWOO','KIA','MITSUBISHI','SSANGYONG','MAZDA','GMC','FIAT',
      'INFINITI','ALFA ROMEO','SUZUKI','ACURA','LINCOLN','VAZ','GAZ','CITROEN',
      'LAND ROVER','MINI','DODGE','CHRYSLER','JAGUAR','ISUZU','SKODA',
      'DAIHATSU','BUICK','TESLA','CADILLAC','PEUGEOT','BENTLEY','VOLVO','სხვა',
      'HAVAL','HUMMER','SCION','UAZ','MERCURY','ZAZ','ROVER','SEAT','LANCIA',
      'MOSKVICH','MASERATI','FERRARI','SAAB','LAMBORGHINI','ROLLS-ROYCE',
      'PONTIAC','SATURN','ASTON MARTIN','GREATWALL']
m2=[16, 13, 17, 43, 27, 31,  6,  9, 21, 30, 40, 15, 12, 46,  1, 42, 24,
       32, 26, 41, 35,  2,  3,  8, 29, 20, 11,  0, 45, 19, 39,  7, 25,  4,
       10, 33, 23, 18,  5, 37, 48, 38, 34, 22, 28, 47, 44, 36, 14]
menu_mapping=dict(zip(m1,m2))  
menu1=st.selectbox('Manufacturer',m1)
menu2=menu_mapping[menu1]
# ------------------------------------------------------------------------------
mm1=[
    'RX 450', 'Equinox' ,'FIT','E 230 124', 'RX 450 F SPORT', 'Prius C aqua'

]
mm2=[298, 287, 585, 521, 267, 171, 371, 598, 527,  80, 289, 203, 118,
       413, 659,  55, 654, 681, 190, 709, 239, 491, 426, 358, 327, 514,
        76, 421, 343, 589, 553, 258, 630, 383,  35, 406, 281,  56, 561,
       194, 683, 661, 233, 296, 385,   6, 368, 151, 667, 558, 594, 101,
        93, 404, 508, 220, 574, 443, 354, 591, 639, 129,  73, 646, 578,
       555, 714, 120, 141, 261, 332, 100, 441, 208, 495, 176, 444, 397,
       627,  79, 207, 130, 559, 411, 106,  85, 592, 285, 657,  63, 419,
        29, 282, 135, 696, 562, 121,  90, 224, 147, 322, 211,  62, 551,
       484, 423, 398, 325, 454, 457, 618, 448, 375, 609, 277,  99, 485,
       265, 685, 582,  44, 402, 232, 221, 575,  65, 550,  68, 369,  27,
       382, 161, 361,  71, 214, 647, 705,  86, 466, 540, 506,   2, 263,
        26, 619, 673, 317, 193, 625, 245, 631, 717, 388, 390, 496, 405,]
model_mapping=dict(zip(mm1,mm2))
model1=st.selectbox('Model',mm1)
model2=model_mapping[model1]
# ----------------------------------
c1=['Jeep','Hatchback','Sedan', 'Microbus', 'Goods wagon', 'Universal', 'Coupe',
 'Minivan' ,'Cabriolet' ,'Limousine' ,'Pickup']
c2=[3, 4, 8, 9, 1, 6, 5, 2, 7, 0]
category_mapping=dict(zip(c1,c2))
category1=st.selectbox('category',c1)
category=category_mapping[category1]
# ----------------------------------
l1=['Yes','No']
l2=[1,2]
leather_mapping=dict(zip(l1,l2))
leather1=st.selectbox('Leather interier',l1)
laether=leather_mapping[leather1]
# ----------------------------------
f1=['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
f2=[2,5,1,6,4,0,3]
feul_mapping=dict(zip(f1,f2))
feul1=st.selectbox('Feul type',f1)
feul=feul_mapping[feul1]
# ----------------------------------
e1 = [
    '3.5','3','1.3','2.5','2','1.8','2.4','4','1.6','3.3',
    '2.0 Turbo','2.2 Turbo','4.7','1.5','4.4','3.0 Turbo','1.4 Turbo','3.6',
    '2.3','1.5 Turbo','1.6 Turbo','2.2','2.3 Turbo','1.4','5.5','2.8 Turbo',
    '3.2','3.8','4.6','1.2','5','1.7','2.9','0.5','1.8 Turbo','2.4 Turbo',
    '3.5 Turbo','1.9','2.7','4.8','5.3','0.4','2.8','3.2 Turbo','1.1','2.1',
    '0.7','5.4','1.3 Turbo','3.7','1','2.5 Turbo','2.6','1.9 Turbo','4.4 Turbo',
    '4.7 Turbo','0.8','0.2 Turbo','5.7','4.8 Turbo','4.6 Turbo','6.7','6.2',
    '1.2 Turbo','3.4','1.7 Turbo','6.3 Turbo','2.7 Turbo','4.3','4.2','2.9 Turbo',
    '0','4.0 Turbo','20','3.6 Turbo','0.3','3.7 Turbo','5.9','5.5 Turbo','0.2',
    '2.1 Turbo','5.6','6','0.7 Turbo','0.6 Turbo','6.8','4.5','0.6','7.3','0.1',
    '1.0 Turbo','6.3','4.5 Turbo','0.8 Turbo','4.2 Turbo','3.1','5.0 Turbo','6.4',
    '3.9','5.7 Turbo','0.9','0.4 Turbo','5.4 Turbo','0.3 Turbo','5.2','5.8','1.1 Turbo'
]

e2=[1.3, 2.5, 2. , 1.8, 1.6, 2.4, 1.5, 2.3, 2.2, 1.4, 1.2, 1.7, 2.9,
       1.9, 3.5, 2.1, 1. , 0.8, 2.7, 3. , 3.2, 1.1, 3.3, 2.8]
Engine_mapping=dict(zip(e1,e2))
engine1=st.selectbox('Engine volume',e1)
engine=Engine_mapping[engine1]
# ----------------------------------
s1=['186005 km', '192000 km', '200000 km', '140607 km', '307325 km',
 '186923 km']
s2=[200000, 168966,  91901, ...,  23430, 132700, 140607]
Mileage_mapping=dict(zip(s1,s2))
Mileage1=st.selectbox('Mileage',s1)
Mileage=Mileage_mapping[Mileage1]
# ---------------------------------
g1= [6 , 4 , 8 , 1, 12, 3, 2, 16,  5,  7,  9, 10, 12]
g2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
Cylinders_mapping=dict(zip(g1,g2))
Cylinders1=st.selectbox('Cylinders',g1)
Cylinders=Cylinders_mapping[Cylinders1]
# -----------------------------
j1=['Automatic', 'Tiptronic', 'Variator' ,'Manual']
j2=[1,2,3,4]
Gear_type_mapping=dict(zip(j1,j2))
Gear_box1=st.selectbox('Gear box type',j1)
Gear_box2=Gear_type_mapping[Gear_box1]
# -----------------
b1=['4x4' ,'Front' ,'Rear']
b2=[1,2,3]
Drive_mapping=dict(zip(b1,b2))
Drive_mapping1=st.selectbox('Drive_mapping',b1)
Drive_mapping2=Drive_mapping[Drive_mapping1]
# ------------------------
o1=['Silver', 'Black', 'White' ,'Grey', 'Blue', 'Green', 'Red', 'Sky blue', 'Orange',
 'Yellow', 'Brown' ,'Golden' ,'Beige' ,'Carnelian red' ,'Purple', 'Pink']
o2=[ 1, 14, 12,  2,  7, 13,  6, 15, 11,  5,  0,  8,  4, 10,  3,  9]
Color_mapping=dict(zip(o1,o2))
Color_mapping1=st.selectbox('Color',o1)
Color_mapping2=Color_mapping[Color_mapping1]
# --------------------
v1=[12  ,8  ,2  ,0 , 4  ,6 ,10  ,3  ,1  ,5  ,7  ,9, 11 ,14 ,15 ,13]
v2=[2,  0,  4, 12,  8,  6,  3, 10, 16,  7,  9,  5, 11, 14,  1, 13]
Airbags_mapping=dict(zip(v1,v2))
Airbags_mapping1=st.selectbox('Airbags',v1)
Airbags_mapping2=Airbags_mapping[Airbags_mapping1]
# -----------------------
Age = st.number_input("Age")
levy=st.number_input('Levy')
# ------------------------------------------------
df = pd.DataFrame({
    'Manufacturer': [menu2],
    'Model': [model2],
    'Category': [category],               
    'Leather interior': [laether],        
    'Fuel type': [feul1],                
    'Engine volume': [engine],
    'Mileage': [Mileage],
    'Cylinders': [Cylinders],
    'Gear box type': [Gear_box1],        
    'Drive wheels': [Drive_mapping1],     
    'Color': [Color_mapping2],           
    'Airbags': [Airbags_mapping2],
    'Age': [Age],
    'Levy': [levy]
}, index=[0])

# --- حوّل لـ One-Hot وزبط الأعمدة لتطابق تدريب الموديل ---
X_expected = getattr(data, "feature_names_in_", None)

df_enc = pd.get_dummies(df)

if X_expected is not None:
    # مواءمة الأعمدة مع تدريب الموديل (المفقود = 0)
    df_enc = df_enc.reindex(columns=X_expected, fill_value=0)

p = st.sidebar.button('predictPrice')
if p:
    pre = data.predict(df_enc)

    st.sidebar.write(f"price is : {pre[0]:,.0f} $")
