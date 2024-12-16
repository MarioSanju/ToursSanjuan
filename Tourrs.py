import streamlit as st
import pandas as pd
import os

# Título principal
st.title("Tours guiados por Madrid")

# Descripción breve del servicio
st.write("""
    ¡Bienvenidos a nuestra plataforma de tours guiados por Madrid!
    Explora la ciudad con expertos locales. Te mostraremos los
    lugares más emblemáticos y ocultos de la capital española.
""")

# Separador
st.markdown("---")

# Sección de tours disponibles
st.header("Nuestros Tours")

# Tours disponibles
tours = {
    "Tour Histórico por Madrid": {
        "Duración": "2 horas",
        "Precio": "25€",
        "Descripción": "Descubre la historia de Madrid, sus monumentos y rincones históricos.",
        "Hora": "10:00 AM - 1:00 PM"
    },
    "Tour Gastronómico": {
        "Duración": "2.5 horas",
        "Precio": "30€",
        "Descripción": "Prueba lo mejor de la gastronomía madrileña en un recorrido culinario único.",
        "Hora": "5:00 PM - 7:30 PM"
    },
    "Tour Nocturno por el centro": {
        "Duración": "2 horas",
        "Precio": "20€",
        "Descripción": "Disfruta de Madrid iluminada y sus historias nocturnas.",
        "Hora": "8:00 PM - 10:00 PM"
    }
}

# Imágenes para los tours
imagenes = {
    "Tour Histórico por Madrid": "historico.jpg",
    "Tour Gastronómico": "gastronomico.jpg",
    "Tour Nocturno por el centro": "nocturno.jpg"
}

# Mostrar los tours con imágenes y detalles
for tour, details in tours.items():
    st.subheader(tour)
    st.image(imagenes[tour], caption=tour, use_column_width=True)
    st.write(f"**Duración:** {details['Duración']}")
    st.write(f"**Precio:** {details['Precio']}")
    st.write(f"**Hora:** {details['Hora']}")
    st.write(details['Descripción'])
    st.markdown("---")

# Sistema de reservas
st.header("Reserva tu Tour")

# Seleccionar un tour
tour_seleccionado = st.selectbox(
    "Selecciona el tour que deseas reservar:",
    list(tours.keys())
)

# Datos del usuario
st.subheader("Tus datos")
nombre = st.text_input("Nombre completo:")
correo = st.text_input("Correo electrónico:")

# Función para guardar reservas en un archivo CSV
def guardar_reserva(nombre, correo, tour):
    reserva = {"Nombre": nombre, "Correo": correo, "Tour": tour}
    if os.path.exists("reservas.csv"):
        df = pd.read_csv("reservas.csv")
        df = df.append(reserva, ignore_index=True)
    else:
        df = pd.DataFrame([reserva])
    df.to_csv("reservas.csv", index=False)

# Botón para confirmar la reserva
if st.button("Reservar ahora"):
    if nombre and correo:
        guardar_reserva(nombre, correo, tour_seleccionado)
        st.success(f"🎉 ¡Gracias {nombre}! Tu reserva para el '{tour_seleccionado}' ha sido confirmada.")
        st.info(f"Detalles del tour:\nDuración: {tours[tour_seleccionado]['Duración']}\nHora: {tours[tour_seleccionado]['Hora']}")
    else:
        st.error("❌ Por favor, completa todos los campos para confirmar tu reserva.")

# Mostrar reservas existentes
st.header("📋 Reservas Existentes")
if os.path.exists("reservas.csv"):
    df_reservas = pd.read_csv("reservas.csv")
    st.dataframe(df_reservas)
else:
    st.write("No hay reservas registradas todavía.")

# Slider de edad para personalización
st.sidebar.header("Personalización")
edad = st.slider(
    "Selecciona tu edad:",
    min_value=0,
    max_value=100,
    value=20,
    step=1
)
st.sidebar.write(f"Edad seleccionada: {edad} años")
