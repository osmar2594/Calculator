from PyQt5.QtWidgets import *
from Calculator import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_zero.clicked.connect(lambda: self.method_zero())
        self.button_one.clicked.connect(lambda: self.method_1())
        self.button_two.clicked.connect(lambda: self.method_2())
        self.button_three.clicked.connect(lambda: self.method_3())
        self.button_four.clicked.connect(lambda: self.method_4())
        self.button_five.clicked.connect(lambda: self.method_5())
        self.button_six.clicked.connect(lambda: self.method_6())
        self.button_seven.clicked.connect(lambda: self.method_7())
        self.button_eight.clicked.connect(lambda: self.method_8())
        self.button_nine.clicked.connect(lambda: self.method_9())
        self.button_clear.clicked.connect(lambda: self.method_clear())
        self.button_delete.clicked.connect(lambda: self.method_delete())
        self.button_sum.clicked.connect(lambda: self.method_sum())
        self.button_substract.clicked.connect(lambda: self.method_substract())
        self.button_multiplication.clicked.connect(lambda: self.method_multiplication())
        self.button_division.clicked.connect(lambda: self.method_division())
        self.button_percentage.clicked.connect(lambda: self.method_percentage())
        self.button_dot.clicked.connect(lambda: self.method_dot())
        self.button_parenthesis_open.clicked.connect(lambda: self.method_parenthesis_open())
        self.button_parenthesis_close.clicked.connect(lambda: self.method_parenthesis_closed())
        self.button_equal.clicked.connect(lambda: self.method_equal())


    def method_zero(self):
        entry = self.label_screen.text()
        entry += "0"
        self.label_screen.setText(entry)

    def method_1(self):
        entry = self.label_screen.text()
        entry += "1"
        self.label_screen.setText(entry)

    def method_2(self):
        entry = self.label_screen.text()
        entry += "2"
        self.label_screen.setText(entry)

    def method_3(self):
        entry = self.label_screen.text()
        entry += "3"
        self.label_screen.setText(entry)

    def method_4(self):
        entry = self.label_screen.text()
        entry += "4"
        self.label_screen.setText(entry)

    def method_5(self):
        entry = self.label_screen.text()
        entry += "5"
        self.label_screen.setText(entry)

    def method_6(self):
        entry = self.label_screen.text()
        entry += "6"
        self.label_screen.setText(entry)

    def method_7(self):
        entry = self.label_screen.text()
        entry += "7"
        self.label_screen.setText(entry)

    def method_8(self):
        entry = self.label_screen.text()
        entry += "8"
        self.label_screen.setText(entry)

    def method_9(self):
        entry = self.label_screen.text()
        entry += "9"
        self.label_screen.setText(entry)

    def method_sum(self):
        entry = self.label_screen.text()
        entry += "+"
        self.label_screen.setText(entry)

    def method_substract(self):
        entry = self.label_screen.text()
        entry += "-"
        self.label_screen.setText(entry)

    def method_multiplication(self):
        entry = self.label_screen.text()
        entry += "*"
        self.label_screen.setText(entry)

    def method_division(self):
        entry = self.label_screen.text()
        entry += "/"
        self.label_screen.setText(entry)

    def method_parenthesis_open(self):
        entry = self.label_screen.text()
        entry += "("
        self.label_screen.setText(entry)

    def method_parenthesis_closed(self):
        entry = self.label_screen.text()
        entry += ")"
        self.label_screen.setText(entry)

    def method_percentage(self):
        entry = self.label_screen.text()
        try:
            self.ans = (entry + "/100")
            self.label_screen.setText(self.ans)
        except:
            self.label_screen.setText("")

    def method_dot(self):
        entry = self.label_screen.text()
        entry += "."
        self.label_screen.setText(entry)

    def method_clear(self):
        entry = self.label_screen.text()
        self.label_screen.setText("")

    def method_delete(self):
        entry = self.label_screen.text()
        self.label_screen.setText(entry[:len(entry)-1])

    def method_equal(self):
        entry = self.label_screen.text()
        try:
            ans = eval(entry)
            self.label_screen.setText(str(ans))
        except:
            self.label_screen.setText("Error")



