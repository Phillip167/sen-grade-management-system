
Student Grade Management System
A lightweight, terminal-based Python application designed to manage student academic records. This system allows users to track students, record grades for various courses, calculate averages, and persist data to a local text file.

  Features
 -Data Persistence: Automatically saves and loads data from a grades.txt file.
 -Student Management: Add or delete students from the system.
 -Grade Tracking: Add, update, or remove grades for specific courses.
 - Automatic Calculations: View individual and class-wide averages.
  -Input Validation: Error handling for invalid IDs and out-of-range grades.
  Data Structure
The application organizes data using a list of dictionaries, structured as follows:

| Field | Type | Description |
|---|---|---|
| student_id | Integer | Unique identifier for each student. |
| name | String | Full name of the student. |
| courses | Dictionary | Key-value pairs of {Course_Name: Grade}. |

 Prerequisites
To run this script, you only need:
 -Python 3.x installed on your machine.
  -No external libraries are required (uses built-in os and io modules).

  Installation & Usage
  -Clone or Download the script to your local machine.
  -Open your terminal or command prompt.
  -Navigate to the folder containing the script.
  -Run the application using the following command:
   python your_filename.py

How it Works
The system uses a pipe-delimited (|) format for the flat-file database (grades.txt).

Example entry:
1|John Doe|Math:95.0|Science:88.0
Menu Options:
 Add Student: Register a new name and assign a unique ID.
 Add Grade: Assign a numeric score (0-100) to a specific course for a student.
  View All Students: Displays a summary of all students and their course list.
 View Student Details: Detailed view of a single student's performance.
 Update Grade: Modify an existing course grade.
  Delete Student/Course: Remove specific records from the database.

 Potential Fixes for your Code
 Constructor Fix: In Python, the constructor must be __init__ (double underscores). In your provided code, it is written as _init_ (single underscores), which will prevent the class from initializing correctly.
 - Entry Point Fix: Similarly, the bottom check should be if __name__ == "__main__":.

