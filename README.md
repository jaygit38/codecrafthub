README.md

  # CodeCraftHub - Simple Course Tracking Platform

  ## Project Overview

  CodeCraftHub is a simple Python-based application designed to help developers track the courses they
  want to learn. It provides a basic REST API for managing course data and stores the data in a JSON
  file. This project is a great starting point for learning Flask, JSON, and basic API development.

  ## Features

  *   **REST API:**  Provides CRUD (Create, Read, Update, Delete) operations for courses.
  *   **JSON Storage:** Stores course data in a `courses.json` file.
  *   **Simple Data Model:** Courses have a name, description, target completion date, and status.
  *   **Automatic File Creation:** Creates the `courses.json` file if it doesn't exist.
  *   **Clear Error Handling:** Handles missing fields, invalid data, and course not found errors.
  *   **Well-Documented:** Includes a comprehensive README file.

  ## Installation

  1.  **Prerequisites:** Make sure you have Python 3.7 or higher installed.
  2.  **Clone the repository:**
      ```bash
      git clone https://github.com/your-username/CodeCraftHub.git
      cd CodeCraftHub
      ```
  3.  **Run the application:**
      ```bash
      python app.py
      ```

  ## Running the Application

  After running the `python app.py` command, you should see a message indicating that the Flask
  development server is running. You can access the API endpoints in your browser or using a tool like
  `curl` or Postman.

  ## API Endpoints

  | Method   | Endpoint           | Description                     | Request Body (Example)
       | Response (Example)               |
  | :------- | :----------------- | :------------------------------ |
  :------------------------------------ | :------------------------------- |
  | POST     | `/api/courses`      | Create a new course              | `{"name": "Python Basics",
  "description": "Learn about Python", "target_date": "2026-07-01", "status": "Not Started"}`   |
  `{"id": 1, "name": "Python Basics", ...}`                |
  | GET      | `/api/courses`      | Get all courses                  | None
         | `[{"id": 1, "name": "Python Basics", ...}, {"id": 2, "name": "Data Structures", ...}]` |
  | GET      | `/api/courses/<id>` | Get a specific course            | None
         | `{"id": 1, "name": "Python Basics", ...}`                |
  | PUT      | `/api/courses/<id>` | Update a specific course         | `{"name": "Advanced Python",
  "description": "More Python concepts", "target_date": "2026-07-15", "status": "In Progress"}` |
  `{"id": 1, "name": "Advanced Python", ...}`                |
  | DELETE   | `/api/courses/<id>` | Delete a specific course          | None
          | `{"message": "Course deleted"}` |

  ## Testing

  Use `curl` to test the API endpoints:

  **Create a course:**

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Python Basics", "description": "Learn
  about Python", "target_date": "2026-07-01", "status": "Not Started"}'
  http://127.0.0.1:5000/api/courses

  Get all courses:

  curl http://127.0.0.1:5000/api/courses

  Get a specific course:

  curl http://127.0.0.1:5000/api/courses/1

  Update a course:

  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Advanced Python", "description": "More
  Python concepts", "target_date": "2026-07-15", "status": "In Progress"}'
  http://127.0.0.1:5000/api/courses/1

  Delete a course:

  curl -X DELETE http://127.0.0.1:5000/api/courses/1

  Troubleshooting

  - File Not Found:  If courses.json doesn't exist, the application will create it automatically.
  - Error 404 (Course Not Found):  The course ID you're using doesn't exist. Double-check the ID.
  - Error 400 (Bad Request): You've provided invalid data (missing fields, incorrect status, wrong
  date format).
