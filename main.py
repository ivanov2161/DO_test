import serial
import time

# Подключение к COM порту (замените 'COM1' на ваш реальный порт)
ser = serial.Serial('COM1', 9600, timeout=1)


# Отправка команды на управление выходом
def control_output(output_number, state):
    command = f"SET_OUT {output_number} {state}\n"
    ser.write(command.encode())


# Чтение состояния входа
def read_input(input_number):
    command = f"READ_IN {input_number}\n"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    return int(response)


# Пример использования
output_number = 1
input_number = 1

# Включение выхода
control_output(output_number, 1)

# Пауза для демонстрации
time.sleep(1)

# Чтение состояния входа
input_state = read_input(input_number)
print(f"Состояние входа {input_number}: {input_state}")

# Выключение выхода
control_output(output_number, 0)

# Закрытие порта
ser.close()
