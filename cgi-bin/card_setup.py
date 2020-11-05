#!/usr/bin/env python3
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import cgi

form = cgi.FieldStorage()

if form.getvalue("rw_mode"):
        mode = form.getvalue("rw_mode")
else:
        mode = "Not Set"

if mode  == "Read":
        print("Content-Type: text/html\n\n")
        Reader = SimpleMFRC522()
        id, data = Reader.read()
        print("<html>")
        print("<head>")
        print("<title>Access Manager 0.1</title>")
        print("</head>")
        print("<body>")
        print('<meta name="viewport" content="width=device-width, initial-scale=1">')
        print('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')
        print('<div class="w3-bar w3-dark-grey">')
        print('<div class="w3-bar-item"></div>')
        print('</div>')
        print('<div class="w3-container w3-blue">')
        print("<h1>Access Manager</h1>")
        print("</div")
        print("<div class='w3-container  w3-light-grey'>")
        print("<p> Card ID: ", id ,"</p>")
        print("<p> User: ", data.split(",")[0] , "</p>")
        print("<p> This user/card has access to: ", data.split(",")[1] , "</p>")
        print("<form method='get' action='/index.html'>")
        print("<input class='w3-btn w3-padding w3-blue'type='submit' value='Back' />")
        print("</form>")
        print("</div>")
        print("<div class='w3-bar w3-grey'>")
        print("<div class='w3-bar-item'></div>")
        print("</div>")
        print("</body>")
        print("</html>")
        GPIO.cleanup()

elif mode == "Write":
        Reader = SimpleMFRC522()
        user = form.getvalue("User")
        if user == None:
                exit
        accesstype = form.getvalue('AccessType')
        text = user + " , " + accesstype
        Reader.write(text)
        id, data = Reader.read()
        print("Content-Type: text/html\n\n")
        print("<html>")
        print("<head>")
        print("<title>Access Manager 0.1</title>")
        print("</head>")
        print("<body>")
        print('<meta name="viewport" content="width=device-width, initial-scale=1">')
        print('<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">')
        print('<div class="w3-bar w3-dark-grey">')
        print('<div class="w3-bar-item"></div>')
        print('</div>')
        print('<div class="w3-container w3-blue">')
        print("<h1>Access Manager</h1>")
        print("</div")
        print("<div class='w3-container  w3-light-grey'>")
        print("<p> Card ID: ", id ,"</p>")
        print("<p> User: ", data.split(",")[0] , "</p>")
        print("<p> Access to the department: ", data.split(",")[1] , "</p>")
        print("<form method='get' action='/index.html'>")
        print("<input class='w3-btn w3-padding w3-blue'type='submit' value='Back' />")
        print("</form>")
        print("</div>")
        print("<div class='w3-bar w3-grey'>")
        print("<div class='w3-bar-item'></div>")
        print("</div>")
        print("</body>")
        print("</html>")
        GPIO.cleanup()
