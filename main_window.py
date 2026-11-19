from PyQt6.QtWidgets import *
from PyQt6.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.connect_signals()

    def init_ui(self):
        self.setWindowTitle("Менеджер задач")
        self.resize(500,400)
        self.title_label = QLabel("Новая задача")
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Название задачи")
        self.add_button = QPushButton("Добавить")
        self.task_list = QListWidget()
        self.delete_button = QPushButton("Удалить")
        self.deleteComplete_button = QPushButton("Удалить выполненные задачи")
        self.clear_button = QPushButton("Очистить всё")
        self.counter_label = QLabel("Количество задач: 0")
        self.counter_completed_label = QLabel("Количество выполненных задач: 0")

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
        main_layout.addWidget(self.deleteComplete_button)
        main_layout.addWidget(self.counter_label)
        main_layout.addWidget(self.counter_completed_label)

        central_widget.setLayout(main_layout)

    def connect_signals(self):
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.clear_button.clicked.connect(self.clear_task)
        self.task_list.doubleClicked.connect(self.setCheckState)
        self.deleteComplete_button.clicked.connect(self.deleteCompleted_task)

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
        array_completed_task = [
            self.task_list.item(i)
            for i in range(self.task_list.count())
            if self.task_list.item(i).background().color() == QColor("#76C457")
        ]
        self.counter_completed_label.setText(f"Количество выполненных задач: {len(array_completed_task)}")

    def setCheckState(self):
        row = self.task_list.currentRow()
        item = self.task_list.item(row)
        if item.background().color() == QColor("#76C457"):
            QMessageBox.warning(
                self,
                "Ошибка",
                "Задача уже завершена"
            )
            return
        answer = QMessageBox.question(self, "Завершение задачи", "Завершить задачу?")
        if answer == QMessageBox.StandardButton.Yes:
            item.setBackground(QColor("#76C457"))
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)
            moved_item = self.task_list.takeItem(row)
            self.task_list.addItem(moved_item)
            self.update_counter()

    def deleteCompleted_task(self):
        answer = QMessageBox.question(
            self,
            "Очистка выполненых задач",
            "Очистить все выполненные задачи?"
        )
        if answer == QMessageBox.StandardButton.Yes:
            array_completed_task = [
                self.task_list.item(i)
                for i in range(self.task_list.count())
                if self.task_list.item(i).background().color() == QColor("#76C457")
            ]

            if not array_completed_task:
                QMessageBox.information(self, "Очистка", "Выполненные задачи отсутствуют")
                return

            for i in array_completed_task:
                row = self.task_list.row(i)
                self.task_list.takeItem(row)

            self.update_counter()
