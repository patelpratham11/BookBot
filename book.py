#import statements
import yagmail
import os
import shutil
#inital global values

def initial():
    folder = "/Users/patelpratham11/Documents/Books"
    if not os.path.exists(folder):
        os.makedirs(folder)
    books = os.listdir(folder)
    for book in books:

    info(folder)

def info(folder):
    email = input("input your email here with @gmail at the end. \ne.g. janedoe@gmail.com\n")
    password = input("input your password here\n")
    rec = input("what is the input email address?\n")
    yag = yagmail.SMTP(email, password)
    emailCreate(folder, books, rec, yag)


def emailCreate(folder, books, rec, yag):
    values = []
    for book in books:
        values.append(folder+"/"+book)

    yag.send(to=rec,attachments=values)

    print("email has been sent")
    delete(folder)

def delete(folder):
    for file in os.scandir(folder):
        os.remove(file.path)
    print("cleared the folder")


initial()
