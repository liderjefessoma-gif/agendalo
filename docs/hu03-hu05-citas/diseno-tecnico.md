# HU03, HU04 y HU05 Citas: diseño técnico

- **Reglas, mensajes y flujo:** están en [reglas-de-negocio.md](reglas-de-negocio.md).
- **Este documento:** explica cómo está armado el código.

Seguí la estructura de HU02 (ver [diseño técnico de HU02](../hu02-registrar-medico/diseno-tecnico.md), "Cómo agregar una historia").

## Qué agregué

```
src/agendalo/
  paciente.py          (nuevo)
    Paciente(Persona)
      dni, telefono, fecha_nacimiento
      describir()
  cita.py              (nuevo)
    RESERVADA, CANCELADA, ATENDIDA
    Cita
      codigo, paciente, medico, fecha_hora, estado
      describir()
  medico.py            (cambia)
    LETRAS_DE_LA_SEMANA
    Medico
      horario_en_texto()
      horarios_del_dia(fecha)
  validaciones.py      (cambia)
    validar_dni
    validar_fecha
    validar_confirmacion
  clinica.py           (cambia)
    mensajes de error de pacientes y citas
    Clinica
      pacientes, citas  (listas nuevas)
      registrar_paciente, buscar_paciente
      buscar_cita
      medico_ocupado, paciente_ocupado
      horarios_libres
      validar_fecha_de_cita
      validar_disponibilidad
      reservar_cita, reprogramar_cita, cancelar_cita
  hu03/
    pantalla.py
      pedir_fecha_y_hora(...)   (la usa también HU04)
      pantalla_reservar_cita(clinica)  (P03)
    datos_ejemplo.py
      proximo_martes()
      cargar_datos_ejemplo(clinica)
      mostrar_citas(clinica)
      mostrar_pruebas(clinica)
  hu04/
    pantalla.py
      pantalla_reprogramar_cita(clinica)  (P04)
    datos_ejemplo.py
      mostrar_pruebas(clinica)
  hu05/
    pantalla.py
      pantalla_cancelar_cita(clinica)  (P05)
    datos_ejemplo.py
      mostrar_pruebas(clinica)
```

## Decisiones

### Paciente

- HU01 todavía no estaba, así que hice lo mínimo para poder reservar citas: la clase `Paciente`, `validar_dni`, `registrar_paciente` y `buscar_paciente`.
- Falta la pantalla P01. Quien haga HU01 puede usar todo esto tal cual.

### Cita

- La fecha y la hora van juntas en un `datetime`, así comparar dos citas es un solo `==`.
- El código se arma con la cantidad de citas: `"C" + str(numero).zfill(4)` → `C0001`.
- Cancelar no borra la cita, solo le cambia el estado.

### Horarios

- `Medico.horarios_del_dia(fecha)` arma la lista de bloques de 30 minutos desde la hora de inicio hasta antes de la hora de fin. Si el médico no atiende ese día, devuelve una lista vacía.
- Para saber qué día es, uso `fecha.weekday()` con `LETRAS_DE_LA_SEMANA` (lunes = 0 → `"L"`).
- `Clinica.horarios_libres` quita las horas que ya pasaron y las que tienen una cita Reservada.

### Una sola validación para reservar y reprogramar

- `Clinica.validar_disponibilidad(paciente, medico, fecha_hora, cita_a_ignorar)` revisa las 5 reglas en orden y lanza `ValueError` con el mensaje de la regla.
- Al reprogramar le paso la misma cita en `cita_a_ignorar`, para que no choque consigo misma.
- Así HU04 aplica las mismas reglas que HU03 sin copiar código.

### Pantallas

- Igual que P02: un `while True` por dato, con `try`/`except ValueError`.
- En DNI y código de cita, `0` vuelve al menú. Lo agregué porque si no hay pacientes o citas, no había forma de salir.
- `pedir_fecha_y_hora` está en `hu03/pantalla.py` y HU04 la importa, porque las dos piden fecha y hora igual.
- El código de cita se acepta en minúscula (`c0001`).

### Menú

- Admisión tiene las opciones 3, 4 y 5. Usé el número de la historia, como en el Word, para que después entre la 1 (HU01).

## Datos de ejemplo

- `hu03/datos_ejemplo.py` carga a la Dra. Carmen Ruiz Paz, dos pacientes y cuatro citas.
- Las citas van el **próximo martes** (`proximo_martes()`). Si usaba una fecha fija, el programa se caía al iniciar cuando esa fecha pasaba, porque la reserva de ejemplo también se valida.
- La Dra. Carmen está para poder probar que un paciente no tenga dos citas a la misma hora con médicos distintos; Luis y Ana Ríos nunca atienden a la misma hora.
- Por eso, la prueba de HU02 ahora lista tres médicos.
- `hu04` y `hu05` no cargan nada propio; sus pruebas usan las citas de HU03. Sus `cargar_datos_ejemplo` están vacías solo para seguir el molde de `__main__.py`.
- Las pruebas de HU04 y HU05 cambian las citas (reprograman C0002 y cancelan C0001), por eso van después de HU03.

## Ejecución

- **Uso normal:** desde la raíz del repo, `PYTHONPATH=src python3 -m agendalo`
- **Solo la prueba automática:** `PYTHONPATH=src python3 -m agendalo --pruebas`
- Si ya estás dentro de `src`, basta con `python3 -m agendalo`.
- Ejecutar `__main__.py` directo (por ejemplo con el botón ▶ del editor) da `ModuleNotFoundError: No module named 'agendalo'`. Hay que usar `-m`.

## Definición de hecho técnica

- [x] Cita guarda fecha y hora en un `datetime`.
- [x] `Paciente` hereda de `Persona`.
- [x] Reservar y reprogramar usan la misma `validar_disponibilidad`.
- [x] Cancelar cambia el estado sin borrar la cita.
- [x] La ZONA DE PRUEBAS tiene la salida real de `--pruebas`, con un caso válido y uno rechazado por cada regla.
- [x] Código, nombres y commits en español.
- [x] Rama `feat/hu03-hu05-citas`, PR a `main`.
