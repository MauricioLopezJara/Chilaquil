import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="ManoTech",
    page_icon="✮",
    layout="centered"
)

# Función para la página de bienvenida
def pagina_bienvenida():
    # Crea 3 columnas
    left_col, mid_col, right_col = st.columns(3)

    # Muestra la imagen en la columna central
    mid_col.image("Nasa.png", width=200)
    st.title("Poster Machine Hand")
    st.write("Ayudame a llenar este pedo")
    st.header("Ayudame a llenar este pedo")
    st.write("Ayudame a llenar este pedo")
    st.write("Ayudame a llenar este pedo")
        # URL del video de YouTube
    video_url = "https://www.youtube.com/watch?v=mgUZwoR0gcE"

    # Mostrar el video de YouTube en la interfaz
    st.video(video_url)
    # Botón
    # Botón
    if st.button("1.- ¡Daño a los sistemas satelitales!"):
        st.write("""Las partículas cargadas pueden acelerarse y dirigirse hacia los satélites. Esta afluencia de partículas cargadas puede provocar la carga de las superficies de los satélites.""")
    if st.button("2.- ¡Perturbaciones en la propagación de las ondas de radio!"):
        st.write("""Los cambios en las condiciones ionosféricas y magnetosféricas durante los fenómenos de reconexión magnética pueden provocar interferencias que pueden afectar a las señales de comunicación de los satélites que atraviesan estas regiones.""")
    if st.button("3.- ¡Cambio en la órbita de los satélites"):
        st.write(""" La interacción de los satélites con los campos magnéticos perturbados durante los fenómenos de reconexión puede inducir cambios en sus órbitas. Aunque este efecto es generalmente pequeño para la mayoría de los satélites, es algo que debe tenerse en cuenta.""")
    if st.button("4.- ¡Errores de navegación"):
        st.write("""Los fenómenos de reconexión magnética pueden influir en el campo magnético de la Tierra, provocando desviaciones temporales en las lecturas de la brújula magnética.""")
    if st.button("5.- ¡Tormentas geomagnéticas"):
        st.write("""Los fenómenos de reconexión magnética intensa en el Sol, como las erupciones solares y las eyecciones de masa coronal, pueden provocar tormentas geomagnéticas en la Tierra. Estas tormentas pueden inducir corrientes eléctricas en la ionosfera terrestre y en el suelo, afectando a los sistemas de satélites y a las redes eléctricas.""")

# Función para la página de información (Opción 2)
def Datos():
    st.title("Información sobre Reconexión Magnética")
    # Agrega más contenido informativo aquí si lo deseas


# Función para analizar los datos
def analyze_data():
    st.title("Datos")
    # Aquí va la implementación real de la función analyze_data
    # Por ahora, puedes dejarla vacía o agregar algún mensaje de prueba

# Función para la página de contacto (Opción 3)
def pagina_contacto():
    st.title("Contáctenos")
    st.write("Si tienes preguntas o comentarios, no dudes en ponerte en contacto con nosotros.")

    # Crea 6 columnas
    Cuatro_col, Cinco_col= st.columns(2)

    with Cuatro_col:
        st.image("4.png", width=200)
        st.markdown("**Nombre:** Mauricio")
        st.markdown("**Apellido:** Lopez")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

    with Cinco_col:
        st.image("5.png", width=200)
        st.markdown("**Nombre:** Sergio")
        st.markdown("**Apellido:** Huerta")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

# Título del menú
st.sidebar.markdown("Bienvenido al Menu")

# Elementos del menú
opciones = ["Bienvenida", "Datos", "Contacto"]
eleccion = st.sidebar.selectbox("Selecciona una opción:", opciones)

# Contenido de la página según la elección
if eleccion == "Bienvenida":
    pagina_bienvenida()
elif eleccion == "Datos":
    Datos()
elif eleccion == "Contacto":
    pagina_contacto()
