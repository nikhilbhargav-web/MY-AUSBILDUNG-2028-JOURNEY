# MY AUSBILDUNG 2028 - DAY 9
# PROJECT: STUDENT GRADE CALCULATOR
# GOAL: for loop + list combo master karna

# ===== GLOBAL LIST - Sab marks yahan =====
student_marks = [85, 92, 78, 65, 88, 95, 73, 45, 90, 67] # 10 students
student_names = ["Rohan", "Priya", "Amit", "Neha", "Vikram", "Sana", "Raj", "Anita", "Karan", "Pooja"]
pass_marks = 60

def calculate_total():
    """for loop se sab marks jodo"""
    total = 0
    for mark in student_marks: # Thaila ka har item nikalo
        total = total + mark # Total mein jodo
    return total

def calculate_average():
    """Average nikalo"""
    total = calculate_total()
    student_count = len(student_marks) # Kitne student
    average = total / student_count
    return average

def show_pass_fail():
    """Har student pass ya fail - for loop se"""
    print("\n----- PASS/FAIL REPORT -----")
    for i in range(len(student_names)): # 0 se 9 tak index
        name = student_names[i]
        mark = student_marks[i]

        if mark >= pass_marks:
            status = "PASS ✅"
        else:
            status = "FAIL ❌"

        print(f"{name}: {mark} marks - {status}")

def find_toppers():
    """Sabse zyada marks - for loop se"""
    highest = student_marks[0] # Pehle ko highest maan lo
    topper_name = student_names[0]

    for i in range(len(student_marks)):
        if student_marks[i] > highest: # Agar naya bada mila
            highest = student_marks[i]
            topper_name = student_names[i]

    print(f"\n----- TOPPER -----")
    print(f"{topper_name}: {highest} marks 🏆")

def show_all_marks():
    """for loop se sab print karo"""
    print("----- SAB MARKS -----")
    for i in range(len(student_names)):
        print(f"{i+1}. {student_names[i]} = {student_marks[i]} marks")

# ===== MAIN PROGRAM =====
def main():
    print("----- IGL STUDENT GRADE SYSTEM -----")
    show_all_marks()

    total = calculate_total()
    avg = calculate_average()

    print(f"\n----- CLASS REPORT -----")
    print(f"Total Students: {len(student_marks)}")
    print(f"Class Total: {total} marks")
    print(f"Class Average: {avg:.2f} marks")

    show_pass_fail()
    find_toppers()

# ===== PROGRAM START =====
main()