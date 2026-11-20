# Guía de prueba: reservar, reprogramar y cancelar citas

## Cómo abrir el programa

En la terminal, dentro de la carpeta `agendalo`, escribe:

```
PYTHONPATH=src python3 -m agendalo
```

- Para llegar a las citas: escribe `1` y Enter (Admisión). Aparecen:
  - `3. Reservar cita`
  - `4. Reprogramar cita`
  - `5. Cancelar cita`
- Para cerrar el programa en cualquier momento: Ctrl + C.

### Datos que ya trae el programa

- **Pacientes:**
  - Ana María Quispe Rojas: DNI `45678912`
  - Jorge Salas Medina: DNI `41234567`
- **Médicos:**
  1. Dr. Luis Fernández Soto: L a V, 08:00 a 13:00
  2. Dra. Ana Ríos Paredes: M J S, 14:00 a 18:30
  3. Dra. Carmen Ruiz Paz: L a V, 14:00 a 19:00
- **Citas**, todas el próximo martes:
  - `C0001`: Ana María con Luis a las 09:00, Reservada
  - `C0002`: Jorge con Luis a las 10:00, Reservada
  - `C0003`: Jorge con Ana Ríos a las 14:00, Cancelada
  - `C0004`: Ana María con Ana Ríos a las 15:00, Reservada

En esta guía, **«martes»** es la fecha del próximo martes, en formato DD/MM/AAAA. Por ejemplo, si hoy es jueves 19/11/2026, el martes es `24/11/2026`.

Cada pregunta empieza abriendo el programa de nuevo, así los datos vuelven a estar como arriba.

## Reservar cita (opción 3)

### 1. ¿Puedo reservar una cita con datos correctos?

| El programa pide | Escribe |
|---|---|
| DNI del paciente | `45678912` |
| Número del médico | `1` |
| Fecha | martes |
| Hora | `09:30` |

Deberías ver:

- `Horarios libres: 08:00  08:30  09:30  10:30  11:00  11:30  12:00  12:30` (faltan las 09:00 y las 10:00, que ya están ocupadas)
- `>> Cita reservada. Código: C0005`
- debajo, la fecha, `09:30` y el Dr. Luis Fernández Soto

### 2. ¿Rechaza un DNI mal escrito o que no existe?

- En DNI escribe `4567`.
  - Deberías ver: `>> Error: el DNI debe tener 8 dígitos numéricos. Intente de nuevo.`
- Luego escribe `99999999`.
  - Deberías ver: `>> Error: paciente no encontrado. Verifique el DNI.`
- Luego escribe `0`: vuelves al menú de Admisión.

### 3. ¿Rechaza fechas que no sirven?

- Llega a Fecha con DNI `45678912` y médico `1`.
- Escribe `2026-11-24`.
  - Deberías ver: `>> Error: la fecha debe tener el formato DD/MM/AAAA.`
- Escribe `01/01/2020`.
  - Deberías ver: `>> Error: la fecha ya pasó.`
- Escribe la fecha del sábado siguiente al martes (martes + 4 días).
  - Deberías ver: `>> Error: el médico no atiende ese día.`

### 4. ¿Rechaza una hora fuera del horario del médico?

- Llega a Hora con DNI `45678912`, médico `1` y fecha martes.
- Escribe `15:00`.
- Deberías ver: `>> Error: la hora está fuera del horario del médico (08:00 a 13:00).`

### 5. ¿Rechaza una hora que ya está ocupada?

- Llega a Hora con DNI `41234567`, médico `1` y fecha martes.
- Escribe `09:00` (es la hora de la cita C0001).
- Deberías ver: `>> Error: horario ocupado. Elija uno de los horarios libres.`

### 6. ¿Evita que un paciente tenga dos citas a la misma hora?

- Ana María ya tiene la cita C0004 el martes a las 15:00 con la Dra. Ana Ríos.
- Reserva con DNI `45678912`, médico `3` (Dra. Carmen), fecha martes.
- Escribe `15:00`.
- Deberías ver: `>> Error: el paciente ya tiene una cita a esa hora.`

## Reprogramar cita (opción 4)

### 7. ¿Puedo cambiar la fecha y hora de una cita?

| El programa pide | Escribe |
|---|---|
| Código de cita | `C0001` |
| Nueva fecha | el miércoles siguiente al martes |
| Nueva hora | `11:00` |
| ¿Confirmar? | `S` |

Deberías ver:

- `>> Cita actual:` con el martes a las 09:00 y el Dr. Luis
- `Cambiar de <martes> 09:00 a <miércoles> 11:00. ¿Confirmar? (S/N):`
- `>> Cita C0001 reprogramada.`

### 8. ¿Rechaza códigos que no sirven?

- En Código de cita escribe `C9999`.
  - Deberías ver: `>> Error: cita no encontrada.`
- Escribe `C0003` (está Cancelada).
  - Deberías ver: `>> Error: solo se reprograman citas en estado "Reservada".`

### 9. ¿Si digo N, la cita queda igual?

- Haz la pregunta 7, pero en ¿Confirmar? escribe `N`.
- Deberías ver: `>> No se hicieron cambios.`
- Vuelve a la opción 4 con `C0001`: la cita actual sigue siendo el martes a las 09:00.

## Cancelar cita (opción 5)

### 10. ¿Puedo cancelar una cita y se libera el horario?

- En Código de cita escribe `C0001`.
- En ¿Seguro que desea cancelar esta cita? escribe `S`.
- Deberías ver: `>> Cita C0001 cancelada. El horario quedó libre.`
- Ahora ve a la opción 3 y reserva con DNI `41234567`, médico `1`, fecha martes.
- En los horarios libres ahora sí aparece `09:00`.

### 11. ¿Si digo N, la cita no se cancela?

- En Código de cita escribe `C0002` y luego `N`.
- Deberías ver: `>> La cita no se canceló.`

### 12. ¿Rechaza cancelar una cita que ya está cancelada?

- En Código de cita escribe `C0003`.
- Deberías ver: `>> Error: solo se cancelan citas en estado "Reservada".`

## Solo Admisión ve estas opciones

### 13. ¿Médico y Administrador no ven las citas?

- En el inicio escribe `2` (Médico): no aparecen las opciones 3, 4 ni 5.
- Escribe `0` y luego `3` (Administrador): solo aparece `2. Registrar médico`.

## Prueba automática

Para ver todos los casos de una vez, sin escribir nada:

```
PYTHONPATH=src python3 -m agendalo --pruebas
```

Debe salir lo mismo que la ZONA DE PRUEBAS al final de `src/agendalo/__main__.py` (cambian solo las fechas, según el día en que lo ejecutes).
