

__author__ = 'wasi'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class HelloEvent(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.label = QLabel("Label")
        line_edit = QLineEdit("type something")
        line_edit.selectAll()
        button = QPushButton("Close")

        layout.addWidget(self.label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.close)

        # this will work
        # line_edit.textChanged.connect(self.label.setText)
        # demonstration of user defined function to do the same
        line_edit.textChanged.connect(self.line_edit_event)

    def line_edit_event(self,text):
        self.label.setText(text)


def main():
    app = QApplication(sys.argv)
    form = HelloEvent()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()