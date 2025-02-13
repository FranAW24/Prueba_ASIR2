import streamlit as st

st.title("🍔Me gusta las hambunguezitas")
st.write(
    "A mi me gusta el pan con pan"
)
st.header("Esto es una cabecera")

cantidad= st.slider("Elija un valor")

print(id(cantidad))

for i in range(cantidad):
    st.button(f'Boton {i}')
    st.checkbox(f'Opcion {i}')