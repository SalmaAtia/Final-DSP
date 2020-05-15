
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from problem3 import Ui_MainWindow
import sys
import numpy as np
import random
from scipy.io import wavfile
import simpleaudio as sa


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.araf1.clicked.connect(self.NOIDEA)
        freqs=[261.63 , 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30,440.00, 466.16, 493.88,523.25,554.37,587.33,622.25, 659.25, 698.46, 739.99, 783.99, 830.61,880.00, 932.33,987.77]
        notes=[self.ui.c4,self.ui.c40,self.ui.d4,self.ui.d40,self.ui.e4,self.ui.f4,self.ui.f40,self.ui.g4,self.ui.g40,self.ui.a4,self.ui.a40,self.ui.b4,self.ui.c5,self.ui.c50,self.ui.d5,self.ui.d50,self.ui.e5,self.ui.f5,self.ui.f50,self.ui.g5,self.ui.g50,self.ui.a5,self.ui.a50,self.ui.b5]
        for i in range(len(freqs)):
            notes[i].clicked.connect(self.noteFunc(freqs[i]))
        # self.ui.c4.clicked.connect(self.noteFunc(freqs[0]))
       
   

    def noteFunc(self,f):
        # A_freq = f
        sample_rate = 44100
        T = 0.25
        t = np.linspace(0, T, T * sample_rate, False)
        A_note = np.sin(f * t * 2 * np.pi)
        audio = np.hstack((A_note))
        # normalize to 16-bit range
        audio *= 32767 / np.max(np.abs(audio))
        # # convert to 16-bit data
        audio = audio.astype(np.int16)
        print(type(audio))
        # start playback
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        # print(type(play_obj))
        play_obj.wait_done()

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
