# HU03, HU04 y HU05 Citas: reglas de negocio

## Para qué sirve

- **HU03 Reservar cita:** Admisión reserva una cita para un paciente con un médico, en una fecha y hora libres.
- **HU04 Reprogramar cita:** Admisión cambia la fecha u hora de una cita, sin crear una cita nueva.
- **HU05 Cancelar cita:** Admisión cancela una cita y el horario del médico queda libre.

## Quién puede hacerlo

- **Admisión:** ve las opciones:
  - 3. Reservar cita
  - 4. Reprogramar cita
  - 5. Cancelar cita
- **Médico y Administrador:** no ven estas opciones.

## Reglas de la cita

- Cada cita dura 30 minutos. Las horas son :00 o :30.
- Cada cita tiene un código único: C0001, C0002, C0003…
- Estados de una cita:
  - **Reservada:** toda cita nueva nace así.
  - **Cancelada:** la cita no se borra; queda en la lista con este estado.
  - **Atendida:** la usa el historial (HU06); estas historias no la asignan.
- Solo las citas **Reservada** ocupan el horario del médico.

## Reglas de disponibilidad

Se revisan al reservar (HU03) y al reprogramar (HU04), en este orden:

| Regla | Mensaje si no se cumple |
|---|---|
| La fecha no es pasada. | `>> Error: la fecha ya pasó.` |
| El médico atiende ese día de la semana. | `>> Error: el médico no atiende ese día.` |
| La hora está dentro del horario del médico. | `>> Error: la hora está fuera del horario del médico (08:00 a 13:00).` |
| El médico no tiene otra cita Reservada a esa hora. | `>> Error: horario ocupado. Elija uno de los horarios libres.` |
| El paciente no tiene otra cita Reservada a esa hora, aunque sea con otro médico. | `>> Error: el paciente ya tiene una cita a esa hora.` |

- El horario del mensaje de "fuera del horario" es el del médico elegido.
- Al reprogramar, la cita no choca consigo misma.

## Reglas de cada dato

| Dato | Regla | Mensaje si no se cumple |
|---|---|---|
| DNI | 8 dígitos numéricos. | `>> Error: el DNI debe tener 8 dígitos numéricos. Intente de nuevo.` |
| DNI | El paciente está registrado. | `>> Error: paciente no encontrado. Verifique el DNI.` |
| Médico | Un número de la lista. | `>> Error: opción no válida. Elija un número de la lista.` |
| Fecha | Formato DD/MM/AAAA. | `>> Error: la fecha debe tener el formato DD/MM/AAAA.` |
| Fecha | El médico tiene al menos un horario libre ese día. | `>> Error: el médico no tiene horarios libres ese día. Elija otra fecha.` |
| Hora | Formato HH:MM, en :00 o :30. | `>> Error: la hora debe tener el formato HH:MM, en :00 o :30.` |
| Código de cita | Existe. | `>> Error: cita no encontrada.` |
| Código de cita (HU04) | La cita está Reservada. | `>> Error: solo se reprograman citas en estado "Reservada".` |
| Código de cita (HU05) | La cita está Reservada. | `>> Error: solo se cancelan citas en estado "Reservada".` |
| Confirmación | S o N, en mayúscula o minúscula. | `>> Error: responda S o N.` |

- Si un dato está mal, el programa dice qué está mal y pide ese mismo dato otra vez.
- En DNI y en código de cita, escribir `0` vuelve al menú sin hacer cambios.

## Cómo se reserva una cita (P03)

```
===== RESERVAR CITA =====
DNI del paciente (0 para volver): 45678912
>> Paciente: Ana María Quispe Rojas (DNI 45678912)
Médicos:
  1. Dr. Luis Fernández Soto — Cardiología — 08:00 a 13:00
  2. Dr. Ana Ríos Paredes — Pediatría — 14:00 a 18:30
Elija el número del médico: 1
Fecha (DD/MM/AAAA): 25/11/2026
Horarios libres: 08:00  08:30  09:30  10:30  11:00  11:30  12:00  12:30
Hora (HH:MM): 09:30
>> Cita reservada. Código: C0004
   25/11/2026 09:30 — Dr. Luis Fernández Soto
Presione Enter para volver al menú.
```

## Cómo se reprograma una cita (P04)

```
===== REPROGRAMAR CITA =====
Código de cita (0 para volver): C0001
>> Cita actual: 25/11/2026 09:00 — Dr. Luis Fernández Soto
   Paciente: Ana María Quispe Rojas
Nueva fecha (DD/MM/AAAA): 26/11/2026
Horarios libres: 08:00  08:30  09:00  ...
Nueva hora (HH:MM): 11:00
Cambiar de 25/11/2026 09:00 a 26/11/2026 11:00. ¿Confirmar? (S/N): S
>> Cita C0001 reprogramada.
Presione Enter para volver al menú.
```

- Si responde N: `>> No se hicieron cambios.`
- La cita conserva su código.

## Cómo se cancela una cita (P05)

```
===== CANCELAR CITA =====
Código de cita (0 para volver): C0001
>> Cita: 26/11/2026 11:00 — Dr. Luis Fernández Soto
   Paciente: Ana María Quispe Rojas
¿Seguro que desea cancelar esta cita? (S/N): S
>> Cita C0001 cancelada. El horario quedó libre.
Presione Enter para volver al menú.
```

- Si responde N: `>> La cita no se canceló.`

## Pacientes y citas de ejemplo

- El registro de pacientes es de HU01. Mientras tanto, el programa empieza con dos pacientes ficticios:
  - **Ana María Quispe Rojas:** DNI 45678912
  - **Jorge Salas Medina:** DNI 41234567
- Y con tres citas de ejemplo:
  - **C0001:** Ana María con el Dr. Luis Fernández Soto, 25/11/2026 09:00, Reservada.
  - **C0002:** Jorge con el Dr. Luis Fernández Soto, 25/11/2026 10:00, Reservada.
  - **C0003:** Jorge con la Dra. Ana Ríos Paredes, 26/11/2026 14:00, Cancelada.
- Los datos se pierden al cerrar el programa.

## Criterios de aceptación

- **HU03:**
  - El paciente y el médico existen.
  - La fecha cae en un día de atención del médico y la hora está dentro de su horario.
  - No permite dos citas del mismo médico ni del mismo paciente a la misma fecha y hora.
  - La fecha no es pasada.
  - Genera un código y deja la cita en estado Reservada.
  - Cada cita dura 30 minutos.
  - Muestra los horarios libres antes de pedir la hora.
- **HU04:**
  - Busca la cita por código; si no existe, muestra "cita no encontrada".
  - Solo reprograma citas Reservada.
  - Aplica las mismas validaciones que HU03.
  - Muestra la fecha anterior y la nueva antes de confirmar.
- **HU05:**
  - Busca la cita por código; si no existe, muestra "cita no encontrada".
  - Pide confirmación antes de cancelar.
  - Cambia el estado a Cancelada sin borrar la cita.
  - El horario queda libre para otra reserva.
- Solo el rol Admisión ve estas opciones.
