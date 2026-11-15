# HU02 Registrar médico: diseño técnico

- **Reglas, mensajes y flujo:** están en [reglas-de-negocio.md](reglas-de-negocio.md).
- **Este documento:** describe cómo los implementa el código.

## Estructura

```
src/agendalo/
  __main__.py
    textos y diccionarios de los menús
    mostrar_menu
    cargar_datos_ejemplo y mostrar_pruebas de todas las historias
    principal(): P00
    ZONA DE PRUEBAS
  persona.py
    Persona (abstracta)
      nombres, apellidos
      nombre_completo()
      describir()  (abstracto)
  medico.py
    ESPECIALIDADES
    DIAS
    Medico(Persona)
      cmp, especialidad, dias, hora_inicio, hora_fin
      describir()
  validaciones.py
    validar_cmp
    validar_nombre
    validar_especialidad
    validar_dias
    validar_hora
  clinica.py
    ERROR_CMP_REPETIDO
    Clinica
      medicos  (lista)
      registrar_medico(medico)
      buscar_medico(cmp)
  hu02/
    __init__.py
      docstring con el número y el nombre de la historia
    pantalla.py
      pantalla_registrar_medico(clinica)  (P02)
    datos_ejemplo.py
      crear_medico_ejemplo(...)
      cargar_datos_ejemplo(clinica)
      mostrar_pruebas(clinica)
```

- **Archivos compartidos:** los usan todas las historias.
  - `persona.py`
  - `medico.py`
  - `validaciones.py`
  - `clinica.py`
- **Carpeta de la historia (`hu02/`):**
  - la pantalla de HU02;
  - los datos de ejemplo de HU02.

## Decisiones de implementación

### Modelo

- **`Persona`:**
  - clase abstracta (`abc.ABC`);
  - `describir()` es abstracto.
- **`Medico`:** hereda de `Persona` e implementa `describir()`.
- **CMP:** se guarda como texto (`str`), para conservar el cero inicial.
- **Horas:** `datetime.time`, leídas con `datetime.strptime(texto, "%H:%M")`.
- **Días:**
  - `DIAS` es un diccionario letra → nombre del día (`"X": "Miércoles"`), en orden de lunes a sábado;
  - el médico guarda la lista de letras en ese orden.

### Validaciones

- **Cada función de `validaciones.py`:**
  - devuelve el dato convertido;
  - o lanza `ValueError` con el mensaje de la regla.
- **Hora de fin:** `validar_hora(texto, inicio=hora_inicio)` valida:
  - el formato;
  - que la hora sea mayor que `inicio`.

### Clínica

- **`Clinica.registrar_medico(medico)`:**
  - recibe un `Medico` ya creado;
  - lanza `ValueError(ERROR_CMP_REPETIDO)` si el CMP ya existe.
- **`buscar_medico`:** recorre la lista con un `for`.
- **Instancia única:**
  - se crea una vez en `principal()`;
  - se pasa a cada pantalla;
  - los datos viven en memoria.

### Pantalla P02

- **Un `while True` por dato:**
  1. lee con `input`;
  2. llama a su validación dentro de `try`/`except ValueError`;
  3. si falla, imprime el mensaje y repite hasta que el dato sea válido.
- **CMP repetido:** se revisa con `clinica.buscar_medico(cmp)` apenas se ingresa el CMP, antes de pedir los demás datos.
- **Opciones en pantalla:** un `for` imprime una opción por línea:
  - sobre `ESPECIALIDADES`;
  - sobre `DIAS`.
- **Mensaje de registro:**
  - primera línea con `describir()`;
  - debajo, con sangría:
    - el CMP;
    - los días, un `- <nombre del día>` por línea;
    - el horario, con `strftime("%H:%M")`.

### Menús

- **Por rol:**
  - un texto con las líneas del menú (`TEXTO_MENU_ADMINISTRADOR`);
  - un diccionario opción → función (`MENU_ADMINISTRADOR = {"2": pantalla_registrar_medico}`).
