from bs4 import BeautifulSoup
import requests
from mechanize import Browser
import mechanize
from bs4 import BeautifulSoup




stream = raw_input("Enter Stream:  ")
year = raw_input("Enter Year:  ")
month = raw_input("Enter Month:  ")


n=1

start12= raw_input("Enter first seat number :    ")
stop12= raw_input("Enter last seat number :    ")
start1=int(start12)
stop1=int(stop12)

def seatnumber():
    
       
    
    br = mechanize.Browser()
    br.open("http://result.saurashtrauniversity.edu/Default1.aspx")



    br.select_form(nr=0)
    control = br.form.find_control("ctl00$ContentPlaceHolder1$ddstr")

    for item in control.items:
        if item.name == stream:
            item.selected = True



    control1 = br.form.find_control("ctl00$ContentPlaceHolder1$ddyr")
    for item1 in control1.items:
        if item1.name == "2017":
            item1.selected = True


    control2 = br.form.find_control("ctl00$ContentPlaceHolder1$ddmon")
    for item2 in control2.items:
        if item2.name == "Mar":
            item2.selected = True
    

    response = br.submit(name="ctl00$ContentPlaceHolder1$ImageButton8")
    counter = 1
    
 
        

    redir = response.read()
    x  = range(start1, stop1)
    
    m = str(0) + str(x[n])
    
    br.select_form(nr=0)
    br.form['ctl00$ContentPlaceHolder1$txtseat'] = m
    resultresp = br.submit(name="ctl00$ContentPlaceHolder1$imgsearch")
    soup = BeautifulSoup(resultresp, "html.parser")
    student = soup.find(attrs={'id': "ctl00_ContentPlaceHolder1_lblnm"})
    studentname = student.text
    print studentname
    for allmarks in soup.findAll(attrs={'style': "background-color:gray;color:white"}):
        msg = allmarks.text
        print msg
    for allgrades in soup.findAll(attrs={'style': "background-color:orange;color:White"}):
        msg1 = allgrades.text
        print msg1

    



while True:
    seatnumber()
    n+=1
    print n



