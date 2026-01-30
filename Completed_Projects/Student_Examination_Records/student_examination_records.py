from datetime import datetime
import json

STUDENT_ID_PREFIXES = {
            1: 'CIS3/', 
            2: 'CIS38/',
        }


class Student:
    def __init__(self, student_id, student_name, exam_date, student_cats_score, student_exam_score, student_total_score, unit_obj):
        self.unit = unit_obj
        self.student_id = student_id
        self.student_name = student_name
        self.exam_date = exam_date
        self.student_cats_score = student_cats_score
        self.student_exam_score = student_exam_score
        self.student_total_score = student_total_score
        
      
class Unit:
    def __init__(self, unit_name, unit_code):
        self.unit_name = unit_name
        self.unit_code = unit_code
        

#student details
def get_student_id():
    while True:
        student_id_prefix = input(
            """Student ID prefix:  
            Enter 1 for CIS3/
            Enter 2 for CIS38
            :  """)
        if not student_id_prefix:
            print("Student ID prefix cannot be empty")
            continue
        elif not student_id_prefix.isdigit():
            print("Please input 1 or 2 (numerical) according to instructions")
            continue
        
        student_id_prefix = int(student_id_prefix)
        
        if student_id_prefix not in STUDENT_ID_PREFIXES:
            print("Enter valid choice")
            continue
                
        student_chosen_prefix = STUDENT_ID_PREFIXES[student_id_prefix]
        
        student_id = input(f"Student ID: {student_chosen_prefix}")
        if not student_id:
            print("Student ID cannot be empty")
            continue
        
        full_student_id = STUDENT_ID_PREFIXES[student_id_prefix] + student_id
        
        return student_id, full_student_id


def get_student_name():
    while True:
        student_name = input("Student Name: ").strip()
        if not student_name:
            print("Student cannot be empty")
            continue
        elif not student_name.replace(" ", "").isalpha():
            print("Please input alphabetical values only")
            continue
            
        return student_name


def get_exam_date():
    while True:
        exam_date = input("Date student did the exam(MM/YY): ")
        if not exam_date:
            exam_date = datetime.now().strftime('%m/%Y')
            print(f"Set to today's date: {exam_date}")
            
        try:
            datetime.strptime(exam_date, '%m/%Y')
        except ValueError:
            print("Please enter correct format. Eg 02/2026")
            continue
        
        return exam_date


def get_scores():
    while True:
        try:
            student_cats_score = float(input("CAT 1 and CAT 2 score: "))
            student_exam_score = float(input("Student exam score: "))
            
            student_total_score = student_cats_score + student_exam_score
            
            print(f"Student total score: {student_total_score}")
            
            return student_cats_score, student_exam_score, round(student_total_score, 2)

        except ValueError:
            print("Kindly input numerical values only")
                    

def unit_details():
    while True:
        unit_name = input("Unit name: ").strip()
        if not unit_name:
            print("Unit name cannot be empty")
            continue
        
        unit_code = input("Unit code: ")
        if not unit_code:
            print("Unit code cannot be empty")
            continue
        break
    
    return unit_name, unit_code


# def save_students():    
#     with open('Students Examination Records.json', 'w') as f:
#         json.dump(students_records, f, indent=4)
#     print("💾")
        
        
# def load_students():
#     global students_records
#     try:
#         with open('Students Examination Records.json', 'r') as f:
#             students_records = json.load(f)
#     except(FileNotFoundError):
#         students_records = []


def get_student_details():
    while True:
        unit_name, unit_code = unit_details()
        unit_obj = Unit(unit_name, unit_code)
        student_id, full_student_id = get_student_id()
        student_name = get_student_name()
        exam_date = get_exam_date()
        student_cats_score, student_exam_score, student_total_score  = get_scores()
        
        comment = input("Add a comment: ")
        
        student_details = Student(unit_obj, student_id, student_name, exam_date, student_cats_score, student_exam_score, student_total_score)
        
        students_records.append(student_details)

        print(f"   Student Name: {student_name}\n   Student ID: {full_student_id}\n   Unit Name: {unit_name}\n   Unit Code: {unit_code}\nSaved Successfully.") 
        #save_students()
        
        add_student = input("Add student(y/n): ").lower()
        if add_student == 'y':
            continue
        elif add_student == 'n':
            break
        
        return student_details
    
    
students_records = []

def main():
    #load_students()
    
    get_student_details()
        
    
if __name__ == '__main__':
    main()



        





