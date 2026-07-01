import json

def get_valid_integer(prompt_message):
    while True:
        try:
            user_input = int(input(prompt_message))
            return user_input 
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
        
def load_data():
    try:
        with open("students_data.json","r") as file:
            return json.load(file)

    except FileNotFoundError:
        return[]
    
    except json.JSONDecodeError:
            print("⚠️ Error: Data file is corrupted.")
            return []

    

students = load_data()

def save_data():
    with open ("students_data.json","w") as file:
        json.dump(students,file, indent=4)

def add_student():
    name = input("Enter name of the student: ")
    age = get_valid_integer("Enter age of the student:")
    roll_number = get_valid_integer("Enter the roll number of the student:")
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
    if len(students) == 0:
        print("\n❌ No students found. The list is empty!")
        return
    print("\n--- Student List ---")
    print(f"{'Name':<15} | {'Age':<5} | {'Roll No':<10}")

    for student in students:
        print(f"{student['name']:<15} | {student['age']:<5} | {student['roll_number']:<10}")

def search_student():
    search_roll = get_valid_integer("Enter Roll Number to search :")
    for student in students:
        if student["roll_number"]== search_roll:
            print(f" \n🔍Found! Name : {student['name']} , Age : {student['age']}")
            return
    print("\n❌Student not Found!")

def update_student():
    roll_to_update= get_valid_integer("Enter Roll Number to update :")
    for student in students:
        if student["roll_number"]==roll_to_update:
            new_name =input("Enter New Name :")
            new_age =get_valid_integer("Enter New Age :")
            student["name"] = new_name
            student["age"] = new_age
            print("✅ Student updated!")
            choice = input("Do you want to update Roll Number? (y/n): ")
   
            if choice=="y":
                new_roll =get_valid_integer("Enter New Roll number : ")
    
                for check_student in students:
                    if check_student["roll_number"]==new_roll:
                        print("Error: This roll number is already taken.")
                        return
                student["roll_number"]=new_roll

            print("✅ Student updated successfully!")
            return
    print("Error: Student with Roll Number",roll_to_update,"not found.")

    
def delete_student():
    delete_roll = get_valid_integer("Enter Roll Number to delete :")
    for student in students:
        if student['roll_number'] == delete_roll:
            students.remove(student)
            print("\n🗑️Student deleted successfully!", student)
            return
    print("\n❌Student not found!")

def clear_all_data():
    global students
    students = [] # RAM khali kar di
    save_data()   # File bhi khali kar di
    print("✅ All data cleared!")
    
while True:     

    print("====================================")  
    print("Welcome to Student Management System")
    print("====================================")
    print("1. Add a New Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Update a Student")
    print("5. Delete a Student")
    print("6. Exit")
    print("7. Clear All Data")
    print("====================================")

    try:
        user_choice = int(input("Enter your choice (1-7): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.")
        continue

    if user_choice == 1:
        add_student()
        save_data()
    elif user_choice == 2:
        view_students()
    elif user_choice == 3:
        search_student()
    elif user_choice==4:
        update_student()
        save_data()
    elif user_choice == 5:
        delete_student()
        save_data()
    elif user_choice == 6:
        print("\nExiting... Have a great day!💐")
        print("\nThank you for using Student Management System.\n")
        break
    elif user_choice == 7:
        clear_all_data()
    else:
        print("\n⚠️Invalid choice! Please select between 1 and 7.")



