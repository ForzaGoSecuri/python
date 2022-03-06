import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import os


def word_on_json():
    print("test")


def Sync():

    firebaseConfig = {
        "project_id": "forzagosecuri",
        "private_key_id": "1aed4a3fa806763a588741eff96edc6ba7c75e10",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCzBHvrkeZhq/BW\nKAmkge1MQzxKBS+cKrDwAPRM/JvCLepq/fWfmDFUG/6prcalUMsl/PjHcRgRW/EG\nwluRGWpNHmUKCB27qU/C5mcHH50obQyPGPlqTuFBYGo6/XvdG01NzTyLQmepkzVI\nCSP7kzjrxLH6uckwxOMtnGZXEZLVWIbvFDaEhzTNBN3HXYOtxPLxw1SYGShUb6Uf\nwjlE/4Kb3jICuvLtihkzhqY1g7me63v+R6PWv9ASNIyNsmsEkbFH+4cXvGn6eZ7Y\nTi4PKE/JMbQ2DeZ7KsMDgovkEBzO7C+CztJEA3hXeryurrVjxH+Q14rl8k/wylsK\nhHUqUPODAgMBAAECggEAAeEaK+7sLDpR25WwBDoY86QBDgXf6hPIp7xa1DQSrocs\n3tKrsXE3k1p34fAhFbszZsKxGebmCcidTyTbMTrDEuwuw1wyc7XjUHh6vGhojfQX\nHal1dNg/JSCN/PCMTFXtCdQNvqiDzhPti0QNTKbPAiqec7NfmVN3zxLFQES+9d5j\njC0ZSKGSIg8qyFAoaGT5F6MwPTD+4xiEGpx5+3e16DzVGRJWI7V20ekUgQ8e8dUs\nlF3eIWp3CybDHgBvDeLFXzADMhdZAqnYQK9iPNAQZ+OuPCI0OMErjilBucuMfmcK\nlN18F+XFqBwIziPhJ4rxCDeB1JxeuBxKM+GS+UWjgQKBgQDg8nPlUJEot3U+kKWI\nv8rrpDJk2QlXmeFZnMIFmEin9AKmM567cP8SLih7GPUj8zvBpthejwLo8C/xyROv\n3nt1YwTT+xufdGlWZZvSG+WsXbxpAlPS+5jEaMkI4ofgiqEGHjqF7z8RTfhpuzba\n9MmngRrF9weY0FIjTVX3z6WwjQKBgQDLuuW6O9RGRLSEnc+GoY5QAY4BdykWpfDT\nRz/7Iyd1dzXXAezh42NjiGG8LRGPXMIt3Ho/l+Nt+Sj4QFJuYPFNBq5e+vACVV+R\n7ODmS7TKIn7sA++GfZBkEAD+5MdiPQZUlyjHWgbNCOE9TgELw8gGg6E3fnhcKEe6\npvBndTtYTwKBgQCnaCiSP1xYRfgOYM2gsMOOjLsoTFFkjVOlQkEusr9XpwQVtpLq\nAlUBrbJYsiE16P3Ox6F89cd/ncjAkxmAp/2PRerA678J8zO1pZbKThKmLXhbWe0S\nNkXh3e3HG/dtRx5BFFwPcxanhTRbU4Wme8hbTXykWYyg0GBgf1x8OV+gvQKBgD1M\ni+jALbvC2mn4rcN9grtx7E9mkjddUJvRmV+wESRX7Rw3WRYSfAors/SRvvHa4BY6\ne5H82pJxYLFpcSQDCTe65eZwLJ0XIP1gP78rUkdrn7LV8FEQIMzqv9Hx9kgJwojb\nPorU/Kzemh7/BHOMwferzWtMI1zfRc3UgwsuC+AjAoGABeFWyAhTMw/mpPrc9tvq\nDDl6x3zbp3ho3BV15Z9YhR1p7efj7HUxUGeXulWBQP2a0xe51sPlWe18V9RPrcTV\n3GNFfGAAk/trjvmltdl8N0/BLcRrk+L8x7nAgg77/HVzRuczixCaDHALIOc9RRFl\n2R5eP3BN+/7u3JG+vrLgleE=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-9szqh@forzagosecuri.iam.gserviceaccount.com",
        "client_id": "111870611056954577916",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9szqh%40forzagosecuri.iam.gserviceaccount.com",
        "apiKey": "AIzaSyDZLWqHO10-YmkThUfeKPQ07Wv540Pujeo",
        "authDomain": "forzagosecuri.firebaseapp.com",
        "projectId": "forzagosecuri",
        "storageBucket": "forzagosecuri.appspot.com",
        "messagingSenderId": "458599727535",
        "appId": "1:458599727535:web:22b34f74723f288bd22f5a",
        "databaseURL": "https://forzagosecuri-default-rtdb.europe-west1.firebasedatabase.app",
    }

    firebase = pyrebase.initialize_app(firebaseConfig)


    db = firebase.database()
    auth = firebase.auth()
    storage = firebase.storage()

    email = "moilechevallier@gmail.com"
    password = "01100110"

    auth.sign_in_with_email_and_password(email, password)

    people = db.child("/").get()

    print(people.val())
    text = people.val().copy()

    text = str(text)

    a = 1
    b = 0
    c = 0
    d = 1
    e = 1
    f = 0
    I = 0
    mot = ''
    firstname = "0"
    lastname = "0"
    job = "0"
    equipement = "0"
    passwords = "0"
    path = ''
    equipements = ''


    files = os.listdir("sendtogit")
    for i in range(0, len(files)):
        os.remove('sendtogit/' + files[i])

    while d == 1:
        I = I + 1
        value = text[I]

        if b == 1 and value != '\'':
            mot = mot + value

        if value == '{':
            a = a + 1
        if value == '}':
            a = a - 1

        if value == '\'':
            print(mot, a)

            if a == 2:
                if e != 0:
                    e = e - 1
                else:
                    e = 3
            if b == 1:
                b = 0
            else:
                b = 1
                c = c - 1

            if e == 3:
                if mot[0] == "E":
                    equipement = "1"
                if mot[0] == "J":
                    job = "1"
                if mot[0] == "f":
                    firstname = "1"
                if mot[0] == "l":
                    lastname = "1"
                if mot[0] == "P":
                    passwords = "1"
            if e == 1:
                if (f == 1):
                    path = "sendtogit/" + mot + ".txt"
                    if equipement == "1":
                        equipement = mot
                    if job == "1":
                        job = mot
                    if firstname == "1":
                        firstname = mot
                    if lastname == "1":
                        lastname = mot
                    if passwords == "1":
                        passwords = mot

                    if a == 1 and mot != "" and mot != "zzequipements":
                        trame = str(lastname) + "\n" + str(firstname) + "\n" + str(job) + "\n" + str(passwords) + "\n\n" + str(equipement) + "\n"
                        #trame = trame.replace("/", "\n")
                        print("----------------------------")
                        print(trame)

                        file = open(path, "w")
                        file.write(trame)
                        file.close()
                f = 1



            mot = ""








        if value == "[":
            I = I + 5
            while d == 1:
                I = I + 1
                value = text[I]
                if value == ",":
                    value = '\t'

                if value == " " or value == "\'":
                    value = ''
                if value == "]":
                    value = ''
                    d = 0
                equipements = equipements + value
            file = open("sendtogit/equipement", "w")
            file.write(equipements)
            file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Sync()
