# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 480)
        Widget.setMinimumSize(QSize(800, 480))
        Widget.setMaximumSize(QSize(800, 480))
        Widget.setStyleSheet(u"QWidget {\n"
"    background-color: #1e1e2f;\n"
"    color: #f0f0f0;\n"
"    font-family: \"Segoe UI\", \"Roboto\", sans-serif;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"/* Label z.\u202fB. Infotext */\n"
"QLabel {\n"
"    color: #aaaaaa;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* Standard-Sender-Buttons */\n"
"QPushButton {\n"
"    background-color: #2d2d44;\n"
"    color: #f0f0f0;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"}\n"
"\n"
"/* Aktiver Sender-Button */\n"
"QPushButton:checked {\n"
"    background-color: #4a90e2;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Beim Dr\u00fccken (nur kurzer visueller Effekt) */\n"
"QPushButton:pressed {\n"
"    background-color: #ba5f00;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Spezielle Buttons: Volume + / - & Power */\n"
"QPushButton#btn_volume_plis,\n"
"QPushButton#btn_volume_minus,\n"
"QPushButton#btn_poweroff {\n"
"    background-color:none;\n"
"}\n"
"\n"
"QPushButton#btn_volume_plis:pr"
                        "essed {\n"
"    background-image: url('/home/pi/radio/icons/audio_2625893p.png');\n"
"}\n"
"QPushButton#btn_volume_minus:pressed {\n"
"    background-image: url('/home/pi/radio/icons/audio_26258932pp.png');\n"
"}\n"
"QPushButton#btn_poweroff:pressed {\n"
"\n"
"}\n"
"\n"
"/* Icons haben keinen Text, zentriert */\n"
"QPushButton::icon {\n"
"    margin: auto;\n"
"}")
        self.btn_volume_plis = QPushButton(Widget)
        self.btn_volume_plis.setObjectName(u"btn_volume_plis")
        self.btn_volume_plis.setGeometry(QRect(40, 10, 91, 61))
        self.btn_volume_plis.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"/home/pi/radio/icons/audio_2625893.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_volume_plis.setIcon(icon)
        self.btn_volume_plis.setIconSize(QSize(50, 50))
        self.btn_volume_minus = QPushButton(Widget)
        self.btn_volume_minus.setObjectName(u"btn_volume_minus")
        self.btn_volume_minus.setGeometry(QRect(350, 10, 81, 61))
        self.btn_volume_minus.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"/home/pi/radio/icons/audio_26258932.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_volume_minus.setIcon(icon1)
        self.btn_volume_minus.setIconSize(QSize(60, 60))
        self.btn_poweroff = QPushButton(Widget)
        self.btn_poweroff.setObjectName(u"btn_poweroff")
        self.btn_poweroff.setGeometry(QRect(680, 0, 51, 81))
        self.btn_poweroff.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"/home/pi/radio/icons/power-button_12892750.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_poweroff.setIcon(icon2)
        self.btn_poweroff.setIconSize(QSize(50, 50))
        self.btn_bayern1 = QPushButton(Widget)
        self.btn_bayern1.setObjectName(u"btn_bayern1")
        self.btn_bayern1.setGeometry(QRect(60, 90, 191, 71))
        self.infoText = QLabel(Widget)
        self.infoText.setObjectName(u"infoText")
        self.infoText.setGeometry(QRect(60, 450, 671, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.infoText.setFont(font)
        self.btn_bayern3 = QPushButton(Widget)
        self.btn_bayern3.setObjectName(u"btn_bayern3")
        self.btn_bayern3.setGeometry(QRect(300, 90, 191, 71))
        self.btn_top_fm = QPushButton(Widget)
        self.btn_top_fm.setObjectName(u"btn_top_fm")
        self.btn_top_fm.setGeometry(QRect(540, 90, 191, 71))
        self.btn_swr1 = QPushButton(Widget)
        self.btn_swr1.setObjectName(u"btn_swr1")
        self.btn_swr1.setGeometry(QRect(60, 180, 191, 71))
        self.btn_swr3 = QPushButton(Widget)
        self.btn_swr3.setObjectName(u"btn_swr3")
        self.btn_swr3.setGeometry(QRect(300, 180, 191, 71))
        self.btn_90s90s_digital = QPushButton(Widget)
        self.btn_90s90s_digital.setObjectName(u"btn_90s90s_digital")
        self.btn_90s90s_digital.setGeometry(QRect(540, 180, 191, 71))
        self.btn_90s90s_sommerhits = QPushButton(Widget)
        self.btn_90s90s_sommerhits.setObjectName(u"btn_90s90s_sommerhits")
        self.btn_90s90s_sommerhits.setGeometry(QRect(60, 270, 191, 71))
        self.btn_90s90s_millenium = QPushButton(Widget)
        self.btn_90s90s_millenium.setObjectName(u"btn_90s90s_millenium")
        self.btn_90s90s_millenium.setGeometry(QRect(300, 270, 191, 71))
        self.btn_90s90s_hiphop = QPushButton(Widget)
        self.btn_90s90s_hiphop.setObjectName(u"btn_90s90s_hiphop")
        self.btn_90s90s_hiphop.setGeometry(QRect(540, 270, 191, 71))
        self.btn_90s90s_boygroups = QPushButton(Widget)
        self.btn_90s90s_boygroups.setObjectName(u"btn_90s90s_boygroups")
        self.btn_90s90s_boygroups.setGeometry(QRect(60, 360, 191, 71))
        self.btn_80s80s_deutsch = QPushButton(Widget)
        self.btn_80s80s_deutsch.setObjectName(u"btn_80s80s_deutsch")
        self.btn_80s80s_deutsch.setGeometry(QRect(300, 360, 191, 71))
        self.btn_80s80s_ndw = QPushButton(Widget)
        self.btn_80s80s_ndw.setObjectName(u"btn_80s80s_ndw")
        self.btn_80s80s_ndw.setGeometry(QRect(540, 360, 191, 71))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btn_volume_plis.setText("")
        self.btn_volume_minus.setText("")
        self.btn_poweroff.setText("")
        self.btn_bayern1.setText(QCoreApplication.translate("Widget", u"Bayern 1", None))
        self.infoText.setText(QCoreApplication.translate("Widget", u"Systeminformationen werden geladen...", None))
        self.btn_bayern3.setText(QCoreApplication.translate("Widget", u"Bayern 3", None))
        self.btn_top_fm.setText(QCoreApplication.translate("Widget", u"Top FM", None))
        self.btn_swr1.setText(QCoreApplication.translate("Widget", u"SWR 1", None))
        self.btn_swr3.setText(QCoreApplication.translate("Widget", u"SWR 3", None))
        self.btn_90s90s_digital.setText(QCoreApplication.translate("Widget", u"90s90s Digital", None))
        self.btn_90s90s_sommerhits.setText(QCoreApplication.translate("Widget", u"90s90s Sommerhits", None))
        self.btn_90s90s_millenium.setText(QCoreApplication.translate("Widget", u"90s90s Millenium", None))
        self.btn_90s90s_hiphop.setText(QCoreApplication.translate("Widget", u"90s90s HipHop", None))
        self.btn_90s90s_boygroups.setText(QCoreApplication.translate("Widget", u"90s90s Boygroups", None))
        self.btn_80s80s_deutsch.setText(QCoreApplication.translate("Widget", u"80s80s Deutsch", None))
        self.btn_80s80s_ndw.setText(QCoreApplication.translate("Widget", u"80s80s NDW", None))
    # retranslateUi

