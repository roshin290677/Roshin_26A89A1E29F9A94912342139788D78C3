class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name={self.name}, roll_number={self.roll_number}, cgpa={self.cgpa})"

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage
if __name__ == "__main__":
    # Creating student objects
    students = [
        Student("Alice", "A001", 3.8),
        Student("Bob", "B002", 3.6),
        Student("Charlie", "C003", 3.9),
        Student("David", "D004", 3.7)
    ]

    # Sorting students based on CGPA
    sorted_students = sort_students(students)

    # Displaying sorted students
    for student in sorted_students:
        print(student)