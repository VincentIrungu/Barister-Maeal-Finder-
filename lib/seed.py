from models import Baristas,session, Clients

"""data = [{
  "barista_id": 1,
  "first_name": "Neil",
  "last_name": "Kaming",
  "meal_served": "Cheeseburger",
  "age": 45,
}, {
  "barista_id": 2,
  "first_name": "Andra",
  "last_name": "Wigginton",
  "meal_served": "Ice Cream",
  "age": 38,
}, {
  "barista_id": 3,
  "first_name": "Ricki",
  "last_name": "Deabill",
  "meal_served": "French Fries",
  "age": 45,
}, {
  "barista_id": 4,
  "first_name": "Jan",
  "last_name": "Plail",
  "meal_served": "Milkshake",
  "age": 18,
}]


baristas = []

for datum in data:
    brst =Baristas(**datum)
    baristas.append(brst)


session.add_all(baristas)
session.commit()
print("Good work Vincent baristas data seeded succesfully. Check your table")"""

"""data = [{
  "client_id": 1,
  "first_name": "Oralle",
  "last_name": "Deards",
  "meal_served": "Chicken Nuggets",
  "rank": 1,
  "barista_id": 1
}, {
  "client_id": 2,
  "first_name": "Culley",
  "last_name": "MacWhan",
  "meal_served": "Milkshake",
  "rank": 2,
  "barista_id": 3
}, {
  "client_id": 3,
  "first_name": "Lilyan",
  "last_name": "Larchiere",
  "meal_served": "Ice Cream",
  "rank": 3,
  "barista_id": 1
}, {
  "client_id": 4,
  "first_name": "Mechelle",
  "last_name": "Adams",
  "meal_served": "Hamburger",
  "rank": 4,
  "barista_id": 3
}, {
  "client_id": 5,
  "first_name": "Laraine",
  "last_name": "Parbrook",
  "meal_served": "Cheeseburger",
  "rank": 5,
  "barista_id": 2
}, {
  "client_id": 6,
  "first_name": "Tyne",
  "last_name": "Britch",
  "meal_served": "Ice Cream",
  "rank": 6,
  "barista_id": 3
}, {
  "client_id": 7,
  "first_name": "Freddi",
  "last_name": "Dearness",
  "meal_served": "Salad",
  "rank": 7,
  "barista_id": 2
}, {
  "client_id": 8,
  "first_name": "Daniela",
  "last_name": "Broxup",
  "meal_served": "Chicken Sandwich",
  "rank": 8,
  "barista_id": 4
}]

clients = []

for datum in data:
    clnt = Clients(**datum)
    clients.append(clnt)


session.add_all(clients)
session.commit()
print("Good work Vincent clients data seeded succesfully. Check your table")
"""
data = [{
  "meal_id": 1,
  "meal_served": "Cheeseburger",
  "specifications": "Brie Cheese",
  "satisfaction_rank": 1,
  "comments": "Medium",
  "barista_id": 3,
  "client_id": 1
}, {
  "meal_id": 2,
  "meal_served": "Hamburger",
  "specifications": "Vegie Burger",
  "satisfaction_rank": 2,
  "comments": "Vegetarian",
  "barista_id": 2,
  "client_id": 2
}, {
  "meal_id": 3,
  "meal_served": "Cheeseburger",
  "specifications": "Harpin",
  "satisfaction_rank": 3,
  "comments": "Smoked Gouda",
  "barista_id": 2,
  "client_id": 1
}, {
  "meal_id": 4,
  "meal_served": "Cheeseburger",
  "specifications": "Cheddar Cheese",
  "satisfaction_rank": 4,
  "comments": "Extra Cheese",
  "barista_id": 1,
  "client_id": 3
}, {
  "meal_id": 5,
  "meal_served": "Cheeseburger",
  "specifications": "Smoked Gouda",
  "satisfaction_rank": 5,
  "comments": "Crispy",
  "barista_id": 3,
  "client_id": 4
}, {
  "meal_id": 6,
  "meal_served": "Pizza",
  "specifications": "Croad",
  "satisfaction_rank": 6,
  "comments": "Barbecue Steak",
  "barista_id": 3,
  "client_id": 3
}, {
  "meal_id": 7,
  "meal_served": "Hamburger",
  "specifications": "Nolda",
  "satisfaction_rank": 7,
  "comments": "Medium",
  "barista_id": 1,
  "client_id": 1
}, {
  "meal_id": 8,
  "meal_served": "Salad",
  "specifications": "Lardner",
  "satisfaction_rank": 8,
  "comments": "Crispy",
  "barista_id": 2,
  "client_id": 5
}, {
  "meal_id": 9,
  "meal_served": "French Fries",
  "specifications": "Hussey",
  "satisfaction_rank": 9,
  "comments": "Small",
  "barista_id": 4,
  "client_id": 6
}]

meal_cards  = []

for datum in data:
    meal_card = meal_cards(**datum)
    meal_cards.append(meal_card)


session.add_all(meal_cards)
session.commit()
print("Good work Vincent meal_card data seeded succesfully. Check your table")
