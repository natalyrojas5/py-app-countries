import streamlit as st
from countries import get_all_countries, get_country_by_name

def load_countries():
  with st.spinner('Cargando datos ...'):
    return get_all_countries()

def reset_filter():
  st.session_state['filter_name'] = ''
  st.session_state['countries'] = load_countries()

def show_filter():
  st.subheader('Filtrar país por nombre')

  col1, col2 = st.columns([3, 1])
  with col1:
    filter_name = st.text_input(
      'Escribe el nombre del pais',
      value=st.session_state['filter_name'],
      on_change=reset_filter)

  with col2:
    if st.button('Resetear', on_click=reset_filter):
      pass

  return filter_name

def display_countries(countries):
    num_columns = 2
    columns = st.columns(num_columns)

    for index, country in enumerate(countries):
      col = columns[index % num_columns]

      country_name = country.get('name', {}).get('common', '-')
      region = country.get('region', '-')
      flag_url = country.get('flags',{}).get('png', '')

      with col:
        with st.container():
          col1, col2 = st.columns([1, 3])

          with col1:
            if(flag_url):
              st.image(flag_url, use_container_width=True)

          with col2:
            st.subheader(country_name)
            st.write(f"Región {region}")

def main():
  st.title('Listado de Países')

  if 'filter_name' not in st.session_state:
    st.session_state['filter_name'] = ''

  if 'countries' not in st.session_state:
     st.session_state['countries'] = load_countries()

  countries = st.session_state['countries']
  filter_name = show_filter()

  if filter_name:
    with st.spinner(f"Buscando países que coincidan con '{filter_name}' ... "):
      countries = get_country_by_name(filter_name)

  st.divider()

  if countries:
    display_countries(countries)
  else:
    st.warning('No se encontraron países')

if __name__ == "__main__":
    main()