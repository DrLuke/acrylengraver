import sys
from PyQt4.QtGui import QApplication, QMainWindow, QFileDialog
from PyQt4.QtGui import QImage, QPixmap
from mainWindow import Ui_MainWindow
from subprocess import call
import os

__author__ = 'drluke'


class Engraver:
    def __init__(self, ui):
        self.ui = ui
        
        self.imageOrig = None
        
        self.width = self.ui.doubleSpinBoxWidth.value()
        self.height = self.ui.doubleSpinBoxHeight.value()
        self.aspectRatio = None
        self.origAspectRatio = None
        self.aspectChecked = self.ui.checkBoxAspect.checkState()
        self.safez = self.ui.doubleSpinBoxSafez.value()
        self.depth = self.ui.doubleSpinBoxDepth.value()
        self.loweringspeed = self.ui.spinBoxLoweringspeed.value()

        self.imageOrig = None
        self.imageR = None
        self.imageRd = None
        self.imageG = None
        self.imageGd = None
        self.imageB = None
        self.imageBd = None

        # Connect all signals from ui
        self.ui.doubleSpinBoxWidth.valueChanged.connect(self.onWidthChanged)
        self.ui.doubleSpinBoxHeight.valueChanged.connect(self.onHeightChanged)
        self.ui.checkBoxAspect.stateChanged.connect(self.onAspectChecked)
        self.ui.buttonResetAspect.clicked.connect(self.onResetAspect)
        self.ui.doubleSpinBoxSafez.valueChanged.connect(self.onSafezChanged)
        self.ui.doubleSpinBoxDepth.valueChanged.connect(self.onDepthChanged)
        self.ui.spinBoxLoweringspeed.valueChanged.connect(self.onLoweringspeedChanged)

        self.ui.radioButtonOrig.clicked.connect(self.showImage)
        self.ui.radioButtonR.clicked.connect(self.showImage)
        self.ui.radioButtonG.clicked.connect(self.showImage)
        self.ui.radioButtonB.clicked.connect(self.showImage)
        self.ui.checkBoxDither.toggled.connect(self.showImage)

        self.ui.buttonLoad.clicked.connect(self.onButtonLoadPressed)
        self.ui.buttonGenerate.clicked.connect(self.onButtonGeneratePressed)

    def onWidthChanged(self, newWidth):
        self.width = newWidth
        if(self.aspectRatio is not None):
            self.height = self.width * (1/self.aspectRatio)
            self.ui.doubleSpinBoxHeight.setValue(self.height)

    def onHeightChanged(self, newHeight):
        self.height = newHeight
        if(self.aspectRatio is not None):
            self.width = self.height * self.aspectRatio
            self.ui.doubleSpinBoxWidth.setValue(self.width)

    def onAspectChecked(self, newState):
        self.aspectChecked = newState
        if self.aspectChecked:
            self.aspectRatio = self.width/self.height
        else:
            self.aspectRatio = None

    def onResetAspect(self):
        if self.origAspectRatio is not None:
            if self.aspectChecked:
                self.aspectRatio = self.origAspectRatio
            self.height = self.width * (1/self.origAspectRatio)
            self.ui.doubleSpinBoxHeight.setValue(self.height)

    def onSafezChanged(self, newSafez):
        self.safez = newSafez

    def onDepthChanged(self, newDepth):
        self.depth = newDepth

    def onLoweringspeedChanged(self, newLoweringspeed):
        self.loweringspeed = newLoweringspeed

    def onButtonLoadPressed(self):
        filedialog = QFileDialog()
        filedialog.setFileMode(QFileDialog.ExistingFile)
        self.ui.progressBar.setValue(0)
        if(filedialog.exec()):
            self.imageOrig = QImage()
            if self.imageOrig.load(filedialog.selectedFiles()[0]):
                self.imagePath = filedialog.selectedFiles()[0]

                self.width = float(self.imageOrig.width())
                self.ui.doubleSpinBoxWidth.setValue(self.width)
                self.height = float(self.imageOrig.height())
                self.ui.doubleSpinBoxHeight.setValue(self.height)
                self.origAspectRatio = self.width/self.height
                if(self.aspectChecked):
                    self.aspectRatio = self.origAspectRatio
                else:
                    self.aspectRatio = None

                self.ui.progressBar.setValue(40)
                call(["convert", self.imagePath, "-channel", "R", "-separate", self.imagePath[:-4] + "_R" + self.imagePath[-4:]])
                self.ui.progressBar.setValue(50)
                self.imageR = QImage()
                self.imageR.load(self.imagePath[:-4] + "_R" + self.imagePath[-4:])
                call(["convert", self.imagePath[:-4] + "_" + "R" + self.imagePath[-4:], "-remap", "pattern:gray50", self.imagePath[:-4] + "_R" + "_d" + self.imagePath[-4:]])
                self.ui.progressBar.setValue(60)
                self.imageRd = QImage()
                self.imageRd.load(self.imagePath[:-4] + "_R" + "_d" + self.imagePath[-4:])

                call(["convert", self.imagePath, "-channel", "G", "-separate", self.imagePath[:-4] + "_G" + self.imagePath[-4:]])
                self.ui.progressBar.setValue(70)
                self.imageG = QImage()
                self.imageG.load(self.imagePath[:-4] + "_G" + self.imagePath[-4:])
                call(["convert", self.imagePath[:-4] + "_" + "G" + self.imagePath[-4:], "-remap", "pattern:gray50", self.imagePath[:-4] + "_G" + "_d" + self.imagePath[-4:]])
                self.ui.progressBar.setValue(80)
                self.imageGd = QImage()
                self.imageGd.load(self.imagePath[:-4] + "_G" + "_d" + self.imagePath[-4:])

                call(["convert", self.imagePath, "-channel", "B", "-separate", self.imagePath[:-4] + "_B" + self.imagePath[-4:]])
                self.ui.progressBar.setValue(90)
                self.imageB = QImage()
                self.imageB.load(self.imagePath[:-4] + "_B" + self.imagePath[-4:])
                call(["convert", self.imagePath[:-4] + "_" + "B" + self.imagePath[-4:], "-remap", "pattern:gray50", self.imagePath[:-4] + "_B" + "_d" + self.imagePath[-4:]])
                self.ui.progressBar.setValue(100)
                self.imageBd = QImage()
                self.imageBd.load(self.imagePath[:-4] + "_B" + "_d" + self.imagePath[-4:])

                self.ui.buttonGenerate.setEnabled(True)

            else:
                print("Error with loading file '" + str(filedialog.selectedFiles()[0]) + "'")

            self.showImage()

    def onButtonGeneratePressed(self):
        filedialog = QFileDialog(caption="Save GCode as", directory=os.path.splitext(self.imagePath)[0] + ".nc", filter="GCode Files (*.nc);;All Files (*)")
        filedialog.setFileMode(QFileDialog.AnyFile)
        filedialog.setAcceptMode(QFileDialog.AcceptSave)
        filedialog.setDefaultSuffix("nc")

        if(filedialog.exec()):
            with open(filedialog.selectedFiles()[0], "w") as f:
                f.write(self.generateGCode(self.imageRd))

    def generateGCode(self, image):
        gcode = ""

        gcode += "( Ditherfraes )\n"
        gcode += "G94\nG21\nG90\nG64 P0.1\nF10.0\nM3\nG00 Z"+str(self.safez)+"\n\n\n"

        coordsList = []
        for x in range(image.width()):
            currentLine = []
            for y in range(image.height()):
                curpixel = image.pixel(x,y)

                if curpixel == 4294967295:  # 4294967295 == White
                    currentLine.append( (self.width * (x/image.width()), self.height * (1 - y/image.height())) )
            if((x-1) % 2):
                currentLine.reverse() # Reverse list on every second line
            coordsList += currentLine

        for coord in coordsList:
            gcode += "G0 X" + str("%.2f" % coord[0]) + " Y" + str("%.2f" % coord[1]) + "\n"
            gcode += "G1 Z-" + str("%.2f" % self.depth) + "\n"
            gcode += "G0 Z" + str("%.2f" % self.safez) + "\n\n"

        gcode += "M5\n"
        gcode += "M2 (Program End)\n"

        return gcode




    def showImage(self):
        if self.imageOrig is not None:
            if self.ui.checkBoxDither.checkState():
                if self.ui.radioButtonOrig.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageOrig)
                elif self.ui.radioButtonR.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageRd)
                elif self.ui.radioButtonG.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageGd)
                elif self.ui.radioButtonB.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageBd)
            else:
                if self.ui.radioButtonOrig.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageOrig)
                elif self.ui.radioButtonR.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageR)
                elif self.ui.radioButtonG.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageG)
                elif self.ui.radioButtonB.isChecked():
                    self.pixmap = QPixmap.fromImage(self.imageB)

            self.ui.imageLabel.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    eng = Engraver(ui)

    window.show()
    sys.exit(app.exec())
