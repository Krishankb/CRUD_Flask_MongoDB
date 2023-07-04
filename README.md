# CRUD_Flask_MongoDB
This is a flask and MongoDB application performing all the CRUD application.

The project is a Flask application utilizing MongoDB for performing CRUD operations. It allows users to create, read, update, and delete data through REST API endpoints. The application is containerized using Docker, providing a portable and scalable environment. Flask is used as the web framework, facilitating the development of the RESTful API. MongoDB acts as the database, storing and retrieving user information. With the integration of Flask, MongoDB, and Docker, the project enables efficient management and manipulation of data with CRUD functionalities.

The project utilizes **Flask**, **MongoDB**, and **Docker**. Flask is used as the web framework for building the REST API. MongoDB serves as the database for storing and retrieving data. Docker is employed for containerization, ensuring a portable and scalable deployment of the application.

To run the project, you have two options:

Option 1: Using Docker (recommended):
1. Install Docker on your system.
2. Clone or download the project repository.
3. Navigate to the project directory in the terminal.
4. Ensure the Dockerfile and requirements.txt are in the project directory.
5. Build the Docker image: `docker build -t myflaskapp .`
6. Run the Docker container: `docker run -p 5000:5000 myflaskapp`
7. Access the application at `http://localhost:5000`.
8. Perform CRUD operations on the User resource using the provided REST API endpoints.

Option 2: Without Docker:
1. Install Flask and PyMongo libraries.
2. Clone or download the project repository.
3. Navigate to the project directory in the terminal.
4. Run `python main.py`.
5. Access the application at `http://localhost:5000`.
6. Perform CRUD operations on the User resource using the provided REST API endpoints.

Both options allow you to run the Flask application with MongoDB and interact with it through the REST API endpoints.


Screenshot of the project : 

1. POST Method
![CR_post](https://github.com/Krishankb/CRUD_Flask_MongoDB/assets/30771097/6df949e7-b10f-4d73-8127-6dcb90699320)

![CR_post2](https://github.com/Krishankb/CRUD_Flask_MongoDB/assets/30771097/b556275f-12dd-4bb2-87fb-c6cec89a762a)

![CR_post3](https://github.com/Krishankb/CRUD_Flask_MongoDB/assets/30771097/85e9e52c-d377-4d7d-bedc-987c05a4dbad)


2. GET Method
![CR_getall](https://github.com/Krishankb/CRUD_Flask_MongoDB/assets/30771097/e982caa0-f7a8-48d9-b070-a967d5a2087e)

3.GET by ID Method
![CR_getone](https://github.com/Krishankb/CRUD_Flask_MongoDB/assets/30771097/ce016d59-0e20-4d37-a4a4-075f7b8d5ad5)


4. PUT Method
![CR_put](https://github.com/Krishankb/CRUD_Flask_MongoDB/assets/30771097/e8afb524-bb42-4006-8a83-ebbd2fd458c6)


5. DELETE Method
![CR_del](https://github.com/Krishankb/CRUD_Flask_MongoDB/assets/30771097/75a8f3a2-fe66-47d8-a035-99a48df9ff09)

