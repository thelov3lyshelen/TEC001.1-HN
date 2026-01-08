import json
import os

GRADEBOOK_FILE = 'gradebook.json'

def load_data():
    if os.path.exists(GRADEBOOK_FILE):
        with open(GRADEBOOK_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(GRADEBOOK_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def add_course(data):
    code = input("Course code: ").strip()
    if code in data:
        print("Course code already exists.")
        return
    name = input("Course name: ").strip()
    credits = int(input("Credits: "))
    semester = input("Semester: ").strip()
    score = float(input("Score (0–100): "))
    if not (0 <= score <= 100):
        print("Invalid score.")
        return
    data[code] = {
        "name": name,
        "credits": credits,
        "semester": semester,
        "score": score
    }
    print("Course added.")

def update_course(data):
    code = input("Course code to update: ").strip()
    if code not in data:
        print("Course not found.")
        return
    print("Leave field blank to keep current value.")
    name = input(f"New name ({data[code]['name']}): ") or data[code]['name']
    credits = input(f"New credits ({data[code]['credits']}): ")
    semester = input(f"New semester ({data[code]['semester']}): ") or data[code]['semester']
    score = input(f"New score ({data[code]['score']}): ")
    data[code] = {
        "name": name,
        "credits": int(credits) if credits else data[code]['credits'],
        "semester": semester,
        "score": float(score) if score else data[code]['score']
    }
    print("Course updated.")

def delete_course(data):
    code = input("Course code to delete: ").strip()
    if code in data:
        del data[code]
        print("Course deleted.")
    else:
        print("Course not found.")

def view_gradebook(data):
    if not data:
        print("Gradebook is empty.")
        return
    print(f"{'Code':<10}{'Name':<20}{'Credits':<8}{'Semester':<10}{'Score':<6}")
    for code, info in data.items():
        print(f"{code:<10}{info['name']:<20}{info['credits']:<8}{info['semester']:<10}{info['score']:<6}")

def calculate_gpa(data):
    if not data:
        print("No courses to calculate GPA.")
        return
    total_points = 0
    total_credits = 0
    semester_gpa = {}
    for info in data.values():
        grade_point = score_to_gpa(info['score'])
        total_points += grade_point * info['credits']
        total_credits += info['credits']
        sem = info['semester']
        semester_gpa.setdefault(sem, []).append((grade_point, info['credits']))
    print(f"Overall GPA: {total_points / total_credits:.2f}")
    for sem, grades in semester_gpa.items():
         sem_points = sum(gp * cr for gp, cr in grades)
         sem_credits = sum(cr for _, cr in grades)
         print(f"{sem} GPA: {sem_points / sem_credits:.2f}")
 
def score_to_gpa(score):
     if score >= 93: return 4.0
     elif score >= 90: return 3.7
     elif score >= 87: return 3.3
     elif score >= 83: return 3.0
     elif score >= 80: return 2.7
     elif score >= 77: return 2.3
     elif score >= 73: return 2.0
     elif score >= 70: return 1.7
     elif score >= 67: return 1.3
     elif score >= 63: return 1.0
     elif score >= 60: return 0.7
     else: return 0.0
 
def main():
     data = load_data()
     while True:
         print("\nGradebook Menu:")
         print("1. Add course")
         print("2. Update course")
         print("3. Delete course")
         print("4. View gradebook")
         print("5. Calculate GPA")
         print("6. Exit")
         choice = input("Choose an option: ")
         if choice == '1': add_course(data)
         elif choice == '2': update_course(data)
         elif choice == '3': delete_course(data)
         elif choice == '4': view_gradebook(data)
         elif choice == '5': calculate_gpa(data)
         elif choice == '6':
             save_data(data)
             print("Goodbye!")
             break
         else:
             print("Invalid choice.")
 
if __name__ == "__main__":
    main()

