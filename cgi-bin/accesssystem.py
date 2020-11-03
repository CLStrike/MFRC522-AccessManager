#!/usr/bin/env python3
import RPi.GPIO as GPIO
import os
from mfrc522 import SimpleMFRC522
import cgi

form = cgi.FieldStorage()
print("Content-Type: text/html\n\n")
print("<html>")
Reader = SimpleMFRC522()
id, data = Reader.read()
department = form.getvalue("Department")
department_stripped = department.strip()

dep_data = str(data.split(",")[1])
dep_data_stripped = dep_data.strip()

command_data = "echo " + dep_data_stripped + "> data.txt" # To check the value of the card (data).
os.system(command_data) # to check the value of the card (data).
command = "echo " +  department_stripped +  "> department.txt" # To check value of dropdown list.
os.system(command) # to check value of dropdown list.

if department_stripped == dep_data_stripped:
        permission = "True"

elif department != data.split(",")[1]:
        permission = "False"
print("<html>")
print("<head>")
print("<title>Access Manager 0.1</title>")
print("</head>")
print("<body>")
print("<meta name='viewport' content='width=device-width, initial-scale=1'>")
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
print("<p> Chosen department: ", department, "</p>")
print("<p> Department read from card: ", data.split(",")[1], "</p>")
print("<p> ACCESS ALLOWED: ", permission,  "</p>")
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
