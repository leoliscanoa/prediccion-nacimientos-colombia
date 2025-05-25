import json
import requests

# Lista de URLs de los JSON de las variables
urls = [
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1780/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1781/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1782/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1783/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1784/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1785/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1786/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1787/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1788/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1789/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1790/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1791/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1792/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1793/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1794/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1795/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1796/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1797/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1798/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1799/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1800/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1801/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1802/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1803/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1804/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1805/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1806/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1807/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1808/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1809/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1810/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1811/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1812/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1813/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1814/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1816/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1817/json",
    "https://microdatos.dane.gov.co/index.php/metadata/export_variable/843/V1818/json"
]

# Usar un set para evitar URLs duplicadas
unique_urls = list(set(urls))

# Lista para almacenar la información de todas las variables
all_variables_info = []
failed_urls = []


def formatear_qstnlit(qstnlit):
    """Formatea el contenido de var_qstn_qstnlit respetando saltos de línea."""
    if qstnlit:
        return qstnlit.replace('\n', '<br>').replace('\r', '<br>')
    return "NA"


def generar_tabla_var_catgry(var_catgry):
    """Genera tabla Markdown para `var_catgry`."""
    if not var_catgry:
        return "| Código | Etiqueta | Frecuencia |\n|--------|----------|------------|\n| NA     | NA       | NA         |\n"

    tabla = "| Código | Etiqueta | Frecuencia |\n"
    tabla += "|--------|----------|------------|\n"
    for item in var_catgry:
        value = item.get("value", "NA")
        labl = item.get("labl", "NA")
        stats = item.get("stats", [])
        freq = "NA"
        for stat in stats:
            if stat.get("type") == "freq":
                freq = stat.get("value", "NA")
        tabla += f"| {value} | {labl} | {freq} |\n"
    return tabla


for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error para códigos de estado HTTP 4xx/5xx
        data = json.loads(response.text)

        # Formatear contenido de var_qstn_qstnlit (preguntas del cuestionario)
        cuestionario_limpio = formatear_qstnlit(data.get("var_qstn_qstnlit", "NA"))

        # Generar la tabla de categorías
        tabla_categorias = generar_tabla_var_catgry(data.get("var_catgry", None))

        # Almacenar información formateada para la variable
        variable_info = {
            'name': data.get('name', 'NA'),
            'labl': data.get('labl', 'NA'),
            'var_qstn_qstnlit': cuestionario_limpio,
            'tabla_categorias': tabla_categorias
        }
        all_variables_info.append(variable_info)
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener o procesar la URL {url}: {e}")
        failed_urls.append(url)
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON de la URL {url}: {e}")
        failed_urls.append(url)

# Construir el documento Markdown
markdown_output = "# Diccionario de Datos de Variables DANE\n\n"
markdown_output += "Este documento contiene la descripción y los valores de las variables obtenidas de los microdatos del DANE.\n\n"

# Tabla inicial con columnas Variable, Etiqueta y Concepto
markdown_output += "| Variable | Etiqueta | Concepto |\n"
markdown_output += "|----------|----------|----------|\n"

# Rellenar la tabla inicial con datos
for var_info in all_variables_info:
    concepto_limpio = formatear_qstnlit(var_info['var_qstn_qstnlit'])
    markdown_output += f"| {var_info['name']} | {var_info['labl']} | {concepto_limpio} |\n"

# Añadir una separación antes del detalle de variables
markdown_output += "\n## Detalle por Variable\n\n"

for var_info in all_variables_info:
    markdown_output += f"## Variable: {var_info['name']}\n\n"
    markdown_output += f"- **Etiqueta**: {var_info['labl']}\n"
    markdown_output += f"- **Preguntas del Cuestionario**:\n  {var_info['var_qstn_qstnlit']}\n\n"
    markdown_output += "### Tabla de Categorías:\n"
    markdown_output += var_info['tabla_categorias'] + "\n"

# Registrar URLs fallidas, si las hay
if failed_urls:
    markdown_output += "\n## URLs que fallaron al cargar:\n\n"
    for url in failed_urls:
        markdown_output += f"- {url}\n"

# Guardar el resultado en un archivo Markdown
with open("../diccionario_de_datos.md", "w", encoding="utf-8") as md_file:
    md_file.write(markdown_output)

print("El diccionario de datos ha sido guardado en el archivo 'diccionario_de_datos.md'")
