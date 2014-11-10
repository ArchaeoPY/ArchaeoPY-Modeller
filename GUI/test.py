import sys
from PyQt4.QtGui import QApplication, QDialog
from MainUI import Ui_MainWindow

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())