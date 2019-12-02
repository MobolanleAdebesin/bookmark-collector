from peewee import *
from tkinter import *
from PIL import ImageTk, Image 
import PySimpleGUI as sg




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
    query_label.grid(row = 8, column = 0, columnspan = 2)

#Create a query single record function 
def query_one(): 
    #querying the database for info
    query_name = Bookmark.get(Bookmark.name == query_field.get()).name
    query_url = Bookmark.get(Bookmark.name == query_field.get()).url
    query_details = Bookmark.get(Bookmark.name == query_field.get()).details
    #creating a label for info 
    query_one_label = Label(root, text= query_name + '-' + query_url + '-' + query_details)
    query_one_label.grid(row=15, column = 0, columnspan = 2)

    query_field.delete(0, END)


#Create delete function 
def delete():
    record = Bookmark.get(Bookmark.name == delete_field.get())
    record.delete_instance()
    delete_field.delete(0, END)

#Create update function to update bookmark
def save_update(): 

    new_record = Bookmark.get(Bookmark.name == query_name)
    new_record.name = new_name_editor.get()
    new_record.url = new_url_editor.get()
    new_record.details = new_details_editor.get()
    new_record.save()
    editor.destroy()

def update():
    global editor
    editor = Tk()
    editor.title('Update Bookmark')
    intro_editor = Label(editor, text="Update Bookmark Records Here")
    intro_editor.grid(row = 0, column = 1, padx=20)

    #setting record_name equal to title entered in text_field
    record_name = delete_field.get()

    #querying the database for info
    global query_name
    query_name = Bookmark.get(Bookmark.name == record_name).name
    query_url = Bookmark.get(Bookmark.name == record_name).url
    query_details = Bookmark.get(Bookmark.name == record_name).details

    # Create text boxes in editor
    WIDTH = 30
    global new_name_editor
    global new_url_editor
    global new_details_editor
    new_name_editor = Entry(editor, width = WIDTH)
    new_name_editor.grid(row = 1, column = 1, padx = 20)
    new_url_editor = Entry(editor, width = WIDTH)
    new_url_editor.grid(row = 2, column = 1)
    new_details_editor = Entry(editor, width = WIDTH)
    new_details_editor.grid(row = 3, column = 1)
 
    #Create labels for text boxes in editor
    name_label_editor = Label(editor, text="Name")
    name_label_editor.grid(row = 1, column = 0 )
    url_label_editor = Label(editor, text = "Url")
    url_label_editor.grid(row = 2, column = 0)
    details_label_editor = Label(editor, text="Details")
    details_label_editor.grid(row = 3, column = 0)

    #pre-filling text fields with data from database
    new_name_editor.insert(0, query_name)
    new_url_editor.insert(0, query_url)
    new_details_editor.insert(0, query_details)

    #Create save button 
    save_button = Button(editor, text="Save Changes", command=save_update)
    save_button.grid(row=4, column=0, columnspan=2, padx = 10, pady = 10, ipadx = 122)
  


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
query_field.grid(row=13, column = 1)

#Create labels for text boxes 

name_label = Label(root, text="Name")
name_label.grid(row = 1, column = 0 )
url_label = Label(root, text = "Url")
url_label.grid(row = 2, column = 0)
details_label = Label(root, text="Details")
details_label.grid(row = 3, column = 0)
delete_field_label = Label(root, text="Select Site Name")
delete_field_label.grid(row=9, column=0 )
query_field_label = Label(root, text="Find Bookmark")
query_field_label.grid(row=13, column=0)

#Create a submit button 
submit_button = Button(root, text="Add Record to Database", command=submit)
submit_button.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 100)

#Create a query button 
query_button = Button(root, text="Show All Bookmarks", command=query)
query_button.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 112)

#Create a delete button 
delete_button = Button(root, text="Delete Bookmark", command=delete)
delete_button.grid(row = 10, column = 0, columnspan = 2, padx = 10, pady = 10, ipadx = 122)

#Create an update button 
update_button = Button(root, text="Update Bookmark", command=update)
update_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx= 122)

#Create a single query button 
query_one_button = Button(root, text="Search Bookmark Name", command=query_one)
query_one_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10, ipadx=100)



root.mainloop()








