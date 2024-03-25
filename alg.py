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
            stud_answers[name] = answer

