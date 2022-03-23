import qrcode
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

# Create the root window
root = tk.Tk()
root.title('QR Code Generator')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfile(
        title='Open a file...',
        initialdir='/',
        filetypes=filetypes)

    img = qrcode.make(filename)
    img.save('qr.jpg')


open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)
root.mainloop()
