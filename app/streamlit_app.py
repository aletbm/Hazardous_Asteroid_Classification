import streamlit as st
import cloudpickle
from streamlit_extras.bottom_container import bottom

path = "/mount/src/Hazardous_Asteroid_Classification/"
path="./"

with open(path+'model/HAP_model.bin', 'rb') as f_in:
    pipe, le, sfs, rf = cloudpickle.load(f_in)

st.set_page_config(layout="wide")
    
st.write("""# ☄️ Hazardous Asteroid Classification - NASA JPL Asteroid by [Alexander D. Rios](https://linktr.ee/aletbm)""")

form = st.form("my_form")
form.write("#### Load your asteroid data")

H = form.number_input("Absolute magnitude parameter",
                      format="%0.15f",
                      help="""# Absolute magnitude parameter
                      In astronomy, absolute magnitude (M) is a measure 
    of the luminosity of a celestial object on an inverse 
    logarithmic astronomical magnitude scale; 
    the more luminous (intrinsically bright) an object, 
    the lower its magnitude number. An object's absolute 
    magnitude is defined to be equal to the apparent magnitude 
    that the object would have if it were viewed from a distance 
    of exactly 10 parsecs (32.6 light-years), 
    without extinction (or dimming) of its light due 
    to absorption by interstellar matter and cosmic dust.""")
diameter = form.number_input("Object diameter (equivalent to a sphere) [Km]", format="%0.15f")
albedo = form.number_input("Geometric albedo", format="%0.15f")
i = form.number_input("Inclination (Angle relative to the x-y ecliptic plane) [Degrees]", format="%0.15f")
om = form.number_input("Longitude of the ascending node [Degrees]", format="%0.15f")
w = form.number_input("Argument of perihelion [Degrees]", format="%0.15f")
ma = form.number_input("Mean anomaly [Degrees]", format="%0.15f")
n = form.number_input("Mean motion [Degrees/Days]", format="%0.15f")
moid = form.number_input("Minimum orbit intersection distance with Earth [AU]", format="%0.15f")
option = form.selectbox(
    "Orbit classification",
    ("AMO - Amor",
    "APO - Apollo",
    "AST - Asteroid",
    "ATE - Aten",
    "CEN - Centaur",
    "HYA - Hyperbolic Asteroid",
    "IEO - Interior Earth Object",
    "IMB - Inner Main-belt Asteroid",
    "MBA - Main-belt Asteroid",
    "MCA - Mars-crossing Asteroid",
    "OMB - Outer Main-belt Asteroid",
    "PAA - Parabolic Asteroid",
    "TJN - Jupiter Trojan",
    "TNO - TransNeptunian Object"),
)

#'H', 'i', 'om', 'w', 'ma', 'n', 'moid', 'diametro', 'class

form.form_submit_button(label="Classify it", type="secondary")

