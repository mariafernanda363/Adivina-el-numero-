# ============================================================
# 1. IMPORTAR LIBRERÍAS
# ============================================================

# Pandas: leer, organizar y manipular datos.
import pandas as pd

# NumPy: realizar operaciones matemáticas y estadísticas.
import numpy as np

# Streamlit: crear aplicaciones web interactivas.
import streamlit as st


# ============================================================
# 2. TÍTULO Y DESCRIPCIÓN
# ============================================================

# title(): muestra el título principal.
st.title("Análisis de población")

# write(): muestra información en pantalla.
st.write("Bienvenido al análisis de datos de población.")
st.write("Selecciona un archivo CSV con los datos de población.")


# ============================================================
# 3. SUBIR ARCHIVO CSV
# ============================================================

# file_uploader(): permite subir archivos.
# type=["csv"]: acepta únicamente archivos CSV.

archivo = st.file_uploader(
    "Sube un archivo CSV con datos de población",
    type=["csv"]
)


# ============================================================
# 4. LEER Y MOSTRAR LOS DATOS
# ============================================================

# if: comprueba si se ha cargado un archivo.
if archivo is not None:

    # read_csv(): lee el archivo CSV.
    datos = pd.read_csv(archivo)

    # Muestra los datos originales en forma de tabla.
    st.subheader("Datos originales")
    st.dataframe(datos)


    # ========================================================
    # 5. SELECCIONAR LOS 10 PAÍSES MÁS POBLADOS
    # ========================================================

    # sort_values(): organiza los datos según una columna.
    # ascending=False: ordena de mayor a menor.
    # head(10): selecciona los primeros 10 registros.

    top10 = datos.sort_values(
        "2022 Population",
        ascending=False
    ).head(10)

    st.subheader("Top 10 países más poblados")
    st.dataframe(top10)


    # ========================================================
    # 6. CONVERTIR COLUMNAS EN ARRAYS DE NUMPY
    # ========================================================

    # to_numpy(): convierte una columna en un array.

    paises = top10["Country/Territory"].to_numpy()

    poblacion_2015 = top10["2015 Population"].to_numpy()

    poblacion_2020 = top10["2020 Population"].to_numpy()

    poblacion_2022 = top10["2022 Population"].to_numpy()


    # ========================================================
    # 7. OPERACIONES ESTADÍSTICAS CON NUMPY
    # ========================================================

    # sum(): suma todos los valores.
    total = np.sum(poblacion_2022)

    # mean(): calcula el promedio.
    promedio = np.mean(poblacion_2022)

    # median(): calcula la mediana.
    mediana = np.median(poblacion_2022)

    # min(): encuentra el valor mínimo.
    minimo = np.min(poblacion_2022)

    # max(): encuentra el valor máximo.
    maximo = np.max(poblacion_2022)


    # ========================================================
    # 8. MOSTRAR ESTADÍSTICAS CON MÉTRICAS
    # ========================================================

    # columns(5): divide la pantalla en cinco columnas.
    # metric(): muestra un indicador numérico.

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Población total",
        f"{total / 1000000:.2f} millones"
    )

    col2.metric(
        "Promedio",
        f"{promedio / 1000000:.2f} millones"
    )

    col3.metric(
        "Mediana",
        f"{mediana / 1000000:.2f} millones"
    )

    col4.metric(
        "Población mínima",
        f"{minimo / 1000000:.2f} millones"
    )

    col5.metric(
        "Población máxima",
        f"{maximo / 1000000:.2f} millones"
    )


    # ========================================================
    # 9. COMPARACIÓN DE POBLACIÓN POR PAÍS
    # ========================================================

    st.subheader("Comparación de la población por país")

    # DataFrame(): crea una tabla con los datos seleccionados.

    comparacion = pd.DataFrame({
        "País": paises,
        "2015 Population": poblacion_2015,
        "2020 Population": poblacion_2020,
        "2022 Population": poblacion_2022
    })

    # Muestra la tabla comparativa.
    st.dataframe(comparacion)


    # ========================================================
    # 10. CALCULAR DIFERENCIAS DE POBLACIÓN
    # ========================================================

    # Resta los arrays para calcular el cambio de población.
    diferencia = poblacion_2022 - poblacion_2015

    st.subheader("Crecimiento de población (2015-2022)")

    crecimiento = pd.DataFrame({
        "País": paises,
        "Población 2015": poblacion_2015,
        "Población 2022": poblacion_2022,
        "Diferencia": diferencia
    })

    st.dataframe(crecimiento)


    # ========================================================
    # 11. CREAR GRÁFICO COMPARATIVO
    # ========================================================

    st.subheader("Comparación de la población por país")

    # set_index(): establece el nombre del país como índice.
    # Selecciona las columnas correspondientes a cada año.

    grafico = top10.set_index("Country/Territory")[
        [
            "2015 Population",
            "2020 Population",
            "2022 Population"
        ]
    ]

    # bar_chart(): crea un gráfico de barras.
    st.bar_chart(grafico)


    # ========================================================
    # 12. SELECCIONAR UN AÑO PARA VISUALIZAR
    # ========================================================

    st.subheader("Visualización por año")

    # selectbox(): crea una lista de opciones.
    # El usuario puede seleccionar el año que desea analizar.

    anio = st.selectbox(
        "Selecciona el año de población",
        [
            "2015 Population",
            "2020 Population",
            "2022 Population"
        ]
    )

    # Muestra el gráfico del año seleccionado.
    grafico_anio = top10.set_index("Country/Territory")[[anio]]

    st.bar_chart(grafico_anio)


    # ========================================================
    # 13. MOSTRAR U OCULTAR DATOS
    # ========================================================

    # checkbox(): crea una casilla de selección.
    # Si está marcada, muestra la información adicional.

    if st.checkbox("Mostrar datos estadísticos"):

        st.write("Total:", total)
        st.write("Promedio:", promedio)
        st.write("Mediana:", mediana)
        st.write("Mínimo:", minimo)
        st.write("Máximo:", maximo)


# ============================================================
# 14. MENSAJE CUANDO NO SE HA CARGADO EL ARCHIVO
# ============================================================

else:

    # warning(): muestra un mensaje de advertencia.
    st.warning("Por favor, sube un archivo CSV para comenzar el análisis.")


# ============================================================
# FIN DEL PROGRAMA
# ============================================================
