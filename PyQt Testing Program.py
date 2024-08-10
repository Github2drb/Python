import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        button = QPushButton('Click me')
        button.clicked.connect(self.on_click)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setWindowTitle('PyQt Example')
        self.show()

    def on_click(self):
        print('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())