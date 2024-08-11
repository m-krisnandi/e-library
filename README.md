# E-Library Application

## Overview

The E-Library Application is a simple web application built using Django, designed to manage and explore a collection of books. Users can browse books, view detailed information, and perform CRUD (Create, Read, Update, Delete) operations on books. Authentication is implemented to ensure that only logged-in users can manage the book catalog.

## Features

- **User Registration & Login**: Users can register and log in to the application.
- **Authentication**: The application uses authentication for secure access.
- **Book Management**: Authenticated users can add, update, and delete books.
- **Book Browsing**: All users can browse the book catalog and view detailed information about each book.
- **Book Search**: All users can search book.

## Installation

To get started with the E-Library Application, follow these steps:

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Django
- Virtualenv (optional but recommended)

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/m-krisnandi/e-library.git
cd e-library
```
## Getting Started

Follow the steps below to set up and run the E-Library application.

### 1. Apply Migrations

First, make sure to create the necessary migrations and apply them to the database:

```bash
python manage.py makemigrations books
python manage.py migrate
```
### 2. Create a Superuser
To create a superuser, which allows you to access the admin interface and manage users, run the following command:

```bash
python manage.py createsuperuser
```
Alternatively, you can create a user directly through the website by using the register menu.

### 3. Run the Server
Finally, start the development server with the following command:

```bash
python manage.py runserver
```
Now, you can access the application by navigating to http://127.0.0.1:8000/ in your web browser.