def main() : 
	employeeName=" sharjeel-bilali "
	#Get the character at position 3 (remember that the first character has the position 0)
	print("character at position 3 is : " + employeeName[3])
	
	#Substring. Get the characters from position 2 to position 5 (not included)
	print("characters from position 2 to position 6 are : " + employeeName[2:6])
	
	#The strip() method removes any whitespace from the beginning or the end
	print("removes any whitespace from the beginning or the end : " + employeeName.strip()) 
	
	#The len() method returns the length of a string
	print("length of a string is : ", len(employeeName))
	
	#The lower() method returns the string in lower case
	print("string in lower case : " + employeeName.lower())
	
	#The upper() method returns the string in upper case
	print("string in upper case : " +  employeeName.upper())
	
	#The replace() method replaces a string with another string
	print("replaces a string with another string : " + employeeName.replace("e", "a"))
	
	#The split() method splits the string into substrings if it finds instances of the separator
	print(" splits the string into substrings if it finds instances of the separator : ",  employeeName.split("-"))
	
main()