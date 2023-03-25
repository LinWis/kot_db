

################################################################################
## Form generated from reading UI file 'kot.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 872)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.db_tab = QWidget()
        self.db_tab.setObjectName(u"db_tab")
        sizePolicy.setHeightForWidth(self.db_tab.sizePolicy().hasHeightForWidth())
        self.db_tab.setSizePolicy(sizePolicy)
        self.db_tab.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.db_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_btn = QPushButton(self.db_tab)
        self.save_btn.setObjectName(u"save_btn")

        self.horizontalLayout.addWidget(self.save_btn)

        self.clear_btn = QPushButton(self.db_tab)
        self.clear_btn.setObjectName(u"clear_btn")

        self.horizontalLayout.addWidget(self.clear_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_14, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_line_btn = QPushButton(self.db_tab)
        self.prev_line_btn.setObjectName(u"prev_line_btn")

        self.horizontalLayout_3.addWidget(self.prev_line_btn)

        self.next_line_btn = QPushButton(self.db_tab)
        self.next_line_btn.setObjectName(u"next_line_btn")

        self.horizontalLayout_3.addWidget(self.next_line_btn)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_16, 7, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_15, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.name_lb = QLabel(self.db_tab)
        self.name_lb.setObjectName(u"name_lb")

        self.verticalLayout.addWidget(self.name_lb)

        self.name_le = QLineEdit(self.db_tab)
        self.name_le.setObjectName(u"name_le")
        sizePolicy.setHeightForWidth(self.name_le.sizePolicy().hasHeightForWidth())
        self.name_le.setSizePolicy(sizePolicy)
        self.name_le.setMouseTracking(True)

        self.verticalLayout.addWidget(self.name_le)

        self.age_lb = QLabel(self.db_tab)
        self.age_lb.setObjectName(u"age_lb")

        self.verticalLayout.addWidget(self.age_lb)

        self.age_le = QLineEdit(self.db_tab)
        self.age_le.setObjectName(u"age_le")
        sizePolicy.setHeightForWidth(self.age_le.sizePolicy().hasHeightForWidth())
        self.age_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.age_le)

        self.nick_lb = QLabel(self.db_tab)
        self.nick_lb.setObjectName(u"nick_lb")

        self.verticalLayout.addWidget(self.nick_lb)

        self.nick_le = QLineEdit(self.db_tab)
        self.nick_le.setObjectName(u"nick_le")
        sizePolicy.setHeightForWidth(self.nick_le.sizePolicy().hasHeightForWidth())
        self.nick_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.nick_le)

        self.discord_lb = QLabel(self.db_tab)
        self.discord_lb.setObjectName(u"discord_lb")

        self.verticalLayout.addWidget(self.discord_lb)

        self.discord_le = QLineEdit(self.db_tab)
        self.discord_le.setObjectName(u"discord_le")
        sizePolicy.setHeightForWidth(self.discord_le.sizePolicy().hasHeightForWidth())
        self.discord_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.discord_le)

        self.town_lb = QLabel(self.db_tab)
        self.town_lb.setObjectName(u"town_lb")

        self.verticalLayout.addWidget(self.town_lb)

        self.town_le = QLineEdit(self.db_tab)
        self.town_le.setObjectName(u"town_le")
        sizePolicy.setHeightForWidth(self.town_le.sizePolicy().hasHeightForWidth())
        self.town_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.town_le)

        self.label = QLabel(self.db_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.country_le = QLineEdit(self.db_tab)
        self.country_le.setObjectName(u"country_le")
        sizePolicy.setHeightForWidth(self.country_le.sizePolicy().hasHeightForWidth())
        self.country_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.country_le)

        self.time_game_lb = QLabel(self.db_tab)
        self.time_game_lb.setObjectName(u"time_game_lb")

        self.verticalLayout.addWidget(self.time_game_lb)

        self.time_game_le = QLineEdit(self.db_tab)
        self.time_game_le.setObjectName(u"time_game_le")
        sizePolicy.setHeightForWidth(self.time_game_le.sizePolicy().hasHeightForWidth())
        self.time_game_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.time_game_le)

        self.all_time_lb = QLabel(self.db_tab)
        self.all_time_lb.setObjectName(u"all_time_lb")

        self.verticalLayout.addWidget(self.all_time_lb)

        self.all_time_le = QLineEdit(self.db_tab)
        self.all_time_le.setObjectName(u"all_time_le")
        sizePolicy.setHeightForWidth(self.all_time_le.sizePolicy().hasHeightForWidth())
        self.all_time_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.all_time_le)

        self.your_help_lb = QLabel(self.db_tab)
        self.your_help_lb.setObjectName(u"your_help_lb")

        self.verticalLayout.addWidget(self.your_help_lb)

        self.your_help_le = QLineEdit(self.db_tab)
        self.your_help_le.setObjectName(u"your_help_le")
        sizePolicy.setHeightForWidth(self.your_help_le.sizePolicy().hasHeightForWidth())
        self.your_help_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.your_help_le)

        self.label_2 = QLabel(self.db_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.our_help_le = QLineEdit(self.db_tab)
        self.our_help_le.setObjectName(u"our_help_le")
        sizePolicy.setHeightForWidth(self.our_help_le.sizePolicy().hasHeightForWidth())
        self.our_help_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.our_help_le)

        self.micro_lb = QLabel(self.db_tab)
        self.micro_lb.setObjectName(u"micro_lb")

        self.verticalLayout.addWidget(self.micro_lb)

        self.micro_le = QLineEdit(self.db_tab)
        self.micro_le.setObjectName(u"micro_le")
        sizePolicy.setHeightForWidth(self.micro_le.sizePolicy().hasHeightForWidth())
        self.micro_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.micro_le)

        self.dislike_lb = QLabel(self.db_tab)
        self.dislike_lb.setObjectName(u"dislike_lb")

        self.verticalLayout.addWidget(self.dislike_lb)

        self.dislike_le = QLineEdit(self.db_tab)
        self.dislike_le.setObjectName(u"dislike_le")
        sizePolicy.setHeightForWidth(self.dislike_le.sizePolicy().hasHeightForWidth())
        self.dislike_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.dislike_le)

        self.label_3 = QLabel(self.db_tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lvl_game_le = QLineEdit(self.db_tab)
        self.lvl_game_le.setObjectName(u"lvl_game_le")
        sizePolicy.setHeightForWidth(self.lvl_game_le.sizePolicy().hasHeightForWidth())
        self.lvl_game_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.lvl_game_le)

        self.reason_lb = QLabel(self.db_tab)
        self.reason_lb.setObjectName(u"reason_lb")

        self.verticalLayout.addWidget(self.reason_lb)

        self.reason_le = QLineEdit(self.db_tab)
        self.reason_le.setObjectName(u"reason_le")
        sizePolicy.setHeightForWidth(self.reason_le.sizePolicy().hasHeightForWidth())
        self.reason_le.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.reason_le)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.find_lst_update_btn = QPushButton(self.db_tab)
        self.find_lst_update_btn.setObjectName(u"find_lst_update_btn")

        self.gridLayout_2.addWidget(self.find_lst_update_btn, 2, 0, 1, 1)

        self.db_fragment_te = QTextEdit(self.db_tab)
        self.db_fragment_te.setObjectName(u"db_fragment_te")
        self.db_fragment_te.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_2.addWidget(self.db_fragment_te, 6, 0, 1, 1)

        self.tabWidget.addTab(self.db_tab, "")
        self.db_search_tab = QWidget()
        self.db_search_tab.setObjectName(u"db_search_tab")
        self.gridLayout_3 = QGridLayout(self.db_search_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.find_btn = QPushButton(self.db_search_tab)
        self.find_btn.setObjectName(u"find_btn")

        self.horizontalLayout_2.addWidget(self.find_btn)

        self.clear_btn_2 = QPushButton(self.db_search_tab)
        self.clear_btn_2.setObjectName(u"clear_btn_2")

        self.horizontalLayout_2.addWidget(self.clear_btn_2)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.db_fragment_le = QLineEdit(self.db_search_tab)
        self.db_fragment_le.setObjectName(u"db_fragment_le")
        sizePolicy.setHeightForWidth(self.db_fragment_le.sizePolicy().hasHeightForWidth())
        self.db_fragment_le.setSizePolicy(sizePolicy)
        self.db_fragment_le.setMaximumSize(QSize(16777215, 40))
        self.db_fragment_le.setBaseSize(QSize(0, 0))

        self.gridLayout_3.addWidget(self.db_fragment_le, 1, 0, 1, 1)

        self.find_lb = QLabel(self.db_search_tab)
        self.find_lb.setObjectName(u"find_lb")
        font1 = QFont()
        font1.setPointSize(14)
        self.find_lb.setFont(font1)
        self.find_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.find_lb, 0, 0, 1, 1)

        self.db_tw = QTableWidget(self.db_search_tab)
        if (self.db_tw.columnCount() < 16):
            self.db_tw.setColumnCount(16)
        __qtablewidgetitem = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.db_tw.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        self.db_tw.setObjectName(u"db_tw")
        self.db_tw.setEnabled(True)
        self.db_tw.setMinimumSize(QSize(0, 0))
        self.db_tw.setMaximumSize(QSize(16777215, 16777215))
        self.db_tw.setRowCount(0)
        self.db_tw.setColumnCount(16)
        self.db_tw.horizontalHeader().setMinimumSectionSize(50)
        self.db_tw.horizontalHeader().setDefaultSectionSize(230)

        self.gridLayout_3.addWidget(self.db_tw, 3, 0, 1, 1)

        self.tabWidget.addTab(self.db_search_tab, "")
        self.preference_tab = QWidget()
        self.preference_tab.setObjectName(u"preference_tab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.preference_tab.sizePolicy().hasHeightForWidth())
        self.preference_tab.setSizePolicy(sizePolicy1)
        self.preference_tab.setMaximumSize(QSize(800, 800))
        self.gridLayout_4 = QGridLayout(self.preference_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.start_char_lb = QLabel(self.preference_tab)
        self.start_char_lb.setObjectName(u"start_char_lb")
        self.start_char_lb.setMaximumSize(QSize(300, 100))
        self.start_char_lb.setAutoFillBackground(True)
        self.start_char_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.start_char_lb, 4, 0, 1, 2)

        self.end_char_lb = QLabel(self.preference_tab)
        self.end_char_lb.setObjectName(u"end_char_lb")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.end_char_lb.sizePolicy().hasHeightForWidth())
        self.end_char_lb.setSizePolicy(sizePolicy2)
        self.end_char_lb.setMaximumSize(QSize(300, 100))
        self.end_char_lb.setLayoutDirection(Qt.LeftToRight)
        self.end_char_lb.setAutoFillBackground(True)
        self.end_char_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.end_char_lb, 6, 0, 1, 2)

        self.file_locate_lb = QLabel(self.preference_tab)
        self.file_locate_lb.setObjectName(u"file_locate_lb")
        self.file_locate_lb.setMaximumSize(QSize(300, 16777215))
        self.file_locate_lb.setAutoFillBackground(True)
        self.file_locate_lb.setAlignment(Qt.AlignCenter)
        self.file_locate_lb.setMargin(0)

        self.gridLayout_4.addWidget(self.file_locate_lb, 0, 0, 1, 1)

        self.file_name_lb = QLabel(self.preference_tab)
        self.file_name_lb.setObjectName(u"file_name_lb")
        self.file_name_lb.setMaximumSize(QSize(300, 16777215))
        self.file_name_lb.setAutoFillBackground(True)
        self.file_name_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.file_name_lb, 2, 0, 1, 1)

        self.file_name_btn = QPushButton(self.preference_tab)
        self.file_name_btn.setObjectName(u"file_name_btn")
        self.file_name_btn.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_4.addWidget(self.file_name_btn, 3, 0, 1, 5)

        self.end_char_le = QLineEdit(self.preference_tab)
        self.end_char_le.setObjectName(u"end_char_le")
        self.end_char_le.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.end_char_le, 6, 2, 1, 1)

        self.separate_char_le = QLineEdit(self.preference_tab)
        self.separate_char_le.setObjectName(u"separate_char_le")
        self.separate_char_le.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.separate_char_le, 5, 2, 1, 1)

        self.file_locate_le = QLineEdit(self.preference_tab)
        self.file_locate_le.setObjectName(u"file_locate_le")
        self.file_locate_le.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.file_locate_le, 0, 1, 1, 4)

        self.separate_char_lb = QLabel(self.preference_tab)
        self.separate_char_lb.setObjectName(u"separate_char_lb")
        self.separate_char_lb.setMaximumSize(QSize(300, 100))
        self.separate_char_lb.setAutoFillBackground(True)
        self.separate_char_lb.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.separate_char_lb, 5, 0, 1, 2)

        self.file_name_le = QLineEdit(self.preference_tab)
        self.file_name_le.setObjectName(u"file_name_le")
        self.file_name_le.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.file_name_le, 2, 1, 1, 1)

        self.file_locate_btn = QPushButton(self.preference_tab)
        self.file_locate_btn.setObjectName(u"file_locate_btn")
        self.file_locate_btn.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_4.addWidget(self.file_locate_btn, 1, 0, 1, 5)

        self.save_pref_btn = QPushButton(self.preference_tab)
        self.save_pref_btn.setObjectName(u"save_pref_btn")
        self.save_pref_btn.setMaximumSize(QSize(500, 16777215))

        self.gridLayout_4.addWidget(self.save_pref_btn, 7, 0, 1, 5)

        self.start_char_le = QLineEdit(self.preference_tab)
        self.start_char_le.setObjectName(u"start_char_le")
        self.start_char_le.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_4.addWidget(self.start_char_le, 4, 2, 1, 1)

        self.tabWidget.addTab(self.preference_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.prev_line_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.next_line_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.name_lb.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.age_lb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.nick_lb.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.discord_lb.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 Discord", None))
        self.town_lb.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.time_game_lb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0438\u0433\u0440\u044b", None))
        self.all_time_lb.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0436", None))
        self.your_help_lb.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043c \u0442\u044b \u043f\u043e\u043c\u043e\u0436\u0435\u0448\u044c \u0413\u0418?", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043c \u0433\u0438 \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0442\u0435\u0431\u0435?", None))
        self.micro_lb.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u043c\u0438\u043a\u0440\u043e\u0444\u043e\u043d\u0430 \u0438 \u0433\u0430\u0440\u043d\u0438\u0442\u0443\u0440\u044b", None))
        self.dislike_lb.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e \u043d\u0435 \u043d\u0440\u0430\u0432\u0438\u043b\u043e\u0441\u044c \u0432 \u043f\u0440\u043e\u0448\u043b\u044b\u0445 \u0413\u0418?", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0438\u0433\u0440\u044b", None))
        self.reason_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0447\u0438\u043d\u0430 \u043f\u043e\u0438\u0441\u043a\u0430 \u043a\u043b\u0430\u043d\u0430", None))
        self.find_lst_update_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0439 \u0438\u0437\u043c\u0435\u043d\u0451\u043d\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.db_tab), QCoreApplication.translate("MainWindow", u"\u0411\u0414 \u041a\u043e\u0442\u0430", None))
        self.find_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.clear_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.find_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0411\u0414", None))
        ___qtablewidgetitem = self.db_tw.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a \u0432 \u0438\u0433\u0440\u0435", None));
        ___qtablewidgetitem1 = self.db_tw.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f ", None));
        ___qtablewidgetitem2 = self.db_tw.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None));
        ___qtablewidgetitem3 = self.db_tw.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem4 = self.db_tw.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u043a \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None));
        ___qtablewidgetitem5 = self.db_tw.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 \u0434\u0441", None));
        ___qtablewidgetitem6 = self.db_tw.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None));
        ___qtablewidgetitem7 = self.db_tw.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u043d\u0430", None));
        ___qtablewidgetitem8 = self.db_tw.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0447. \u0432 \u0434\u0435\u043d\u044c(\u043f\u043e\u0435)", None));
        ___qtablewidgetitem9 = self.db_tw.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435\u0433\u043e \u0441\u044b\u0433\u0440\u0430\u043d\u043e \u0447. \u0432 \u043f\u043e\u0435", None));
        ___qtablewidgetitem10 = self.db_tw.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043c \u043c\u043e\u0436\u0435\u0448\u044c \u043f\u043e\u043c\u043e\u0447\u044c \u0433\u0438", None));
        ___qtablewidgetitem11 = self.db_tw.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043c \u0433\u0438 \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0442\u0435\u0431\u0435", None));
        ___qtablewidgetitem12 = self.db_tw.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u0442\u044c \u043b\u0438 \u0433\u0430\u0440\u043d\u0438\u0442\u0443\u0440\u0430", None));
        ___qtablewidgetitem13 = self.db_tw.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u043c \u043d\u0435\u0434\u043e\u0432\u043e\u043b\u0435\u043d \u0432 \u043f\u0440\u043e\u0448\u043b\u044b\u0445 \u0433\u0438", None));
        ___qtablewidgetitem14 = self.db_tw.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0432\u043e\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u0438\u0433\u0440\u044b \u0432 \u043f\u043e\u0435", None));
        ___qtablewidgetitem15 = self.db_tw.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u044c \u0432\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f \u0432 \u0433\u0438", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.db_search_tab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0411\u0414", None))
        self.start_char_lb.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b \u043d\u0430\u0447\u0430\u043b\u0430 \u0441\u0442\u0440\u043e\u043a\u0438", None))
        self.end_char_lb.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0441\u0442\u0440\u043e\u043a\u0438", None))
        self.file_locate_lb.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u043a \u0444\u0430\u0439\u043b\u0443", None))
        self.file_name_lb.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430", None))
        self.file_name_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.separate_char_lb.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043c\u0432\u043e\u043b \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b\u044c \u0441\u0442\u0440\u043e\u043a\u0438", None))
        self.file_locate_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435", None))
        self.save_pref_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preference_tab), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

