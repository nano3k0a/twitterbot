# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tweet_bot.ui'
#
# Created: Sat Dec 13 06:50:04 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(807, 749)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.twitter_tab = QtGui.QWidget()
        self.twitter_tab.setObjectName(_fromUtf8("twitter_tab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.twitter_tab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.twitter_tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tweets_listView = QtGui.QListView(self.groupBox)
        self.tweets_listView.setObjectName(_fromUtf8("tweets_listView"))
        self.horizontalLayout_5.addWidget(self.tweets_listView)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.log_listView = QtGui.QListView(self.groupBox_2)
        self.log_listView.setObjectName(_fromUtf8("log_listView"))
        self.horizontalLayout_6.addWidget(self.log_listView, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.hashtag_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.hashtag_lineEdit.setObjectName(_fromUtf8("hashtag_lineEdit"))
        self.horizontalLayout_7.addWidget(self.hashtag_lineEdit)
        self.start_btn = QtGui.QPushButton(self.groupBox_3)
        self.start_btn.setObjectName(_fromUtf8("start_btn"))
        self.horizontalLayout_7.addWidget(self.start_btn)
        self.stop_btn = QtGui.QPushButton(self.groupBox_3)
        self.stop_btn.setObjectName(_fromUtf8("stop_btn"))
        self.horizontalLayout_7.addWidget(self.stop_btn)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.twitter_tab, _fromUtf8(""))
        self.twitteraccount_tab = QtGui.QWidget()
        self.twitteraccount_tab.setObjectName(_fromUtf8("twitteraccount_tab"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.twitteraccount_tab)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.twitteraccount_tab)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.webView = QtWebKit.QWebView(self.groupBox_4)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout_9.addWidget(self.webView)
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.twitteraccountname_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.twitteraccountname_lineEdit.setObjectName(_fromUtf8("twitteraccountname_lineEdit"))
        self.verticalLayout_3.addWidget(self.twitteraccountname_lineEdit)
        self.addtwitteraccount_btn = QtGui.QPushButton(self.groupBox_5)
        self.addtwitteraccount_btn.setObjectName(_fromUtf8("addtwitteraccount_btn"))
        self.verticalLayout_3.addWidget(self.addtwitteraccount_btn)
        self.pin_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        self.pin_lineEdit.setObjectName(_fromUtf8("pin_lineEdit"))
        self.verticalLayout_3.addWidget(self.pin_lineEdit)
        self.verifypin_btn = QtGui.QPushButton(self.groupBox_5)
        self.verifypin_btn.setObjectName(_fromUtf8("verifypin_btn"))
        self.verticalLayout_3.addWidget(self.verifypin_btn)
        self.horizontalLayout_9.addWidget(self.groupBox_5, QtCore.Qt.AlignTop)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.twitteraccount_tab, _fromUtf8(""))
        self.settings_tab = QtGui.QWidget()
        self.settings_tab.setObjectName(_fromUtf8("settings_tab"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.settings_tab)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.groupBox_8 = QtGui.QGroupBox(self.settings_tab)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.twitteraccounts_listWidget = QtGui.QListWidget(self.groupBox_8)
        self.twitteraccounts_listWidget.setObjectName(_fromUtf8("twitteraccounts_listWidget"))
        self.verticalLayout_10.addWidget(self.twitteraccounts_listWidget, QtCore.Qt.AlignLeft)
        self.removeall_btn = QtGui.QPushButton(self.groupBox_8)
        self.removeall_btn.setObjectName(_fromUtf8("removeall_btn"))
        self.verticalLayout_10.addWidget(self.removeall_btn)
        self.remove_btn = QtGui.QPushButton(self.groupBox_8)
        self.remove_btn.setObjectName(_fromUtf8("remove_btn"))
        self.verticalLayout_10.addWidget(self.remove_btn)
        self.edit_btn = QtGui.QPushButton(self.groupBox_8)
        self.edit_btn.setObjectName(_fromUtf8("edit_btn"))
        self.verticalLayout_10.addWidget(self.edit_btn)
        self.horizontalLayout_8.addWidget(self.groupBox_8)
        self.groupBox_10 = QtGui.QGroupBox(self.settings_tab)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.databaseuri_lineEdit = QtGui.QLineEdit(self.groupBox_10)
        self.databaseuri_lineEdit.setObjectName(_fromUtf8("databaseuri_lineEdit"))
        self.verticalLayout_11.addWidget(self.databaseuri_lineEdit)
        self.database_lineEdit = QtGui.QLineEdit(self.groupBox_10)
        self.database_lineEdit.setObjectName(_fromUtf8("database_lineEdit"))
        self.verticalLayout_11.addWidget(self.database_lineEdit)
        self.savedatabase_btn = QtGui.QPushButton(self.groupBox_10)
        self.savedatabase_btn.setObjectName(_fromUtf8("savedatabase_btn"))
        self.verticalLayout_11.addWidget(self.savedatabase_btn, QtCore.Qt.AlignLeft)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.openfile_btn = QtGui.QPushButton(self.groupBox_7)
        self.openfile_btn.setObjectName(_fromUtf8("openfile_btn"))
        self.horizontalLayout_10.addWidget(self.openfile_btn, QtCore.Qt.AlignLeft)
        self.filename_lineEdit = QtGui.QLineEdit(self.groupBox_7)
        self.filename_lineEdit.setObjectName(_fromUtf8("filename_lineEdit"))
        self.horizontalLayout_10.addWidget(self.filename_lineEdit)
        self.verticalLayout_11.addWidget(self.groupBox_7, QtCore.Qt.AlignTop)
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.usedatabase_radio = QtGui.QRadioButton(self.groupBox_9)
        self.usedatabase_radio.setObjectName(_fromUtf8("usedatabase_radio"))
        self.verticalLayout_7.addWidget(self.usedatabase_radio)
        self.usetextfile_radio = QtGui.QRadioButton(self.groupBox_9)
        self.usetextfile_radio.setObjectName(_fromUtf8("usetextfile_radio"))
        self.verticalLayout_7.addWidget(self.usetextfile_radio)
        self.savesource_btn = QtGui.QPushButton(self.groupBox_9)
        self.savesource_btn.setObjectName(_fromUtf8("savesource_btn"))
        self.verticalLayout_7.addWidget(self.savesource_btn, QtCore.Qt.AlignLeft)
        self.verticalLayout_11.addWidget(self.groupBox_9)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_10)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.delaybetweenaccounts_timeEdit = QtGui.QTimeEdit(self.groupBox_6)
        self.delaybetweenaccounts_timeEdit.setObjectName(_fromUtf8("delaybetweenaccounts_timeEdit"))
        self.verticalLayout_6.addWidget(self.delaybetweenaccounts_timeEdit)
        self.label_2 = QtGui.QLabel(self.groupBox_6)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_6.addWidget(self.label_2, QtCore.Qt.AlignLeft)
        self.delayaftertweet_timeEdit = QtGui.QTimeEdit(self.groupBox_6)
        self.delayaftertweet_timeEdit.setObjectName(_fromUtf8("delayaftertweet_timeEdit"))
        self.verticalLayout_6.addWidget(self.delayaftertweet_timeEdit)
        self.label = QtGui.QLabel(self.groupBox_6)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_6.addWidget(self.label, QtCore.Qt.AlignLeft)
        self.savetiming_btn = QtGui.QPushButton(self.groupBox_6)
        self.savetiming_btn.setObjectName(_fromUtf8("savetiming_btn"))
        self.verticalLayout_6.addWidget(self.savetiming_btn, QtCore.Qt.AlignLeft)
        self.verticalLayout_11.addWidget(self.groupBox_6)
        self.horizontalLayout_8.addWidget(self.groupBox_10)
        self.tabWidget.addTab(self.settings_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave_log = QtGui.QAction(MainWindow)
        self.actionSave_log.setObjectName(_fromUtf8("actionSave_log"))
        self.menuMenu.addAction(self.actionSave_log)
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.groupBox.setTitle(_translate("MainWindow", "Tweets", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Log", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Hashtag", None))
        self.start_btn.setText(_translate("MainWindow", "Start Bot", None))
        self.stop_btn.setText(_translate("MainWindow", "Stop Bot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.twitter_tab), _translate("MainWindow", "Twitter", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Web View", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Add Twitter Account", None))
        self.addtwitteraccount_btn.setText(_translate("MainWindow", "Add", None))
        self.verifypin_btn.setText(_translate("MainWindow", "Verify PIN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.twitteraccount_tab), _translate("MainWindow", "Add Twitter Account", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Twitter Accounts", None))
        self.removeall_btn.setText(_translate("MainWindow", "Remove all", None))
        self.remove_btn.setText(_translate("MainWindow", "Remove", None))
        self.edit_btn.setText(_translate("MainWindow", "Edit", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Mongo Database", None))
        self.savedatabase_btn.setText(_translate("MainWindow", "Save Database", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Tweet Text File", None))
        self.openfile_btn.setText(_translate("MainWindow", "Open File", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Tweet Source", None))
        self.usedatabase_radio.setText(_translate("MainWindow", "Use Database", None))
        self.usetextfile_radio.setText(_translate("MainWindow", "Use Text File", None))
        self.savesource_btn.setText(_translate("MainWindow", "Save source", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Timing Settings mm:ss", None))
        self.delaybetweenaccounts_timeEdit.setDisplayFormat(_translate("MainWindow", "mm:ss", None))
        self.label_2.setText(_translate("MainWindow", "Tweet Delay between Accounts", None))
        self.delayaftertweet_timeEdit.setDisplayFormat(_translate("MainWindow", "mm:ss", None))
        self.label.setText(_translate("MainWindow", "Tweet Delay after every single Tweet", None))
        self.savetiming_btn.setText(_translate("MainWindow", "Save Timing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Settings", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionSave_log.setText(_translate("MainWindow", "Save log", None))

from PyQt4 import QtWebKit
