from peewee import *
from tkinter import *
from PIL import ImageTk, Image 



db = PostgresqlDatabase('bookmarks', user='postgres', password='',
                        host='localhost', port=5432)


class BaseModel(Model):
    """A base model that will use our Postgresql database. We don't have to do
    this, but it makes connecting models to our database a lot easier."""
    class Meta:
        database = db


class Bookmark(BaseModel):
    name = CharField()
    url = CharField()
    details = CharField()


db.connect()
# db.drop_tables([Bookmark])
db.create_tables([Bookmark])

# google = Bookmark(name='Google', url='https://www.google.com/', details='Google LLC is an American multinational technology company.')
# google.save()

# facebook = Bookmark(name="Facebook", url='https://www.facebook.com/', details='Facebook, Inc. is an American online social media and social networking service company.')
# facebook.save()

# instagram = Bookmark(name='Instagram', url='https://www.instagram.com/', details='https://en.wikipedia.org/wiki/Instagram')
# instagram.save()


# print(f"{instagram.name} - {instagram.url} - {instagram.details}")
# print(f"{google.name} - {google.url} - {google.details}")
# print(f"{facebook.name} - {facebook.url} - {facebook.details}")

# query = Bookmark.get(Bookmark.name == 'Google').name
# print(query)

# def intro(): 
#     print("Welcome to the bookmark collector app. You have 5 options. Select 'c' to create a new bookmark, 'r' to see all bookmarks, 'u' to update an existing bookmark, 'd' to delete a bookmark, or 's' to search for a specific bookmark" )
#     choice = input('What is your choice?')
#     if choice == 'c':
#         create()
#     elif choice == 'r': 
#         read()
#     elif choice == 'u': 
#         update()
#     elif choice == 'd': 
#         delete()
#     elif choice == 's': 
#         read_one()
#     else: 
#         print('Sorry that is not a valid choice, please try again')
#         intro()



root = Tk()
root.title('Bookmark Collector')

#Label for the GUI 
intro = Label(root, text="Welcome to the bookmark collector app.")
intro.grid(row = 0, column = 1, padx=20)

#Create submit function 
def submit(): 
    #Insert into table 
    record = Bookmark(name = new_name.get(), url = new_url.get(), details = new_details.get())
    record.save()

    #Clear the text boxes 
    new_name.delete(0, END)
    new_url.delete(0, END)
    new_details.delete(0, END)

#Create query function 
def query(): 
    #Loop through results 
    print_site = ''
    query = Bookmark.select()
    for site in query: 
        print_site += str(site.name) + '-' + str(site.details) + '-' + str(site.url) + "\n"
    query_label = Label(root, text=print_site)
    query_label.grid(row = 11, column = 0, columnspan = 2)

#Create a query single record function 
def query_one(): 
    #querying the database for info
    query_name = Bookmark.get(Bookmark.name == query_field.get()).name
    query_url = Bookmark.get(Bookmark.name == query_field.get()).url
    query_details = Bookmark.get(Bookmark.name == query_field.get()).details
    #creating a label for info 
    query_one_label = Label(root, text= query_name + '-' + query_url + '-' + query_details)
    query_one_label.grid(row=14, column = 0, columnspan = 2)

    query_field.delete(0, END)


#Create delete function 
def delete():
    record = Bookmark.get(Bookmark.name == delete_field.get())
    record.delete_instance()
    delete_field.delete(0, END)


# Create text boxes 
WIDTH = 30
new_name = Entry(root, width = WIDTH)
new_name.grid(row = 1, column = 1, padx = 20)
new_url = Entry(root, width = WIDTH)
new_url.grid(row = 2, column = 1)
new_details = Entry(root, width = WIDTH)
new_details.grid(row = 3, column = 1)
delete_field = Entry(root, width = WIDTH)
delete_field.grid(row=9, column = 1)
query_field = Entry(root, width=WIDTH)
query_field.grid(row=12, column = 1)

#Create labels for text boxes 

name_label = Label(root, text="Name")
name_label.grid(row = 1, column = 0 )
url_label = Label(root, text = "Url")
url_label.grid(row = 2, column = 0)
details_label = Label(root, text="Details")
details_label.grid(row = 3, column = 0)
delete_field_label = Label(root, text="Delete Site Name")
delete_field_label.grid(row=9, column=0 )
query_field_label = Label(root, text="Find Bookmark")
query_field_label.grid(row=12, column=0)

#Create a submit button 
submit_button = Button(root, text="Add Record to Database", command=submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)

#Create a query button 
query_button = Button(root, text="Show All Bookmarks", command=query)
query_button.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 112)

#Create a delete button 
delete_button = Button(root, text="Delete Bookmark", command=delete)
delete_button.grid(row = 10, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 122)

#Create a single query button 
query_one_button = Button(root, text="Search Bookmark Name", command=query_one)
query_one_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10, ipadx=100)


# def create(): 
#     print("Each bookmark must include: the name of the website, the website url, and details about the bookmark")
#     new_name = input('What is the name of the website?')
#     new_url = input('What is the url of the website?')
#     new_details = input('Tell me a little bit  about this website')
#     new_name = Bookmark(name=new_name, url=new_url, details=new_details)
#     new_name.save()
#     print('Your bookmark has been added!')

    
# def read():
#     query = Bookmark.select()
#     for site in query: 
#         print(site.name, '->', site.details, ' ->', site.url)

# def read_one(): 
#     name = input('Please enter the name of the website you are looking for')
#     record_name = Bookmark.get(Bookmark.name == name).name
#     record_url = Bookmark.get(Bookmark.name == name).url
#     record_details = Bookmark.get(Bookmark.name == name).details
#     print(record_name, '->', record_details, '->', record_url)

# def update(): 
#     print('To update a bookmark from our collection, please enter the name of the website you would like to update')
#     name = input('What is the name of the website?')
#     record = Bookmark.get(Bookmark.name == name)
#     print(f"How would you like to update '{name}'?")
#     choice = input("Select 'n' to update website name, 'u' to update website url, or 'd' to update website details")
#     if choice == 'n': 
#         new_name = input('Please enter new name of website')
#         record.name = new_name
#         record.save()
#         print(f"The new name for {name} is now {new_name}")
#     elif choice == 'u': 
#         new_url = input('Please enter the new url of the website')
#         record.url = new_url
#         record.save()
#         print(f"The new url for {name} is now {new_url}")
#     elif choice == 'd': 
#         new_details = input('Please enter the new details of the website')
#         record.details = new_details
#         record.save()
#         print(f"The new details for {name} are {new_details}")
#     else: 
#         option = input("Sorry that was not a valid choice. Select 'y' to try again or 'n' to leave bookmark collection" )
#         if option == 'y': 
#             update()
#         elif option == 'n': 
#             print('Goodbye!')
#         else: 
#             pass 


# def delete(): 
#     print('To delete a bookmark from our collection, please enter the name of the website you would like to delete')
#     name = input('what is the name of the website?')
#     record = Bookmark.get(Bookmark.name == name)
#     record.delete_instance()
#     print(f"{name} has been deleted")

root.mainloop()
# intro()





