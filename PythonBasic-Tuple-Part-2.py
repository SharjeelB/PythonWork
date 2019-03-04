def main() : 
	lstFriends = ("sharjeel", "GOPESH PANDEY", "Rupak")
	print(lstFriends)
	
	#Return the item in position 1
	print(lstFriends[1])
	
	#Tuples are unchangeabl: Once a tuple is created, you cannot change its values. 
	#lstFriends[1] = "AFFAN"
	# The values will remain the same:
	print(lstFriends)
	
	#Use For loop : Iterate through the items and print the values
	for frnd in lstFriends:
		print(frnd)
		
	#To determine how many items a list have, use the len() method
	print(len(lstFriends))
	
	"""Add Items
	#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
	
	lstFriends[3] = "affan" # This will raise an error
	print(lstFriends)
	
	#Remove and Item : The del keyword can delete the tuple completely
	del lstFriends
	print(lstFriends) #this will raise an error because the tuple no longer exists
	
	
	#To execute above section, remove multiline comment (") and run the program
	"""
	
	#The tuple() Constructor : Using the tuple() method to make a tuple
	
	lstFriends = tuple(("sharjeel", "gopesh", "affan")) # note the double round-brackets
	print(lstFriends)
	
	"""
	Searches the tuple for a specified value and returns the position of where it was found
	Definition and Usage
	The index() method finds the first occurrence of the specified value.
	The index() method raises an exception if the value is not found."""
	
	friendName = lstFriends.index("gopesh")
	print(friendName)

	
main()
