import sys
sys.version


class Beverage:
	def __init__(self, name, cost, num):
		self.name = name
		self.cost = cost
		self.num = num
		
	#def addBeverage(self):
	"""
	def substractBevarage(self):	
		self.num -= 1
	"""
	
	
class MoneyManager:
	def __init__(self):
		self.money = 0
	
	def addMoney(self, money):	
		self.money += money
		
	def substractMoney(self, money):	
		self.money -= money



class VendingMachine:
	mm = MoneyManager()
	
	def __init__(self):
		self.beverage = [Beverage('Oranc', 500, 5), Beverage('Milkis', 700, 5), Beverage('Sprite', 600, 5), Beverage('Coke', 400, 5), Beverage('Nescafe', 500, 5)]	
		
	def selectBeverage(self):	
		name = int(input("Select Beverage: "))
		
		if name-1 == 0:
			if self.beverage[0].num > 0:
				if self.mm.money >= self.beverage[0].cost:
					print("Here is "+ self.beverage[0].name+"!")
					self.mm.substractMoney(self.beverage[0].cost)
					self.beverage[0].num -= 1		
				else:
					self.orderFail(name)
			else:
				print("Sorry :( There is not enough Oranc.")
					
		elif name-1 == 1:
			if self.beverage[1].num > 0:
				if self.mm.money >= self.beverage[1].cost:
					print("Here is "+ self.beverage[1].name+"!")
					self.mm.substractMoney(self.beverage[1].cost)
					self.beverage[1].num -= 1		
				else:
					self.orderFail(name)
			else:
				print("Sorry :( There is not enough Milkis.")
				
		elif name-1 == 2:
			if self.beverage[2].num > 0:
				if self.mm.money >= self.beverage[2].cost:
					print("Here is "+ self.beverage[2].name+"!")
					self.mm.substractMoney(self.beverage[2].cost)
					self.beverage[2].num -= 1		
				else:
					self.orderFail(name)
			else:
				print("Sorry :( There is not enough Sprite.")
							
		elif name-1 == 3:
			if self.beverage[3].num > 0:
				if self.mm.money >= self.beverage[3].cost:
					print("Here is "+ self.beverage[3].name+"!")
					self.mm.substractMoney(self.beverage[3].cost)
					self.beverage[3].num -= 1		
				else:
					self.orderFail(name)
			else:
				print("Sorry :( There is not enough Coke.")
				
		elif name-1 == 4:
			if self.beverage[4].num > 0:
				if self.mm.money >= self.beverage[4].cost:	
					print("Here is "+ self.beverage[4].name+"!")
					self.mm.substractMoney(self.beverage[4].cost)
					self.beverage[4].num -= 1		
				else:
					self.orderFail(name)
			else:
				print("Sorry :( There is not enough Nescafe.")
		
		else:
			print("You pressed it wrong.")
		
		
	def insertMoney(self):
		money = input("Please enter the money: ")
		self.mm.addMoney(int(money))
		
		
	def returnMoney(self):
		print("Return "+ str(self.mm.money) +"Won.")
		self.mm.money = 0
	
	
	def orderFail(self, name):
		print("There is not enough money :(")
		"""
		print("y: continue the order / n: return the money")
		select = input()
		if select == 'y':
			insertMoney()
			selectBeverage(name)
		else if select == 'n':
			returnMoney()
		else:
			print("You pressed it wrong.")
			
		"""	




vm = VendingMachine()
while True:
	print("\n*----------------------------------------------------------------*")
	print("| 1.Oranc_500 2.Milkis_700 3.Sprite_600 4.Coke_400 5.Nescafe_500 |")
	print("*----------------------------------------------------------------*")
	print("Balance: "+ str(vm.mm.money))
	print("Select Menu: ")
	print("	1.Insert Money")
	print("	2.Select Beverage")
	print("	3.Return money")
	print("If you want to exit enter Ctrl+C")
	select = input()
	
	if select =='1':
		vm.insertMoney()
	elif select =='2':
		vm.selectBeverage()
	elif select =='3':
		vm.returnMoney()
	else:
		print("You pressed it wrong.")

	
