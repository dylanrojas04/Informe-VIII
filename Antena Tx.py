#TX
from machine import Pin, SPI, I2C, ADC
from nrf24l01 import NRF24L01, POWER_3, SPEED_1M
import utime

# --- Configuración NRF24L01 ---
spi = SPI(0, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
csn = Pin(15, Pin.OUT)
ce = Pin(14, Pin.OUT)

nrf = NRF24L01(spi, csn, ce, channel=90, payload_size=32)

# Configurar máxima potencia (0 dBm) y velocidad de 1 Mbps
nrf.set_power_speed(POWER_3,SPEED_1M)

# Dirección TX → RX
nrf.open_tx_pipe(b'\xe1\xf0\xf0\xf0\xf0')
nrf.open_rx_pipe(1, b'\xd2\xf0\xf0\xf0\xf0')

# --- Configuración I2C (MPU6050) ---
i2c = I2C(0, scl=Pin(13), sda=Pin(12))
MPU_ADDR = 0x68
i2c.writeto_mem(MPU_ADDR, 0x6B, b'\x00')  # Despertar sensor

def read_word(reg):
    high = i2c.readfrom_mem(MPU_ADDR, reg, 1)[0]
    low = i2c.readfrom_mem(MPU_ADDR, reg + 1, 1)[0]
    value = (high << 8) | low
    if value >= 0x8000:
        value = -((65535 - value) + 1)
    return value

def read_accel():
    ax = read_word(0x3B) / 16384.0
    ay = read_word(0x3D) / 16384.0
    az = read_word(0x3F) / 16384.0
    return ax, ay, az

# --- Joystick ---
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

print("🚀 Transmisor listo. Enviando datos cada 100 ms...")

# --- Bucle principal ---
while True:
    try:
        ax, ay, az = read_accel()
        x_val = xAxis.read_u16()
        y_val = yAxis.read_u16()

        # Mapear joystick X a ángulo de 0° a 180°
        angulo = int((x_val / 65535) * 180)
        angulo = max(0, min(180, angulo))

        mensaje = f"ACC,{ax:.2f},{ay:.2f},{az:.2f},SERVO,{angulo}"
        nrf.send(mensaje.encode())
        print("📤 Enviado:", mensaje)

    except OSError:
        print("⚠️ Error al enviar datos (NRF no responde)")

    utime.sleep(0.001)