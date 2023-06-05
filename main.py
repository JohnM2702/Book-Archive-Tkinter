from tkinter import *
import tkinter as tk
from datetime import datetime, date
import pickle
from PIL import Image

#classes and functions________________________________________________________________________________________________
class Book(object):
	def __init__(self, series, title, author, pages, dateFinished):
		self.series = series
		self.title = title
		self.author = author
		self.pages = pages
		self.dateFinished = dateFinished

#adding option functions
def add_book_actual():
	add = Toplevel()
	add.configure(bg='black')
	add.geometry("904x620")

	window_title = Label(add, text="Add Book", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	inquiry_label = Label(add, text="Is it a standalone book or a book from a series? Choose your option.", fg="#04c1de", bg="black", font=("Helvetica 10 italic"))
	standalone_mode = Button(add, text="Standalone", command=lambda: add_book(0, 2, add))
	series_mode = Button(add, text="From a Series", command=lambda: ab_series_mode(add))

	window_title.grid(row=0, column=0, padx=350, pady=10)
	inquiry_label.grid(row=1, column=0, padx=100, sticky="w")
	standalone_mode.grid(row=2, column=0, pady=10)
	series_mode.grid(row=3, column=0, pady=10)
def ab_series_mode(window):
	for widget in window.winfo_children():
		widget.destroy()

	window_title = Label(window, text="Add Book", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	ask_series_title = Label(window, text="Find the series on the database", fg="#04c1de", bg="black", font=("Helvetica 10 italic"))
	ask_series = Text(window, bg="white", fg="black", border=5, height=1, width=20)
	ask_series_button = Button(window, text="Enter", command=lambda: ab_series_mode2(window, ask_series))

	window_title.grid(row=0, column=0, padx=350, pady=30)
	ask_series_title.grid(row=1, column=0)
	ask_series.grid(row=2, column=0)
	ask_series_button.grid(row=3, column=0, pady=20)
def ab_series_mode2(window, textbox):
	response = textbox.get("1.0","end-1c")
	with open ('book_record.pkl', 'rb') as inp:
		my_list = pickle.load(inp)

	i=0
	for book in my_list:
		if response.lower() == book.series.lower():
			add_book(i, 1, window)
			print(str(i)+response+book.series)
			return
		i += 1
	series_status = Label(window, text="Series is not yet recorded in database. Do you want to add it?")
	yes_button = Button(window, text="Yes", command= lambda: add_book(0, 0, window))
	fail_button = Button(window, text="Back to Menu", command=window.destroy)

	series_status.grid(row=3, column=0)
	yes_button.grid(row=4, column=0)
	fail_button.grid(row=5, column=0)

def add_book(i, mode, add):
	for widget in add.winfo_children():
		widget.destroy()

	#define buttons and inout boxes
	window_title = Label(add, text="Add Book", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	label_series = Label(add, text="Series: ", fg="white", bg="black", font = "Helvetica 10 bold italic")
	label_title = Label(add, text="Title: ", fg="white", bg="black", font = "Helvetica 10 bold italic")
	label_author = Label(add, text="Author: ", fg="white", bg="black", font = "Helvetica 10 bold italic")
	label_pages = Label(add, text="Pages: ", fg="white", bg="black", font = "Helvetica 10 bold italic")
	label_df = Label(add, text="Date Finished: ", fg="white", bg="black", font = "Helvetica 10 bold italic")
	inp_series = Text(add, bg="white", fg="black", border=5, height=1, width=20)
	inp_title = Text(add, bg="white", fg="black", border=5, height=1, width=20)
	inp_author = Text(add, bg="white", fg="black", border=5, height=1, width=20)
	inp_pages = Text(add, bg="white", fg="black", border=5, height=1, width=20)
	inp_df = Text(add, bg="white", fg="black", border=5, height=1, width=20)
	sub_button = Button(add, text="Add to Record", fg="black", bg="gold", command= lambda: collect_book(add, inp_series, inp_title, inp_author, inp_pages, inp_df, mode))
	add_exit = Button(add, text="Back to Menu", command=add.destroy)

	if mode == 1:
		with open('book_record.pkl', 'rb') as inp:
   			my_list = pickle.load(inp)

		j=0
		for book in my_list:
			if i == j:
				print(str(i)+str(j)+book.series+book.author)
				inp_series.insert(INSERT, book.series)
				inp_author.insert(INSERT, book.author)
				break
			j += 1
		
	#display buttons and input boxes
	window_title.grid(row=0, column=0, columnspan=2, pady=15, padx=320)
	if mode != 2:
		label_series.grid(row=1,column=0)
		inp_series.grid(row=1, column=1, pady=5)

	label_title.grid(row=2,column=0)
	label_author.grid(row=3,column=0)
	label_pages.grid(row=4,column=0)
	label_df.grid(row=5,column=0)
	inp_title.grid(row=2, column=1, pady=5)
	inp_author.grid(row=3, column=1, pady=5)
	inp_pages.grid(row=4, column=1, pady=5)
	inp_df.grid(row=5, column=1, pady=5)
	sub_button.grid(row = 6, column=0, pady=5, columnspan=2)
	add_exit.grid(row=9, column=0, pady=5, columnspan=2)
def collect_book(add, inp_series, inp_title, inp_author, inp_pages, inp_df, mode):

	#collecting data and storing
	with open('book_record.pkl', 'rb') as inps:
		my_list = pickle.load(inps)

	if mode != 2:
		b_series = inp_series.get("1.0","end-1c")
	else:
		b_series = "N/A"
	b_title = inp_title.get("1.0","end-1c")
	b_author = inp_author.get("1.0","end-1c")
	b_pages = inp_pages.get("1.0","end-1c")
	b_df = inp_df.get("1.0","end-1c")

	for book in my_list:
		if book.title.lower() == b_title.lower():
			label_status = Label(add, text="Book already exist in the record.", fg="red", bg="black", font="Helvetica 10 bold")
			label_status.grid(row = 7, column=0, columnspan=2)
			add_another = Button(add, text="Add Another Book", fg="black", bg="gold", command= lambda: add_another_book(add)) 
			add_another.grid(row=8, column=0, pady=5, columnspan=2)
			return

	my_book = Book(b_series, b_title, b_author, b_pages, b_df)
	my_list.append(my_book)

	with open('book_record.pkl', 'wb') as outp:
		pickle.dump(my_list, outp, pickle.HIGHEST_PROTOCOL)

	#post collection
	label_status = Label(add, text="Successfully added to database.", fg="green", bg="black", font="Helvetica 10 bold")
	label_status.grid(row = 7, column=0, columnspan=2)
	add_another = Button(add, text="Add Another Book", fg="black", bg="gold", command= lambda: add_another_book(add)) 
	add_another.grid(row=8, column=0, pady=5, columnspan=2)
def add_another_book(add):
	for widget in add.winfo_children():
		widget.destroy()

	window_title = Label(add, text="Add Book", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	inquiry_label = Label(add, text="Is it a standalone book or a book from a series? Choose your option.", fg="#04c1de", bg="black", font=("Helvetica 10 italic"))
	standalone_mode = Button(add, text="Standalone", command=lambda: add_book(0, 2, add))
	series_mode = Button(add, text="From a Series", command=lambda: ab_series_mode(add))

	window_title.grid(row=0, column=0, padx=350, pady=10)
	inquiry_label.grid(row=1, column=0, padx=100, sticky="w")
	standalone_mode.grid(row=2, column=0, pady=10)
	series_mode.grid(row=3, column=0, pady=10)

#statistics option functions
def statistics():
	stat = Toplevel()
	stat.configure(bg='black')
	stat.geometry("904x620")

	#time and date
	today = date.today()
	now = datetime.now()
	dt_string = now.strftime("%H:%M:%S")

	#setting up datas
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	f = 0
	with open('book_record.pkl', 'rb') as inp:
   		my_list = pickle.load(inp)


	for book in my_list:
		num = len(book.dateFinished)-4
		if book.dateFinished[num:] == "2021":
			a += 1
		elif book.dateFinished[num:] == "2020":
			b += 1
		elif book.dateFinished[num:] == "2019":
			c += 1
		elif book.dateFinished[num:] == "2018":
			d += 1

		if book.series == "N/A":
			e += 1
		else: 
			f += 1

	#defining the content
	window_title = Label(stat, text="Book Stats", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	start_up_label = Label(stat, text="As of " + today.strftime("%B %d, %Y")+", "+ dt_string + ", the recorded total number of books you've read is  "+ str(len(my_list)), fg="white", bg="black", font=("Times", 15))
	bpy_title = Label(stat, text="BOOKS PER YEAR\n__________________________", fg="gold", bg="black", font=("Times", 12))
	s_title = Label(stat, text="SERIES OR STANDALONE\n__________________________", fg="gold", bg="black", font=("Times", 12))
	books_per_year = Label(stat, text="Books read in 2021: " +str(a)+ "\nBooks read in 2020: "+str(b)+"\nBooks read in 2019: "+str(c)+"\nBooks read in 2018: "+str(d),  fg="white", bg="black", font=("Times", 12))
	series_and_indies = Label(stat, text = "Book Series: " +str(f)+ "\nStandalone Books: " +str(e), fg="white", bg="black", font=("Times", 12))
	stat_exit = Button(stat, text="Back to Menu", command=stat.destroy)
	

	#flashing the content
	window_title.grid(row=0, column=0, columnspan=2, pady=5)
	start_up_label.grid(row=1, column=0, columnspan=2, padx=100, pady=10)
	bpy_title.grid(row=2, column=0)
	s_title.grid(row=2, column=1)
	books_per_year.grid(row=3, column=0, pady=5)
	series_and_indies.grid(row=3, column=1, pady=5)
	stat_exit.grid(row=4, column=0, columnspan=2, pady=5)

#display option functions 								
#needs major revamp (display modes by author, month, etc)
def display_books():
	display = Toplevel()
	display.configure(bg='black')
	display.grid_columnconfigure(1, weight=1)
	display.geometry("904x620")

	global my_list
	global button_forward
	global button_backward
	global book_count
	global book_detail
	with open('book_record.pkl', 'rb') as inp:
   		my_list = pickle.load(inp)

	book = my_list[0]

	#defining content
	window_title = Label(display, text="Display Book", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	book_detail = Label(display, text="Series              : " +book.series+ "\nTitle                 : "+book.title+ "\nAuthor            : "+book.author+ "\nPages              : "+str(book.pages)+"\nDate Finished : "+book.dateFinished, anchor="e", justify="left")
	book_count = Label(display, text="Displaying ("+ str(1) +") out of (" + str(len(my_list)) +") books.", fg="black", bg="white", font=("Copperplate Gothic Bold", 15), anchor="center")
	button_forward = Button(display, text=">>", command= lambda: forward(1, display))
	button_backward = Button(display, text="<<", state=DISABLED)
	display_exit = Button(display, text="Back to Menu", command=display.destroy)

	#flashing content
	window_title.grid(row=0, column=1, columnspan=2, pady=10)
	book_detail.grid(row=1, column=1,columnspan=2)
	book_count.grid(row=2, column=1, columnspan=2, pady=10)
	button_backward.grid(row=3, column=0, sticky="w", pady=10)
	button_forward.grid(row=3, column=3, sticky="e", pady=10)
	display_exit.grid(row=3, column=1, columnspan=2, pady=10)
def forward(image_i, display):
	global my_list
	global button_forward
	global button_backward
	global book_detail
	global book_count
	book = my_list[image_i]

	#rewriting content
	book_detail.grid_forget()
	book_count.grid_forget()
	book_detail = Label(display, text="Series              : " +book.series+ "\nTitle                 : "+book.title+ "\nAuthor            : "+book.author+ "\nPages              : "+str(book.pages)+"\nDate Finished : "+book.dateFinished, anchor="e", justify="left")
	book_count = Label(display, text="Displaying ("+ str(image_i+1) +") out of (" + str(len(my_list)) +") books.", fg="black", bg="white", font=("Copperplate Gothic Bold", 15))
	button_forward = Button(display, text=">>", command=lambda:forward(image_i+1, display))
	button_backward = Button(display, text="<<", command=lambda:backward(image_i-1, display))

	if image_i+1 == len(my_list):
		button_forward = Button(display, text=">>", state=DISABLED)

	book_detail.grid(row=1, column=1,columnspan=2)
	book_count.grid(row=2, column=1, columnspan=2, pady=10)
	button_backward.grid(row=3, column=0, sticky="w", pady=10)
	button_forward.grid(row=3, column=3, sticky="e", pady=10)
def backward(image_i, display):
	global my_list
	global button_forward
	global button_backward
	global book_detail
	global book_count
	book = my_list[image_i]

	#rewriting content
	book_detail.grid_forget()
	book_count.grid_forget()
	book_detail = Label(display, text="Series              : " +book.series+ "\nTitle                 : "+book.title+ "\nAuthor            : "+book.author+ "\nPages              : "+str(book.pages)+"\nDate Finished : "+book.dateFinished, anchor="e", justify="left")
	book_count = Label(display, text="Displaying ("+ str(image_i+1) +") out of (" + str(len(my_list)) +") books.", fg="black", bg="white", font=("Copperplate Gothic Bold", 15))
	button_forward = Button(display, text=">>", command=lambda:forward(image_i+1, display))
	button_backward = Button(display, text="<<", command=lambda:backward(image_i-1, display))

	if image_i+1 == 1:
		button_backward = Button(display, text="<<", state=DISABLED)

	book_detail.grid(row=1, column=1,columnspan=2)
	book_count.grid(row=2, column=1, columnspan=2, pady=10)
	button_backward.grid(row=3, column=0, sticky="w", pady=10)
	button_forward.grid(row=3, column=3, sticky="e", pady=10)

#search option functions
#search accuracy for typos in searching - being able to search for a related book title even with a less than 100 percent accuracy in typing
def search_book():
	search = Toplevel()
	search.configure(bg='black')
	search.geometry("904x620")


	window_title = Label(search, text="Search Books", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	search_title = Text(search, bg="white", fg="black", border=5, height=1, width=40)
	search_title_label = Label(search, text="Enter the title of the book: ")
	search_button = Button(search, text="Search", command= lambda: search_book_actual(search_title, search))
	search_exit = Button(search, text="Back to Menu", command=search.destroy)

	window_title.grid(row=0, column=0, pady=10)
	search_title_label.grid(row=1, column=0, pady=10)
	search_title.grid(row=2, column=0, padx=270, pady=10)
	search_button.grid(row=3, column=0, pady=10)
	search_exit.grid(row=7, column=0, pady=10)
def search_book_actual(search_title, search):
	title = search_title.get("1.0","end-1c")

	for widget in search.winfo_children():
		widget.destroy()

	window_title = Label(search, text="Search Books", fg="black", bg="gold", font=("Copperplate Gothic Bold", 30))
	search_title = Text(search, bg="white", fg="black", border=5, height=1, width=40)
	search_title_label = Label(search, text="Enter the title of the book: ")
	search_button = Button(search, text="Search", command= lambda: search_book_actual(search_title, search))
	search_exit = Button(search, text="Back to Menu", command=search.destroy)

	window_title.grid(row=0, column=0, pady=10)
	search_title_label.grid(row=1, column=0, pady=10)
	search_title.grid(row=2, column=0, padx=270, pady=10)
	search_button.grid(row=3, column=0, pady=10)
	search_exit.grid(row=7, column=0, pady=10)

	
	with open('book_record.pkl', 'rb') as inp:
		my_list = pickle.load(inp)

	book_not_found = Label(search, text="Book does not exist in database.")
	search_button = Button(search, text="Search", command= lambda: search_book_actual(search_title, search))

	i=0
	for book in my_list:
		i += 1
		if title.lower() == book.title.lower(): 
			book_found_label = Label(search, text="Book #" +str(i)+ " out of "+str(len(my_list)) +" books from database matches the searched book title, \"" +title+ "\".")
			book_found = Label(search, text="Series              : " +book.series+ "\nTitle                 : "+book.title+ "\nAuthor            : "+book.author+ "\nPages              : "+str(book.pages)+"\nDate Finished : "+book.dateFinished, anchor="e", justify="left")
			book_found_label.grid(row=4, column=0, pady=10)
			book_found.grid(row=5, column=0, pady=10)
			return
	search_button.grid(row=3, column=0, pady=10)
	book_not_found.grid(row=4, column=0, pady=10)
def searching_algo(search_entry, book, my_list):
	match = 0
	total = 0
	accuracy = 0




#main_________________________________________________________________________________________________________________
root = Tk()
root.title("Book Database")
root.iconbitmap("./dt.ico")
# Create a PhotoImage object from the image file

bg_image = tk.PhotoImage(file="./bg_img.png")
with Image.open("./bg_img.png") as img:
    width, height = img.size

# Create a Label widget and set the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the size of the Tkinter window to match the size of the image
root.geometry(f"{width}x{height}")



#LOBBY WINDOW


title1 = Label(root, text="Book Archive", font=("Copperplate Gothic Bold", 30), bg="black", fg="gold").pack(pady=30)
butt_a = Button(root, text="Add a Book", font=("Cambria", 12), bg="black", fg="white", command=add_book_actual).pack()
butt_d = Button(root, text="Display Books", font=("Cambria", 12), bg="black", fg="white", command=display_books).pack()
butt_s = Button(root, text="Search", font=("Cambria", 12),bg="black", fg="white", command=search_book).pack()
butt_st= Button(root, text="Statistics", font=("Cambria", 12),bg="black", fg="white", command=statistics).pack()
butt_ex= Button(root, text="Exit", font=("Cambria", 12),bg="black", fg="white", command=root.quit).pack()

root.mainloop()