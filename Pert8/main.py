from phone import Phone
from keyboard import Keyboard

merek_Hp = input("Masukkan Merek Hp: ")
merek_Keyboard = input("Masukkan Merek Keyboard: ")

item1 = Keyboard(merek_Keyboard, 1000, 3)
item2 = Phone(merek_Hp, 2000000, 2)
item1.apply_discount()
print(item2.name)
print(item1.price)