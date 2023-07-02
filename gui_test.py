import os
import sys
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_image(filename, width, height):               #读取图片
    img = Image.open(resource_path(filename))
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Sample App")
        self.overrideredirect(True)  # Make the window borderless
        self.attributes('-topmost', True)

        self._offsetx = 0
        self._offsety = 0

        self.bind('<Button-1>', self.clickwin)
        self.bind('<B1-Motion>', self.dragwin)
        self.bind('<Button-3>', self.popup)

        self.attributes('-alpha', 1)
        # Load images
        self.geometry("350x500")

        bg_img = Image.open("test.png")
        image = Image.open("安可64.png")
        # Convert the image to a tkinter-compatible photo image
        self.tk_img = ImageTk.PhotoImage(bg_img) # Replace with your image path
        self.tk_image = ImageTk.PhotoImage(image)

        self.background_label = tk.Label(self, image=self.tk_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.avatar_label = tk.Label(self, image=self.tk_image)
        self.avatar_label.grid(row=0, column=0, rowspan=2, padx=20, pady=20)

        # create chat box
        self.chat_box = tk.Text(self, height=20, width=50)
        self.chat_box.grid(row=0, column=1, rowspan=2, padx=20, pady=20)

        # create message entry
        self.message_entry = tk.Entry(self, width=40)
        self.message_entry.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        # create send button
        self.send_button = tk.Button(self, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=1, padx=20, pady=20)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_box.insert(tk.END, "\n" + message)
            self.message_entry.delete(0, tk.END)


    def popup(self, event):
        self.popup_menu = tk.Menu(self, tearoff=0)
        self.popup_menu.add_command(label="关闭", command=self.quit)
        self.popup_menu.post(event.x_root, event.y_root)

    def quit(self):
        self.destroy()


    def update_text(self):
        # Get the text from entry
        input_text = self.entry.get()

        # Insert the text to text box
        self.text_box.insert("end", input_text)

        # Clear the entry
        self.entry.delete(0, "end")

    def clickwin(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def dragwin(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{0}+{1}'.format(x, y))


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
