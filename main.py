import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui import Ui_Form  # Replace 'ui_file' with the name of your generated Python file

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    
def main():
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
