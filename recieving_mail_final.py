import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
import learning_requests1
qtCreatorFile = "subscribe.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.subscribe_button.clicked.connect(self.mail)  # mail is a function

    def mail(self):
        email1 = self.email_box.text()
        learning_requests1.input_data(email1)
        final_message=("Congrats,check your mail for further instructions.")
        self.results_window.setText(final_message)
    
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
