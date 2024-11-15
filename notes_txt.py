#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QTextEdit, QLineEdit, QListWidget, QButtonGroup, QGroupBox, QApplication, QRadioButton, QHBoxLayout, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
from PyQt5 import QtGui, QtCore
import json

notes = {
    "Добро пожаловать!":{
        "текст": "В этом приложении можно создавать заметки с тегами",

        "теги": ["умные заметки", "инструкция"]
    }
}





app = QApplication([])
main_win = QWidget()

main_win.resize(900, 600)
main_win.setStyleSheet("background-color: rgb(113, 199, 111);")

main_win.setWindowTitle("Умные заметки")

field_text = QTextEdit()
text1 = QLabel("Список заметок")
list_notes = QListWidget()
btn_create = QPushButton("Создать заметку")
btn_delete = QPushButton("Удалить заметку")
btn_save = QPushButton("Сохранить заметку")


text2 = QLabel("Список тегов")

list_tags = QListWidget()
field_tag = QLineEdit()

btn_add = QPushButton("Добавить к заметке")
btn_del_teg= QPushButton("Открепить от заметки")
btn_hide_teg = QPushButton("Искать заметки по тегу")

btn_save.setStyleSheet("background-color: rgb(13, 199, 111);")
btn_create.setStyleSheet("background-color: rgb(13, 199, 111);")
btn_delete.setStyleSheet("background-color: rgb(13, 199, 111);")
btn_add.setStyleSheet("background-color: rgb(13, 199, 111);")
btn_del_teg.setStyleSheet("background-color: rgb(13, 199, 111);")
btn_hide_teg.setStyleSheet("background-color: rgb(13, 199, 111);")



main_line = QHBoxLayout()
line1V = QVBoxLayout()
line2V = QVBoxLayout()

lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()

lineH3 = QHBoxLayout()
lineH4 = QHBoxLayout()


line1V.addWidget(field_text)
line2V.addWidget(text1)
line2V.addWidget(list_notes)

lineH1.addWidget(btn_create)
lineH1.addWidget(btn_delete)
lineH2.addWidget(btn_save)

line2V.addLayout(lineH1)
line2V.addLayout(lineH2)

line2V.addWidget(text2)

line2V.addWidget(list_tags)
line2V.addWidget(field_tag)
lineH3.addWidget(btn_add)
lineH3.addWidget(btn_del_teg)
lineH4.addWidget(btn_hide_teg)


line2V.addLayout(lineH3)
line2V.addLayout(lineH4)
main_line.addLayout(line1V)
main_line.addLayout(line2V)
main_line.addLayout(lineH1)
main_line.addLayout(lineH2)
main_win.setLayout(main_line)

def show_note():
    name = list_notes.selectedItems()[0].text()
    print(name)
    for note in notes:
        if note[0] == name:
            field_text.setText(note[1])
            list_tags.clear()
            list_tags.addItems(note[2])



#добавить заметку

def add_note():
    note_name, result = QInputDialog.getText(main_win, "Добавить заметку","Название заметки:" )
    if result and note_name != "":
        note = []
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tags.addItems(note[2])
        filename = str(len(notes) -1)+".txt"
        with open(filename, "w") as file:
            file.write(note[0]+"\n")




#сохранить заметку
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        i = 0
        for note in notes:
            if note[0] == key:
                note[1] = field_text.toPlainText()
                filename = str(i)+".txt"
                with open(filename, "w") as file:
                    file.write(note[0]+"\n")
                    file.write(note[1]+"\n")
                    for tag in note[2]:
                        file.write(tag+" ")
                    file.write("\n")
        i += 1
       

        

with open("f.json", "r", encoding="utf-8") as file:
    notes = json.load(file)

list_notes.addItems(notes)
btn_save.clicked.connect(save_note)
btn_delete.clicked.connect(del_note)
btn_create.clicked.connect(add_note)
btn_del_teg.clicked.connect(del_tag)
btn_hide_teg.clicked.connect(search_tag)
list_notes.itemClicked.connect(show_note)
btn_add.clicked.connect(add_tag)



main_win.show()
app.exec_()
#затем запрограммируй демо-версию функционала
