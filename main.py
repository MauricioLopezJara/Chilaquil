import streamlit as st
import pandas as pd
import numpy as np
import base64

# Configuración de la página
st.set_page_config(
    page_title="ManoTech",
    page_icon="🤖",
    layout="centered"
)

# Función para la página de bienvenida
def pagina_bienvenida():
    # Crea 3 columnas
    left_col, mid_col, right_col = st.columns(3)

    # Muestra la imagen en la columna central
    mid_col.image("Uni.png", width=200)
    st.title("Poster Machine Hand")
    st.write("Este proyecto busca demostrar el poder que se puede generar con un poco de conocimiento en programación, al igual que en electrónica.")
    
    def show_pdf(file_path):
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    if st.button("Ocultar PDF"):
        st.markdown("")
    if st.button("Mostrar PDF del proyecto ManoTech"):
        show_pdf('PosterFinalManotechFinal.pdf')
    
    st.header("Fase Inicial del proyecto")
    st.write("Esta iniciativa posee numerosas ventajas y se sugiere llevar a cabo para fomentar el interés tanto en tecnología como en programación. Este sitio web ha sido desarrollado utilizando Python y la biblioteca Streamlit. Esperamos que lo encuentren útil y puedan aprovechar los recursos de código abierto que deseamos ofrecerles. Asimismo, dispone de enlaces a través de los cuales pueden ponerse en contacto con nosotros. Agradecemos mucho su visita a nuestra página web oficial del proyecto.")
             
    # URL del video de YouTube
    video_url = "https://youtu.be/lvIDTmyw6RU?si=I0cxedUcPvUTHEkY"

    # Mostrar el video de YouTube en la interfaz
    st.video(video_url)
    st.header("Presiona los siguientes botones para obtener mas informacion al respecto")
    # Botón
    if st.button("1.- ¡Arriesgar la salud de los trabajadores!"):
        st.write("""En algunos trabajos, en diversos campos como el desarrollo de cultivos celulares, es crucial garantizar la bioseguridad de los trabajadores. También es fundamental para los empleadores velar por la seguridad de sus empleados. Por tal motivo, resulta preferible que algunas máquinas realicen las tareas en lugar de los seres humanos.""")
    if st.button("2.- ¡Automatizacion de procesos que requieran alta precision!"):
        st.write("""Algunas máquinas requieren un elevado grado de precisión, y qué mejor que una computadora o una máquina pueda replicar exactamente el movimiento de una persona. Se puede programar con precisión el movimiento a realizar para lograr una ejecución óptima de la tarea o trabajo que se esté buscando desempeñar.""")
    if st.button("3.- ¡Puede servir para mejorar las capacitaciones de los trabajadores "):
        st.write("""Al mejorar los procesos, podemos registrar los objetivos alcanzados mediante seguimientos precisos de manos. Estos seguimientos pueden proporcionar a los trabajadores una comprensión más clara de qué y cómo se debe realizar la actividad. Con esto como base, se pueden minimizar los riesgos y maximizar el éxito en las actividades.""")
    if st.button("4.- ¡Mejorar la calidad de vida de los trabajadores "):
        st.write("""Al cuidar a los trabajadores y brindarles capacitaciones mejoradas junto con herramientas más eficientes, no solo mejoramos la calidad de vida de los trabajadores, sino que también incrementamos su productividad. Esto, en términos económicos, siempre se traduce en beneficios para todos.""")
    if st.button("5.- ¡Optimizacion de Procesos mecanicos "):
        st.write("""Este proyecto presenta una gran ventaja: la escalabilidad y automatización de procesos. A primera vista, utilizar simplemente una mano puede no parecer una buena idea. Sin embargo, el proceso de copiar y reproducir el movimiento de una mano humana no solo tiene este potencial, sino que también puede aplicarse a 10, 100 o incluso 1000 manos simultáneamente. Esto podría reducir significativamente los tiempos de diversas actividades.""")

# Función para la página de información (Opción 2)
def Datos_del_proyecto():
    st.title("Información sobre la contruccion del proyecto Mano Tech")
    st.write("A continuación, podrá observar el diagrama esquemático del proyecto, así como algunos videos que muestran las fases de la construcción de este proyecto, que es muy bonito e interesante.")
    st.title("Diagrama esquimatico")
    st.image("Esquematico.jpeg")
    st.title("Materiales para el circuito:")
    # Crear un DataFrame de pandas con un solo valor
    datos = {"Componente": ["Servomotores", "Cables Dupont", "Fuente de alimentación externa", "Arduino Uno", "Otro Componente"],
    "Cantidad": [5, 16, 1, 1, 10]}
    df = pd.DataFrame(datos)
    # Mostrar la tabla
    st.table(df)
    st.title("Diagrama de conecciones")
    st.write("Enseguida, presentaremos el diagrama esquemático en formato de Tinkercad, diseñado de manera más sencilla para facilitar la distinción de las conexiones.")
    st.image("Imagen3.png")
    st.title("Resultados Obtenidos")
    st.write("Con toda sinceridad, consideramos que este proyecto posee un alcance significativo y, al mismo tiempo, ofrece una experiencia sumamente enriquecedora. La realización de este proyecto ha sido de gran utilidad para nosotros, demostrándonos que, efectivamente, si puedes imaginarlo, puedes crearlo. Agradecemos profundamente su visita a nuestra página y la revisión de nuestro proyecto.")
    video_url2 = "https://youtu.be/T943gCbbA9U"
    st.video(video_url2)

# Función para la página de contacto (Opción 3)
def pagina_contacto():
    st.title("Contáctenos")
    st.write("Si tienes preguntas o comentarios, no dudes en ponerte en contacto con nosotros.")

    # Crea 2 columnas
    Cuatro_col, Cinco_col= st.columns(2)

    with Cuatro_col:
        st.image("4.png", width=180)
        st.markdown("**Nombre:** Luis Mauricio")
        st.markdown("**Apellido:** Lopez Jaramillo")
        link = '<a href="procesamientodigitalsi@gmail.com" target="_blank">Correo</a>'
        st.markdown(link, unsafe_allow_html=True)

    with Cinco_col:
        st.image("5.png", width=180)
        st.markdown("**Nombre:** Sergio Arturo")
        st.markdown("**Apellido:** Meza Huerta")
        link = '<a href="https://www.linkedin.com/in/luis-mauricio-lopez-jaramillo-108b09290/" target="_blank">Linkedin</a>'
        st.markdown(link, unsafe_allow_html=True)

# Título del menú
st.sidebar.markdown("Bienvenido al Menu... 🏡")

# Elementos del menú
opciones = ["Bienvenida 🎇", "Datos del proyecto ✍🏼", "Contacto 📪"]
eleccion = st.sidebar.selectbox("Selecciona una opción:", opciones)

# Contenido de la página según la elección
if eleccion == "Bienvenida 🎇":
    pagina_bienvenida()
elif eleccion == "Datos del proyecto ✍🏼":
    Datos_del_proyecto()
elif eleccion == "Contacto 📪":
    pagina_contacto()

st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.image("Mano.png", width = 150)
