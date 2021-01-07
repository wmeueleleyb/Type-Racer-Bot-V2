from bs4 import BeautifulSoup
import keyboard, time, pyperclip

time.sleep(10)
keyboard.press_and_release("ctrl+shift+i")
time.sleep(0.5)
keyboard.press_and_release("left arrow, left arrow, left arrow")
time.sleep(0.3)
keyboard.press_and_release("shift+f10")
time.sleep(0.3)
keyboard.press_and_release("down arrow, down arrow")
time.sleep(0.2)
keyboard.press_and_release("enter")
time.sleep(0.2)
keyboard.press_and_release("ctrl+a, ctrl+c")
time.sleep(0.2)
keyboard.press_and_release("ctrl+shift+i")
time.sleep(2)

html = pyperclip.paste()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table' , {'class' : 'inputPanel'})
div = table.find_all('div')
Div = str(div[0])
text1 = []
flag = 0

for i in Div:
    if i == '>': flag = 1
    elif i == '<': flag = 0
    if flag == 1: text1.append(i)
    else: continue

text2 = ''.join(i for i in text1 if i != '>')

for i in text2:
    if i in ['<','>','?',':','"','{','}','|','+','_',')','(','*','&','^','%','$','@','!','~'] or i.isupper():
        keyboard.press_and_release('shift+'+i)
    else:    
        keyboard.press_and_release(i)
    time.sleep(0.1)
