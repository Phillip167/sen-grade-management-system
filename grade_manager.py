import os

class GradeManager:
    def _init(self):  # Fixed: Changed _init to _init_
        self.students = []  # List of student dicts: {'student_id': int, 'name': str, 'courses': {'Course': grade}}
        self.file_name = 'grades.txt'
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) < 2:
                        continue
                    student_id = int(parts[0])
                    name = parts[1]
                    courses = {}
                    for item in parts[2:]:
                        if ':' in item:
                            course, grade_str = item.split(':')
                            try:
                                grade = float(grade_str)
                                courses[course] = grade
                            except ValueError:
                                continue
                    self.students.append({
                        'student_id': student_id,
                        'name': name,
                        'courses': courses
                    })

    def save_data(self):
        with open(self.file_name, 'w') as file:
            for student in self.students:
                course_entries = [f"{course}:{grade}" for course, grade in student['courses'].items()]
                line = f"{student['student_id']}|{student['name']}|" + '|'.join(course_entries)
                file.write(line + '\n')

    def add_student(self, name):
        if not name.strip():
            print("Name cannot be empty.")
            return
        new_id = len(self.students) + 1
        self.students.append({
            'student_id': new_id,
            'name': name.strip(),
            'courses': {}
        })
        self.save_data()
        print(f"Student added: ID {new_id}, Name: {name.strip()}")

    def add_grade(self, student_id, course, grade_str):
        try:
            grade = float(grade_str)
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100.")
                return
        except ValueError:
            print("Grade must be a number.")
            return

        for student in self.students:
            if student['student_id'] == student_id:
                student['courses'][course.strip()] = grade
                self.save_data()
                print(f"Grade {grade} added for {course.strip()} (Student ID: {student_id})")
                return
        print(f"Student ID {student_id} not found.")

    def view_all_students(self):
        if not self.students:
            print("No students registered yet.")
            return
        print("\nStudent Records:")
        print("-" * 60)
        for student in self.students:
            avg = self.calculate_average(student['student_id'])
            avg_str = f"{avg:.2f}" if avg is not None else "N/A"
            print(f"ID: {student['student_id']} | Name: {student['name']} | Average: {avg_str}")
            for course, grade in student['courses'].items():
                print(f"   → {course}: {grade}")
            print("-" * 60)

    def view_student_details(self, student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                avg = self.calculate_average(student_id)
                avg_str = f"{avg:.2f}" if avg is not None else "N/A"
                print(f"\nDetails for Student ID {student_id}: {student['name']}")
                print("Courses and Grades:")
                if not student['courses']:
                    print("   No grades recorded.")
                else:
                    for course, grade in student['courses'].items():
                        print(f"   {course}: {grade}")
                print(f"   Average Grade: {avg_str}")
                return
        print(f"Student ID {student_id} not found.")

    def calculate_average(self, student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                if not student['courses']:
                    return None
                total = sum(student['courses'].values())
                return total / len(student['courses'])
        return None

    def update_grade(self, student_id, course, new_grade_str):
        try:
            new_grade = float(new_grade_str)
        except ValueError:
            print("Grade must be a number.")
            return
        for student in self.students:
            if student['student_id'] == student_id:
                if course.strip() in student['courses']:
                    student['courses'][course.strip()] = new_grade
                    self.save_data()
                    print(f"Grade for {course.strip()} updated to {new_grade}")
                    return
                else:
                    print(f"Course {course} not found for this student.")
                    return
        print(f"Student ID {student_id} not found.")

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student['student_id'] == student_id:
                del self.students[i]
                self.save_data()
                print(f"Student ID {student_id} deleted.")
                return
        print(f"Student ID {student_id} not found.")

    def delete_course_grade(self, student_id, course):
        for student in self.students:
            if student['student_id'] == student_id:
                if course.strip() in student['courses']:
                    del student['courses'][course.strip()]
                    self.save_data()
                    print(f"Grade for {course.strip()} deleted.")
                    return
                else:
                    print(f"Course {course} not found.")
                    return
        print(f"Student ID {student_id} not found.")


def main():
    manager = GradeManager()
    while True:
        print("\n=== Student Grade Management System ===")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View All Students")
        print("4. View Student Details")
        print("5. Update Grade")
        print("6. Delete Student")
        print("7. Delete Course Grade")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            manager.add_student(name)
        elif choice == '2':
            try:
                sid = int(input("Enter student ID: "))
                course = input("Enter course name: ")
                grade = input("Enter grade (0-100): ")
                manager.add_grade(sid, course, grade)
            except ValueError:
                print("Invalid student ID.")
        elif choice == '3':
            manager.view_all_students()
        elif choice == '4':
            try:
                sid = int(input("Enter student ID: "))
                manager.view_student_details(sid)
            except ValueError:
                print("Invalid student ID.")
        elif choice == '5':
            try:
                sid = int(input("Enter student ID: "))
                course = input("Enter course name: ")
                new_grade = input("Enter new grade: ")
                manager.update_grade(sid, course, new_grade)
            except ValueError:
                print("Invalid input.")
        elif choice == '6':
            try:
                sid = int(input("Enter student ID to delete: "))
                manager.delete_student(sid)
            except ValueError:
                print("Invalid student ID.")
        elif choice == '7':
            try:
                sid = int(input("Enter student ID: "))
                course = input("Enter course name to delete: ")
                manager.delete_course_grade(sid, course)
            except ValueError:
                print("Invalid student ID.")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== "_main_":  # Fixed: Changed _main to _main_
    main()