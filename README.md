# Predicción de Nacimientos en Colombia
Un modelo de Machine Learning predictivo para analizar y proyectar las tasas de natalidad en Colombia utilizando datos históricos del DANE.

## Tabla de Contenidos
- [Características](#caracter%C3%ADsticas)
- [Visualizaciones](#visualizaciones)
- [Requisitos](#requisitos)
- [Datos utilizados](#datos-utilizados)
- [Instalación](#instalaci%C3%B3n)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Colaboradores](#colaboradores)
- [Referencias](#referencias)

## Características
- **Modelo predictivo**: Implementación de modelos de aprendizaje automático para pronosticar nacimientos basados en patrones históricos.
- **Datos oficiales**: Uso de microdatos suministrados por el DANE para asegurar precisión y calidad en las predicciones.
- **Visualizaciones**: Gráficos y tablas informativas con bibliotecas como `matplotlib` y . `seaborn`
- **Análisis descriptivo**: Exploración de las tendencias de natalidad y sus relaciones con factores demográficos.
- **Documentación y transparencia**: Proceso y código bien documentado para replicabilidad y ampliación del proyecto.

## Visualizaciones
El análisis incluye las siguientes visualizaciones:
1. **Tendencia anual de nacimientos**: Gráficas de líneas que muestran la evolución de los nacimientos por año.
2. **Distribución por género**: Histograma de la proporción de nacimientos masculinos y femeninos.
3. **Características geográficas**: Mapas temáticos que proyectan tasas de nacimiento por departamento y municipio.
4. **Factores asociados con la natalidad**: Gráficos de barras para explorar características como edad materna, peso al nacer y nivel educativo de las madres.
5. **Tendencia mensual de nacimientos**: Análisis por mes para observar estacionalidad en las tasas de natalidad.

## Requisitos
- **Python 3.9 o superior**
- Librerías principales:
    - pandas 2.0.0 o superior
    - numpy 1.24.0 o superior
    - matplotlib 3.7.0 o superior
    - seaborn 0.12.0 o superior
    - scikit-learn 1.2 o superior

## Datos utilizados:

Se utilizarán los siguientes archivos CSV, que contienen datos de nacimientos en Colombia para los años 2020, 2021, 2022 y 2023:
- [Estadísticas Vitales - EEVV – 2020](https://microdatos.dane.gov.co/index.php/catalog/732)
- [Estadísticas Vitales - EEVV – 2021](https://microdatos.dane.gov.co/index.php/catalog/775)
- [Estadísticas Vitales - EEVV – 2022](https://microdatos.dane.gov.co/index.php/catalog/807)
- [Estadísticas Vitales - EEVV – 2023](https://microdatos.dane.gov.co/index.php/catalog/843)

>Fuente: Departamento Administrativo Nacional de Estadística: www.dane.gov.co. Queda en cambio prohibida la copia o reproducción de los datos en cualquier medio electrónico (redes, bases de datos, cd rom, diskettes) que permita la disponibilidad de esta información a múltiples usuarios sin el previo visto bueno del DANE por medio escrito.

## Instalación
1. Crear un entorno virtual:
``` 
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
```
1. Instalar las dependencias:
``` 
   pip install -r requirements.txt
```
## Uso
1. Asegúrate de abrir el archivo Jupyter Notebook () y verifica que tu entorno contiene todas las dependencias necesarias. `actividad-5.ipynb`
2. Ejecuta el Notebook paso a paso:
    - Las celdas están organizadas de manera secuencial, iniciando con el análisis exploratorio de datos (EDA) y terminando con el modelo predictivo.
    - Asegúrate de seguir las instrucciones documentadas en cada celda para utilizarlo correctamente.

3. Analiza los resultados:
    - Interactúa con los gráficos generados.
    - Observa las salidas de los modelos predictivos.
    - Explora las visualizaciones obtenidas y ajusta los parámetros de ser necesario dentro de las celdas.

4. Modifica o adapta el Notebook de ser necesario para nuevos análisis o predicciones.

## Estructura del Proyecto
``` 
aplicaciones-1-machine-learning/
├── data/
│   ├── nac2020.csv                    # Microdatos de nacimientos del 2020
│   ├── nac2021.csv                    # Microdatos de nacimientos del 2021
│   ├── nac2022.csv                    # Microdatos del 2022
│   └── BD-EEVV-Nacimientos-2023.csv   # Microdatos más recientes
├── helpers/
│   └── generate_dict.py               # Script para generar diccionario de datos
├── html/
│   └── actividad-5.html               # Archivo HTML de actividad-5.ipynb
├── actividad-5.ipynb                  # Archivo con implementación de machine learning
├── CONTRIBUTING.md                    # Archivo con participantes del proyecto
├── LICENSE.txt                        # Licencia del proyecto
├── README.md                          # Documentación del proyecto
└── requirements.txt                   # Dependencias necesarias
```

## Licencia
El proyecto está licenciado bajo [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](http://creativecommons.org/licenses/by-nc-sa/4.0/).
### Eres libre de:
- **Compartir**: Copiar y redistribuir el material en cualquier formato.
- **Adaptar**: Modificar el material bajo atribuciones especificadas.

### Condiciones:
- **Reconocimiento**: Dar crédito a los autores originales.
- **No comercial**: No usar el proyecto para fines comerciales.
- **Mismos términos**: Distribuir las obras derivadas bajo la misma licencia.

Consulta el archivo [LICENSE.txt](LICENSE.txt) para más detalles.

## Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Hbechara-dev">
        <img src="https://github.com/Hbechara-dev.png" width="100px;" alt="Hermes Bechara"/><br>
        <sub><b>Hermes Bechara</b></sub>
      </a><br>
      <sub>hacordoba77@unisalle.edu.co</sub>
    </td>
    <td align="center">
      <a href="https://github.com/leoliscanoa">
        <img src="https://github.com/leoliscanoa.png" width="100px;" alt="Andrés Liscano"/><br>
        <sub><b>Andrés Liscano</b></sub>
      </a><br>
      <sub>aliscano20@unisalle.edu.co</sub>
    </td>
    <td align="center">
      <a href="https://github.com/EfraMonR">
        <img src="https://github.com/EfraMonR.png" width="100px;" alt="Efrain Montealegre"/><br>
        <sub><b>Efrain Montealegre</b></sub>
      </a><br>
      <sub>emontealegre19@unisalle.edu.co)</sub>
    </td>
  </tr>
</table>

Para conocer más sobre cómo contribuir a este proyecto, consulta nuestro [archivo de contribución](CONTRIBUTING.md).

## Referencias
- DANE. (2023). Microdatos de Estadísticas Vitales. Recuperado de: [DANE Colombia](https://www.dane.gov.co)
- pandas development team. (s.f.). *pandas: Powerful data analysis toolkit*. Recuperado de https://pandas.pydata.org/
- NumPy developers. (s.f.). *NumPy*. Recuperado de https://numpy.org/
- Matplotlib. (s.f.). *Matplotlib: Python Plotting*. Recuperado de https://matplotlib.org/
- Seaborn developers. (s.f.). *seaborn: statistical data visualization*. Recuperado de https://seaborn.pydata.org/
- scikit-learn developers. (s.f.). *scikit-learn: machine learning in Python*. Recuperado de https://scikit-learn.org/stable/
