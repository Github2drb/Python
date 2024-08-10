import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from pycomm3 import LogixDriver

class PLCInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.plc = LogixDriver('192.168.1.100')

    def initUI(self):
        self.setWindowTitle('PLC Interface')
        layout = QVBoxLayout()
        
        readButton = QPushButton('Read PLC Data')
        readButton.clicked.connect(self.readPLCData)
        layout.addWidget(readButton)

        writeButton = QPushButton('Write to PLC')
        writeButton.clicked.connect(self.writeToPLC)
        layout.addWidget(writeButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def readPLCData(self):
        with self.plc:
            data = self.plc.read('SomeTag')
        print(f"Read data: {data}")

    def writeToPLC(self):
        with self.plc:
            self.plc.write(('SomeTag', 100))
        print("Data written to PLC")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PLCInterface()
    ex.show()
    sys.exit(app.exec_())