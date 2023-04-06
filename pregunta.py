"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    Datos = pd.read_fwf("clusters_report.txt", skiprows=4, skipfooter=0, names=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
    Datos['cluster'] = Datos['cluster'].fillna(method="ffill")
    Datos['principales_palabras_clave'] = Datos[['cluster','principales_palabras_clave']].groupby(['cluster'])['principales_palabras_clave'].transform(lambda x: ' '.join((x)))
    Datos = Datos.dropna()
    Datos = Datos.reset_index()
    del Datos["index"]
    Datos = Datos.replace(r'\s+', ' ', regex=True)
    Datos['principales_palabras_clave'] = Datos['principales_palabras_clave'].str.replace('.','')
    Datos['porcentaje_de_palabras_clave'] = Datos['porcentaje_de_palabras_clave'].str[:-2]
    Datos['porcentaje_de_palabras_clave'] = Datos['porcentaje_de_palabras_clave'].str.replace(',','.')
    Datos['porcentaje_de_palabras_clave'] = pd.to_numeric(Datos['porcentaje_de_palabras_clave'])
    Datos = Datos.astype({'principales_palabras_clave':'string'})
    
    return Datos
