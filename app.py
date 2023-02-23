import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from main import Control


class GUI:
    def __init__(self, master):
        self.master = master
        master.geometry("200x200")
        master.title("Hide Data in Images")
        
        # Initialize a Control object 
        self.control = Control("", "")

        # Create a file selection button
        self.select_image_button = tk.Button(master, text="Select Image for hiding data", command=self.load_image)
        self.select_image_button.pack()

        # Create a button to encode the image 
        self.encode_button = tk.Button(master, text="Encode", command=self.encode)
        self.encode_button.pack()
        
        # Create a button to decode the image
        self.decode_button = tk.Button(master, text="Decode", command=self.decode)
        self.decode_button.pack()
        
        """
        # Create a canvas to display the image
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()
        """
        # Create a text field to enter text
        self.text_field = tk.Entry(master)
        self.text_field.pack()

        # Bind the <Return> key to the text field to a callback function
        self.text_field.bind("<Return>", self.save_text)

        
        # Create a label
        self.label = tk.Label(master, text="No notification")
        self.label.pack()

        # The image path for encryption or decryption
        self.image_path = ""

    def decode(self):
        self.control.decode = self.image_path
        message = self.control.decrypt()
        self.label['text'] = message
        
    def encode(self):
        self.control.encode = self.image_path
        self.control.encrypt()
    def save_text(self, event):
        text = self.text_field.get()
        self.control.text = text
    def load_image(self):
        # Use filedialog to select an image from the file system
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
        self.image_path = file_path
        print(file_path)
        """
        
        if file_path:
            # Load the selected image and display it on the canvas
            image = Image.open(file_path)
            image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=image)
            self.canvas.image = image
        """


if __name__ == "__main__": 
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
