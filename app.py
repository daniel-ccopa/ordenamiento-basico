import streamlit as st
import io

def bubble_sort(data, reverse=False):
    n = len(data)
    data = data.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            a = data[j]
            b = data[j + 1]
            if isinstance(a, str) and isinstance(b, str):
                a_cmp = a.upper()
                b_cmp = b.upper()
            else:
                a_cmp = a
                b_cmp = b
            if (a_cmp > b_cmp and not reverse) or (a_cmp < b_cmp and reverse):
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def main():
    st.set_page_config(page_title="Ordenador de Datos", page_icon="📊", layout="centered")

    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
        background: url("https://raw.githubusercontent.com/daniel-ccopa/Apuntes-7semestre/refs/heads/main/fondo.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.sidebar.image("https://raw.githubusercontent.com/daniel-ccopa/Apuntes-7semestre/refs/heads/main/finesi.png", use_column_width=True)

    st.title("📋 Ordenador de Cadenas y Números")
    st.markdown("""
    **Universidad Nacional del Altiplano - PUNO**

    **Facultad de Ingeniería Estadística e Informática**

    **Curso:** Ingeniería de Software I

    **Semestre:** Séptimo - 2024-II

    **Autor:** Cristian Daniel Ccopa Acero

    **Docente:** Ing. Juan Reynaldo Paredes Quispe

    ---
    """)

    st.sidebar.write("Esta aplicación te permite ordenar **cadenas** o **números** en orden ascendente o descendente. Puedes cargar los datos desde un archivo o ingresarlos manualmente, visualizarlos, ordenarlos y guardar el resultado en otro archivo.")
    st.sidebar.title("Opciones")

    data_type = st.sidebar.selectbox("Selecciona el tipo de datos", ["Cadenas", "Números"])

    sort_order = st.sidebar.radio("Selecciona el orden", ["Ascendente", "Descendente"])

    st.header("Entrada de Datos")
    input_option = st.radio("Selecciona una opción para ingresar los datos:", ["Cargar desde archivo", "Ingresar manualmente"])

    data = []
    if input_option == "Cargar desde archivo":
        uploaded_file = st.file_uploader("Selecciona un archivo de texto", type=["txt", "csv"])

        if uploaded_file is not None:
            try:
                content = uploaded_file.read().decode('utf-8')
                data = content.strip().splitlines()
                if data_type == "Números":
                    data = [float(item.strip()) for item in data if item.strip()]
                else:
                    data = [item.strip() for item in data if item.strip()]
            except Exception as e:
                st.error(f"Error al procesar el archivo: {e}")
        else:
            st.info("Por favor, carga un archivo para continuar.")

    else:
        manual_input = st.text_area("Ingresa los datos separados por comas o nuevas líneas:")
        if manual_input:
            try:
                if ',' in manual_input:
                    data = manual_input.strip().split(',')
                else:
                    data = manual_input.strip().splitlines()
                if data_type == "Números":
                    data = [float(item.strip()) for item in data if item.strip()]
                else:
                    data = [item.strip() for item in data if item.strip()]
            except Exception as e:
                st.error(f"Error al procesar los datos ingresados: {e}")
        else:
            st.info("Por favor, ingresa los datos para continuar.")

    if data:
        st.subheader("Datos Ingresados")
        st.write(data)

        reverse_order = True if sort_order == "Descendente" else False
        sorted_data = bubble_sort(data, reverse=reverse_order)

        st.subheader(f"Datos Ordenados ({sort_order})")
        st.write(sorted_data)

        if data_type == "Números":
            output_data = '\n'.join([str(item) for item in sorted_data])
        else:
            output_data = '\n'.join(sorted_data)
        output = io.BytesIO()
        output.write(output_data.encode('utf-8'))
        output.seek(0)

        st.download_button(
            label="💾 Descargar Datos Ordenados",
            data=output,
            file_name='datos_ordenados.txt',
            mime='text/plain'
        )
    else:
        st.info("No hay datos para procesar.")

if __name__ == "__main__":
    main()