- **P00:** `principal()` elige el menú del rol con `if`/`elif`.

### Estilo del código

- Sintaxis básica de Python:
  - `if`
  - `for`
  - `while`
  - `try`/`except`
  - funciones y clases
- Un nombre descriptivo por valor.
- Un docstring de una línea en cada clase y función.

## Datos de ejemplo y modo de prueba

- **`hu02/datos_ejemplo.py`:**
  - **`crear_medico_ejemplo(...)`:** pasa cada dato por su función de validación y devuelve el `Medico`.
  - **`cargar_datos_ejemplo(clinica)`:**
    - registra los médicos de ejemplo sin imprimir nada;
    - `principal()` lo ejecuta siempre al iniciar, desde `cargar_datos_ejemplo` del main.
  - **`mostrar_pruebas(clinica)`:** imprime:
    - el título `===== HU02 REGISTRAR MÉDICO: DATOS DE EJEMPLO =====`;
    - los médicos registrados;
    - un caso rechazado por cada regla, con su mensaje.
- **Flag `--pruebas`:** `principal()` revisa `sys.argv`. Con el flag:
  1. imprime «Prueba automática del sistema.»;
  2. ejecuta `mostrar_pruebas` de cada historia;
  3. termina, sin mostrar P00.

## ZONA DE PRUEBAS

- **Qué es:**
  - un solo comentario de bloque (`'''`) al final de `__main__.py`;
  - con la salida de consola de una ejecución real con `--pruebas`, copiada tal cual;
  - cada historia aparece bajo su título.
- **Cómo actualizarla:**
  1. Desde la raíz del repo, ejecuta `PYTHONPATH=src python3 -m agendalo --pruebas`.
  2. Copia la salida completa.
  3. Reemplaza el contenido del bloque `ZONA DE PRUEBAS` con esa salida.

## Ejecución

- **Uso normal:** `PYTHONPATH=src python3 -m agendalo`
- **Solo la prueba automática:** `PYTHONPATH=src python3 -m agendalo --pruebas`

## Cómo agregar una historia

1. Crea `src/agendalo/huNN/` (por ejemplo `hu05`) con:
   - `__init__.py`
   - `pantalla.py`
   - `datos_ejemplo.py`
2. En `__main__.py`:
   - importa su pantalla y su `datos_ejemplo`;
   - agrega su opción:
     - en el texto del menú del rol;
     - en el diccionario de ese rol;
   - en el orden de las historias, llama a:
     - su `cargar_datos_ejemplo(clinica)`, dentro de `cargar_datos_ejemplo` del main;
     - su `mostrar_pruebas(clinica)`, dentro de `mostrar_pruebas` del main.
3. Según lo que necesite la historia:
   - **subclases nuevas de `Persona`** (por ejemplo `Paciente`): implementan `describir()`;
   - **listas nuevas** (`pacientes`, `citas`): van en `Clinica`, con sus métodos `registrar_*` y `buscar_*`;
   - **métodos nuevos de `Medico`** (horarios libres, horas disponibles): van en `medico.py`;
   - **validaciones nuevas** (DNI, fecha): van en `validaciones.py`, con el mismo estilo.
4. Ejecuta con `--pruebas` y actualiza la ZONA DE PRUEBAS.

## Definición de hecho técnica

- [ ] Las horas se guardan como `datetime.time`.
- [ ] `Persona` es abstracta y `Medico` hereda de ella.
- [ ] Las clases y funciones de "Estructura" existen con esos nombres.
- [ ] La ZONA DE PRUEBAS:
  - [ ] tiene la salida real de una ejecución con `--pruebas`;
  - [ ] tiene un caso válido y un caso rechazado por cada regla.
- [ ] Todo el código, los nombres y los commits están en español.
- [ ] Rama `feat/hu02-registrar-medico`, PR a `main`.
