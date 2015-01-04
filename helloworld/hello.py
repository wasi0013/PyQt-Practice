__author__ = 'wasi'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    # Overriding Constructor method of inherited QDialog
    def __init__(self):

        QDialog.__init__(self)
        # Another way: super(HelloWorld,self).__init__()

        layout = QVBoxLayout()

        label = QLabel("This is a Label")
        line_edit = QLineEdit("Line Edit (Editable)")

        # This button won't do anything
        button = QPushButton("close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle("Hello World!")


def main():
    app = QApplication(sys.argv)
    form = HelloWorld()
    form.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()