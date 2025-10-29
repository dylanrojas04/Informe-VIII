# Comunicación inalámbrica punto a punto con NRF24L01 y Raspberry Pi Pico 2W

Este proyecto implementa un **enlace inalámbrico punto–punto** utilizando módulos **NRF24L01** y **Raspberry Pi Pico 2W**, con control remoto de **servomotor** en tiempo real y visualización en pantalla **OLED (RX)**.

Además, se realiza un **análisis del espectro en 2.4 GHz**, selección óptima de canal, evaluación de alcance y análisis del protocolo **SPI** con analizador lógico.

---

## 🎯 Objetivos del proyecto

- Implementar un enlace **NRF24L01 (SPI)** entre dos Raspberry Pi Pico 2W (TX/RX).
- Controlar un **servomotor remotamente** desde el TX con visualización del ángulo.
- Visualizar los datos recibidos en **pantalla OLED (RX)**.
- Analizar el **espectro 2.4–2.5 GHz** para seleccionar un canal libre.
- Evaluar **alcance en exteriores** con diferentes potencias y data rates.
- Capturar y analizar el protocolo **SPI** con analizador lógico.
- (Opcional) Comparar con **presupuesto teórico de enlace (link budget)**.

---

## 📡 Tecnologías utilizadas

| Componente | Función principal |
|------------|-------------------|
| **NRF24L01** | Comunicación inalámbrica SPI (2.4 GHz) |
| **Raspberry Pi Pico 2W** | Microcontrolador principal (TX/RX) |
| **Joystick + MPU6050** | Entrada analógica y movimiento (TX) |
| **Servo PWM** | Actuador de control remoto (RX) |
| **OLED SSD1306 (I2C)** | Visualización de datos en RX |

---


## ✅ Estado actual

- ✔ Control remoto del **servomotor** funcionando
- ✔ Canal seleccionado: **44** (baja interferencia)
- ✔ Pruebas documentadas en este repositorio

> **Todo el análisis de pruebas, capturas y validaciones está documentado dentro de este repositorio GitHub.**
