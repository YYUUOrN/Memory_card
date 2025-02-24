from random import choice, shuffle   
from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget
from time import sleep
from style import *

app = QApplication([])

app.setStyleSheet(style)

from main_window import *
from menu_window import *

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Наступне питання")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Відповісти")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def check_result():
    correct = answer.isChecked()
    if correct:
        lb_result.setText(text_correct)
        cur_q.got_right()
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            lb_result.setText(text_wrong)
            cur_q.got_wrong()
            show_result()

def click_OK():
    if btn_ok.text() == 'Відповісти':
        check_result()
        lb_result.show()
        show_result()
    else:
        new_question()
        show_question()

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.attempts = 0
        self.correct = 0

    def got_right(self):
        self.attempts += 1
        self.correct += 1
    
    def got_wrong(self):
        self.attempts += 1

q1 = Question("Яблуко", "Apple", "Application", "Building", "caterpillar")
q2 = Question("Кіт", "Cat", "Dog", "Mouse", "Elephant")
q3 = Question("Машина", "Car", "Bike", "Plane", "Ship")
q4 = Question("Книга", "Book", "Pen", "Pencil", "Ruler")

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_correct.setText(cur_q.answer)
    answers = [cur_q.answer, cur_q.wrong_answer1, cur_q.wrong_answer2, cur_q.wrong_answer3]
    shuffle(answers)

    for btn, text in zip(radio_buttons, answers):
        btn.setText(text)

new_question()
show_question()
btn_ok.clicked.connect(click_OK)

def rest():
    win_card.hide()
    n = btn_minutes.value() * 60
    sleep(n)
    win_card.show()

btn_sleep.clicked.connect(rest)

def show_menu():
    win_card.hide()
    menu_win.show()

btn_menu.clicked.connect(show_menu)

def hide_menu():
    menu_win.hide()
    win_card.show()

btn_back.clicked.connect(hide_menu)

def clear():
    for line_edit in [line_quest, line_right_ans, line_wrong1_ans, line_wrong2_ans, line_wrong3_ans]:
        line_edit.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(line_quest.text(), line_right_ans.text(), line_wrong1_ans.text(), line_wrong2_ans.text(), line_wrong3_ans.text())
    questions.append(new_q)
    clear()

btn_add_quest.clicked.connect(add_question)

def show_stat():
    if cur_q.attempts == 0:
        c = 0
    else:
        c = (cur_q.correct / cur_q.attempts * 100)

    text = f'Разів відповіли: {cur_q.attempts}\n ' \
           f'Правильних відповідей: {cur_q.correct}\n ' \
           f'Відсоток правильних відповідей: {c:.2f}%'

    lb_statistic.setText(text)
    menu_win.show()
    win_card.hide()

app.exec_()
