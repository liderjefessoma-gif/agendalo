# Guía de prueba: registrar médico

## Cómo abrir el programa

En la terminal, dentro de la carpeta `agendalo`, escribe:

```
PYTHONPATH=src python3 -m agendalo
```

- Aparece la pantalla de inicio con los roles.
- El programa ya tiene registrados dos médicos de ejemplo, aunque no los muestra al abrir:
  - **Luis Fernández Soto:** CMP 054321
  - **Ana Ríos Paredes:** CMP 061234
- Para llegar a "Registrar médico":
  1. escribe `3` y Enter (Administrador);
  2. escribe `2` y Enter (Registrar médico).
- Para cerrar el programa en cualquier momento: Ctrl + C.

## Preguntas

Cada pregunta empieza en "Registrar médico", salvo la 10.

### 1. ¿Puedo registrar un médico con datos correctos?

Escribe, uno por uno:

| El programa pide | Escribe |
|---|---|
| CMP | `070707` |
| Nombres | `Rosa` |
| Apellidos | `Quispe Huamán` |
| Especialidad | `1` |
| Días de atención | `L X V` |
| Hora de inicio | `09:00` |
| Hora de fin | `12:30` |

Deberías ver:

```
>> Médico registrado: Dr. Rosa Quispe Huamán — Medicina general
   CMP: 070707
   Días de atención:
     - Lunes
     - Miércoles
     - Viernes
   Horario: de 09:00 a 12:30
```

### 2. ¿Rechaza un CMP que no tiene 6 números?

- En CMP escribe `12345`.
- Deberías ver:
  - `>> Error: el CMP debe tener 6 dígitos numéricos. Intente de nuevo.`
  - otra vez `CMP:`

### 3. ¿Rechaza un CMP que ya está registrado?

- En CMP escribe `054321`. Es el CMP del médico de ejemplo Luis Fernández Soto.
- Deberías ver:
  - `>> Error: el CMP ya está registrado. Ingrese otro CMP.`
  - otra vez `CMP:`

### 4. ¿Pide los nombres si los dejo en blanco?

- En CMP escribe `070708`.
- En Nombres presiona solo Enter.
- Deberías ver:
  - `>> Error: ingrese nombres y apellidos.`
  - otra vez `Nombres:`

### 5. ¿Rechaza una especialidad que no está en la lista?

- Llega a Especialidad con datos correctos:
  - CMP: `070709`
  - Nombres: `Rosa`
  - Apellidos: `Quispe`
- En Especialidad escribe `4`.
- Deberías ver:
  - `>> Error: opción no válida. Elija un número de la lista.`
  - otra vez `Elija el número de la especialidad:`

### 6. ¿Pide al menos un día de atención?

- Llega a Días de atención con datos correctos.
- Presiona solo Enter.
- Deberías ver:
  - `>> Error: ingrese al menos un día (L M X J V S).`
  - otra vez `Escriba las letras de los días, separadas por espacios:`

### 7. ¿Rechaza un día que no existe?

- En Días de atención escribe `D`.
- Deberías ver:
  - `>> Error: ingrese al menos un día (L M X J V S).`
  - otra vez `Escriba las letras de los días, separadas por espacios:`

### 8. ¿Rechaza una hora mal escrita?

- En Hora de inicio escribe `8:15`.
- Deberías ver:
  - `>> Error: la hora debe tener el formato HH:MM, en :00 o :30.`
  - otra vez `Hora de inicio (HH:MM):`

### 9. ¿Rechaza una hora de fin anterior a la de inicio?

- En Hora de inicio escribe `10:00`.
- En Hora de fin escribe `09:00`.
- Deberías ver:
  - `>> Error: la hora de inicio debe ser menor que la hora de fin.`
  - otra vez `Hora de fin (HH:MM):`

### 10. ¿Solo el Administrador ve "Registrar médico"?

- En la pantalla de inicio escribe `1` (Admisión).
- Deberías ver un menú con solo `0. Volver al inicio`, sin "Registrar médico".
- Escribe `0` para volver y prueba con `2` (Médico): tampoco aparece.
- Escribe `0` y luego `3` (Administrador): aquí sí aparece `2. Registrar médico`.

### 11. ¿Vuelve al menú con Enter después de registrar?

- Termina la pregunta 1.
- Cuando veas `Presione Enter para volver al menú.`, presiona Enter.
- Deberías ver otra vez el menú de Administrador.
