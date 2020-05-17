from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from xyl import Ui_MainWindow
import sys
import music21
from music21 import instrument, stream,midi,note




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushButton.clicked.connect(self.besmallah)
        self.buttons=[self.ui.c4,self.ui.d4,self.ui.e4,self.ui.f4,self.ui.g4,self.ui.a4,self.ui.b4]
        self.notes=['C4','D4','E4','F4','G4','A4','B4']
        for i in range(len(self.notes)):
            self.notesInvoke(i)
        

    def notesInvoke(self,i):
        self.buttons[i].clicked.connect(lambda: self.xylophone(self.notes[i]))

    def xylophone(self,n):
        n = note.Note(n, quarterLength=2)
        drumPart = stream.Part()
        drumPart.insert(0, instrument.Xylophone())
        drumMeasure = stream.Measure()
        drumMeasure.append(n)
        drumPart.append(drumMeasure)
        stream2=stream.Stream()
        stream2.append(drumPart)
        sp2=midi.realtime.StreamPlayer(stream2)
        sp2.play()


 


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()
