# définir chacun votre fonction

def divide(a,b):
	res = a/b
	return res

def soustr (a,b):
	res = a - b
	return res

if __name__ == '__main__':
	x = 2
	y = 8
	print("la division vaut", divide(x,y))
    print("la soustraction vaut", soustr(x, y))
