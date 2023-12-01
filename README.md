# Project Title

PrimaryED CMS

## Detailed project scope

https://cs50.harvard.edu/web/2020/projects/final/capstone/

## Overview

PrimaryEd CMS is a Learning Management System (LMS) designed for primary school teachers. It provides a platform to find, organize, and utilize educational resources, quizzes, and exercises for classroom learning. This project is developed as part of the CS50W course's final capstone project.

## Distinctiveness and Complexity

PrimaryEd CMS stands out due to its focus on primary education, providing a specialized resource repository and interactive tools for teachers. The complexity of the project is evident in its comprehensive set of features, including user authentication, resource management, a community forum, and an interactive quiz system. The application integrates Django's powerful backend capabilities with a user-friendly frontend, ensuring a seamless user experience.

## Project Structure

- core/: Main application directory.
  - templates/: Contains HTML templates for the application.
  - base.html: Base template with common layout and navigation.
  - index.html: Homepage of the application.
  - login.html, register.html: Authentication templates.
  - subject_list.html, subject_detail.html: Templates for subject listing and details.
  - forum.html: Community forum template.
  - faq.html: Frequently Asked Questions page.
  - contact_support.html: Contact form for user support.
  - resource_list.html, resource_detail.html: Resource library and individual resource detail templates.
- models.py: Defines models like User, Subject, Post, and Resource.
- views.py: Contains views for handling different application functionalities.
- urls.py: URL configurations for the application.
- admin.py: Admin configurations for managing application models.
- forms.py: Django forms for resource upload and other functionalities.
- PrimaryEdLMS/: Project configuration directory.
  - settings.py: Settings for the Django project.
  - urls.py: Root URL configurations.
- requirements.txt: Lists Python packages required for the project.
- manage.py: Django command-line utility for administrative tasks.

## Installation

To run PrimaryEd CMS:

1. Clone the repository: git clone https://github.com/mark-goudie/capstone.git
2. Navigate to the project directory: cd capstone
3. Install required packages: pip install -r requirements.txt
4. Run migrations: python manage.py migrate
5. Start the Django server: python manage.py runserver
6. Access the application at http://localhost:8000/

## Features

The project includes a custom user model for authentication.
Resources can be filtered by grade level and type in the resource library.
The forum allows for community discussions and interactions.
The application is designed with responsiveness in mind, ensuring compatibility across various devices.
The project includes a custom interactive quiz feature within the resource detail view, showcasing the application's dynamic capabilities.
User-generated content, such as forum posts and resource contributions, demonstrates the application's interactive nature.
The project adheres to Django's security best practices, ensuring a secure user experience.

## Disclosures

The project references code snippets from the previous submission of the CS50W course's Project 4 (Network) assignment. The snippets are used to implement the Forum feature of the application.

## License

Information about the license under which your project is distributed.

## Users

Superuser

- username: admin
- email: admin@foo.com
- password: password0

Primary user

- username: johndoe
- email: johndoe@foo.com
- password: password1

## Detailed project scope

https://cs50.harvard.edu/web/2020/projects/4/network/

## Youtube video

https://youtu.be/..........
