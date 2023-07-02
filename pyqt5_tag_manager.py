import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QListWidget, QTextEdit, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.file_names = []
        self.extensions = [".safetensors", ".ckpt"]
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.display_info)

        button = QPushButton("文件路径")
        button.clicked.connect(self.get_files)

        v_box = QVBoxLayout()
        v_box.addWidget(button)
        v_box.addWidget(self.list_widget)

        layout.addLayout(v_box)

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(250, 250)

        self.text_box = QTextEdit(self)

        self.save_button = QPushButton("保存")
        self.save_button.clicked.connect(self.save_file)

        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.image_label)
        v_box2.addWidget(self.text_box)
        v_box2.addWidget(self.save_button)

        layout.addLayout(v_box2)

        self.setLayout(layout)
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('File Browser')

    def get_files(self):
        dir_path = QFileDialog.getExistingDirectory(self, 'Select a directory')
        self.list_widget.clear()
        self.file_names.clear()

        for file in os.listdir(dir_path):
            if file.endswith(tuple(self.extensions)):
                self.file_names.append(os.path.join(dir_path, file))
                self.list_widget.addItem(file)

    def display_info(self):
        index = self.list_widget.currentRow()
        file_path = self.file_names[index]
        self.text_box.clear()
        self.image_label.clear()

        txt_file_path = os.path.splitext(file_path)[0] + '.txt'
        if os.path.isfile(txt_file_path):
            with open(txt_file_path, 'r') as file:
                content = file.read()
                self.text_box.insertPlainText(content)

        image_path = os.path.splitext(file_path)[0] + '.png'
        if os.path.isfile(image_path):
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaled(250, 250, Qt.KeepAspectRatio,Qt.SmoothTransformation))

    def save_file(self):
        index = self.list_widget.currentRow()
        file_path = self.file_names[index]
        txt_file_path = os.path.splitext(file_path)[0] + '.txt'
        content = self.text_box.toPlainText()

        with open(txt_file_path, 'w') as file:
            file.write(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())


#pyinstaller --noconsole --onefile  pyqt5_tag_manager.py