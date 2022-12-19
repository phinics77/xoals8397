from bs4 import BeautifulSoup as bs
import urllib.request
import tkinter
from tkinter import *
from urllib.request import urlretrieve
import requests
import os
f = open("새파일.txt", 'w')
f.close()
url = "http://jinyang-h.gne.go.kr/"
def pressed():
    label.configure(text="버튼을 누름")

def confirm():
    in_text = "입력 내용 : " + input_text.get()
    label.configure(text=in_text)

window = Tk()
window.title("학교 앨범 추출기")
window.geometry('640x600')

label = Label(window, text="라벨테스트", font=("돋음", 10))
label.grid(column=0, row=0)

input_text = Entry(window, width=30)
input_text.grid(column=0, row=2)

button = Button(window, text="확인", command=confirm)
button.grid(column=1, row=2)

window.mainloop()

plus_url = "/jinyang-h/na/ntt/selectNttInfo.do?nttSn=87621512&mi=122187"
next_url = url + plus_url
file = 'C:/Users/xoals/jinyang/image/'
response = requests.get(next_url)
html_text = response.text
soup = bs(response.text, 'html.parser')
next_link = soup.select("li.next")
number = 0
while next_link != []:
    number += 1
    response = requests.get(next_url)
    html_text = response.text
    soup = bs(response.text, 'html.parser')
    next_link = soup.select("li.next")

    title = soup.find(class_ ="title")
    for name in title:
        name = name.strip()
        name = name.replace(" ",'_')
        name = name.replace('"','_')
        name = name.replace(":",'_')
        name = name.replace(".",'_')
        name = name.replace("*",'_')
    newfile = file + f'{number}' + '_' + name 
    print(newfile)
    os.makedirs(newfile)
    link = soup.select("a.photoView")
    count = 0
    for i in link:          ##이미지 다운로드
        print(i)
        count += 1
        imgurl = i.attrs['href']
        urlretrieve(url + imgurl,newfile + '/' + f'{count}.jpg')
                    
    for i in next_link:        ##다음글로 링크 바꾸기
        plus_url = i.find('a')['href']
        next_url = url + plus_url