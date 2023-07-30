# TodoList - Backend Project

TodoList is a backend project developed using Flask, HTML, CSS, Jinja2, Postman, and MongoDB. It serves as a backend application to manage todo lists efficiently.

## Technologies Used

- Flask: Python web framework for building the backend application.
- HTML: Markup language for creating the frontend templates.
- CSS: Stylesheet language for enhancing the user interface.
- Jinja2: Templating engine for rendering dynamic content in HTML templates.
- Postman: Tool for API development and testing.
- MongoDB: NoSQL database for storing todo list data.

## Getting Started

Follow these steps to set up the TodoList backend project:

1. Clone the repository: `git clone https://github.com/your-username/TodoList.git`
2. Navigate to the project directory: `cd TodoList`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up the MongoDB connection URL in the configuration file or as an environment variable.
5. Run the Flask application: `python app.py`

Ensure you have MongoDB installed and running on your system to connect to the database.

## API Endpoints

The TodoList backend project provides the following API endpoints:

- `GET /`: Retrieve Home Page.
- `GET /todos`: Retrieve all todo items.
- `GET /complete/:id`: Retrieve a specific todo item by its ID.
- `POST /add`: Create a new todo item.
- `DELETE /delete_completed`: Delete a todo item.
- `DELETE /delete_all`: Delete all todo item.

## Frontend Templates

The frontend templates are built using HTML and CSS, with dynamic content rendered using Jinja2 templates.

## Authentication

As this is a backend project, it might not include user authentication by default. However, you can extend it to include authentication using Flask extensions like Flask-Login or Flask-JWT.

## Contribution

Contributions to the TodoList backend project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
