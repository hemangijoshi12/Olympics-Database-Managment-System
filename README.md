# Olympics Database Management System

A Flask-based **Olympics Database Management System** that integrates a web interface with a PostgreSQL database to manage Olympic player and sports records. The application provides CRUD functionality and allows users to execute predefined SQL queries through a simple web interface.

## Overview

The project is built using **Python Flask** for the backend and **PostgreSQL** for data storage. Users can manage player and sports information through HTML forms and view database records directly from the application.

The system supports:

* Managing Olympic player records
* Managing sports participation records
* Creating, viewing, updating, and deleting data
* Executing predefined SQL queries
* Displaying query results through web pages

## Tech Stack

* **Python**
* **Flask**
* **PostgreSQL**
* **Psycopg2**
* **HTML / Jinja2**

The backend uses `psycopg2` to connect Flask to a PostgreSQL database named `olympics_db`.

## Features

### Player Management

The application provides complete CRUD operations for player records.

Player information includes:

* Player ID
* First Name
* Last Name
* Gender
* Height
* Weight
* Date of Birth

Supported operations:

* Add a player
* View all players
* Edit player information
* Delete a player

These operations are implemented through Flask routes connected to the PostgreSQL `player` table.

### Sports Management

Sports participation records can also be managed through the application.

Each record contains:

* Player ID
* Sports Name
* Location
* Year

Supported operations:

* Add a sports record
* View sports records
* Edit sports information
* Delete sports records

The application stores these records in the PostgreSQL `sports` table.

## SQL Queries

The project includes two predefined database queries.

### Sports After 2000

Retrieves sports records where the participation year is greater than 2000.

```sql
SELECT sports_name, player_id, year, location
FROM olympics_db.sports
WHERE year > 2000;
```

### Players Ordered by Height

Retrieves player information and sorts the results by height.

```sql
SELECT player_id, first_name, last_name, gender, height, weight
FROM olympics_db.player
ORDER BY height;
```

Both queries are exposed through dedicated Flask routes and rendered using HTML templates.

## Application Routes

| Route             | Description                       |
| ----------------- | --------------------------------- |
| `/`               | Homepage                          |
| `/insert_sports`  | Add a sports record               |
| `/show_sports`    | Display sports records            |
| `/edit_sports`    | Edit a sports record              |
| `/delete_sports`  | Delete a sports record            |
| `/insert_player`  | Add a player                      |
| `/show_player`    | Display player records            |
| `/edit_player`    | Edit a player                     |
| `/delete_player`  | Delete a player                   |
| `/runquerysports` | Display sports records after 2000 |
| `/runqueryplayer` | Display players ordered by height |

The routes and their database operations are implemented in `main.py`.

## Project Structure

```text
Olympics-Database-Managment-System/
│
├── templates/
│   ├── Homepage.html
│   ├── insert_player.html
│   ├── show_player.html
│   ├── edit_player.html
│   ├── delete_player.html
│   ├── insert_sports.html
│   ├── show_sports.html
│   ├── edit_sports.html
│   ├── delete_sports.html
│   ├── runqueryplayer.html
│   └── runquerysports.html
│
├── main.py
├── package.json
├── package-lock.json
└── README.md
```

The repository also currently contains development/environment directories such as `venv`, `.vscode`, and `node_modules`.

## Database

The application connects to PostgreSQL using:

```python
conn = psycopg2.connect(
    host="localhost",
    database="olympics_db",
    user="postgres",
    password="admin"
)
```

The application expects the PostgreSQL schema `olympics_db` with the relevant `player` and `sports` tables.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/hemangijoshi12/Olympics-Database-Managment-System.git
cd Olympics-Database-Managment-System
```

### 2. Install Python dependencies

```bash
pip install flask psycopg2-binary
```

### 3. Configure PostgreSQL

Create the required PostgreSQL database and tables expected by `main.py`.

The application currently expects:

```text
Database: olympics_db
Host: localhost
User: postgres
```

Update the credentials in `main.py` to match your local PostgreSQL setup.

### 4. Run the application

```bash
python main.py
```

The Flask application runs in debug mode and can be accessed locally at:

```text
http://127.0.0.1:5000/
```

## Architecture

```text
           Web Browser
                │
                ▼
        Flask Web Application
                │
                ▼
          Flask Routes
                │
                ▼
             Psycopg2
                │
                ▼
          PostgreSQL
          ┌─────┴─────┐
          │           │
       player       sports
          │           │
          └─────┬─────┘
                │
                ▼
        Query / CRUD Results
                │
                ▼
        HTML / Jinja Templates
```

## Key Learning Outcomes

This project demonstrates practical implementation of:

* Relational database design
* SQL queries
* PostgreSQL database integration
* Flask backend development
* CRUD operations
* HTML form handling
* Server-side rendering with Jinja2
* Connecting a web application to a relational database

## Future Improvements

Potential improvements include:

* Moving database credentials to environment variables
* Adding input validation and error handling
* Using connection pooling
* Adding authentication and authorization
* Improving database schema constraints
* Adding search and filtering functionality
* Adding pagination for large datasets
* Improving the frontend UI
* Adding automated tests
