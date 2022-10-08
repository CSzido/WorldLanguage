import Interpreter

while True:
	text = input('World >> ')
	result, error = Interpreter.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)
