import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from design import Ui_MainWindow
import config


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_font(font_name="OpenSans-Regular.ttf")
        
        self.display = self.ui.display
        self.temp = self.ui.label
        
        # connect digits
        self.connect_digit_buttons()
        self.connect_operations()
        
        # connect actions
        self.connect_clear()
        self.ui.btn_point.clicked.connect(self.add_point)
        
        self.reset_calculation_state()
    
    # load font method    
    def load_font(self, *, font_name: str) -> None:
        font_path = os.path.join(os.path.dirname(__file__), "fonts", font_name)
        if os.path.exists(font_path):
            QFontDatabase.addApplicationFont(font_path)
        else:
            print(f"Warning: Шрифт {font_name} не найден")
    
    # connect methods
    
    def connect_digit_buttons(self):
        for btn in config.DIGIT_BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.add_digit)
    
    def connect_operations(self):
        self.ui.btn_prod.clicked.connect(self.calculate)
        for btn in config.OPERATOR_BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.push_operator)
    
    def connect_clear(self):
        self.ui.btn_clear.clicked.connect(self.handle_clear)
    
    # # backend methods
       
    # def add_digit(self) -> None:
    #     btn = self.sender()
    #     digit = btn.text()
    #     current_text = self.display.text()
        
    #     self.display.setText(digit if current_text == "0" else current_text + digit)

    # def add_point(self) -> None:
    #     if "." not in self.display.text():
    #         self.display.setText(self.display.text() + ".")

    # def handle_clear(self) -> None:
    #     if self.display.text() == "0":
    #         self.temp.clear()
    #     else:
    #         self.display.setText("0")

    # @staticmethod
    # def remove_trailing_zeros(number: str) -> str:
    #     n = str(float(number))  # cut trailing zeros to x.0 state for integer values and to x.x for float values
    #     return n[:-2] if n.endswith(".0") else n  # cut .0 for integer values
    
    # def set_temp(self) -> None:
    #     btn = self.sender()
    #     temp = self.temp.text()
    #     entry = self.remove_trailing_zeros(self.display.text())
        
    #     if not temp or self.get_math_sign() == "=":
    #         self.temp.setText(entry + f" {btn.text()} ")
    #     else:
    #         self.temp.setText(temp + entry + f" {btn.text()} ")
    #     self.display.setText("0")

    # def get_display_num(self) -> int | float:
    #     entry = self.display.text().strip(".")
    #     return float(entry) if "." in entry else int(entry)
        
    # def get_temp_num(self) -> int | float | None:
    #     temp = self.temp.text().strip(".").split()[0]
    #     return float(temp) if "." in temp else int(temp)

    # def get_math_sign(self) -> str | None:
    #     temp = self.temp.text()
    #     if temp:
    #         return temp.strip(".").split()[-1]
    
    # def calculate(self) -> str | None:
    #     entry = self.display.text()
    #     temp = self.temp.text()
    #     sign = self.get_math_sign()
        
    #     result = self.remove_trailing_zeros((config.OPERATIONS[sign](self.get_temp_num(), self.get_display_num())))
    #     self.temp.setText(temp + self.remove_trailing_zeros(entry) + ' =')
    #     self.display.setText(result)
        
    #     return result
        
    # def math_operation(self) -> None:
    #     btn = self.sender()
    #     temp = self.temp.text()
        
    #     if not temp:
    #         self.set_temp()
    #     else:
    #         if self.get_math_sign != btn.text():
    #             if self.get_math_sign() == "=":
    #                 self.set_temp()
    #             else:
    #                 self.temp.setText(temp[:-2] + f"{btn.text()} ")
    #         else:
    #             self.temp.setText(self.calculate() + f" {btn.text()}")
    
    # backend logic
    
    def reset_calculation_state(self):
        self.expression_stack: list[float | str] = []
        self.current_number = ''
        self.temp.clear()
        self.display.setText('0')
    
    @staticmethod
    def remove_trailing_zeros(number: str) -> str:
        n = str(float(number))  # cut trailing zeros to x.0 state for integer values and to x.x for float values
        return n[:-2] if n.endswith('.0') else n  # cut .0 for integer values
    
    def add_digit(self) -> None:
        button = self.sender()
        digit = button.text()
      
        if not self.current_number or self.current_number == '0':
            self.current_number = digit
        else:
            self.current_number += digit
        
        self.display.setText(self.current_number)
        
    def add_point(self) -> None:
        if '.' not in self.current_number:
            if not self.current_number:
                self.current_number = '0.'
            else:
                self.current_number += '.'
        self.display.setText(self.current_number)
        
    def push_operator(self) -> None:
        button = self.sender()
        operator = button.text()
        
        if not self.current_number and not self.expression_stack:
            self.expression_stack.append(0.0)
        
        if self.current_number:
            self.expression_stack.append(float(self.current_number))
            self.current_number = '' 
        
        if isinstance(self.expression_stack[-1], str):
            self.expression_stack[-1] = operator
        else:
            self.expression_stack.append(operator)
        
        if len(self.expression_stack) >= 3:
                self.collapse_stack(new_operator=operator)
        
        self.update_temp()
        self.display.setText('0')
        
    def calculate(self):
        if self.current_number:
            self.expression_stack.append(float(self.current_number))
            self.current_number = ''
        
        while len(self.expression_stack) >= 3:
            b = self.expression_stack.pop()
            operation = self.expression_stack.pop()
            a = self.expression_stack.pop()
            
            result = config.OPERATIONS[operation](a, b)
            
            self.expression_stack.append(result)
        
        if self.expression_stack:
            result = self.expression_stack.pop()
            self.temp.clear()
            self.current_number = str(result)
            self.display.setText(self.current_number)
        else:
            self.display.setText('0')  # обработка нажатия '=' если и current_number и expression_stack пустые

    def collapse_stack(self, *, new_operator: str) -> None:
        # Определяем приоритеты операторов
        priorities = {'+': 1, '-': 1, '×': 2, '/': 2}
    
        # Проверяем, если стек содержит минимум три элемента (число, оператор, число)
        while len(self.expression_stack) >= 3:
            b = self.expression_stack.pop()  # Второй операнд
            operator = self.expression_stack.pop()  # Оператор
            a = self.expression_stack.pop()  # Первый операнд
    
            # Проверяем приоритет последнего оператора и нового
            if priorities[operator] >= priorities[new_operator]:
                # Выполняем операцию, если приоритет текущего оператора >= нового
                result = config.OPERATIONS[operator](a, b)
                # Помещаем результат обратно в стек
                self.expression_stack.append(result)
                return
            else:
                # Если приоритет меньше, возвращаем элементы обратно и выходим
                self.expression_stack.append(a)
                self.expression_stack.append(operator)
                self.expression_stack.append(b)
                return
    
    def handle_clear(self) -> None:
        if not self.current_number or self.current_number == '0':
            self.reset_calculation_state()            
        else:
            self.current_number = '0'
            self.display.setText(self.current_number)
    
    def update_temp(self) -> None:
            temp_text = " ".join(
                [self.remove_trailing_zeros(str(x)) if isinstance(x, float) else x 
                 for x in self.expression_stack]
            )
            self.temp.setText(temp_text)    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Calculator()
    window.show()
 
    sys.exit(app.exec())
