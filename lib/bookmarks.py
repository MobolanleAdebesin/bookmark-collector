from peewee import *



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

def intro(): 
    print("Welcome to the bookmark collector app. You have 5 options. Select 'c' to create a new bookmark, 'r' to see all bookmarks, 'u' to update an existing bookmark, 'd' to delete a bookmark, or 's' to search for a specific bookmark" )
    choice = input('What is your choice?')
    if choice == 'c':
        create()
    elif choice == 'r': 
        read()
    elif choice == 'u': 
        update()
    elif choice == 'd': 
        delete()
    elif choice == 's': 
        read_one()
    else: 
        print('Sorry that is not a valid choice, please try again')
        intro()

def create(): 
    print("Each bookmark must include: the name of the website, the website url, and details about the bookmark")
    new_name = input('What is the name of the website?')
    new_url = input('What is the url of the website?')
    new_details = input('Tell me a little bit  about this website')
    new_name = Bookmark(name=new_name, url=new_url, details=new_details)
    new_name.save()
    print('Your bookmark has been added!')

    
def read():
    query = Bookmark.select()
    for site in query: 
        print(site.name, '   ', site.details, '   ', site.url)

def read_one(): 
    name = input('Please enter the name of the website you are looking for')
    record_name = Bookmark.get(Bookmark.name == name).name
    record_url = Bookmark.get(Bookmark.name == name).url
    record_details = Bookmark.get(Bookmark.name == name).details
    print(record_name, '->', record_details, '->', record_url)

def update(): 
    print('To update a bookmark from our collection, please enter the name of the website you would like to update')
    name = input('What is the name of the website?')
    record = Bookmark.get(Bookmark.name == name)
    print(f"How would you like to update '{name}'?")
    choice = input("Select 'n' to update website name, 'u' to update website url, or 'd' to update website details")
    if choice == 'n': 
        new_name = input('Please enter new name of website')
        record.name = new_name
        record.save()
        print(f"The new name for {name} is now {new_name}")
    elif choice == 'u': 
        new_url = input('Please enter the new url of the website')
        record.url = new_url
        record.save()
        print(f"The new url for {name} is now {new_url}")
    elif choice == 'd': 
        new_details = input('Please enter the new details of the website')
        record.details = new_details
        record.save()
        print(f"The new details for {name} are {new_details}")
    else: 
        option = input("Sorry that was not a valid choice. Select 'y' to try again or 'n' to leave bookmark collection" )
        if option == 'y': 
            update()
        elif option == 'n': 
            print('Goodbye!')
        else: 
            pass 


def delete(): 
    print('To delete a bookmark from our collection, please enter the name of the website you would like to delete')
    name = input('what is the name of the website?')
    record = Bookmark.get(Bookmark.name == name)
    record.delete_instance()
    print(f"{name} has been deleted")


intro()





