# Olympics-Database-Managment-System

# Olympics Database Management System

A web-based **Olympics Database Management System** built with **Python Flask** and **PostgreSQL**. The application provides a simple interface for managing Olympic player and sports information through CRUD operations and running predefined SQL queries.

## 🚀 Overview

This project demonstrates how a relational database can be integrated with a web application to store, retrieve, update, and delete Olympic-related data.

The application connects to a PostgreSQL database named `olympics_db` and provides functionality for managing:

* Player information
* Sports information
* Database records through CRUD operations
* Predefined SQL queries and sorted results

## ✨ Features

### Player Management

The application supports:

* Add a new player
* View all players
* Update player details
* Delete player records
* View players ordered by height

Player attributes include:

* Player ID
* First name
* Last name
* Gender
* Height
* Weight
* Date of birth

### Sports Management

The application supports:

* Add sports participation information
* View sports records
* Update sports records
* Delete sports records
* Query sports records for events after the year 2000

Sports records include:

* Player ID
* Sports name
* Location
* Year

### Database Queries

The application includes predefined query pages for:

**Sports after 2000**

```sql
SELECT sports_name, player_id, year, location
FROM olympics_db.sports
WHERE year > 2000;
```

**Players ordered by height**

```sql
SELECT player_id, first_name, last_name, gender, height, weight
FROM olympics_db.player
ORDER BY height;
```

## 🛠️ Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Backend programming       |
| Flask      | Web application framework |
| PostgreSQL | Relational database       |
| psycopg2   | PostgreSQL connectivity   |
| HTML       | Frontend templates        |
| Jinja2     | Dynamic HTML rendering    |

## 📁 Project Structure

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

## 🗄️ Database Structure

The Flask application interacts with the following PostgreSQL tables:

### `player`

| Column       | Description              |
| ------------ | ------------------------ |
| `player_id`  | Unique player identifier |
| `first_name` | Player's first name      |
| `last_name`  | Player's last name       |
| `gender`     | Player's gender          |
| `height`     | Player's height          |
| `weight`     | Player's weight          |
| `dob`        | Player's date of birth   |

### `sports`

| Column        | Description           |
| ------------- | --------------------- |
| `player_id`   | Player identifier     |
| `sports_name` | Name of the sport     |
| `location`    | Location of the event |
| `year`        | Year of participation |

The application accesses these tables using the PostgreSQL schema `olympics_db`.

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/hemangijoshi12/Olympics-Database-Managment-System.git
cd Olympics-Database-Managment-System
```

### 2. Create a PostgreSQL database

Create a PostgreSQL database named:

```text
olympics_db
```

Create the required schema and tables according to the fields used by the application.

The current repository does not contain a SQL schema or database dump, so the PostgreSQL tables need to be created separately.

### 3. Install Python dependencies

Install Flask and PostgreSQL connectivity:

```bash
pip install flask psycopg2-binary
```

### 4. Configure the database connection

The application currently uses the following connection configuration in `main.py`:

```python
conn = psycopg2.connect(
    host="localhost",
    database="olympics_db",
    user="postgres",
    password="admin"
)
```

Update these values to match your local PostgreSQL configuration.

For production or shared environments, database credentials should be stored in environment variables rather than hard-coded in the source code.

### 5. Run the application

```bash
python main.py
```

The Flask development server will start locally.

Open the application in your browser at:

```text
http://127.0.0.1:5000/
```

## 🌐 Application Routes

| Route             | Function                          |
| ----------------- | --------------------------------- |
| `/`               | Homepage                          |
| `/insert_sports`  | Add sports record                 |
| `/show_sports`    | Display sports records            |
| `/edit_sports`    | Update sports record              |
| `/delete_sports`  | Delete sports record              |
| `/insert_player`  | Add player                        |
| `/show_player`    | Display players                   |
| `/edit_player`    | Update player                     |
| `/delete_player`  | Delete player                     |
| `/runquerysports` | Query sports after 2000           |
| `/runqueryplayer` | Display players ordered by height |

## 🔄 CRUD Operations

The system demonstrates the four fundamental database operations:

```text
Create  → Insert player/sports records
Read    → Display stored records
Update  → Edit existing records
Delete  → Remove records
```

All database modifications are committed through PostgreSQL transactions using `psycopg2`.

## 🧩 How It Works

The application follows a simple web application flow:

```text
User
 │
 ▼
Flask Web Interface
 │
 ▼
HTTP Request
 │
 ▼
Flask Route
 │
 ▼
SQL Query via psycopg2
 │
 ▼
PostgreSQL Database
 │
 ▼
Query Result
 │
 ▼
Jinja2 HTML Template
 │
 ▼
User
```

## 🎯 Project Objectives

This project demonstrates practical implementation of:

* Relational database management
* PostgreSQL integration with Python
* Flask web application development
* CRUD operations
* SQL querying
* Database-backed HTML interfaces
* Server-side form processing

## 🔐 Notes

The current application is configured for local development and uses `debug=True` when running Flask. Database credentials are also currently present directly in `main.py`. These settings should be changed before deploying the application to a production environment.
