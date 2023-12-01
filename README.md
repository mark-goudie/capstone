# Project Title

PrimaryED CMS

## Detailed project scope

https://cs50.harvard.edu/web/2020/projects/final/capstone/

## Overview

PrimaryEd CMS is a Learning Management System (LMS) designed for primary school teachers. It provides a platform to find, organize, and utilize educational resources, quizzes, and exercises for classroom learning. This project is developed as part of the CS50W course's final capstone project.

## Distinctiveness and Complexity

PrimaryEd CMS is a unique and complex project tailored specifically for primary education. It stands out with its specialised focus on providing a comprehensive resource repository and interactive tools for teachers. The complexity of the project is evident in its multifaceted features and the integration of various models that aggregate learning from previous projects into a more comprehensive web application.

### Key Models and Features

- **User Model**: Inherits from Django's `AbstractUser`, providing a foundation for user authentication and profile management.
- **Subject Model**: Manages subjects with fields for subject name and description, to appropriately organise the educational content.
- **Post Model**: Facilitates a community forum where teachers can share insights and discuss educational topics. It includes features for posting content, user association, timestamps, and likes.
- **UserExtended Model**: An extension of the User model, allowing for additional user-specific data and customisation.
- **ContactSubmission Model**: Handles user-submitted queries and feedback, storing them for admin review. This model includes fields for name, email, message, and submission timestamp.
- **Resource Model**: A versatile model for managing educational resources. It includes fields for title, description, file links, subject association, grade level, and resource type (e.g., Video, Document, Quiz).

### Testing

Comprehensive tests have been included to ensure the reliability and functionality of the models and views. These tests cover the creation and validation of subjects and posts, the functionality of the index view, and the listing of subjects in the SubjectListView.

### Forms and Admin Configuration

- **Forms**: Utilised to capture user data within the admin module, enhancing the interactivity and usability of the CMS.
- **Admin Model Setup**: Carefully configured to manage resources, subjects, and maintain user information effectively.

### UI Design

A significant emphasis was placed on UI design to ensure a modern, aesthetically consistent, mobile-responsive user experience. This approach caters to the needs of primary education professionals, providing them with an intuitive and engaging platform.

### Conclusion

In summary, PrimaryEd CMS exemplifies distinctiveness through its specialised focus on primary education and complexity through its integration of various Django features, building upon the learnings from previous projects within CS50W. The project not only serves as an educational resource repository but also fosters a community of educators through its forum and interactive tools. The application's backend and user-friendly frontend make it a comprehensive solution for primary school teachers' needs.

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

### Using pipenv (recommended)

1.  Ensure you have `pipenv` installed. If not, install it using `pip install pipenv`.
2.  Clone the repository: git clone https://github.com/mark-goudie/capstone.git
3.  Navigate to the project directory: cd capstone, and run `pipenv install` to set up the project environment and install dependencies.
4.  Activate the virtual environment: pipenv shell
5.  Install required packages: pip install -r requirements.txt
6.  Run migrations: python3 manage.py migrate
7.  Start the Django server: python3 manage.py runserver
8.  Access the application at http://localhost:8000/

### Using requirements.txt

If you prefer not to use pipenv, you can set up the project using a virtual environment and `requirements.txt`.

1. Clone the repository to your local machine.
2. Create a virtual environment in the project directory (`python -m venv venv`).
3. Activate the virtual environment (`source venv/bin/activate` on Unix/macOS or `venv\Scripts\activate` on Windows).
4. Install dependencies with `pip install -r requirements.txt`.
5. Run the application using `python3 manage.py runserver`.

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
