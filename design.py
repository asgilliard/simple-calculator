# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(300, 450))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculate.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: #ffffff;\n"
"    background-color: #121212;\n"
"    font-family: Open Sans;\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #202020;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}\n"
"\n"
"QPushButton#btn_prod,\n"
"QPushButton#btn_sum,\n"
"QPushButton#btn_dif,\n"
"QPushButton#btn_mul,\n"
"QPushButton#btn_sub {\n"
"    background-color: #FA5000;\n"
"    color: #121212\n"
"}\n"
"\n"
"QPushButton#btn_prod:pressed,\n"
"QPushButton#btn_sum:pressed,\n"
"QPushButton#btn_dif:pressed,\n"
"QPushButton#btn_mul:pressed,\n"
"QPushButton#btn_sub:pressed {\n"
"    background-color: #FF6F00;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    font-size: 40pt;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #2c2c2c;\n"
"    color: #ffffff;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #555;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 20pt;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
#endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"color: #888;")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy2)
        self.display.setLayoutDirection(Qt.LeftToRight)
        self.display.setStyleSheet(u"")
        self.display.setMaxLength(16)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.display.setReadOnly(True)

        self.verticalLayout.addWidget(self.display)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setSpacing(0)
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.btn_percent = QPushButton(self.centralwidget)
        self.btn_percent.setObjectName(u"btn_percent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_percent.sizePolicy().hasHeightForWidth())
        self.btn_percent.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/percent.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_percent.setIcon(icon1)
        self.btn_percent.setIconSize(QSize(24, 24))

        self.layout_buttons.addWidget(self.btn_percent, 0, 2, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy3.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy3)
        self.btn_sub.setStyleSheet(u"")

        self.layout_buttons.addWidget(self.btn_sub, 0, 3, 1, 1)

        self.btn_prod = QPushButton(self.centralwidget)
        self.btn_prod.setObjectName(u"btn_prod")
        sizePolicy3.setHeightForWidth(self.btn_prod.sizePolicy().hasHeightForWidth())
        self.btn_prod.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setFamilies([u"Open Sans"])
        font.setBold(True)
        self.btn_prod.setFont(font)

        self.layout_buttons.addWidget(self.btn_prod, 4, 3, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy3.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy3.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_sum = QPushButton(self.centralwidget)
        self.btn_sum.setObjectName(u"btn_sum")
        sizePolicy3.setHeightForWidth(self.btn_sum.sizePolicy().hasHeightForWidth())
        self.btn_sum.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_sum, 3, 3, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy3.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy3.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy3.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_dif = QPushButton(self.centralwidget)
        self.btn_dif.setObjectName(u"btn_dif")
        sizePolicy3.setHeightForWidth(self.btn_dif.sizePolicy().hasHeightForWidth())
        self.btn_dif.setSizePolicy(sizePolicy3)
        self.btn_dif.setAutoFillBackground(False)
        self.btn_dif.setFlat(False)

        self.layout_buttons.addWidget(self.btn_dif, 2, 3, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy4)

        self.layout_buttons.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy3.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_back = QPushButton(self.centralwidget)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy3.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon2)
        self.btn_back.setIconSize(QSize(24, 24))

        self.layout_buttons.addWidget(self.btn_back, 0, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy3.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy3.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy3.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_sign = QPushButton(self.centralwidget)
        self.btn_sign.setObjectName(u"btn_sign")
        sizePolicy3.setHeightForWidth(self.btn_sign.sizePolicy().hasHeightForWidth())
        self.btn_sign.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_sign, 4, 0, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy3.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy3.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy3.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy3)

        self.layout_buttons.addWidget(self.btn_8, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"simple calculator", None))
        self.label.setText("")
        self.display.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_percent.setText("")
#if QT_CONFIG(shortcut)
        self.btn_percent.setShortcut(QCoreApplication.translate("MainWindow", u"%", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_prod.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.btn_prod.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sum.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_sum.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_dif.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_dif.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
#if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_back.setText("")
#if QT_CONFIG(shortcut)
        self.btn_back.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_sign.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
#if QT_CONFIG(shortcut)
        self.btn_sign.setShortcut(QCoreApplication.translate("MainWindow", u"\u00b1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
#if QT_CONFIG(shortcut)
        self.btn_clear.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

