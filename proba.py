import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Calculadora de Notas por Asignatura")

st.write("Ingresa las notas parciales y de examen para calcular la nota final (ponderación: 40% Parcial, 60% Examen).")

# DataFrame inicial con algunas asignaturas de ejemplo
data = {
    "Asignatura": ["Matemáticas", "Lengua", "Ciencias", "Historia"],
    "Nota Parcial": [0, 0, 0, 0],
    "Nota Examen": [0, 0, 0, 0]
}
df = pd.DataFrame(data)

# Permitir al usuario editar la tabla de notas
df_editado = st.experimental_data_editor(df, num_rows="dynamic", key="editor")

# Calcular la nota final para cada asignatura
df_editado["Nota Final"] = df_editado["Nota Parcial"] * 0.4 + df_editado["Nota Examen"] * 0.6

st.subheader("Tabla de Notas Calculadas")
st.dataframe(df_editado)
