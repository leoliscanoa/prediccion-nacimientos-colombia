# Predicción de Nacimientos en Colombia
Un modelo de Machine Learning predictivo para analizar y proyectar las tasas de natalidad en Colombia utilizando datos históricos del DANE. Este proyecto tiene como objetivo apoyar la planificación de políticas públicas relacionadas con salud, educación e infraestructura, mediante un análisis detallado de los datos y visualizaciones gráficas interactivas.
## Tabla de Contenidos
- [Características](#caracter%C3%ADsticas)
- [Visualizaciones](#visualizaciones)
- [Requisitos](#requisitos)
- [Instalación](#instalaci%C3%B3n)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Licencia](#licencia)
- [Colaboradores](#colaboradores)
- [Referencias](#referencias)

## Características
- **Modelo Predictivo**: Implementación de modelos de aprendizaje automático para pronosticar nacimientos basados en patrones históricos.
- **Datos Oficiales**: Uso de microdatos suministrados por el DANE para asegurar precisión y calidad en las predicciones.
- **Visualizaciones Dinámicas**: Gráficos y tablas informativas con bibliotecas como `matplotlib` y . `seaborn`
- **Análisis Descriptivo**: Exploración de las tendencias de natalidad y sus relaciones con factores demográficos.
- **Documentación y Transparencia**: Proceso y código bien documentado para replicabilidad y ampliación del proyecto.

## Visualizaciones
El análisis incluye las siguientes visualizaciones:
1. **Tendencia Anual de Nacimientos**: Gráficas de líneas que muestran la evolución de los nacimientos por año.
2. **Distribución por Género**: Histograma de la proporción de nacimientos masculinos y femeninos.
3. **Características Geográficas**: Mapas temáticos que proyectan tasas de nacimiento por departamento y municipio.
4. **Factores Asociados con la Natalidad**: Gráficos de barras para explorar características como edad materna, peso al nacer y nivel educativo de las madres.
5. **Tendencia Mensual de Nacimientos**: Análisis por mes para observar estacionalidad en las tasas de natalidad.

## Requisitos
- **Python 3.9 o superior**
- Librerías principales:
    - pandas 2.0.0 o superior
    - numpy 1.24.0 o superior
    - matplotlib 3.7.0 o superior
    - seaborn 0.12.0 o superior
    - scikit-learn 1.2 o superior

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
1. Explorar y preprocesar los datos:
    - Ejecutar el archivo correspondiente al análisis exploratorio de datos (EDA).

2. Entrenar el modelo:
    - Correr el script encargado del entrenamiento de modelos predictivos:
``` 
     python train_model.py
```
1. Visualizar resultados:
    - Consultar los gráficos generados en el proceso de análisis:
``` 
     python visualize_results.py
```
1. Hacer predicciones con nuevos datos:
    - Usar el modelo guardado para generar predicciones:
``` 
     python predict.py --input input_data.csv --output predictions.csv
```
## Estructura del Proyecto
``` 
birth-prediction/
├── data/
│   ├── nac2020.csv                    # Microdatos de nacimientos del 2020
│   ├── nac2021.csv                    # Microdatos de nacimientos del 2021
│   ├── nac2022.csv                    # Microdatos del 2022
│   └── BD-EEVV-Nacimientos-2023.csv   # Microdatos más recientes
├── actividad-5.ipynb                  # Archivo con implementación de machine learning
├── CONTRIBUTING.md                    # Archivo con participantes del proyecto
├── diccionario_de_datos.md            # Archivo con ampliación del diccionario de datos del DANE
├── requirements.txt                   # Dependencias necesarias
├── README.md                          # Documentación del proyecto
└── LICENSE.txt                        # Licencia del proyecto
```

## Licencia
El proyecto está licenciado bajo [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](http://creativecommons.org/licenses/by-nc-sa/4.0/).
### Eres libre de:
- **Compartir**: Copiar y redistribuir el material en cualquier formato.
- **Adaptar**: Modificar el material bajo atribuciones especificadas.

### Condiciones:
- **Reconocimiento**: Dar crédito a los autores originales.
- **No Comercial**: No usar el proyecto para fines comerciales.
- **Mismos Términos**: Distribuir las obras derivadas bajo la misma licencia.

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
