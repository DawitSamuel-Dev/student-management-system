# Import required Module
import os
import getpass
import datetime

#-------------------
# File paths
#-------------------

user_file = "user.txt"
student_file = "student.txt"
log_file = "activity_log.txt"

def log_activity(username, action):
    """
    log user action with timestamp
    """
    with open(log_file, "a") as log:
        log.write(f"{datetime.datetime.now()} - {username} - {action}\n")

def load_users():
    """
    Load users from file into a dictionary
    """
    users = {}
    if os.path.exists(user_file):
        with open(user_file, "r") as f:
            for line in f:
                if "," in line:
                    uname, pwd = line.strip().split(",",1)
                    users[uname] = pwd
    return users

def save_users(username, password):
    """
    save new user to the file
    """
    with open(user_file, "a") as f:
        f.write(f"{username}, {password}\n")
def authenticate():
    """
    Authenticate user login
    """
    users = load_users()
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")

    if username in users and users[username] == password:
        log_activity(username, "Logged in")
        print("\n✅) Login Successfil!\n")
        return username
    else:
        print("\n❌ Invalid credentials!\n")
        return None
def add_student(username):
    roll = input("Enter Roll Number:")
    name = input("Enter name:")
    grade = input("Enter grade: ")

    with open(student_file, "a") as f:
        f.write(f"{roll}, {name}, {grade}\n")
    log_activity(username, f"Add student {roll}")
    print("✅ Student added successfully!")
def view_students():
    if not os.path.exists(student_file):
        print("No record found.")
        return
    with open(student_file, "r") as f:
        print("\n--- Student Records ---")
        for line in f:
            roll, name, grade = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Grade: {grade}")
def search_student():
    roll_no = input("EnterRoll Number to search:")
    found = False

    if os.path.exists(student_file):
        with open(student_file, "r") as f:
            for line in f:
                # Skip empty or invalid lines
                parts = line.strip().split(",")
                if len(parts) != 3:
                    continue
                roll, name, grade = parts
                if roll == roll_no:
                    print(f"✅ Found: Roll: {roll} | Name: {name} | Grade: {grade}")
                    found = True
                    break

def update_student(username):
    roll_no = input("Enter Roll Number to update: ")
    students = []
    updated = False

    if os.path.exists(student_file):
        with open(student_file, "r") as f:
            students = f.readlines()

        with open(student_file, "w") as f:
            for line in students:
                roll, name, grade = line.strip().split(",")
                if roll == roll_no:
                    print(f"Current Date → Name: {name}, Grade: {grade}")
                    new_name = input("Enter new Name: ")
                    new_grade = input("Enter new Grade: ")
                    f.write(f"{roll}, {new_name}, {new_grade}\n")
                    update = True
                    log_activity(username, f"Update student {roll}")
                else:
                    f.write(line)
    if updated:
        print("✅ Student record update.")
    else:
        print("❌ Student not found.")

def delete_student(username):
    roll_no = input("Enter Roll Number to delete: ")
    students = []
    deleted = False

    if os.path.exists(student_file):
        with open(student_file, "r") as f:
            students = f.readlines()

        with open(student_file, "w") as f:
            for line in students:
                # Skip empty or invalid lines
                parts = line.strip().split(",")
                if len(parts) != 3:
                    f.write(line) # Keep invalid lines unchanged
                    continue
                roll, name, grade = parts
                if roll == roll_no:
                    deleted = True  # Log Deletion
                    log_activity(username, f"Deleted student {roll}")
                else:
                    f.write(line)
    if deleted:
        print("✅ Student record deleted.")
    else:
        print("❌ Student not found.")
def generate_report():
    if not os.path.exists(student_file):
        print("No records available.")
        return
    total = 0
    grades = {}
    with open(student_file, "r") as f:
        for line in f:
            roll, name, grade = line.strip().split(",")
            total += 1
            grades[grade] = grades.get(grade, 0) + 1
    print("\n📊 Student Report")
    print(f"Total Students: {total}")
    for g, count in grades.items():
        print(f"Grade {g}: {count} student(s")
def main():
    print("===== Student Management System =====")

    # Ensure admin user exists
    if not os.path.exists(user_file):
        print("No users found. Create an Admin account. ")
        uname = input("Set Admin Username: ")
        pwd = getpass.getpass("Set Admin Password: ")
        save_users(uname, pwd)
        print("✅ Admin created! Please restart the program.")
    username = None
    while not username:
        username = authenticate()
    # Menu
    while not username:
        print("\n--- Main Menu ---")
        print("1. Add Student")
        print("2. View all Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Generate Report")
        print("7. Logout & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(username)
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student(username)
        elif choice == "5":
            delete_student(username)
        elif choice == "6":
            generate_report()
        elif choice == "7":
            log_activity(username, "Logged out")
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")
if __name__=="__main__":
    main()







