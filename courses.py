from flask import Blueprint, jsonify
courses = Blueprint('courses', __name__)

courses_1 = [
    {'id': 1, 'name': 'Math', 'credit': '3'},
    {'id': 2, 'name': 'English', 'credit': '4'},
    {'id': 3, 'name': 'History', 'credit': '2'},
]

@courses.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses_1)

@courses.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    for course in courses_1:
        if course['id'] == course_id:
            return jsonify(course)

    return jsonify({'error': 'Course not found'}), 404
