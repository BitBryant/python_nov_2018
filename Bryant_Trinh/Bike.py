class bike:
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
		miles = 0

	def displayinfo(self):
		print("$" + self.price)
		print(self.max_speed)
		print(abs(self.miles) + "miles")

	def ride(self):
		print("Riding")
		self.miles+=10
		return self

	def reverse(self):
		print("Reversing")
		self.mile-=5
		return self

bike1 = bike(220,"30 MPH")
bike2 = bike(100,"20 MPH")
bike3 = bike(300,"40 MPH")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()

#To prevent instance from having negative miles whenever we print we put the value inside of an abs() for absolute value.
#return self is only applicable to ride and reverse methods
