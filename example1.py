#task 1

## Given 5 students who are highschooler students, 
# create a subject score dictionary for each student with their respective scores in Math, Science, and English. 
# Then, calculate the average score for each student and print the results.

# Creating a subject score dictionary for each student
students_scores = {
    "Student1": {"Math": 85, "Science": 90, "English": 78},
    "Student2": {"Math": 92, "Science": 88, "English": 95}, 
    "Student3": {"Math": 76, "Science": 85, "English": 80},
    "Student4": {"Math": 89, "Science": 92, "English": 84},
    "Student5": {"Math": 95, "Science": 94, "English": 90}
}
# Calculating the average score for each student and printing the results
# using one liner average calculation and printing
average = [sum(scores.values()) / len(scores) for scores in students_scores.values()]

for i, avg in enumerate(average):
    print(f"Average score for Student{i+1}: {avg:.2f}")

# Task 2
## calculate the area and perimeter of a rectangle and square 
# using a function of you own or Math module.

def calculate_rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
def calculate_square_area_perimeter(side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter