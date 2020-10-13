import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from disain import Ui_Dialog

# create app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook Logik
def get_time():
    time_now = ui.lineEdit.text().split()
    ui.label.setText("Будильник установлен" +
                     f" на {time_now[0]}.{time_now[1]}" +
                     f" {time_now[2]}:{time_now[3]}")

ui.pushButton.clicked.connect(get_time)
# main loop
sys.exit(app.exec_())
