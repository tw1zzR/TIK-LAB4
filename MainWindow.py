from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from calculate_methods import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.info_loss = QLabel(self)
        self.transfer_time = QLabel(self)

        self.calculate_btn = QPushButton("CALCULATE", self)

        self.layout = QVBoxLayout()
        self.container = QWidget()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Transfer Info Calculator")
        self.setGeometry(1100, 500, 300, 200)
        self.setWindowIcon(QIcon("icon.png"))

        self.calculate_btn.clicked.connect(self.calculate_and_display)
        self.calculate_btn.setFixedHeight(50)

        self.layout.addWidget(self.info_loss, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.transfer_time, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.calculate_btn)

        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                font-family: Arial;
            }
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                font-family: Arial;
                background-color: rgb(95, 237, 107);
                border: 2px solid rgb(62, 130, 68);
            }
            QMainWindow {
                font-size: 16px;
                font-weight: bold;
                font-family: Arial;
                background-color: rgb(197, 201, 198);
            }
        """)

    def calculate_and_display(self):
        p_b_a = np.array([
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0.1, 0.9]
        ])

        info_loss = calculate_information_loss(p_b_a)
        transfer_time = calculate_transfer_time(100, 100_000_000)

        self.info_loss.setText(f"Information Loss: {info_loss:.4f} bits")
        self.transfer_time.setText(f"Transfer Time: {transfer_time:.6f} seconds")