#Treasure island project
#Print a welcome message
print("""


░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ███╗░░░███╗██╗░░░██╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ████╗░████║╚██╗░██╔╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ██╔████╔██║░╚████╔╝░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██║╚██╔╝██║░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░╚═╝░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝░░░╚═╝░░░

██╗░██████╗██╗░░░░░░█████╗░███╗░░██╗██████╗░░░░
██║██╔════╝██║░░░░░██╔══██╗████╗░██║██╔══██╗░░░
██║╚█████╗░██║░░░░░███████║██╔██╗██║██║░░██║░░░
██║░╚═══██╗██║░░░░░██╔══██║██║╚████║██║░░██║░░░
██║██████╔╝███████╗██║░░██║██║░╚███║██████╔╝██╗
╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝
""")
 #Create a variable to save user selection
door = input("you have a 3 door : green door , red door , black door , Choose one \n").lower()
#Check user selection
if door == "green" :
	print("good Selection ")
#Create a new blender for new values
	boxe = input("now you have a 3 boxe : white boxe , blue boxe , pink boxe . choose one \n").lower()
#Check again from user selection
	if boxe == "blue" :
		print (" Bad choice . he opened the crocodile box 🐊. ")
	elif boxe == "pink" :
		print ("Bad choice . he opened the snakes box 🐍.")
	elif boxe == "white" :
		print ("Pick a concise. you found the treasure 💰🎉.")
	else :
		print (f"Your choice {boxe} is not on the list ❌.")
elif door == "red" :
	print ("Wrong door. You fell into fire 🔥.")
elif door == "black" :
	print ("Wrong test. you opened the Wolf 🐺 door.")
else :
	print (f"your choice {door} is not on the list.")