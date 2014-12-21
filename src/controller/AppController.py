# -*- coding: utf-8 -*-
# coding: utf8
import random
import sys
import os
import string
import time
import pymongo
import md5

import urlparse
import oauth2 as oauth
import configparser
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from twython import Twython, TwythonError, TwythonRateLimitError

class AppController():

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, REQUEST_TOKEN_URL, 
            ACCESS_TOKEN_URL, AUTHORIZE_URL, mainWindow):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.REQUEST_TOKEN_URL = REQUEST_TOKEN_URL
        self.ACCESS_TOKEN_URL = ACCESS_TOKEN_URL
        self.AUTHORIZE_URL = AUTHORIZE_URL
        self.mainWindow = mainWindow
        self.twitter_account_ini_name = 'twitter_accounts_file.ini'

        try:
            if not os.path.isfile(self.twitter_account_ini_name):
                twitter_accounts_file = open(self.twitter_account_ini_name, 'w')
                twitter_accounts_file.close()
        except IOError:
            self.raiseErrorBox("ini File could not be created!")
        
        self.populateAccountList()

    def main(self, listView):
        db = self.db_client.furkantweet
        listView.append("Hallo Welt")
        collection_names = db.collection_names()
        tweet_collection = db.generaltweets
        twitter_instance = self.getTwitterInstance(db, collection_names)
        self.fireBot(listView, twitter_instance, tweet_collection)

    def fireBot(listView, twitter, tweet_collection):
        print "\n"
        print "********************************************"
        print "Token wurden gefunden! Elhamdulillah!"
        print "Der Bot kann jetzt gestartet werden!"
        print "********************************************"
        start_bot = raw_input('::Bot starten [y/n]?: ')
        if start_bot == 'y':
            hashtag = raw_input('::Hashtag bitte eingeben: ').decode(sys.stdin.encoding)
        else:
            print "Bot wird beendet! Khair Insallah..."
            sys.exit()
        tweet_counter = 1
        tweet_cursor = tweet_collection.find()
        while True:
            try:
                successful_tweets = 0
                failed_tweets = 0
                print "\n==> Für folgende Benutzer wird getweeted:"
                for user in twitter:
                    print " %s" %getAccountName(user)
                print "\n"
                tweet_cursor = shuffleCursor(tweet_cursor)
                for counter, tweet in enumerate(tweet_cursor):
                    listView.append("::Tweet Nr.%i senden...\n '%s'") %(counter+1, tweet['tweet'])
                    text = "%s %s" %(tweet['tweet'], hashtag)
                    success = sendTweet(twitter, text)
                    if success:
                        successful_tweets += 1
                    else:
                        failed_tweets += 1
                        #status = user.get_application_rate_limit_status(resources=['statuses'])
                        #left = status['resources']['statuses']['/statuses/update']['remaining']
                    print "::Kurze Pause..."
                    print " ==> Tweets Insgesamt: %i\n  Erfolgreich: %i\n  Gescheitert: %i" %(counter+1,
                            successful_tweets, failed_tweets)
                    startSleep(random.uniform(5, 20))
                    if counter == 100:
                        print "50 Tweets erreicht lange Pause für ca. 5 min"
                        startSleep(random.randint(120, 190))
            except TwythonError as e:
                print e
                sys.exit()

    def addTwitterAccount(self):
        url = getRequestToken()

    def shuffleCursor(tweet_cursor):
        for i in range(random.randint(100, 1000)):
            tweet_cursor.next()
        return tweet_cursor

    def sendTweet(twitter, text):
        for user in twitter:
            try:
                user.update_status(status=text)
                time.sleep(2)
            except TwythonError as e:
                print "\n::Fehler beim Senden!\n Status Code: %s" %user._last_call["status_code"]
                print " Betroffener Account: %s" %getAccountName(user)
                print " Tweet Nachricht wird übersprungen...\n"
                return False
        print "\n::Tweet mit allen Accounts gesendet!"

        return True

    def checkUsername(username, collection_names):
        if username in collection_names:
            return True
        else:
            return False

    def getAccountName(twitter):
        try:
            return twitter.verify_credentials()['name']
        except TwythonRateLimitError, e:
            print "\n::Fehler"
            print " Limit Erreicht!"
            print " %s" %e
            print " Schlafen für 15min!"
            startSleep(60*15)
            return

    def startSleep(seconds):
        while seconds > 0:
            print "\r Countdown: %i Sek." %seconds,
            sys.stdout.flush()
            seconds -= 1
            time.sleep(1)
        print "\n"

    def getRequestToken():
        consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        client = oauth.Client(consumer)
        response, content = client.request(REQUEST_TOKEN_URL, "GET")
        if response['status'] != '200':
            return None
            raise Exception("Invalid response %s" %response['status'])
        else:
            request_token = dict(urlparse.parse_qsl(content))
            oauth_verifier = getPinFromUser(request_token)
            token = oauth.Token(request_token['oauth_token'],
                request_token['oauth_token_secret'])
            token.set_verifier(oauth_verifier)
            client = oauth.Client(consumer, token)
            response, content = client.request(ACCESS_TOKEN_URL, "POST")
            access_token = dict(urlparse.parse_qsl(content))
            return access_token

    def startAuthentication(self):
        self.twitter_account_username = str(self.mainWindow.twitteraccountname_lineEdit.text())
        is_new_user = self.checkUser(self.twitter_account_username)
        if is_new_user:
            self.consumer = oauth.Consumer(self.CONSUMER_KEY, self.CONSUMER_SECRET)
            client = oauth.Client(self.consumer)
            response, content = client.request(self.REQUEST_TOKEN_URL, "GET")

            if response['status'] != '200':
                raise Exception("Invalid response %s" %response['status'])
            else:
                self.request_token = dict(urlparse.parse_qsl(content))
                url = "%s?oauth_token=%s" %(self.AUTHORIZE_URL, self.request_token['oauth_token']) 
                self.mainWindow.webView.load(QUrl(url))      

        elif is_new_user is None:
            self.raiseErrorBox("Username cannot be empty!")
        else:
            self.raiseErrorBox("Twitter Username: '%s' already exists! Delete it first" %
                    self.twitter_account_username)

    def verifyPin(self):
        try:
            oauth_verifier_pin = str(self.mainWindow.pin_lineEdit.text())
            try:
                if self.twitter_account_username and oauth_verifier_pin.isdigit():
                    request_token = self.request_token
                    token = oauth.Token(request_token['oauth_token'],
                            request_token['oauth_token_secret'])
                    token.set_verifier(oauth_verifier_pin)
                    client = oauth.Client(self.consumer, token)
                    response, content = client.request(self.ACCESS_TOKEN_URL, 'POST')
                    access_token = dict(urlparse.parse_qsl(content))
                else:
                    self.raiseErrorBox("No Username specified! Or PIN is not digit!")
                    return
            except Exception as e:
                self.raiseErrorBox("PIN was not accepted!")
                print e
                return
        except Exception:
            self.raiseErrorBox("PIN can only be numbers!")
            return
        
        self.saveOAuthToken(self.twitter_account_username, access_token)
            
    def saveOAuthToken(self, twitter_account_username, access_token):
        twitter_accounts_file = self.getTwitterAccountsFile()
        try:
            config_parser = configparser.SafeConfigParser()
            config_parser.add_section(str(twitter_account_username))
            config_parser.set(str(twitter_account_username), 'oauth_token',
                    access_token['oauth_token'])
            config_parser.set(str(twitter_account_username), 'oauth_token_secret',
                    access_token['oauth_token_secret'])
            config_parser.write(twitter_accounts_file)
            twitter_accounts_file.close()

            self.mainWindow.twitteraccounts_listWidget.addItem(twitter_account_username)
            self.raiseInfoBox("OK! Token was saved!")
        except KeyError:
            self.raiseErrorBox("PIN was wrong, or token timed out!")
    
    def getTwitterAccountsFile(self):
        try:
            twitter_accounts_file = open(self.twitter_account_ini_name, 'a')
            return twitter_accounts_file
        except IOError:
            self.raiseErrorBox("File cannot be opened!")

    def populateAccountList(self):
        config_parser = configparser.SafeConfigParser()
        config_parser.read(self.twitter_account_ini_name)
        sections = config_parser.sections()
        if sections:
            for section in sections:
                self.mainWindow.twitteraccounts_listWidget.addItem(section)
        else:
            self.raiseInfoBox("No Twitter Accounts found! You have to add at least one")

    def updateAccountName(self, old_name, new_name):
        config_parser = configparser.SafeConfigParser()
        config_parser.read(self.twitter_account_ini_name)
        token = config_parser.get(old_name, 'oauth_token')
        token_secret = config_parser.get(old_name, 'oauth_token_secret')

        if config_parser.remove_section(old_name):
            config_parser.add_section(new_name)
            config_parser.set(new_name, 'oauth_token', token)
            config_parser.set(new_name, 'oauth_token_secret', token_secret)
            self.saveIniFile(self.twitter_account_ini_name, config_parser)
            self.raiseInfoBox("Ok Edits were saved")
        else:
            self.raiseErrorBox("Ini File could not be updated!")
    
    def deleteAccount(self):
        config_parser = configparser.SafeConfigParser()
        config_parser.read(self.twitter_account_ini_name)
        for item in self.mainWindow.twitteraccounts_listWidget.selectedItems():
            current_item = self.mainWindow.twitteraccounts_listWidget.row(item)
            user_name = str(self.mainWindow.twitteraccounts_listWidget.takeItem(current_item).text())
            if config_parser.remove_section(user_name):
                self.saveIniFile(self.twitter_account_ini_name, config_parser)
                self.raiseInfoBox("User has been deleted")
            else:
                self.raiseErrorBox("User could not be deleted!")

    def saveIniFile(self, ini_file_name, config_parser):
        with open(ini_file_name, 'wb') as configfile:
            config_parser.write(configfile)


    def editUserName(self):
        current_name = self.mainWindow.twitteraccounts_listWidget.currentItem()
        if current_name:
            new_name, ok = QInputDialog.getText(None, "Enter new Name", "Enter new Name")
            if ok and (len(new_name) !=0):
                self.updateAccountName(str(current_name.text()), str(new_name))
                current_name.setText(new_name)
        else:
            self.raiseErrorBox("The List is empty!")
        
    def checkUser(self, twitter_account_username):
        config_parser = configparser.SafeConfigParser()
        config_parser.read(self.twitter_account_ini_name)
        if twitter_account_username:
            if config_parser.has_section(twitter_account_username):
                return False
            else:
                return True
        else:
            return None
        

    def getOAuthToken(user_collection):
        if user_collection.count() > 1:
            return user_collection.find()
        else:
            print "==> Fehler!"
            print " Die Datenbank hat noch keine Twitter Account"
            print " Es muss erst ein Twitter Account hinzugefügt werden"
            return None

    def getPinFromUser(request_token):
        print "*************Du musst diese Anwednung verifizieren*********************"
        print "    Kopiere dazu den unten aufgeführten Link einfach in deinen Browser"
        print "    Autorisiere die App und geb die PIN unten ein"
        print "***********************************************************************"
        print "::Zu kopierender Link\n %s?oauth_token=%s" %(AUTHORIZE_URL,
            request_token['oauth_token'])

        is_not_digit = True
        while is_not_digit: 
            oauth_verifier = raw_input(' Den PIN hier eingeben!: ')
            if oauth_verifier.isdigit():
                print " OK! PIN wird geprüft..."
                is_not_digit = False
            else:
                print "Die PIN kann nur aus Zahlen bestehen, versuchs nocheinmal!"

        return oauth_verifier
        
    def raiseErrorBox(self, text):
        QMessageBox.critical(None, "Error", text, QMessageBox.Ok)

    def raiseInfoBox(self, text):
        QMessageBox.information(None, "Info", text, QMessageBox.Ok)
