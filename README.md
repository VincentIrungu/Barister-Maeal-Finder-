# Barister-Meal Finder

Barister-Meal Finder is a command-line interface (CLI) application that simplifies the management of baristas and clients in a meal-sharing community. Easily add, view, edit, and delete profiles, and connect with others based on shared meal preferences.

## Features

- **Barista Activities:**
  - Add Barista
  - View All Baristas
  - Find Barista by First Name
  - Find Barista by ID
  - Find Baristas Serving a Specific Meal
  - Edit Barista Information
  - Delete Barista

- **Client Activities:**
  - Add Client
  - View All Clients
  - Find Client by First Name
  - Find Client by ID
  - Find Clients Serving a Desired Meal
  - Edit Client Information
  - Delete Client

## File Structure

- **models.py:** Defines SQLAlchemy models for Baristas and Clients, including the relationship between them and meal cards.
- **meal_cards table:** Represents the meal cards that connect baristas and clients.
- **app.py:** Contains the CLI functionality using the Click library.
- **parlor.db:** SQLite database file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Barister-Meal-Finder.git
Navigate to the project directory:

bash
Copy code
cd Barister-Meal-Finder
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the CLI application:

bash
Copy code
python app.py
Follow the prompts to perform various barista and client activities.

Database
SQLite database: parlor.db
Contributing
Vincent Irungu

License
This project is licensed under the MIT License - see the LICENSE file for details.

