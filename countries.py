import requests
import streamlit as st

def get_all_countries():
  try:
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)

    if response.status_code == 200:
      return response.json()
    else:
      print('Error', response)
      return []
  except Exception as error:
    st.error(f"Error al cargar países: {error}")
    return []

def get_country_by_name(name):
  try:
    url = f'https://restcountries.com/v3.1/name/{name}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
      return []
  except Exception as error:
    st.error(f"Error al cargar países: {error}")
    return []