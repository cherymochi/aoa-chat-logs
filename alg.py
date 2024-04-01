# Title:  Analysis of Algorithms Group Project -  Chat Grader
# Date: March 17, 2024 
# Contributors: 
# Nathalea Evans – 2101707 
# Tyler Myers – 2003217 
# Christopher Jugar – 1503860 
# Deiondre Emanuel - 2104559 




# Function that reads and prints chat log to screen from a given file path.
def read_chat_log(file_path):
    try:
        with open(file_path, 'r') as file:
            chat_log = file.read()
        return chat_log
    # Error Handling if File Not Found
    except FileNotFoundError:
        print("\n***No such chat file exists***")
        print("\nTry Again")
        return main()


def main():
    print("\n-=Chat Log Reader=-\n")

    # Prompt for username with error handling
    while True:
        profName = input("\nPlease state your username as it appears in the Chat : \n")
        if profName.strip():
            break
        else:
            print("\nInvalid username. Please try again.")

    file_path = input("Upload or enter the directory of the chat log file located your device: ")
    chat_log = read_chat_log(file_path)
    if chat_log:
        print("\nChat log Recovered:\n")
        print(chat_log)

        # Dictionary to store student names and answers
        stud_answers = {}

        # Open file for reading
        with open('chat.txt', 'r') as file:
            lines = file.readlines()  # Read all lines from the file

        # Iterate through lines of file
        for line in lines:
            if 'From' in line and 'To Everyone' in line:
                name = line.split('From ')[1].split(' To Everyone')[0]  # Get the name of the student
                answer = line.split(': ')[1].strip()  # Get the student's answer

                # Exclude teacher
                if name != profName:
                    stud_answers.setdefault(name, 0)
                    if answer:
                        if stud_answers[name] < 5:
                            stud_answers[name] += 1

        # Function to calculate grade percentage
        def calculate_grade_percentage(grade):
            return (grade / 5) * 100

        # Function to display grades
        def display_grades():
            for student, grade in stud_answers.items():
                percent = calculate_grade_percentage(grade)
                print(f'{student}\t\t{grade}\t{percent}%')

        print("\n\n------------------------------")
        print("Student Participation Grades")
        print("------------------------------\n")
        print("Name\t\t\tGrade\t\t%")

        display_grades()

if __name__ == "__main__":
    main()
