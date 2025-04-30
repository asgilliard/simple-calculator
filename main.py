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
        self.priorities = {'+': 1, '-': 1, '×': 2, '/': 2}
        self.display_max_len = self.display.maxLength() # 16 символов
        
        # connect digits and operations
        self.connect_digit_buttons()
        self.connect_operations()
        
        # connect actions
        self.connect_clear()
        self.connect_point()
        self.connect_sign()
        self.connect_backspace()
        self.connect_percent()
        
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
            getattr(self.ui, btn).clicked.connect(self.handle_digit)
    
    def connect_operations(self):
        self.ui.btn_prod.clicked.connect(self.calculate)
        for btn in config.OPERATOR_BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.handle_operator)
    
    def connect_point(self):
        self.ui.btn_point.clicked.connect(self.handle_point)
    
    def connect_clear(self):
        self.ui.btn_clear.clicked.connect(self.handle_clear)
        
    def connect_sign(self):
        self.ui.btn_sign.clicked.connect(self.handle_sign)
        
    def connect_backspace(self):
        self.ui.btn_back.clicked.connect(self.handle_backspace)
    
    def connect_percent(self):
        self.ui.btn_percent.clicked.connect(self.handle_percent)
    
    # backend logic
    
    def reset_calculation_state(self) -> None:
        self.expression_stack: list[float | str] = []
        self.current_number = '0'
        self.is_pushed_operator = False
        self.update_temp()
        self.update_display()
    
    @staticmethod
    def remove_trailing_zeros(number: str) -> str:
        n = str(float(number))  # обрезаем лишние нули до состояния x.0 для int и x.x для float
        return n[:-2] if n.endswith('.0') else n  # обрезаем лишний .0 для int
    
    def handle_digit(self) -> None:
        button = self.sender()
        digit = button.text()
      
        if self.current_number == '0' or self.is_pushed_operator == True:
            self.current_number = digit
        else:
            self.current_number += digit

        self.avoid_display_max_len_overflow()
        self.is_pushed_operator = False
        self.update_display()
        
    def handle_point(self) -> None:
        if '.' not in self.current_number:
            self.current_number += '.'
            self.avoid_display_max_len_overflow()
            self.update_display()
        
    def handle_operator(self) -> None:
        button = self.sender()
        operator = str(button.text())
        
        if not self.is_pushed_operator:
            self.expression_stack.append(float(self.current_number))
            self.update_temp()
            self.is_pushed_operator = True
        
        if self.expression_stack and isinstance(self.expression_stack[-1], str):  # если последний в стеке - str (оператор) - меняем его на нажатый
            self.expression_stack[-1] = operator
        else:
            self.expression_stack.append(operator)
        self.update_temp()
        
        self.collapse_stack()
        
        self.update_temp()
        self.update_display()
        
    def collapse_stack(self) -> None:
        numbers = []
        operators = []
        
        for item in self.expression_stack:
            if isinstance(item, (float, int)):
                numbers.append(item)
            elif isinstance(item, str):
                while operators and self.priorities[operators[-1]] >= self.priorities[item]:
                    self.perform_operation(numbers, operators)
                operators.append(item)
        
        self.expression_stack.clear()
                
        for i in range(len(operators)):
            self.expression_stack.append(numbers[i])
            self.expression_stack.append(operators[i])
            
        if len(self.expression_stack) == 2:
            self.current_number = self.remove_trailing_zeros(str(self.expression_stack[0]))
    
    def calculate(self) -> None:
        self.expression_stack.append(float(self.current_number))
        numbers = []
        operators = []
        
        # Заполняем стеки, одновременно сжимая их, если возможно. Результат - операторы будут выстроены по приоритету от меньшего к большему.  
        for item in self.expression_stack:
            if isinstance(item, (float, int)):
                numbers.append(item)
            elif isinstance(item, str):
                while operators and self.priorities[operators[-1]] >= self.priorities[item]:
                    self.perform_operation(numbers, operators)
                operators.append(item)
        
        # Подсчитываем итоговый результат, разматывая стеки с конца
        while operators:
            self.perform_operation(numbers, operators)
        
        if numbers:
            result = numbers[0]
            result = round(result, 4)
            result_str = self.remove_trailing_zeros(str(result))
            self.current_number = result_str
            self.expression_stack = []
            self.update_temp()
            self.update_display() 
        
    def perform_operation(self, numbers: list[float | int], operators: list[str]) -> None:
        if len(numbers) < 2 or not operators:
            return
        b = numbers.pop()
        a = numbers.pop()
        op = operators.pop()
        try:
            result = config.OPERATIONS[op](a, b)
            numbers.append(result)
        except ZeroDivisionError:
            self.handle_zero_division_error()
    
    # actions handling
    def handle_clear(self) -> None:
        if self.current_number == '0':
            self.reset_calculation_state()            
        else:
            self.current_number = '0'
            self.display.setText(self.current_number)
            
    def handle_sign(self) -> None:
        if '-' not in self.current_number:
            if self.current_number != '0':
                self.current_number = '-' + self.current_number
        else:
            self.current_number = self.current_number[1:]
           
        self.update_display()
            
    def handle_backspace(self) -> None:
        if len(self.current_number) == 1:
            self.current_number = '0'
        elif len(self.current_number) == 2 and '-' in self.current_number:
            self.current_number = '0'
        else:
            self.current_number = self.current_number[:-1]
            
        self.update_display()
        
    def handle_percent(self) -> None:
        current = float(self.current_number)
        current /= 100
        
        if len(self.expression_stack) >= 2:
            whole = self.expression_stack[-2]
            if isinstance(whole, float):
                self.current_number = self.remove_trailing_zeros(str(round(float(whole) * current, 12)))
        else:
            self.current_number = self.remove_trailing_zeros(str(round(current, 12)))
        
        self.update_display()
    
    def update_display(self) -> None:
        self.display.setMaxLength(15)
        self.display.setText(self.current_number)
        self.adjust_display_font_size()
    
    def update_temp(self) -> None:
        temp_text = ''
            
        for i in self.expression_stack:
            if isinstance(i, float):
                temp_text += self.remove_trailing_zeros(str(i))
                temp_text += ' '
            else:
                temp_text += str(i)
                temp_text += ' '
              
        self.temp.setText(temp_text)
        self.adjust_temp_font_size() 
           
    # errors handling
    def avoid_display_max_len_overflow(self) -> None:
        while len(self.current_number) >= self.display_max_len:
            self.current_number = self.current_number[:-1]
    
    def handle_zero_division_error(self) -> None:
        text = config.ZERO_DIVISION_ERROR
        
        self.expression_stack.clear()
        self.update_temp()
        
        self.display.setMaxLength(len(text))
        self.display.setStyleSheet('font-size: 32pt; color: #99ccff;')
        self.display.setText(text)
        
        self.current_number = '0'
        
    # UI
    
    def get_display_text_width(self) -> int:
        return self.display.fontMetrics().boundingRect(self.display.text()).width()
    
    def get_temp_text_width(self) -> int:
        return self.temp.fontMetrics().boundingRect(self.temp.text()).width()
    
    def adjust_display_font_size(self) -> None:
        font_size = config.DEFAULT_DISPLAY_FONT_SIZE
        while self.get_display_text_width() > self.display.width() - 30:
            font_size -= 1
            self.display.setStyleSheet(f'font-size: {font_size}pt; border: none;')

        font_size = 1
        while self.get_display_text_width() < self.display.width() - 60:
            font_size += 1

            if font_size > config.DEFAULT_DISPLAY_FONT_SIZE:
                break

            self.display.setStyleSheet(f'font-size: {font_size}pt; border: none;')

    def adjust_temp_font_size(self) -> None:
        font_size = config.DEFAULT_FONT_SIZE
        while self.get_temp_text_width() > self.temp.width() - 30:
            font_size -= 1
            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

        font_size = 1
        while self.get_temp_text_width() < self.temp.width() - 60:
            font_size += 2

            if font_size > config.DEFAULT_FONT_SIZE:
                break

            self.temp.setStyleSheet(f'font-size: {font_size}pt; color: #888;')

    def resizeEvent(self, event) -> None:
        self.adjust_display_font_size()
        self.adjust_temp_font_size()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Calculator()
    window.show()
 
    sys.exit(app.exec())
