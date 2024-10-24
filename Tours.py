import streamlit as st
# Título principal
st.title("Tours guiados por Madrid")

# Descripción breve del servicio
st.write("""
    ¡Bienvenidos a nuestra plataforma de tours guiados por Madrid!
    Explora la ciudad con expertos locales.Te mostraremos los
    lugares más emblemáticos y ocultos de la capital española.
""")

# Separador
st.markdown("---")
# Sección de tours disponibles
st.header("Nuestros Tours")

# Crear una lista de tours como ejemplo
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

# Mostrar tours en formato de tabla
for tour, details in tours.items():
    st.subheader(tour)
    st.write(f"**Duración:** {details['Duración']}")
    st.write(f"**Precio:** {details['Precio']}")
    st.write(f"**Hora:** {details['Hora']}")
    st.write(details['Descripción'])
    st.markdown("---")