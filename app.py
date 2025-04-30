import os
cls = lambda:os.system("cls")
cls()
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.core.window import Window as win


class calculator(App):
	def build(self):
		win.size =  (300,300)
		win.minimum_width = 300
		win.minimum_height = 300

		container = GridLayout(cols=1)
		more_btns = GridLayout(cols=10)
		btns_container = GridLayout(cols=4)
		

		# more btns
		cancel_btn = Image(source="images/prev.png", size_hint=(0.4,0.4))

		self.calc_input = TextInput(hint_text="enter:", size_hint=(0.6,None), multiline=False)

		# btns container
		btn_one = Button(text="1", size_hint=(0.4,0.4))
		btn_one.bind(on_press=self.click_one)

		btn_two = Button(text="2", size_hint=(0.4,0.4))
		btn_two.bind(on_press=self.click_two)

		btn_three = Button(text="3", size_hint=(0.4,0.4))
		btn_three.bind(on_press=self.click_three)

		btn_four = Button(text="+", size_hint=(0.4,0.4))
		btn_four.bind(on_press=self.click_four)

		btn_five = Button(text="4", size_hint=(0.4,0.4))
		btn_five.bind(on_press=self.click_five)

		btn_six = Button(text="5", size_hint=(0.4,0.4))
		btn_six.bind(on_press=self.click_six)

		btn_seven = Button(text="6", size_hint=(0.4,0.4))
		btn_seven.bind(on_press=self.click_seven)

		btn_eight = Button(text="-", size_hint=(0.4,0.4))
		btn_eight.bind(on_press=self.click_eight)

		btn_nine = Button(text="7", size_hint=(0.4,0.4))
		btn_nine.bind(on_press=self.click_nine)

		btn_ten = Button(text="8", size_hint=(0.4,0.4))
		btn_ten.bind(on_press=self.click_ten)

		btn_eleven = Button(text="9", size_hint=(0.4,0.4))
		btn_eleven.bind(on_press=self.click_eleven)

		btn_twelve = Button(text="*", size_hint=(0.4,0.4))
		btn_twelve.bind(on_press=self.click_twelve)


		btn_o1 = Button(text="%", size_hint=(0.4,0.4))
		btn_o1.bind(on_press=self.click_o1)

		btn_o2 = Button(text="^", size_hint=(0.4,0.4))
		btn_o2.bind(on_press=self.click_o2)

		btn_o3 = Button(text="°", size_hint=(0.4,0.4))
		btn_o3.bind(on_press=self.click_o3)

		btn_o4 = Button(text="=", size_hint=(0.4,0.4))
		btn_o4.bind(on_press=self.click_o4)

		# add wigdets to btns.container
		btns_container.add_widget(btn_one)
		btns_container.add_widget(btn_two)
		btns_container.add_widget(btn_three)
		btns_container.add_widget(btn_four)
		btns_container.add_widget(btn_five)
		btns_container.add_widget(btn_six)
		btns_container.add_widget(btn_seven)
		btns_container.add_widget(btn_eight)
		btns_container.add_widget(btn_nine)
		btns_container.add_widget(btn_ten)
		btns_container.add_widget(btn_eleven)
		btns_container.add_widget(btn_twelve)

		btns_container.add_widget(btn_o1)
		btns_container.add_widget(btn_o2)
		btns_container.add_widget(btn_o3)
		btns_container.add_widget(btn_o4)

		#more_btns.add_widget(cancel_btn)


		container.add_widget(self.calc_input)
		container.add_widget(btns_container)
		# container.add_widget(more_btns)

		return container

	# button functionalities
	def click_one(self, instance):
		self.calc_input.text = self.calc_input.text + "1"

	def click_two(self, instance):
		self.calc_input.text = self.calc_input.text + "2"

	def click_three(self, instance):
		self.calc_input.text = self.calc_input.text + "3"

	def click_four(self, instance):
		self.calc_input.text = self.calc_input.text + "+"

	def click_five(self, instance):
		self.calc_input.text = self.calc_input.text + "4"

	def click_six(self, instance):
		self.calc_input.text = self.calc_input.text + "5"

	def click_seven(self, instance):
		self.calc_input.text = self.calc_input.text + "6"
		print("added: 2")

	def click_eight(self, instance):
		self.calc_input.text = self.calc_input.text + "-"

	def click_nine(self, instance):
		self.calc_input.text = self.calc_input.text + "7"

	def click_ten(self, instance):
		self.calc_input.text = self.calc_input.text + "8"

	def click_eleven(self, instance):
		self.calc_input.text = self.calc_input.text + "9"

	def click_twelve(self, instance):
		self.calc_input.text = self.calc_input.text + "*"

	def click_o1(self, instance):
		self.calc_input.text = self.calc_input.text + "%"

	def click_o2(self, instance):
		self.calc_input.text = self.calc_input.text + "^"

	def click_o3(self, instance):
		self.calc_input.text = self.calc_input.text + "°"


	def click_o4(self, instance):
		import fun
		text = str(self.calc_input.text)
		if fun.char_detector(text) == "+":
			try:
				sp = text.split("+")
				calc = sum(map(int, sp))
				self.calc_input.text=str(calc)
			except:
				self.calc_input.text="ValueError:E"
		elif fun.char_detector(text) == "-":
			try:
				calc = fun.sub(text)
				self.calc_input.text=calc
			except:
				self.calc_input.text="ValueError:E"
		
		print("answer:",text)


if __name__ == "__main__":
	calculator().run()