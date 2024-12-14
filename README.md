# Listado de Países 🇵🇪

Este es un proyecto de Streamlit que permite visualizar y buscar países en una lista.

## Características

- **Visualización de países**: Se cargan y muestran países con su nombre, región y bandera.
- **Filtro de búsqueda**: Permite filtrar países por nombre.
- **Recarga de lista**: Si el filtro se borra o se hace clic en el botón "Resetear", la lista de países se recarga con todos los países disponibles.
- **Interacción simple**: Los usuarios pueden interactuar con la interfaz de manera fácil y rápida.

## Requisitos

Este proyecto utiliza **Streamlit** para la interfaz de usuario. Asegúrate de tener las siguientes dependencias instaladas:

- Python 3.x
- `streamlit`
- `requests` (si estás obteniendo la lista de países de una API externa)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   ```

2. Accede al directorio del proyecto:

   ```bash
   cd app_countries
   ```

## Uso

1. Ejecuta la aplicación de Streamlit:

   ```bash
   streamlit run app.py
   ```

2. La aplicación se abrirá en tu navegador. Ahora podrás ver la lista de países y usar el campo de filtro para buscar un país por su nombre.

### Funciones de la aplicación:

- **Campo de texto de búsqueda**: Permite al usuario escribir el nombre del país para filtrar los resultados.
- **Botón de reset**: Permite al usuario restablecer el filtro y recargar la lista de todos los países.
- **Listado de países**: Muestra el nombre, región y bandera de cada país.

## Estructura del proyecto

```plaintext
app-contries/
│
├── app.py                # Archivo principal de Streamlit
├── countries.py          # Módulo para obtener la lista de países
└── README.md             # Este archivo
```
