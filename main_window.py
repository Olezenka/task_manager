from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.resize(500,400)
        self.title_label = QLabel("Новая задача")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        self.task_list = QListWidget()
        self.delete_button = QPushButton("Удалить")
        self.clear_button = QPushButton("Очистить всё")
        self.counter_label = QLabel("Количество задач: 0")

        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        central_widget = QWidget()  # Задать окно
        self.setCentralWidget(central_widget)  # Пустой контейнер для содержания окна

        input_layout = QHBoxLayout()  # Горизонтальный контейнер
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        buttons_layout = QHBoxLayout()  # Горизонтальный контейнер
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addWidget(self.clear_button)

        main_layout = QVBoxLayout()  # Вертикальный главный контейнер
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.counter_label)

        central_widget.setLayout(main_layout)

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_task)

    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Введите название задачи"
            )
            return
        self.task_list.addItem(text)
        self.task_input.clear()

        self.update_counter()

    def delete_task(self):
        row = self.task_list.currentRow()
        if row < 0:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Выберете строку"
            )
            return
        answer = QMessageBox.question(
            self,
            "Удаление",
            "Удалить выбранную задачу?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.task_list.takeItem(row)
            self.update_counter()

    def clear_task(self):
        answer = QMessageBox.question(
            self,
            "Очистка задач",
            "Очистить все задачи?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            if self.task_list.count() == 0:
                QMessageBox.information(self, "Очистка", "Список уже пуст")
                return
            self.task_list.clear()
            self.update_counter()

    def update_counter(self):
        self.counter_label.setText(f"Количество задач: {len(self.task_list)}")