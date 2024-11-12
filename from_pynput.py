from pynput.keyboard import Key, Controller
import time

# Initialize the keyboard controller
keyboard = Controller()

print('Starting Anti-AFK Script...')
print("Press 'ESC' to exit...")
print('Starting Anti-AFK-Protocol in 10 seconds...')
time.sleep(10)
print('Starting Anti-AFK-Protocol now...')

# Start Anti-AFK-Mechanism (jumping, typing)
while True:
    # Jump 5 times
    for _ in range(5):  # Jump 5 times
        keyboard.press(Key.space)  # Press space for jump
        time.sleep(0.1)  # Hold space for a short moment
        keyboard.release(Key.space)
        time.sleep(0.2)  # Wait before the next jump

    # Wait for 2.5 seconds after jumping before typing the message
    time.sleep(2.5)

    # Press Enter and type the message slowly
    keyboard.press(Key.enter)
    time.sleep(0.1)
    keyboard.release(Key.enter)
    time.sleep(0.2)
    
    # Type the message slowly (added slight delay between keystrokes for a more natural speed)
    message = "Gemacht Für RaspBerry Vom Lieben Oni (!Cat) Not For Retail discord.gg/oniware "
    for char in message:
        keyboard.type(char)
        time.sleep(0.1)  # Slow down typing slightly

    # Press Enter again to send the message
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)  # Wait for the message to be sent

    # Wait for 10 seconds before repeating the process
    time.sleep(10)
