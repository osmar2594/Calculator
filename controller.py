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
        '''
        This function adds a number zero to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "0"
        self.label_screen.setText(entry)

    def method_1(self):
        '''
        This function adds a number one to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "1"
        self.label_screen.setText(entry)

    def method_2(self):
        '''
        This function adds a number two to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "2"
        self.label_screen.setText(entry)

    def method_3(self):
        '''
        This function adds a number three to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "3"
        self.label_screen.setText(entry)

    def method_4(self):
        '''
        This function adds a number four to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "4"
        self.label_screen.setText(entry)

    def method_5(self):
        '''
        This function adds a number five to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "5"
        self.label_screen.setText(entry)

    def method_6(self):
        '''
        This function adds a number six to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "6"
        self.label_screen.setText(entry)

    def method_7(self):
        '''
        This function adds a number seven to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "7"
        self.label_screen.setText(entry)

    def method_8(self):
        '''
        This function adds a number eight to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "8"
        self.label_screen.setText(entry)

    def method_9(self):
        '''
        This function adds a number nine to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "9"
        self.label_screen.setText(entry)

    def method_sum(self):
        '''
        This function adds the sum operator to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "+"
        self.label_screen.setText(entry)

    def method_substract(self):
        '''
        This function adds the substraction operator to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "-"
        self.label_screen.setText(entry)

    def method_multiplication(self):
        '''
        This function adds the multiplication operator to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "*"
        self.label_screen.setText(entry)

    def method_division(self):
        '''
        This function adds the division operator to the operations label screen of the calculator

        '''
        entry = self.label_screen.text()
        entry += "/"
        self.label_screen.setText(entry)

    def method_parenthesis_open(self):
        '''
        This function opens a parenthesis in the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "("
        self.label_screen.setText(entry)

    def method_parenthesis_closed(self):
        '''
        This function closes a parenthesis in the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += ")"
        self.label_screen.setText(entry)

    def method_percentage(self):
        '''
        This function adds a division by 100 to perform a percentage operation on the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        try:
            self.ans = (entry + "/100")
            self.label_screen.setText(self.ans)
        except:
            self.label_screen.setText("")

    def method_dot(self):
        '''
        This function adds a dot to the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        entry += "."
        self.label_screen.setText(entry)

    def method_clear(self):
        '''
        This function clears completely whatever text is in the screen
        '''
        entry = self.label_screen.text()
        self.label_screen.setText("")

    def method_delete(self):
        '''
        This function deletes one character on the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        self.label_screen.setText(entry[:len(entry)-1])

    def method_equal(self):
        '''
        This function performs the math operation of the text inserted on the operations label screen of the calculator
        '''
        entry = self.label_screen.text()
        try:
            ans = eval(entry)
            self.label_screen.setText(str(ans))
        except:
            self.label_screen.setText("Error")



