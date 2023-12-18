from models import session, Baristas, Clients

#SEARCHES BASED ON BARISTA'S ATTRIBUTES
# Seeing all baristas available
def search_all_baristas():
    result = session.query(Baristas).all()
    return f'Our team comprises {result}'

print(search_all_baristas())

print("......................................................................................................................")
# Searching for a  barista to serve a client, given only firstname

def search_barista_name (first_name: str):
    result = session.query(Baristas).filter_by(first_name = first_name).first()
    return f'Your search response is {result}'

print(search_barista_name('Neil'))
print(search_barista_name('Andra'))

print("......................................................................................................................")
# Searching for a Barista to serve a client, given only id

def search_barista_id (barista_id: int):
    result = session.query(Baristas).filter_by(barista_id = barista_id).all()
    return f'Your barista id {barista_id} belongs to {result}'

print(search_barista_id(1))
print(search_barista_id(4))


print(".......................................................................................................................")
# Searching for a barista who can serve a particular desired meal
def search_barista_meal_serve(meal_served: str):
    result = session.query(Baristas).filter_by(meal_served = meal_served).all()
    return f'Your meal is always served by {result}'

print(search_barista_meal_serve('Ice Cream'))
print(search_barista_meal_serve('French Fries'))

#
print(search_barista_meal_serve('Brocolli'))

print(".........................................................................................................................")
# SEARCHES BASED ON CLIENT'S ATTRIBUTES
# Searching for all clients served by Barister-Meal Finder
def search_all_clients():
    result = session.query(Clients).all()
    return f'Our beloved clients comprise {result}'

print(search_all_clients())

print(".......................................................................................................................")
#Searching for a client to serve a client, given only firstname

def search_clients_name(first_name: str):
    result = session.query(Clients).filter_by(first_name = first_name).all()
    return f'Your name search is {result}'
print(search_clients_name('Oralle'))
print(search_clients_name('Culley'))

print("................................................................")
# Searching for a Barista to serve a client, given only id
def search_client_id(client_id:int):
    result = session.query(Clients).filter_by(client_id = client_id).all()
    return f'Your id search belongs to {result}'

print(search_client_id(1))
print(search_client_id(3))
print(search_client_id(6))

print("...........................................................................")
# Searching for a client  who enjoys my  particular desired meal.... Good for linking up and networking
def search_client_meal(meal_served:str):
    result = session.query(Clients).filter_by(meal_served = meal_served).all()
    return f'Clients who ordered {meal_served} include: {result}'


print(search_client_meal('Ice Cream'))
print(search_client_meal('Milkshake'))
print(search_client_meal('Chicken Nuggets'))

print("..................................................")





