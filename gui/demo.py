import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def percent_insult(sentence):
    return len(sentence)
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Insult Detection demo | Credits - pythonspot.com'
        self.left = 400
        self.top = 400
        self.width = 1050
        self.height = 220
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Height
        a = 80
        wi = 1000
        font = QFont("Times", 20, QFont.Bold) 

        # Create a Parent Label
        self.label = QLabel(self)
        self.label.setText("Insult Detection of Social Comentary")
        self.label.resize(wi,40)
        self.label.setFont(font)
        self.label.move(20, 20)

        # Create a main Label
        self.label_names = QLabel(self)
        self.label_names.setText("Team Members: Abhavya | Apoorv"
                                 " | Atishay | Ritik | Varun | Rithwik")
        font = QFont("Times", 14) 
        self.label_names.setFont(font)
        self.label_names.resize(wi,40)
        self.label_names.move(20, 55)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, a + 20)
        self.textbox.resize(wi,40)
 
        # Create a button in the window
        self.button = QPushButton('Calc. Porbability', self)
        self.button.move(wi-100, a + 80)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        percent_value = percent_insult(textboxValue)
        QMessageBox.question(self, 'Insult ' +'%' +' detected', "Porbability of Insult: " \
                             + str(percent_value), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # print(app)
    # print(type(app))
    ex = App()
    sys.exit(app.exec_())

# Abhavya is a fucking bitch
# - test sentence
