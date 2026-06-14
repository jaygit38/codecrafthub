from flask import Flask, jsonify, request
import json
import datetime

app = Flask(__name__)

# File to store courses
COURSES_FILE = "courses.json"

# Load courses from file on startup
def load_courses():
    try:
        with open(COURSES_FILE, "r") as f:
            courses = json.load(f)
    except FileNotFoundError:
        courses = []
    return courses

# Save courses to file on exit
def save_courses(courses):
    with open(COURSES_FILE, "w") as f:
        json.dump(courses, f, indent=4)

# Generate a unique ID for each course
def generate_id():
    if not hasattr(app, 'next_course_id'):
        app.next_course_id = 1
    else:
        app.next_course_id += 1
    return app.next_course_id

# Helper function to check if a course exists
def course_exists(course_id):
    courses = load_courses()
    return any(course['id'] == course_id for course in courses)

# --- API Endpoints ---

@app.route('/api/courses', methods=['POST'])
def create_course():
    """
    Creates a new course.
    Expected JSON payload:
    {
        "name": "Course Name",
        "description": "Course Description",
        "target_date": "YYYY-MM-DD",
        "status": "Not Started"
    }
    """
    data = request.get_json()
    required_fields = ["name", "description", "target_date", "status"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    if data["status"] not in ["Not Started", "In Progress", "Completed"]:
        return jsonify({"error": "Invalid status value"}), 400

    try:
        datetime.datetime.strptime(data["target_date"], "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid target_date format. Use YYYY-MM-DD"}), 400

    new_course = {
        "id": generate_id(),
        "name": data["name"],
        "description": data["description"],
        "target_date": data["target_date"],
        "status": data["status"],
        "created_at": datetime.datetime.now().isoformat()
    }

    courses = load_courses()
    courses.append(new_course)
    save_courses(courses)

    return jsonify(new_course), 201

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    Gets all courses.
    Returns:
    A JSON list of all courses.
    """
    courses = load_courses()
    return jsonify(courses)

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Gets a specific course by ID.
    Args:
        course_id (int): The ID of the course to retrieve.
    Returns:
    A JSON representation of the course if found.
    """
    courses = load_courses()
    for course in courses:
        if course['id'] == course_id:
            return jsonify(course)
    return jsonify({"error": "Course not found"}), 404

@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Updates a specific course by ID.
    Args:
        course_id (int): The ID of the course to update.
    Expected JSON payload:
    {
        "name": "New Course Name",
        "description": "New Course Description",
        "target_date": "YYYY-MM-DD",
        "status": "New Status"
    }
    """
    data = request.get_json()
    required_fields = ["name", "description", "target_date", "status"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    if data["status"] not in ["Not Started", "In Progress", "Completed"]:
        return jsonify({"error": "Invalid status value"}), 400

    try:
        datetime.datetime.strptime(data["target_date"], "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid target_date format. Use YYYY-MM-DD"}), 400

    courses = load_courses()
    for course in courses:
        if course['id'] == course_id:
            course['name'] = data['name']
            course['description'] = data['description']
            course['target_date'] = data['target_date']
            course['status'] = data['status']
            course['created_at'] = datetime.datetime.now().isoformat()
            save_courses(courses)
            return jsonify(course)
    return jsonify({"error": "Course not found"}), 404

@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Deletes a specific course by ID.
    Args:
        course_id (int): The ID of the course to delete.
    """
    courses = load_courses()
    courses = [course for course in courses if course['id'] != course_id]
    save_courses(courses)
    return jsonify({"message": "Course deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Enable debug mode for development
