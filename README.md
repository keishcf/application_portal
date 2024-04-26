Installation Guide for Django Application
Follow these steps to install and run the Django application:

Prerequisites
Ensure you have the following installed on your system:

Python 3.8 or newer. You can download it from here.
pip (Python package installer). It's usually installed with Python.
Steps
Clone the repository

Open your terminal and run the following command:

Replace <repository_url> with the URL of this repository.

Navigate to the project directory

Replace <project_directory> with the name of the directory where the project is located.

Create a virtual environment

It's recommended to create a virtual environment to isolate your project and avoid conflicts with other projects.

Activate the virtual environment

On Windows, run:

On Unix or MacOS, run:

Install the required packages

Apply migrations

Django uses migrations to propagate changes you make to your models (adding a field, deleting a model, etc.) into the database schema.

Run the server

The application will be available at http://127.0.0.1:8000/.
