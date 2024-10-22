# FastAPI

## FastAPI course that I deliver to my colleagues.

- pip install poetry (or safer, follow the instructions: https://python-poetry.org/docs/#installation)
- pip install requeriments.txt
- Install dependencies cd into the directory where the pyproject.toml is located then poetry install
- [UNIX]: Run the FastAPI server via poetry with the bash script: poetry run ./run.sh
- [WINDOWS]: Run the FastAPI server via poetry with the Python command: poetry run python app/main.py
- Open http://localhost:8001/
- To stop the server, press CTRL+C

---

## Entornos

Para crear un entorno virtual en Python en Windows, puedes seguir los pasos a continuación. Usar entornos virtuales es una buena práctica, ya que te permite aislar las dependencias de diferentes proyectos.

### Pasos para crear un entorno virtual en Windows:

#### 1. **Instalar Python (si aún no lo tienes)**

- Primero, asegúrate de tener Python instalado en tu sistema. Puedes verificarlo abriendo el símbolo del sistema (CMD) y ejecutando:

`python --version`

Si Python no está instalado, descárgalo de la página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/) y asegúrate de seleccionar la opción **"Add Python to PATH"** durante la instalación.

#### 2. **Abrir el Símbolo del Sistema (CMD)**

- Presiona `Windows + R`, escribe `cmd` y presiona `Enter`.

#### 3. **Instalar `virtualenv` (opcional)**

- Python 3.3 y versiones superiores ya incluyen el módulo `venv` para crear entornos virtuales, por lo que no es necesario instalar `virtualenv` a menos que prefieras usarlo.
- Si prefieres usar `virtualenv`, instálalo ejecutando:

  ```
  pip install virtualenv
  ```

#### 4. **Crear un entorno virtual**

- Navega a la carpeta de tu proyecto o a la carpeta donde deseas crear el entorno virtual. Usa el comando `cd` para cambiar de directorio, por ejemplo:

  ```
  cd C:\ruta\de\mi\proyecto
  ```

. Crea el entorno virtual usando el siguiente comando:

- Crea el entorno virtual usando el siguiente comando:

  - Si usas el módulo `venv` incluido en Python 3:
  - ```bash
     python -m venv nombre_del_entorno
    ```

  - Si prefieres virtualenv (después de instalarlo):
  - ````bash
         virtualenv nombre_del_entorno
        ```
    ````

Esto creará una carpeta llamada nombre_del_entorno en el directorio actual. Dentro de esta carpeta estarán los archivos necesarios para ejecutar el entorno virtual.

#### 5. **Activar el entorno virtual**

- Una vez creado el entorno virtual, debes activarlo. Ejecuta el siguiente comando:

  ```bash
     nombre_del_entorno\Scripts\activate
  ```

Si el entorno se activa correctamente, verás el nombre del entorno virtual al principio del prompt del símbolo del sistema. Por ejemplo:

```bash
(nombre_del_entorno) C:\ruta\de\mi\proyecto>

```

#### 6. **Instalar paquetes en el entorno**

- Ahora que el entorno está activo, puedes instalar paquetes usando pip y estarán aislados en este entorno. Por ejemplo:

```bash
pip install nombre_paquete

```

aca hacemos pip install requeriments.txt

#### 7. **Desactivar el entorno virtual**

- Cuando termines de trabajar en el entorno virtual, puedes desactivarlo ejecutando:

```bash
deactivate

