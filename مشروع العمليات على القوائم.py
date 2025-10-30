#Create libraries

list_books = []
hiswish_list = []

#Create a mini for the first book

your_book = input("Enter your book name. :\n ")
list_books.append(your_book)

#Create a mini for second book

your_book_2 = input ("Enter your other book name(or preas 'enter' to skip)\n")

#Check the entry of a book

if your_book_2 :
	list_books.append(your_book_2)
	print(f"your Library is {list_books}")
else :
	print("")
	print(f"the your list books {list_books}")

#Variable for the first wish book

fut_book = input ("Enter the name of a book you want to get in the future :\n")

hiswish_list .append(fut_book)


#Variable for the second wish book

fut_book_2 = input("Enter the name of another book yourself, answer the future : (or preas 'enter' to skip)\n")

#Check the entry of  wish book

if fut_book_2 :
	hiswish_list.append(fut_book_2)
	print(f"your hiswish list is {hiswish_list}" )

else :
	print (fut_book_2)
	print(f"your hiswish list is {hiswish_list}" )

#Variable to save the book he got.

get = input("Enter the name of a book you got from the wish list ( or press enter for planning ) \n ")

#Check the writing of the wish book and who is in the wish list

if get :
	if get in hiswish_list :
			list_books.append(get)
			hiswish_list.remove(get)
			print(f"your update library is {list_books}")
			print(f"your update hiswise list is {hiswish_list}")
	

	else :
			print (f"your {get} not in the hiswish list ")
else :
	print (f"your library is {list_books}")
	print(f"your hiswish list is {hiswish_list}")
	
#Create variable donation

Donate = input("Get in the name of your Library. you want to donate it : \n")

#Check the entry of the donation book and who is in the book list

if Donate :
	if Donate in list_books :
		list_books.remove(Donate)
		print(f"your library after donate is {list_books}")
	else :
		print(f"the {Donate} not in the list ")
else :
	print (f"your libaray is {list_books}")

