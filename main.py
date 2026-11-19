import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QListWidget
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# def main():
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle("Менеджер задач")
#     window.resize(500,400)
#     layout = QVBoxLayout()
#     layout.addWidget(QLabel("Новая задача"))
#     layout.addWidget(QLineEdit())
#     layout.addWidget(QListWidget())
#
#     window.setLayout(layout)
#     window.show()
#     sys.exit(app.exec())


if __name__ == "__main__":
    main()

