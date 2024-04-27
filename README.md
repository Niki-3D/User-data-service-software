**Flask User Management App**

This Flask application serves as a simple user management system, allowing CRUD (Create, Read, Update, Delete) operations on user entities. It provides a RESTful API for managing users, with endpoints for listing all users, retrieving a user by ID, creating a new user, updating an existing user, and deleting a user.

### Features

- **User Creation**: Allows the creation of new users with attributes such as first name, last name, birth year, and group.
- **User Retrieval**: Provides endpoints for retrieving user information, either for a specific user by ID or for all users.
- **User Modification**: Supports updating existing user information, including first name, last name, birth year, and group.
- **User Deletion**: Enables the removal of users from the system by their ID.

### Endpoints

1. **Ping Endpoint**
   - **GET** `/ping`
   - Returns "pong" if the server is running.

2. **List All Users**
   - **GET** `/users`
   - Returns a JSON array of all users stored in the system.

3. **Get User by ID**
   - **GET** `/users/<int:id>`
   - Retrieves a user by their ID. Returns the user's information in JSON format.

4. **Create User**
   - **POST** `/users`
   - Creates a new user with the provided data. Requires JSON payload containing user information.

5. **Update User**
   - **PATCH** `/users/<int:id>`
   - Updates an existing user with the provided data. Requires JSON payload containing updated user information.

6. **Delete User**
   - **DELETE** `/users/<int:id>`
   - Deletes a user by their ID.

### Running the Application

1. Clone the repository: `git clone https://github.com/your_username/flask-user-management.git`
2. Navigate to the project directory: `cd flask-user-management`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Flask app: `python app.py`

The server will start running locally on `http://localhost:8080`.

### Testing

The application includes both unit and integration tests to ensure its functionality is working as expected. To run the tests:

1. Navigate to the project directory if not already there.
2. Run the tests using a test runner or individually:
   - For unit tests: `python -m unittest test_unit.py`
   - For integration tests: `python -m unittest test_integration.py`

### Dependencies

- **Flask**: A micro web framework for Python.
- **dataclasses**: Provides a decorator and functions for creating classes that act as immutable records.
- **pytest**: Testing framework for Python.
- **requests**: HTTP library for making requests.
- **json**: Library for working with JSON data in Python.

### Structure

- **app.py**: Main Flask application file containing all the endpoints.
- **src/**:
  - **repositories.py**: Contains the `UserRepository` class responsible for data management.
  - **repository_controllers.py**: Contains the `UserController` class, which acts as an interface between the Flask endpoints and the repository.
  - **status_codes.py**: Defines various HTTP status codes used throughout the application.
- **tests/**:
  - **test_unit.py**: Unit tests for individual components.
  - **test_integration.py**: Integration tests for testing the application's endpoints.

### Contributors

<nbrozyniak@gmail.com>

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
