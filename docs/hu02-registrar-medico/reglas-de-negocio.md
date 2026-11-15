# HU02 Registrar médico: reglas de negocio

## Para qué sirve

- El administrador de la clínica registra a un médico con:
  - sus datos;
  - su especialidad;
  - su horario de atención.

## Quién puede hacerlo

- **Administrador:** ve la opción "Registrar médico".
- **Admisión y Médico:** tienen su propio menú, sin esa opción.

## Cómo se registra un médico

1. Al abrir el programa, la persona elige su rol:
   - 1. Admisión
   - 2. Médico
   - 3. Administrador
   - 0. Salir
2. El administrador elige "2. Registrar médico".
3. El programa pide los datos del médico, uno por uno, en este orden:
   - CMP
   - nombres
   - apellidos
   - especialidad
   - días de atención
   - hora de inicio
   - hora de fin
4. Si un dato está mal:
   - el programa dice qué está mal;
   - pide ese mismo dato otra vez;
   - los datos ya escritos se conservan.
5. Al terminar, muestra el médico registrado y espera Enter para volver al menú.
6. Para volver o salir:
   - en cualquier menú, 0 vuelve al inicio;
   - en el inicio, 0 cierra el programa.

### Ejemplo de lo que ve el administrador

```
===== REGISTRAR MÉDICO =====
CMP: 054321
Nombres: Luis
Apellidos: Fernández Soto
Especialidad:
  1. Medicina general
  2. Cardiología
  3. Pediatría
Elija el número de la especialidad: 2
Días de atención:
  L. Lunes
  M. Martes
  X. Miércoles
  J. Jueves
  V. Viernes
  S. Sábado
Escriba las letras de los días, separadas por espacios: L M X J V
Hora de inicio (HH:MM): 08:00
Hora de fin (HH:MM): 13:00
>> Médico registrado: Dr. Luis Fernández Soto — Cardiología
   CMP: 054321
   Días de atención:
     - Lunes
     - Martes
     - Miércoles
     - Jueves
     - Viernes
   Horario: de 08:00 a 13:00
Presione Enter para volver al menú.
```

## Reglas de cada dato

### CMP

- **Regla:** exactamente 6 números. Puede empezar con 0, por ejemplo 054321.
  - Mensaje si no se cumple: `>> Error: el CMP debe tener 6 dígitos numéricos. Intente de nuevo.`
- **Regla:** cada médico tiene un CMP distinto. Un CMP ya registrado no se acepta.
  - Mensaje si no se cumple: `>> Error: el CMP ya está registrado. Ingrese otro CMP.`

### Nombres y apellidos

- **Regla:** se escriben los dos; ninguno queda en blanco.
  - Mensaje si no se cumple: `>> Error: ingrese nombres y apellidos.`

### Especialidad

- **Regla:** se elige de la lista:
  - 1. Medicina general
  - 2. Cardiología
  - 3. Pediatría
- Mensaje si no se cumple: `>> Error: opción no válida. Elija un número de la lista.`

### Días de atención

- **Regla:** al menos un día, de lunes a sábado:
  - L: lunes
  - M: martes
  - X: miércoles
  - J: jueves
  - V: viernes
  - S: sábado
- **Cómo se escriben:**
  - separados por espacios;
  - sin repetir;
  - en mayúscula o minúscula.
- Mensaje si no se cumple: `>> Error: ingrese al menos un día (L M X J V S).`

### Hora de inicio y hora de fin

- **Regla:** horas y minutos, como 08:00. Los minutos son :00 o :30.
  - Mensaje si no se cumple: `>> Error: la hora debe tener el formato HH:MM, en :00 o :30.`
- **Regla:** la hora de fin es más tarde que la hora de inicio.
  - Mensaje si no se cumple: `>> Error: la hora de inicio debe ser menor que la hora de fin.`

### Opción de un menú

- **Regla:** es uno de los números que muestra el menú.
  - Mensaje si no se cumple: `>> Error: opción no válida. Elija un número del menú.`

## Mensaje al registrar

```
>> Médico registrado: Dr. <nombres> <apellidos> — <especialidad>
   CMP: <CMP>
   Días de atención:
     - <un día por línea>
   Horario: de <hora de inicio> a <hora de fin>
```

## Cómo se muestran las opciones

- Cuando el programa ofrece opciones, las muestra una debajo de otra:
  - roles;
  - menús;
  - especialidades;
  - días.

## Médicos de ejemplo

- El programa empieza con dos médicos ficticios ya registrados, aunque no los muestra al abrir:
  - **Dr. Luis Fernández Soto**
    - Especialidad: Cardiología
    - CMP: 054321
  - **Dr. Ana Ríos Paredes**
    - Especialidad: Pediatría
    - CMP: 061234
- Sus CMP ya están ocupados: sirven para ver el rechazo de un CMP repetido.
- Los médicos registrados se pierden al cerrar el programa.

## Criterios de aceptación

- Pide los datos del médico:
  - CMP
  - nombres
  - apellidos
  - especialidad
  - días de atención
  - horario de atención
- No permite un CMP ya registrado.
- La hora de inicio es menor que la hora de fin.
- Pide al menos un día de atención.
- La especialidad se elige de una lista:
  - 1. Medicina general
  - 2. Cardiología
  - 3. Pediatría
- Formatos:
  - días: L M X J V S;
  - horas: HH:MM.
- Al terminar:
  - muestra «>> Médico registrado: Dr. … — <especialidad>»;
  - vuelve al menú con Enter.
- Solo el rol Administrador ve esta opción.
