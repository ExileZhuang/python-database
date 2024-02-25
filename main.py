import sys
from MyMainWindow import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec_())