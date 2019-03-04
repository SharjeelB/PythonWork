def main() : 
	#Create a set
	lstOrganizations = {"sharjeelswork", "Fiserv", "R Systems"}
	print(lstOrganizations) # Sets are unordered, so the items will appear in a random order.
	
	"""Access Items
	You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
	But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword."""
	
	#Loop through the set, and print the values
	for organization in lstOrganizations:
	  print(organization)

	#Check if "banana" is present in the set
	print("gopesh" in lstOrganizations)
	
	"""Change Items
	Once a set is created, you cannot change its items, but you can add new items.
	Add Items
		To add one item to a set use the add() method.
		To add more than one item to a set use the update() method."""
	
	lstOrganizations.add("nashit")
	print(lstOrganizations)
	
	lstOrganizations.update(["Edynamic", "Sitecore"])
	print(lstOrganizations)
	
	#Get the number of items in a set
	print(len(lstOrganizations))
	
	#Remove Item : To remove an item in a set, use the remove(), or the discard() method.
	lstOrganizations.remove("nashit") #If the item to remove does not exist, remove() will raise an error.
	print(lstOrganizations)
	
	#To remove an item, use discard
	lstOrganizations.discard("Sitecore") #If the item to remove does not exist, discard() will NOT raise an error.
	print(lstOrganizations)

	"""You can also use the pop(), method to remove an item, but this method will remove the last item. 
	Remember that sets are unordered, so you will not know what item that gets removed. 
	The return value of the pop() method is the removed item."""
	removedItem = lstOrganizations.pop()
	print(removedItem)
	print(lstOrganizations)
	
	#The clear() method empties the set
	lstOrganizations.clear()
	
	#The del keyword will delete the set completely
	del lstOrganizations
	
	#The set() Constructor : It is also possible to use the set() constructor to make a set.
	lstOrganizations = set(("sharjeelswork", "Fiserv", "R Systems")) # note the double round-brackets
	print(lstOrganizations)
	
	
main()
