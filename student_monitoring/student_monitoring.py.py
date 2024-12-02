import datetime
import json
import os


def line():
    print("=" * 50)


def key_list():
    try:
        with open("masterkeys.txt", "r") as f:
            master_keys = f.read().splitlines()
        return master_keys
    except FileNotFoundError:
        print("Invalid")
        return []
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


def sign_up_master_key(master_key):
    try:
        with open("masterkeys.txt", "a") as f:
            f.write(f"{master_key}\n")
        print("Masterkey saved")
    except Exception as e:
        print(f"Error occurred: {e}")


def verify_master_key(master_key):
    key = input("Enter masterkey: ")
    if key in master_key:
        return key
    else:
        print("Invalid")
        return None


def save_attendance(master_key, name, log):
    try:
        current_time = datetime.datetime.now()
        time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        week = current_time.strftime("%A")
        attendance_record = {
            f"name": name,
            f"log": log,
            f"time": time,
            f"week": week
        }
        file_attendance = f"{master_key}.json"
        if os.path.exists(file_attendance):
            with open(file_attendance, "r") as file:
                attendance_data = json.load(file)
        else:
            attendance_data = []

        attendance_data.append(attendance_record)

        with open(file_attendance, "w") as file:
            json.dump(attendance_data, file, indent=4)
        print("Attendance saved")
    except Exception as e:
        print(f"Error occurred when logging attendance: {e}")


def logging(master_key, name):
    try:
        if not name:
            raise ValueError("This cannot be empty")
        save_attendance(master_key, name, "log")
        print("Your attendance has been recorded")
    except Exception as e:
        print(f"Error occurred: {e}")


def view_attendance(master_key):
    file_attendance = f"{master_key}.json"
    try:
        with open(file_attendance, "r") as file:
            attendance_data = json.load(file)
            print("Name \t Log \t Time \t\t\t Day of Week")
            line()
            for record in attendance_data:
                print(f"{record['name']} \t {record['log']} \t {record['time']} \t {record['week']}")
    except FileNotFoundError:
        print("No attendance records found.")
    except Exception as e:
        print(f"Error occurred: {e}")




def main_menu(masterkeys): 
    while True:
        line()
        print("\n1. Write attendance")
        print("2. View attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            name = input("Enter the name of the student: ")
            logging(masterkeys, name)
        elif choice == "2":
            print()
            print("This is the attendance record")
            view_attendance(masterkeys) 
        elif choice == "3":
            print("Thank you. Have a nice day!")
            break
        else:
            print("Select a valid choice")


def main():
    master_key = key_list()
    while True:
        line()
        print("Welcome to Online attendance sheet")
        line()

        print("\n1. Create master key: ")
        print("2. Enter the master key:")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter masterkey: ")
            sign_up_master_key(key)
            master_key.append(key)
        elif choice == "2":
            masterkeys = verify_master_key(master_key)
            if masterkeys:
                main_menu(masterkeys) 
        elif choice == "3":
            print("Have a good day!!")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
