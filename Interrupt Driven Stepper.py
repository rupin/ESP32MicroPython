# Write your code here :-)
from machine import Pin, Timer

# Define GPIO pins for ULN2003 driver
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(21, Pin.OUT)
IN4 = Pin(22, Pin.OUT)

# Step sequence (Half-Step Mode)
step_sequence = [
    [1, 0, 0, 1],  # Step 1
    [1, 0, 0, 0],  # Step 2
    [1, 1, 0, 0],  # Step 3
    [0, 1, 0, 0],  # Step 4
    [0, 1, 1, 0],  # Step 5
    [0, 0, 1, 0],  # Step 6
    [0, 0, 1, 1],  # Step 7
    [0, 0, 0, 1],  # Step 8
]

# Variables for stepping
step_index = 0  # Tracks current step
direction = 1   # 1 = Forward, -1 = Reverse
step_limit = 2048  # Steps for one full revolution (adjust as needed)
step_count = 0  # Count steps

# Create a timer object
timer = Timer(0)

def stepper_interrupt(timer):
    global step_index, step_count, direction

    # Set GPIO pins based on step sequence
    IN1.value(step_sequence[step_index][0])
    IN2.value(step_sequence[step_index][1])
    IN3.value(step_sequence[step_index][2])
    IN4.value(step_sequence[step_index][3])

    # Move to the next step
    step_index += direction

    # Wrap around step sequence (0-7)
    if step_index >= len(step_sequence):
        step_index = 0
    elif step_index < 0:
        step_index = len(step_sequence) - 1

    # Step counting and direction reversal
    step_count += 1
    if step_count >= step_limit:
        step_count = 0  # Reset step counter
        direction *= -1  # Reverse direction

# Start timer with 5ms interval (200Hz)
timer.init(mode=Timer.PERIODIC, period=5, callback=stepper_interrupt)
