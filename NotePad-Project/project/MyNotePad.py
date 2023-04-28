import sys
import os
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QLayout,QWidget,QLineEdit,QTextEdit,QPushButton,QApplication,QAction,QFileDialog #for class wındow
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow  #for class menu
class Wındow(QWidget):

    def __init__(self):

        super().__init__()
        self.AnaEkran()

    def AnaEkran(self):
        #attribute
        self.yazıalanı = QTextEdit()
        # layout page
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.yazıalanı)
        v_box.addStretch()
        v_box.addStretch()

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)# added v_box
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Notepad")


    def Sil(self):

        return self.yazıalanı.clear()

    def Ac(self):
        dosya=QFileDialog.getOpenFileName(self,"DosyaAç",os.getenv("Desktop"))

        with open(dosya[0],"r",encoding="utf-8") as file:  #here we write this code to read the file.

            self.yazıalanı.setText(file.read())

    def Kaydet(self):

        dosya = QFileDialog.getSaveFileName(self,"DosyaKaydet",os.getenv("Desktop"))

        with open(dosya[0],"w",encoding="utf-8") as file2:

            file2.write(self.yazıalanı.toPlainText()) #we have received all the texts on the writing forehead



class Menu(QMainWindow):

    def __init__(self):

        super().__init__()
        #We created a variable to use the window class
        self.pencere = Wındow()

        self.setCentralWidget(self.pencere)


        #Create MenuBar Tools
        menubar = self.menuBar()
        dosya = menubar.addMenu("File") # dosya added in menubar
        düzenle = menubar.addMenu("Edit") #düzenle adde in menubar

        #We created an element in the menubar

        open= QAction("Open",self)
        open.setShortcut("Ctrl+O")
        save =QAction("Save",self)
        save.setShortcut("Ctrl+S")
        delete = QAction("Delete",self)
        delete.setShortcut("Ctrl+D")
        exıt = QAction("Exit",self)
        exıt.setShortcut("Ctrl+Q")
        #color
        menubar.setStyleSheet("background-color:grey")

        #We added the elements we created for the menubar to the menubar.

        dosya.addAction(open)
        dosya.addAction(save)
        düzenle.addAction(delete)
        düzenle.addAction(exıt)
        #called
        exıt.triggered.connect(self.Exit)
        dosya.triggered.connect(self.AllPosition)
        düzenle.triggered.connect(self.AllPosition)

        self.show()

    def Exit(self):

        return qApp.quit()  #quit çıkış işlemini sağlar

        self.setWindowTitle("MyNotePad")

    def AllPosition(self,action):

        if action.text() =="Open":
            self.pencere.Ac()
        elif action.text() =="Save":
            self.pencere.Kaydet()
        elif action.text() =="Delete":
            self.pencere.Sil()
        else:
            qApp.quit() #quiit çıkış sağlar




#We can say , created application
app = QApplication(sys.argv)

menu = Menu()
menu.setGeometry(100,100,250,250)

sys.exit(app.exec())