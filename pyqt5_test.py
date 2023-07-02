from datetime import datetime

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QFontMetrics, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QFrame, QVBoxLayout, QLabel, QLineEdit, QPushButton, \
    QDialog, QPlainTextEdit, QSizePolicy


class ChatBubblePlainText(QPlainTextEdit):
    def __init__(self, parent=None):
        super(ChatBubblePlainText, self).__init__(parent)
        self.setReadOnly(True)
        self.adjustSize()
        self.setStyleSheet("background-color: white; color: black; border-radius: 10px; padding: 10px;")

    def sizeHint(self):
        doc_layout = self.document().documentLayout()
        doc_size = doc_layout.documentSize()
        return doc_size.toSize()


class ChatBubbleLabel(QLabel):
    def __init__(self, sender, message, timestamp):
        super().__init__()

        # 根据发送者改变气泡的颜色
        if sender == 'user':
            self.setStyleSheet("""
                background-color: #D2E1FF;
                border-radius: 10px;
                padding: 10px;
                color: black;
            """)
            self.setAlignment(Qt.AlignRight)
        else:
            self.setStyleSheet("""
                background-color: #EAEAEA;
                border-radius: 10px;
                padding: 10px;
                color: black;
            """)
            self.setAlignment(Qt.AlignLeft)

        # 设置气泡的文本为消息和时间戳
        self.setText(f"{message}\n{timestamp}")

        # 设置气泡的尺寸策略
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.setWordWrap(True)


class ChatDialog(QDialog):
    def __init__(self):
        super().__init__()

        # 设置窗口样式为对话框风格
        self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)



        # 创建垂直布局
        layout = QVBoxLayout()



        # 创建输入文本框和发送按钮
        self.input_text = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.handleSendButton)

        # 添加输入文本框和发送按钮到布局中
        layout.addWidget(self.input_text)
        layout.addWidget(self.send_button)


        # 将布局设置为对话框的布局
        self.setLayout(layout)

    def handleSendButton(self):
        message = self.input_text.text()
        if message:
            timestamp = datetime.now().strftime("%H:%M")
            chat_bubble = ChatBubbleLabel('user', message, timestamp)
            self.layout().insertWidget(0, chat_bubble)
            self.input_text.clear()



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.draggable:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False
            event.accept()

if __name__ == "__main__":
    app = QApplication([])
    chat_dialog = ChatDialog()
    chat_dialog.show()
    app.exec_()