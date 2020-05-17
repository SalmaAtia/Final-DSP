
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from problem3 import Ui_MainWindow
import sys
import numpy as np
import random
from scipy.io import wavfile
import simpleaudio as sa
import music21
from music21 import note, stream, midi

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.c='C4'
        # self.ui.c4.clicked.connect(lambda: self.musictwo(self.c))
        self.connected=True
        self.freqs=[261.63 , 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30,440.00, 466.16, 493.88,523.25,554.37,587.33,622.25, 659.25, 698.46, 739.99, 783.99, 830.61,880.00, 932.33,987.77]
        self.notes=['C4', 'C#4', 'D4',"D#4","E4","F4","F#4","G4","G#4","A4","A#4","B4","C5","C#5","D5","D#5","E5","F5","F#5","G5","G#5","A5","A#5","B5"]
        self.buttons=[self.ui.c4,self.ui.c40,self.ui.d4,self.ui.d40,self.ui.e4,self.ui.f4,self.ui.f40,self.ui.g4,self.ui.g40,self.ui.a4,self.ui.a40,self.ui.b4,self.ui.c5,self.ui.c50,self.ui.d5,self.ui.d50,self.ui.e5,self.ui.f5,self.ui.f50,self.ui.g5,self.ui.g50,self.ui.a5,self.ui.a50,self.ui.b5]
        self.ui.comboBox.currentTextChanged.connect(self.detectChange)
        
        



    def detectChange(self):
        for i in range(len(self.notes)):
                self.conNormalPiano(i)
        if self.ui.comboBox.currentText()=="Regular Piano":
            for i in range(len(self.notes)):
                self.disDigitalPiano(i)
                self.conNormalPiano(i)
        elif self.ui.comboBox.currentText()=="Digital Piano":        
            for i in range(len(self.notes)):
                self.disNormalPiano(i)
                self.conDigitalPiano(i)

    def conNormalPiano(self,i):
        self.buttons[i].clicked.connect(lambda: self.regularPiano(self.notes[i]))

    def disNormalPiano(self,i):
        self.buttons[i].clicked.disconnect()

    def disDigitalPiano(self,i):
        self.buttons[i].clicked.disconnect()
        
    def conDigitalPiano(self,i):
        self.buttons[i].clicked.connect(lambda: self.digitalSound(self.freqs[i]))


    def digitalSound(self,f):
        sample_rate = 44100
        T = 0.25
        t = np.linspace(0, T, T * sample_rate, False)
        A_note = np.sin(f * t * 2 * np.pi)
        audio = np.hstack((A_note))
        audio *= 32767 / np.max(np.abs(audio))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        play_obj.wait_done()



    def regularPiano(self,n):
        note1=note.Note(n)
        stream1 = stream.Stream()
        stream1.append(note1)
        sp = midi.realtime.StreamPlayer(stream1)
        sp.play()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()
