import os
import tkinter as tk
from tkinter import filedialog, Text, Listbox, END
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        root.geometry("724x464")
        self.file_names = []
        self.extensions = [".safetensors", ".ckpt"]

        self.button_frame = tk.Frame(root,)
        self.button_frame.pack(side=tk.LEFT)

        self.button = tk.Button(self.button_frame, text="文件路径", command=self.get_files)
        self.button.pack(side=tk.TOP)

        self.list_box = Listbox(self.button_frame)
        self.list_box.pack(fill=tk.BOTH)

        self.list_box.bind('<<ListboxSelect>>', self.display_info)

        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.RIGHT)

        self.image_label = tk.Label(self.right_frame)
        self.image_label.pack(side=tk.TOP)

        self.text_box = Text(self.right_frame, height=10)
        self.text_box.pack(side=tk.TOP, fill=tk.X)

        self.save_button = tk.Button(self.right_frame, text="保存", command=self.save_file)
        self.save_button.pack(side=tk.TOP)

    def get_files(self):
        dir_path = filedialog.askdirectory()
        self.list_box.delete(0, END)
        self.file_names.clear()

        for file in os.listdir(dir_path):
            if file.endswith(tuple(self.extensions)):
                self.file_names.append(os.path.join(dir_path, file))
                self.list_box.insert(END, file)

    def display_info(self, event):
        index = self.list_box.curselection()[0]
        file_path = self.file_names[index]
        self.text_box.delete('1.0', tk.END)
        self.image_label.config(image='')

        txt_file_path = os.path.splitext(file_path)[0] + '.txt'
        if os.path.isfile(txt_file_path):
            with open(txt_file_path, 'r') as file:
                content = file.read()
                self.text_box.insert('1.0', content)

        image_path = os.path.splitext(file_path)[0] + '.png'
        if os.path.isfile(image_path):
            image = Image.open(image_path)
            image.thumbnail((250, 250))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def save_file(self):
        index = self.list_box.curselection()[0]
        file_path = self.file_names[index]
        txt_file_path = os.path.splitext(file_path)[0] + '.txt'
        content = self.text_box.get('1.0', tk.END)

        with open(txt_file_path, 'w') as file:
            file.write(content)

root = tk.Tk()
app = App(root)
root.mainloop()


#pyinstaller --noconsole --onefile  tag_manager.py