```

#### 8. **Ejemplo completo:**

8.1. Crear el entorno virtual:

```bash
python -m venv mi_entorno
```

8.2. Activar el entorno:

```bash
mi_entorno\Scripts\activate
```

8.3. Instalar paquetes (por ejemplo, FastAPI):

```bash
pip install fastap
```

8.4. Desactivar el entorno:

```bash
deactivate
```

## Introducción a los Tipos de Python

Estos type hints son una nueva sintaxis, desde Python 3.6+, que permite declarar el tipo de una variable.

Usando las declaraciones de tipos para tus variables, los editores y otras herramientas pueden proveerte un soporte mejor.

Este es solo un tutorial corto sobre los Python type hints. Solo cubre lo mínimo necesario para usarlos con FastAPI... realmente es muy poco lo que necesitas.

Todo FastAPI está basado en estos type hints, lo que le da muchas ventajas y beneficios.

Pero, así nunca uses FastAPI te beneficiarás de aprender un poco sobre los type hints.

[Lectura Obligatoria](https://fastapi.tiangolo.com/es/python-types/)

---

## algo mas de Python

### 1. **Tupla (`tuple`)**

Una **tupla** es una secuencia ordenada de elementos inmutables. No puedes modificar, añadir o eliminar elementos de una tupla una vez que ha sido creada.

- **Características** :
- Inmutable: No se puede modificar una vez creada.
- Puede contener elementos duplicados.
- Puede almacenar cualquier tipo de datos.

```python
#Definición de una tupla
mi_tupla = (1, 2, 3, "a", "b")
print(mi_tupla)  # Salida: (1, 2, 3, 'a', 'b')

#Accediendo a un elemento
print(mi_tupla[0])  # Salida: 1

#Intentar modificar una tupla lanzará un error
mi_tupla[0] = 100  # Esto generaría un error
```

### 2. **Conjunto (`set`)**

Un **conjunto** es una colección desordenada de elementos únicos. No permite duplicados, y sus elementos no están indexados ni ordenados.

- **Características** :
- Desordenado: No tiene un orden específico.
- No se permite duplicados.
- Mutable: Puedes agregar y eliminar elementos.

```python
# Definición de un set
mi_set = {1, 2, 3, 4, 5, 3, 2}
print(mi_set)  # Salida: {1, 2, 3, 4, 5} (Los duplicados se eliminan)

# Agregar un elemento
mi_set.add(6)
print(mi_set)  # Salida: {1, 2, 3, 4, 5, 6}

# Eliminar un elemento
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4, 5, 6}

```

### 3. **Lista (`list`)**

Una **lista** es una colección ordenada y mutable de elementos. A diferencia de las tuplas, las listas pueden modificarse: puedes agregar, eliminar o cambiar sus elementos.

- **Características** :
- Ordenada: Mantiene el orden de inserción de los elementos.
- Mutable: Los elementos pueden ser modificados.
- Puede contener elementos duplicados.

```python
# Definición de una lista
mi_lista = [1, 2, 3, "a", "b", "a"]
print(mi_lista)  # Salida: [1, 2, 3, 'a', 'b', 'a']

# Agregar un elemento
mi_lista.append(4)
print(mi_lista)  # Salida: [1, 2, 3, 'a', 'b', 'a', 4]

# Eliminar un elemento
mi_lista.remove("a")
print(mi_lista)  # Salida: [1, 2, 3, 'b', 'a', 4]

# Modificar un elemento
mi_lista[0] = 100
print(mi_lista)  # Salida: [100, 2, 3, 'b', 'a', 4]

```

### 4. **Diccionario (`dict`)**

Un **diccionario** es una colección desordenada de pares clave-valor. Cada clave debe ser única, y se usa para acceder a su valor asociado.

- **Características** :
- Desordenado (aunque en versiones recientes de Python mantiene el orden de inserción).
- Mutable: Se pueden agregar, eliminar y modificar los pares clave-valor.
- Las claves deben ser únicas, pero los valores pueden repetirse.

```python
# Definición de un diccionario
mi_dict = {"nombre": "Cristian", "edad": 30, "ciudad": "Buenos Aires"}
print(mi_dict)  # Salida: {'nombre': 'Cristian', 'edad': 30, 'ciudad': 'Buenos Aires'}

# Acceder a un valor por su clave
print(mi_dict["nombre"])  # Salida: Cristian

# Agregar un nuevo par clave-valor
mi_dict["profesion"] = "Programador"
print(mi_dict)  # Salida: {'nombre': 'Cristian', 'edad': 30, 'ciudad': 'Buenos Aires', 'profesion': 'Programador'}

# Modificar un valor
mi_dict["edad"] = 31
print(mi_dict)  # Salida: {'nombre': 'Cristian', 'edad': 31, 'ciudad': 'Buenos Aires', 'profesion': 'Programador'}

# Eliminar un par clave-valor
del mi_dict["ciudad"]
print(mi_dict)  # Salida: {'nombre': 'Cristian', 'edad': 31, 'profesion': 'Programador'}

```
