import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from disain2 import Ui_TitileBudilnic

# create app
app = QtWidgets.QApplication(sys.argv)

# init

TitileBudilnic = QtWidgets.QDialog()
ui = Ui_TitileBudilnic()
ui.setupUi(TitileBudilnic)
TitileBudilnic.show()


# Hook Logik
def get_time():
    day_need, moth_need, hour_need, minutes_need = ui.lineEdit.text(),\
                                                   ui.lineEdit_2.text(), ui.lineEdit_3.text(), ui.lineEdit_4.text()
    ui.label_5.setText(f"Alarm clock set {day_need}.{moth_need} {hour_need}:{minutes_need}")



ui.pushButton.clicked.connect(get_time)
# main loop
sys.exit(app.exec_())
