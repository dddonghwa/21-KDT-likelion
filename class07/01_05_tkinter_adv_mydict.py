'''
data = 한국보건의료인 국가시험원 용어
단어를 입력 후 검색 버튼을 누르면 대분류/중분류/영어표기/정의가 검색됩니다.
'''

from tkinter import *
import pandas as pd


def click():
    word = entry.get()
    output1.delete(0, END)
    output2.delete(0, END)
    output3.delete(0, END)
    output4.delete(0.0, END)

    try:
        class1 = data.loc[data['용어'] == word, '대분류'].values[0]
        class2 = data.loc[data['용어'] == word, '중분류'].values[0]
        eng = data.loc[data['용어'] == word, '영어 표기'].values[0]
        def_word = data.loc[data['용어'] == word, '정의'].values[0]
        # print(class1, class2, eng, def_word)
    except:
        class1 = class2 = eng = ""
        def_word = "단어를 찾을 수 없습니다."

    output1.insert(END, class1)
    output2.insert(END, class2)
    output3.insert(END, eng)
    output4.insert(END, def_word)
    pass

data = pd.read_csv("publicdata.csv")
# print(data)

window = Tk()
window.title("한국보건의료인국가시험원 용어사전")

label = Label(window, text="한국보건의료인국가시험원 용어사전입니다.\n원하는 단어를 입력 후, 검색 버튼을 눌러주세요.")
label.grid(row=0, column=0, sticky=W)

entry = Entry(window,width=15, bg='light green')
entry.grid(row=1, column=0, sticky=W) # 위치

bnt = Button(window, text="검색", command=click)
bnt.grid(row=2, column=0, sticky=W)

class1 = Label(window, text="대분류 : ")
class1.grid(row=3, column=0, sticky=W )
output1 = Entry(window, bg='light green')
output1.grid(row=4, column=0, sticky=W) # 위치

class2 = Label(window, text="중분류 : ")
class2.grid(row=5, column=0, sticky=W)
output2 = Entry(window, bg='light green')
output2.grid(row=6, column=0, sticky=W)

eng = Label(window, text="영어표기 : ")
eng.grid(row=7, column=0, sticky=W)
output3 = Entry(window, bg='light green')
output3.grid(row=8, column=0, sticky=W)

desc = Label(window, text='정의 : ')
desc.grid(row=9, column=0, sticky=W)
output4 = Text(window, width=50, height=6, wrap=WORD, background="light green")
output4.grid(row=10, column=0, columnspan=2, sticky=W)


window.mainloop()




