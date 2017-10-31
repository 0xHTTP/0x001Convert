import sys, math
def byte(decimal) :
	return int(math.log(decimal, 2)) + 1
def main() :
	# Asks user for a decimal number
	decimal = input("Type a decimal/integer: ")
	dec = decimal
	#Converts decimal to Hex
	hexa = hex(dec)
	#Converts deimal to binary
	binary = "{0:b}".format(dec)
	print("Decimal: ", dec)
	print("Hexadecimal: ", hexa)
	print("Binary", binary)
	a = byte(dec) # This links the dec variable, to the byte function which states how big the input is in Bits
	print("Size of number typed: ", a, " Bits")
	#Above, just displays the coonverted values of the decimal you typed, below just stops the program so that you can see the results
	end = raw_input("This was programmed in only 19 lines of code!!!! Hit any key to exit: ")
main()