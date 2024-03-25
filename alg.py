# Dictionary to store student names and answers
stud_answers = {}

# Open file for reading
with open('chat.txt', 'r') as file:
    lines = file.readlines()  # Read all lines from the file
    
# Iterate through lines of file
for line in lines:
    if 'From' in line and 'To Everyone' in line:
        name = line.split('From ')[1].split(' To Everyone')[0] # Get the name of the student
        answer = line.split(': ')[1].strip() # Get the student's answer
        
        # Exclude teacher
        if name != 'Dr. Arnett Campell':
            stud_answers.setdefault(name, 0)
            if answer:
                if stud_answers[name] < 5:
                    stud_answers[name] += 1
                    
# Function to calculate grade percentage
def calculate_grade_percentage(grade):
    return (grade/5) * 100

# Function to display grades
def display_grades():
    for student, grade in stud_answers.items():
        percent = calculate_grade_percentage(grade)
        print(f'{student}: Grade {grade} - {percent} %')

display_grades()

