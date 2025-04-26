import sys
import os
from typing import Union, Optional

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
        
        # digits
        self.connect_digit_buttons()
        
        # actions
        self.ui.btn_clear.clicked.connect(self.handle_clear)
        self.ui.btn_point.clicked.connect(self.add_point)
        
        # math
        self.ui.btn_sum.clicked.connect(lambda: self.set_temp(math_sign="+"))
        self.ui.btn_dif.clicked.connect(lambda: self.set_temp(math_sign="-"))
        self.ui.btn_mul.clicked.connect(lambda: self.set_temp(math_sign="*"))
        self.ui.btn_sub.clicked.connect(lambda: self.set_temp(math_sign="/"))
        
    def load_font(self, *, font_name: str) -> None:
        font_path = os.path.join(os.path.dirname(__file__), "fonts", font_name)
        if os.path.exists(font_path):
            QFontDatabase.addApplicationFont(font_path)
        else:
            print(f"Warning: Шрифт {font_name} не найден")
    
    def connect_digit_buttons(self):
        for btn in config.DIGIT_BUTTONS:
            getattr(self.ui, btn).clicked.connect(self.add_digit)
       
    def add_digit(self) -> None:
        btn = self.sender()
        digit = btn.text()
        current_text = self.display.text()
        
        self.display.setText(digit if current_text == "0" else current_text + digit)

    def add_point(self) -> None:
        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

    def handle_clear(self) -> None:
        if self.display.text() == "0":
            self.temp.clear()
        else:
            self.display.setText("0")

    @staticmethod
    def remove_trailing_zeros(number: str) -> str:
        n = str(float(number))
        return n[:-2] if n.endswith(".0") else n
    
    def set_temp(self, *, math_sign:str) -> None:
        # btn = self.sender()
        temp = self.temp.text()
        entry = self.remove_trailing_zeros(self.display.text())
        
        if not temp:
            self.temp.setText(entry + f" {math_sign} ")
        else:
            self.temp.setText(temp + entry + f" {math_sign} ")
        self.display.setText("0")

   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = Calculator()
    window.show()
 
    sys.exit(app.exec())
