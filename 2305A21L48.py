import math as math
import streamlit as st
st.title("2305A21L48-PS7")
st.write("calculate the resistance (R0) and reactance (X0) of a transformer basedon OC test measurements like V0,I0 and WO. ")
# Function to calculate R0 and X0
def Tran_Eff(V0, I0, W0):
    NP_F = W0 / (V0 * I0)
    Iu = I0 * (1 - NP_F**2)**0.5
    Iw = I0 * NP_F
    R0 = V0 / Iw
    X0 = V0 / Iu
    return R0, X0
col1,col2=st.columns(2)

# Streamlit UI

# Input fields
with col1:
    with st.container(border=True):
        V0 = st.number_input("Enter V0 (Voltage):", value=100)
        I0 = st.number_input("Enter I0 (Current):", value=100)
        W0 = st.number_input("Enter W0 (Power):", value=100)
        a=st.button("calculate")
    



# Calculate and display results
with col2:
    if a:
        R0, X0 = Tran_Eff(V0, I0, W0)
        st.write(f"Resistance (R0): {R0:.2f} ohms")
        st.write(f"Reactance (X0): {X0:.2f} ohms")
   




    