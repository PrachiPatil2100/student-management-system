import json

def load_data():
    try:
        with open("students_data.json","r") as file:
            return json.load(file)

    except FileNotFoundError:
        return[]
    

students = load_data()

def save_data():
    with open ("students_data.json","w") as file:
        json.dump(students,file, indent=4)

def add_student():
    name = input("Enter name of the student: ")
    age = int(input("Enter age of the student:"))
    roll_number = int(input("Enter the roll number of the student:"))
    for student in students:
        if student["roll_number"]==roll_number:
            print("\n⚠️ Error: This Roll Number already exists! Try again.")
            return
    
    student_data = { "name":name,
                     "age": age,
                     "roll_number":roll_number
                     }
    students.append(student_data)
    print("\n✅Student added successfully!")

def view_students():
    print("\n--- Student List ---")
    for student in students:
        print(student)

def search_student():
    search_roll = int(input("Enter Roll Number to search :"))
    for student in students:
        if student["roll_number"]== search_roll:
            print(f" \n🔍Found! Name : {student['name']} , Age : {student['age']}")
            return
    print("\n❌Student not Found!")
    
def delete_student():
    delete_roll = int(input("Enter Roll Number to delete :"))
    for student in students:
        if student['roll_number'] == delete_roll:
            students.remove(student)
            print("\n🗑️Student deleted successfully!", student)
            return
    print("\n❌Student not found!")
    
while True:     

    print("====================================")  
    print("Welcome to Student Management System")
    print("====================================")
    print("1. Add a New Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Delete a Student")
    print("5. Exit")
    print("====================================")

    user_choice = int(input("Enter your choice (1-5): "))

    if user_choice == 1:
        add_student()
        save_data()
    elif user_choice == 2:
        view_students()
    elif user_choice == 3:
        search_student()
    elif user_choice == 4:
        delete_student()
        save_data()
    elif user_choice == 5:
        print("\nExiting... Have a great day!")
        break
    else:
        print("\n⚠️Invalid choice! Please select between 1 and 5.")



