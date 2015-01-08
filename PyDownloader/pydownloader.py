import urllib.request

__author__ = 'wasi'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class PyDownloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        
        layout = QVBoxLayout()
        
        self.url = QLineEdit()
        self.file_location = QLineEdit()
        download = QPushButton("Download")
        
        self.progress_bar =  QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignHCenter)

        self.url.setPlaceholderText("url")
        self.file_location.setPlaceholderText("File Location")

        layout.addWidget(self.url)
        layout.addWidget(self.file_location)
        layout.addWidget(self.progress_bar)
        layout.addWidget(download)
        
        self.setLayout(layout)
        self.setWindowTitle("PyDownloader")
        self.setFocus()
        
        download.clicked.connect(self.downloader)

    def downloader(self):
        
        url = self.url.text()
        file_location = self.file_location.text()
        
        try:
            urllib.request.urlretrieve(url,file_location,self.status)
        
        except Exception:
            QMessageBox.warning(self,"Warning","Download Failed!")
            return

        QMessageBox.information(self,"Information","Download is complete")
        
        self.progress_bar.setValue(0)
        self.file_location.setText("")
        self.url.setText("")


    def status(self,blocknum,blocksize,totalsize):
        
        readsofar= blocknum*blocksize
        
        if totalsize>0:
            percent = readsofar*100/totalsize
            self.progress_bar.setValue(int(percent))

def main():
    app = QApplication(sys.argv)
    form = PyDownloader()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
