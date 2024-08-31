# Sample student data
student_data = [
    {"student_name": "Ankur", "grades": {"Math": 85, "Science": 92, "English": 78}},
    {"student_name": "Priya", "grades": {"Math": 88, "Science": 79, "English": 95}},
    {"student_name": "Ravi", "grades": {"Math": 70, "Science": 85, "English": 80}},
    {"student_name": "Neha", "grades": {"Math": 90, "Science": 93, "English": 88}},
    {"student_name": "Amit", "grades": {"Math": 60, "Science": 75, "English": 70}},
]
print()
# Function to calculate the average grade for each student
def calculate_average_grades(data):
    averages = {}
    for student in data:
        grades = student["grades"]
        avg_grade = sum(grades.values()) / len(grades)
        averages[student["student_name"]] = avg_grade
    return averages

# Function to find the top-performing student
def find_top_student(averages):
    top_student = max(averages, key=averages.get)
    return top_student, averages[top_student]

# Function to calculate grade distribution
def calculate_grade_distribution(data):
    distribution = {}
    for student in data:
        for course, grade in student["grades"].items():
            if course in distribution:
                distribution[course].append(grade)
            else:
                distribution[course] = [grade]
    return distribution

# Function to find highest and lowest grades in each course
def find_highest_lowest_grades(distribution):
    highest_lowest = {}
    for course, grades in distribution.items():
        highest_lowest[course] = {
            "highest": max(grades),
            "lowest": min(grades)
        }
    return highest_lowest

# Running the analysis
average_grades = calculate_average_grades(student_data)
top_student, top_grade = find_top_student(average_grades)
grade_distribution = calculate_grade_distribution(student_data)
highest_lowest_grades = find_highest_lowest_grades(grade_distribution)

# Printing the results
print("Average Grades per Student:")
for student, avg in average_grades.items():
    print(f"  {student}: {avg:.2f}")

print(f"\nTop-Performing Student: {top_student} with an average grade of {top_grade:.2f}")

print("\nGrade Distribution by Course:")
for course, grades in grade_distribution.items():
    print(f"  {course}: {grades}")

print("\nHighest and Lowest Grades per Course:")
for course, grades in highest_lowest_grades.items():
    print(f"  {course}: Highest = {grades['highest']}, Lowest = {grades['lowest']}")
