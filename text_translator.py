from tkinter import *
from tkinter.ttk import Combobox
from  tkinter import  messagebox
from textblob import  TextBlob
root = Tk()
root.geometry('500x400')
root.title('Translator')
root.iconbitmap('trans.ico')
root.resizable(False,False)
root.configure(bg='turquoise1')
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
##functions
def click(event=None):
    try:
        word = TextBlob(name.get())
        lang = word.detect_language()
        lang_to_dict = languages.get()
        lang_to = lang_dict[lang_to_dict]
        word = word.translate(from_lang=lang,to=lang_to)
        label3.configure(text=word)
        name1.set(word)
    except:
        name1.set('Try another Keyword')

def main_exit():
    res = messagebox.askyesnocancel('Notification','Are you sure?',parent=root)
    if(res == True):
        root.destroy()

##Binding Functions
def on_enterentry(e):
    entry1['bg'] = 'springgreen'
def on_leaveentry(e):
    entry1['bg'] = 'white'

def on_enterentry2(e):
    entry2['bg'] = 'springgreen'
def on_leaveentry2(e):
    entry2['bg'] = 'white'

def on_enterbtn1(e):
    btn1['bg'] = 'springgreen'
def on_leavebtn1(e):
    btn1['bg'] = 'yellow'

def on_enterbtn2(e):
    btn2['bg'] = 'springgreen'
def on_leavebtn2(e):
    btn2['bg'] = 'yellow'




##Combo Box Languages
languages = StringVar()
font_box =Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)


###Entry Box
name= StringVar()
entry1 = Entry(root,width=30,textvariable=name,font=('times',15,'italic bold'))
entry1.place(x=150,y=40)

name1= StringVar()
entry2 = Entry(root,width=30,textvariable=name1,font=('times',15,'italic bold'))
entry2.place(x=150,y=100)

##Label
label1 = Label(root,text='Enter words : ',font=('times',15,'italic bold'),bg='turquoise1')
label1.place(x=5,y=40)

label2 = Label(root,text='Translated :',font=('times',15,'italic bold'),bg='turquoise1')
label2.place(x=5,y=100)

label3 = Label(root,text='',font=('times',15,'italic bold'),bg='turquoise1')
label3.place(x=10,y=250)

##Buttons

btn1= Button(root,text = 'Click', bd=10, bg='yellow', activebackground='red',width=10,
             font=('times',15,'italic bold'),command=click)
btn1.place(x=70,y=170)

btn2= Button(root,text = 'EXIT', bd=10, bg='yellow', activebackground='red',width=10,
             font=('times',15,'italic bold'),command=main_exit)
btn2.place(x=280,y=170)
root.bind('<Return>',click)

##Binding
entry1.bind('<Enter>',on_enterentry)
entry1.bind('<Leave>',on_leaveentry)

entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)

btn1.bind('<Enter>',on_enterbtn1)
btn1.bind('<Leave>',on_leavebtn1)

btn2.bind('<Enter>',on_enterbtn2)
btn2.bind('<Leave>',on_leavebtn2)


root.mainloop()
