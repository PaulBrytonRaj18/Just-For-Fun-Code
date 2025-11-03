# Complete Python Program to Calculate Student's GPA and CGPA

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.semesters = []
    
    def add_semester(self, semester_courses):
        """
        Add a semester with courses
        semester_courses: list of tuples (course_name, credits, grade)
        grade can be letter grade (A, B, C, etc.) or grade points (0-10)
        """
        self.semesters.append(semester_courses)
    
    def letter_to_grade_point(self, letter_grade):
        """
        Convert letter grade to grade points (10-point scale)
        """
        grade_mapping = {
            'O': 10, 'A+': 10, 'A': 9, 'B+': 8, 'B': 7,
            'C+': 6, 'C': 5, 'D': 4, 'E': 0, 'F': 0
        }
        return grade_mapping.get(letter_grade.upper(), 0)
    
    def calculate_semester_gpa(self, semester_index):
        """
        Calculate GPA for a specific semester
        GPA = Sum of (Credits × Grade Points) / Total Credits
        """
        if semester_index >= len(self.semesters):
            return None
        
        semester_courses = self.semesters[semester_index]
        total_credits = 0
        weighted_sum = 0
        
        for course_name, credits, grade in semester_courses:
            # Convert letter grade to grade point if needed
            if isinstance(grade, str):
                grade_point = self.letter_to_grade_point(grade)
            else:
                grade_point = grade
            
            weighted_sum += credits * grade_point
            total_credits += credits
        
        if total_credits == 0:
            return 0
        
        gpa = weighted_sum / total_credits
        return round(gpa, 2)
    
    def calculate_cgpa(self):
        """
        Calculate CGPA (Cumulative GPA) across all semesters
        CGPA = Sum of all (Credits × Grade Points) / Total Credits across all semesters
        """
        total_credits = 0
        total_weighted_sum = 0
        
        for semester_courses in self.semesters:
            for course_name, credits, grade in semester_courses:
                # Convert letter grade to grade point if needed
                if isinstance(grade, str):
                    grade_point = self.letter_to_grade_point(grade)
                else:
                    grade_point = grade
                
                total_weighted_sum += credits * grade_point
                total_credits += credits
        
        if total_credits == 0:
            return 0
        
        cgpa = total_weighted_sum / total_credits
        return round(cgpa, 2)
    
    def display_results(self):
        """
        Display semester-wise GPA and overall CGPA
        """
        print("=" * 60)
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("=" * 60)
        
        for i, semester_courses in enumerate(self.semesters, 1):
            print(f"\nSemester {i} Courses:")
            print("-" * 60)
            print(f"{'Course Name':<30} {'Credits':<10} {'Grade':<10}")
            print("-" * 60)
            
            for course_name, credits, grade in semester_courses:
                print(f"{course_name:<30} {credits:<10} {grade:<10}")
            
            gpa = self.calculate_semester_gpa(i - 1)
            print("-" * 60)
            print(f"Semester {i} GPA: {gpa}")
        
        cgpa = self.calculate_cgpa()
        print("\n" + "=" * 60)
        print(f"Overall CGPA: {cgpa}")
        print("=" * 60)


# Example Usage
if __name__ == "__main__":
    # Create a student
    student = Student(input("Enter your name: "), input("Enter your student ID: "))
    
    # Semester 1
    semester1 = [
        ("Engineering Mathematics I", int(input("Enter the number of credits for Engineering Mathematics I: ")), input("\nEnter your grade for Engineering Mathematics I: ")),
        ("Programming in C", int(input("\nEnter the number of credits for Programming in C: ")), input("\nEnter your grade for Programming in C: ")),
        ("Engineering Physics", int(input("\nEnter the number of credits for Engineering Physics: ")), input("\nEnter your grade for Engineering Physics: ")),
        ("Communication English", int(input("\nEnter the number of credits for Communication English: ")), input("\nEnter your grade for Communication English: ")),
        ("Engineering Graphics", int(input("\nEnter the number of credits for Engineering Graphics: ")), input("\nEnter your grade for Engineering Graphics: ")),
        ("Heritage of Tamil", int(input("\nEnter the number of credits for Heritage of Tamil: ")), input("\nEnter your grade for Heritage of Tamil: "))
    ]
    student.add_semester(semester1)
    
    # Semester 2
    semester2 = [
        ("Engineering Mathematics II", int(input("Enter the number of credits for Engineering Mathematics II: ")), input("\nEnter your grade for Engineering Mathematics II: ")),
        ("Data Structures", int(input("\nEnter the number of credits for Data Structures: ")), input("\nEnter your grade for Data Structures: ")),
        ("Digital Electronics", int(input("\nEnter the number of credits for Digital Electronics: ")), input("\nEnter your grade for Digital Electronics: ")),
        ("Environmental Science", int(input("\nEnter the number of credits for Environmental Science: ")), input("\nEnter your grade for Environmental Science: ")),
        ("Professional Ethics", int(input("\nEnter the number of credits for Professional Ethics: ")), input("\nEnter your grade for Professional Ethics: "))
    ]
    student.add_semester(semester2)
    
    # Display results
    student.display_results()
