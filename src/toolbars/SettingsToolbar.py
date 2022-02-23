from PyQt5.QtWidgets import *
from src.toolbars.style import checkbox_style

class SettingsToolbar(QToolBar):

    def __init__(self) -> None:
        super().__init__("Settings Toolbar")
        self.initGunSize()
        self.initGunX()
        self.initGunY()
        self.initGunZ()
        self.initFov()
        self.initFrameRate()
        self.initHideHud()
        self.initNoParams() # avoid to override player config if checked
        self.initVideoPipe()

    def initGunSize(self):
        self.guns = QSpinBox(self)
        self.guns.setMinimum(0)
        self.guns.setMaximum(1)
        self.guns.setValue(0)
        self.guns.setPrefix(" Gun Size : ")
        self.addWidget(self.guns)

    def initGunX(self):
        self.gunx = QSpinBox(self)
        self.gunx.setMinimum(0)
        self.gunx.setValue(0)
        self.gunx.setPrefix(" Gun X : ")
        self.addWidget(self.gunx)

    def initGunY(self):
        self.guny = QSpinBox(self)
        self.guny.setMinimum(0)
        self.guny.setValue(0)
        self.guny.setPrefix(" Gun Y : ")
        self.addWidget(self.guny)

    def initGunZ(self):
        self.gunz = QSpinBox(self)
        self.gunz.setMinimum(0)
        self.gunz.setValue(0)
        self.gunz.setPrefix(" Gun Z : ")
        self.addWidget(self.gunz)

    def initFov(self):
        self.fov = QSpinBox(self)
        self.fov.setMinimum(50)
        self.fov.setMaximum(150)
        self.fov.setValue(110)
        self.fov.setPrefix(" DemoFov : ")
        self.addWidget(self.fov)

    def initFrameRate(self):
        self.framerate = QSpinBox(self)
        self.framerate.setMinimum(0)
        self.framerate.setMaximum(250)
        self.framerate.setValue(25)
        self.framerate.setPrefix(" FrameRate : ")
        self.addWidget(self.framerate)

    def initHideHud(self):
        self.hud = QCheckBox()
        self.hud.setText("Hide Hud")
        self.hud.setStyleSheet(checkbox_style)
        self.addWidget(self.hud)

    def initNoParams(self):
        self.a_override = QCheckBox()
        self.a_override.setText("Avoid Override")
        self.a_override.setStyleSheet(checkbox_style)
        self.addWidget(self.a_override)

    def initVideoPipe(self):
        self.pipe = QCheckBox()
        self.pipe.setText("video-pipe")
        self.pipe.setStyleSheet(checkbox_style)
        self.addWidget(self.pipe)


    def getGunSize(self) :
        return self.guns.cleanText()

    def getGunx(self):
        return self.gunx.cleanText()

    def getGuny(self):
        return self.guny.cleanText()

    def getGunz(self):
        return self.gunz.cleanText()

    def getFov(self):
        return self.fov.cleanText()

    def getFramerate(self) :
        return self.framerate.cleanText()

    def isHudChecked(self):
        return True if self.hud.checkState() else False

    def isAvoidOverrideChecked(self):
        return True if self.a_override.checkState() else False

    def isVideoPipeChecked(self):
        return True if self.pipe.checkState() else False
