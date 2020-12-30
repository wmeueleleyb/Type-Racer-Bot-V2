from bs4 import BeautifulSoup
import keyboard, time, pyperclip

time.sleep(9)
keyboard.press_and_release("ctrl+shift+i")
time.sleep(1)
keyboard.press_and_release("left arrow, left arrow, left arrow")
time.sleep(0.5)
keyboard.press_and_release("shift+f10")
time.sleep(0.5)
keyboard.press_and_release("down arrow, down arrow")
time.sleep(0.2)
keyboard.press_and_release("enter")
time.sleep(0.2)
keyboard.press_and_release("ctrl+a, ctrl+c")
time.sleep(0.2)
keyboard.press_and_release("ctrl+shift+i")
time.sleep(3)
html = pyperclip.paste()

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table' , {'class' : 'inputPanel'})
div = table.find_all('div')
counter = 0
marks = []
Div = str(div[0])
for i in Div:
    if i == '<' or i == '>':
        marks.append(counter)
    counter += 1

text = Div[marks[5]+1]+Div[marks[9]+1:marks[10]]+Div[marks[13]+1:marks[14]]
print(text)
for i in text:
    if i in ['<','>','?',':','"','{','}','|','+','_',')','(','*','&','^','%','$','@','!','~'] or i.isupper():
        keyboard.press_and_release('shift+'+i)
    else:    
        keyboard.press_and_release(i)
    time.sleep(0.1)
    
