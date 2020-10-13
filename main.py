import sys

#create app
app = QtWidgets.QApplication(sys.argv)

#init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook Logik


#main loop
sys.exit(app.exec_())