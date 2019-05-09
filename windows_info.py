
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush, QPixmap
from PyQt5.QtCore import QSize , Qt, QCoreApplication
import sys

class WindowsInfo(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(500, 500, 500, 500)


        ## ---------- Textos ----------

        infoheader = QLabel('Terminal Academico Remoto')
        infoheader.setStyleSheet('font-size: 25px')

        infotext = QLabel('Ao acessar o termianal acadêmico da UFSC é possível acessar programas \n'
                          'como Photoshop, Autocad, entre outros.\n')

        infowarning = QLabel('Aviso: Audio indisponível.')
        infowarning.setStyleSheet('color: red')

        #------------------------------

        # --------- Imagem ------------
        image = QLabel(self)
        pixmap = QPixmap('resources/softwarelist.png')
        image.setPixmap(pixmap)

        #---------- Botoes ------------

        closeButton = QPushButton('Fechar')
        closeButton.clicked.connect(self.close)

        #------------------------------


        #---------- Layout ------------

        infolayout = QVBoxLayout()
        infolayout.addWidget(infoheader)

        infomidlayout = QHBoxLayout()
        infomidlayout.addWidget(infotext)
        infomidlayout.addWidget(image)

        infolayout.addLayout(infomidlayout)
        infolayout.addWidget(infotext)
        infolayout.addWidget(infowarning)
        infolayout.addWidget(closeButton)
        self.setLayout(infolayout)
        self.show()

        #------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    infoWindow = WindowsInfo()
    sys.exit(app.exec_())

