# définir chacun votre fonction

def divide(a,b):
	res = float("NaN")
	try:
		res = a / b
	except Exception as e:
		print("Pas de division par zéro")
	
	return res

def soustr (a,b):
	res = a - b
	return res

def multiply(a,b):
	res=a*b	
	return res

if __name__ == '__main__':
	x = 2
	y = 8
	print("la division vaut", divide(x,y))
	print("la multiplication vaut", multiply(x,y))
	print("la soustraction vaut", soustr(x, y))
	print("la division vaut", divide(x,0))
