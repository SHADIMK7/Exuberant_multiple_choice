# Exuberant_multiple_choice
## Overview
This project is a Django REST API application that allows users to register, log in, answer questions, and view their total score. It provides endpoints for user registration, authentication, question management, answering questions, and retrieving total scores.

## Technologies Used
- Django: Web framework for building the API.
- Django REST Framework: Toolkit for building RESTful APIs.
- SQLite: Database management system.
- Token Authentication: For user authentication and authorization.

## Features
- User Registration: Users can register with a username and password.
- User Authentication: Registered users can log in to the system using their credentials.
- Question Management: Admin users can create, update, delete, and list questions.
- Answer Questions: Authenticated users can answer questions.
- Total Score: Users can view their total score, including the number of correct and incorrect answers.

## Setup Instructions
1. Clone the repository to your local machine.
2. Install Python and pip if not already installed.
3. Install dependencies listed in the `requirements.txt` file using `pip install -r requirements.txt`.
4. Set up a MySQL database and update the database configuration in `settings.py`.
5. Run database migrations using `python manage.py migrate`.
6. Start the Django development server using `python manage.py runserver`.

## Code Explanation:

## Registration View:
1. This view handles user registration.
2. When a user registers, their information is validated.
3. If the information is valid, a new user account is created.
4. A unique token is generated for the user.
5. The token is sent back to the user for future authentication.

## Logout View:
1. This view handles user logout.
2. When a user logs out, their authentication token is deleted.
3. This effectively logs them out of the system.

## Question List and Create View:
1. This view provides a list of questions and allows the creation of new questions.
2. It fetches all questions from the database and sends them to the user.
3. Users can also create new questions through this endpoint.

## User Answer View:
1. This view records a user's answer to a question.
2. When a user submits an answer, it saves their choice along with the question ID and user ID.

## User Total Score View:
1. This view calculates the total score of a user based on their answered questions.
2. It counts how many questions the user has answered.
3. Then, it checks each answered question to see if the user's choice matches the correct answer.
4. Based on this, it calculates the total number of correct and incorrect answers.
5. Finally, it calculates the user's score as a percentage of correct answers out of the total number of questions.

## Token Authorization:
1. Token authorization is used to authenticate users and grant access to protected endpoints.
2. When a user registers or logs in, a token is generated and returned to the client.
3. The client must include this token in the request headers (typically as Authorization: Token <token_value>)to access protected endpoints.

