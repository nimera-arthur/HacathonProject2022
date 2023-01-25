from bd import add
import tkinter as tk
result = add()

# window = tk.Tk()
# window.title("6 Вопросов")
# window.geometry("500x150")
# score = 0
# def inst():
#     t = tk.Label(window, text="Все что вам нужно это ответить 1, 2, 3")
#     t.pack()
#
#
# def start():
#     def submit():
#         print (ans.get())
#
#
# greet = tk.Label(window, text="Добро пожаловать в наш тест")
# greet.pack()
# startButton = tk.Button(window, command=start, text="Старт")
# startButton.pack()
# instr = tk.Button(window, text="Инструкции", command=inst)
# instr.pack()
# end = tk.Button(window, text="Выход", command=window.destroy)
# end.pack()






q_list = []
for el in result:
	if isinstance(el, tuple):
		#print(el, type(el))
		q = [el[1], el[3]]
		letters = ['a', 'b', 'c', 'd']
		ans_list = el[2].split(';')
		d = {letters[ind]: ans_list[ind] for ind in range(len(ans_list))}
		# for key, value in d.items():
		# 	if value == q[1]:
		# 		q[1] = key
		q.append(d)
		q_list.append(q)


from tkinter import *
class TestQuestion: # класс Тестовый вопрос
	def __init__(self,text,correct_variant,variant_of_ansver):
		self.text = text # текст вопроса
		self.correct_variant = correct_variant # правильный вариант
		self.variant_of_answer= variant_of_ansver # варианты ответа

class Test: # класс Тест
	def __init__(self,title='test',test_question_list = []):
		self.title = title # название теста
		self.test_question_list = test_question_list # список тестовых вопросов
		self.total_questions = len(test_question_list) # количество вопросов в тесте

class TestInterface: # интерфейс для теста
	def __init__(self,test):
		self.root = Tk() # основное окно
		self.root.title(test.title) # надпись вверху окна
		self.root.geometry("500x500")# геометрия окна
		self.font = "Arial 18 bold"# шрифт виджетов
		self.lbl_text = StringVar()# переменная lbl
		self.lbl_text.set("для начала теста нажмите 'начать'")
		self.lbl = Label(textvariable=self.lbl_text,font = self.font,wraplength =300)
		self.lbl.pack(side=TOP)#расположение вверху окна
		self.checkbtn_list =[] #список галочек
		self.score = 0 #счет
		self.variant = StringVar() # вариант ответа выбранный пользователем
		self.variant.set(0) # вариант не выбран
		self.n = 0 # счетчик шагов
		self.lbl_checked = Label(font = "Arial 18 bold") # lbl который пишет Правильно\ неправильно
		self.lbl_checked.pack(side=BOTTOM) # внизу окна
		self.btn = Button(text="начать",font = "Arial 16 bold", command=self.change_lbl_text) # кнопка
		self.btn.pack(side=BOTTOM) #
		self.root.mainloop() #обновление окна
	def change_lbl_text(self): #изменение текста верхнего lbl
		if self.n< test.total_questions:# если число шагов меньше количества вопросов в тесте:
			self.btn.config(text="следующий>>", state=DISABLED,command = self.next_quest) #кнопка меняет текст и тд...
			self.lbl_text.set("Задача № {}\n{}".format(self.n+1,test.test_question_list[self.n].text)) # меняется текст лейбла
			self.set_check_btn()# метод установки галочек
			self.lbl_checked.config(text="\nНабрано баллов: {}".format(self.score)) # изменяется текст другог лейбла
		else:
			print("вопросы закончились") # чтобы понять что вопросы кончились
			self.end() # метод конец
	def set_check_btn(self): #метод установки галочек
		for key,value in test.test_question_list[self.n].variant_of_answer.items(): # для ключ,значение присвоить ключ,значение из каждого варианта ответа тестового вопроса
			ch =Checkbutton(text ="{}) {}".format(key,value),font = "Arial 12 bold",onvalue =key,variable =self.variant,command = self.checked)# создает галочку
			ch.pack() # прикручивает к окну
			self.checkbtn_list.append(ch) # добавляет в список галочек
	def remove_check_btn(self): # метод удаляет галочки с окна
		if self.checkbtn_list: # если список не пустой
			for ch in self.checkbtn_list: # каждую галочку
				ch.destroy() # убирает с окна
			self.checkbtn_list.clear() # очищает список
	def change_check_btn(self):# метод изменяет свойства галочек
		for ch in self.checkbtn_list:
			ch.config(state=DISABLED) #отключает
			if ch["onvalue"] == test.test_question_list[self.n].correct_variant: # если правильный вариант
				ch.config( disabledforeground="#000", bg="#0f0") # зеленый
			elif ch["onvalue"]== self.variant.get():# иначе
				ch.config(disabledforeground="#000", bg="#f00") # красный
	def checked(self): # проверка варианта с вариантом ответа
		if self.variant.get() == test.test_question_list[self.n].correct_variant: # если сходится
			self.score+=1  #прибавлет балл
			self.btn.config(state = NORMAL) #делает кнопку активной
			self.lbl_checked.config(text="Правильно\nНабрано баллов: {}".format(self.score))#изменяет лейбл
		else:
			self.lbl_checked.config(text="Вы ошиблись\nНабрано баллов: {}".format(self.score))#изменяет лейбл
			self.btn.config(text ="Попробовать снова",command = self.reset,state = NORMAL)# изменяет свойства кнопки
		self.change_check_btn() # изменяет цвет галочки
	def reset(self): # обнуляет переменные в начальное положение
		self.n = 0
		self.score = 0
		self.variant.set(0)
		self.remove_check_btn()
		self.lbl_text.set("для начала теста нажмите 'начать'")
		self.lbl_checked.config(text='')
		self.btn.config(text="начать", command=self.change_lbl_text)
	def next_quest(self): # следующий шаг
		self.n+=1
		self.variant.set(0)# обнуляет вариант ответа
		self.remove_check_btn()# удаляет старые галки
		self.change_lbl_text() # изменяет лейбл на следующий вопрос
	def end(self): # титры в конце
		self.remove_check_btn()
		self.lbl_checked.config(text="Тест пройден.Вы свободны\nНабрано баллов: {}".format(self.score))
		self.lbl_text.set("Вопросы закончились")
		self.btn.config(text="Пройти тест снова", command=self.reset)

test_question_list=[]

for q in q_list:
	test_question_list.append(TestQuestion(q[0], q[1], q[2]))
	#print(q, 'check')


# test_question_list.append(TestQuestion("x+2=4", 'a', {'a': 'x=2', 'b': 'x=4', 'c': 'x=3', 'd': 'x=9'}))
# test_question_list.append(TestQuestion("2+2*2", 'b', {'a': '8', 'b': '6'}))
# test_question_list.append(TestQuestion("2+2*2", 'b', {'a': '8', 'b': '6'}))
test = Test("тест по высшей математике",test_question_list) #  класс тест принимает на вход список из тестовыйх вопросов
TestInterface(test) # интерфейс принимает тест
test_question_list  # класс тест принимает на вход список из тестовыйх вопросов
TestInterface(test)  # интерфейс принимает тест



