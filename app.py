import io
import PySimpleGUI as sg
import textwrap

import cv2

from main import Control

def make_window():

    sg.theme('TanBlue')
    sg.set_options(font=("Helvetica", 14))

    image_viewer_column = [
        [
            sg.Text("Image File"),
            sg.In(size=(25, 1), enable_events=True, key="-File-"),
            sg.FileBrowse(file_types=((('PNG Files', '*.png'),))),
        ],
        [
            sg.Image(key="-IMAGE-", size=(400, 400)),
        ]
    ]

    key_column = [
        [sg.Text("Private key", key="-KEY-")],
    ]

    encode_column = [
        [sg.Text("Public key", key="-ENCODE-PUBLIC-")],
        [sg.In(size=(25, 1), enable_events=True, key="-ENCODE-PUBLIC-INPUT-"), sg.FileBrowse(file_types=(('Key Files', '*.key'),))],
        [sg.Text("Enter text to encode")],
        [sg.InputText("", key="-ENCODE-MES-", size=(35, 2))],
        [sg.Text("Save in folder", key="-ENCODE-FILE-")],
        [sg.In(size=(25, 1), enable_events=True, key="-ENCODE-FILE-INPUT-"), sg.FolderBrowse()],
        [sg.Button("Encode", key="-ENCODE-BUTTON-", disabled=True)],
    ]

    decode_column = [
        [sg.Text("Decoded text:", key="-DECODED-", size=(35, 1))],
        [sg.Button("Decode", key="-DECODE-BUTTON-", disabled=True)],
    ]

    settings_column = [
        [sg.Text("Choose an image first!", key="-STATUS-", font=("Helvetica", 16), size=(40, None))],
        [sg.Text('_' * 40, size=(40, 2))],
        [sg.Frame("Encode", encode_column)],
        [sg.Text('_' * 40, size=(40, 2))],
        [sg.Frame("Decode", decode_column)],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(image_viewer_column),
            sg.VSeperator(),
            sg.Column(settings_column),
        ],
        [
            sg.Text("By: Luong, Son va Thang (K65-DSAI-HUST)")
        ]
    ]

    window = sg.Window("Image Steganography Project", layout)

    return window


if __name__ == "__main__":
    window = make_window()
    control = Control("")
    # event loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Event when an image is selected
        if event == "-File-" and values["-File-"]:
            filename = values["-File-"]

            # Get image size
            img = cv2.imread(filename)
            size = (img.shape[1], img.shape[0])

            # Resize the image to fit the window
            scale = 400 / max(size)
            size = (int(size[0] * scale), int(size[1] * scale))
            img = cv2.resize(img, size)

            # Convert the image to bytes
            is_success, buffer = cv2.imencode(".png", img)
            io_buf = io.BytesIO(buffer)
            ppl = io_buf.getvalue()

            try:
                window.Element("-IMAGE-").update(source=ppl, size=size)

                window.Element("-ENCODE-BUTTON-").update(disabled=False)
                window.Element("-DECODE-BUTTON-").update(disabled=False)

                window.Element("-STATUS-").update("Hide a message into an image or decrypt a message hidden in one")

                control.set_filename(filename)
            except Exception as e:
                window.Element("-TOUT-").update("Failed opening file or invalid file type")

        if event == "-ENCODE-BUTTON-":
            message = values["-ENCODE-MES-"]
            output_path = values["-ENCODE-FILE-INPUT-"]
            public_key = values["-ENCODE-PUBLIC-INPUT-"]
            if message == "":
                window.Element("-STATUS-").update("Please enter a message to encode")

            elif output_path == "":
                window.Element("-STATUS-").update("Please choose a directory to save the encoded image")
            elif public_key == "":
                window.Element("-STATUS-").update("Please choose a directory of a public key")
            else:
                control.encrypt(message, output_path, public_key)
                window.Element("-STATUS-").update("Message encoded successfully")


        if event == "-DECODE-BUTTON-":    
            
            message = control.decrypt()

            if message == "":
                window.Element("-STATUS-").update("No message found in the image")

            else:
                window.Element("-DECODED-").update("Decoded text: " + message)
                
    window.close()

