class StudentInfo:# class created
    def __init__(self, id, name, age, school_name, completed_course, ongoing_course):
        self.id = id
        self.name = name
        self.age = age
        self.school_name = school_name
        self.completed_course = completed_course
        self.ongoing_course = ongoing_course 

    def viewAll(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, School: {self.school_name}")
        print(f"Completed Courses: {self.completed_course}")
        print(f"Ongoing Courses: {self.ongoing_course}")

    def showOngoing(self):
        print(f"Ongoing grades: {self.ongoing_course}") # which courses going on

    def showCompleted(self):
        print(f"Completed courses: {self.completed_course}") # which course completed

    def showAverageCompleted(self): #show the average of completed course
        if self.completed_course:
            avg = sum(self.completed_course.values()) / len(self.completed_course)
            print(f"Average grade: {avg:.2f}")
        else:
            print("No completed courses yet.")

    def showCourseGrade(self, course_name): #grades will be showed using this method
        course_name = course_name.title()
        if course_name in self.completed_course:
            print(f"{course_name}: Completed, Grade = {self.completed_course[course_name]}")
        elif course_name in self.ongoing_course:
            print(f"{course_name}: Ongoing, Current Grade = {self.ongoing_course[course_name]}")
        else:
            print("Sorry! Course not found.")


#  Create sample students
student1 = StudentInfo(
    1, "Harneet", 22, "ABC School",
    {"Physics": 50, "Math": 23, "Geo": 34},
    {"History": 67, "Arts": 55}
)

student2 = StudentInfo(
    2, "Har", 23, "XYZ School",
    {"Physics": 80, "Math": 70, "Geo": 90},
    {"History": 88, "Arts": 76}
)

# Use a dictionary for easy ID lookup
students = {
    1: student1,
    2: student2
}

#  Main Menu Loop
while True:
    print("\n===== Student Information System =====")
    print("1. View all students’ information")
    print("2. View information on specific student")
    print("3. View ongoing grades of specific student")
    print("4. View completed grades of specific student")
    print("5. View average completed grades of student")
    print("6. View specific grade of specific student")
    print("7. Exit")

    choice = input("Enter your choice (1–7): ")

    try:
        if choice == "1":
            for s in students.values():
                s.viewAll()

        elif choice == "2":
            sid = int(input("Enter Student ID: "))
            if sid in students:
                students[sid].viewAll()
            else:
                print(" Student not found.")

        elif choice == "3":
            sid = int(input("Enter Student ID: "))
            if sid in students:
                students[sid].showOngoing()
            else:
                print(" Student not found.")

        elif choice == "4":
            sid = int(input("Enter Student ID: "))
            if sid in students:
                students[sid].showCompleted()
            else:
                print(" Student not found.")

        elif choice == "5":
            sid = int(input("Enter Student ID: "))
            if sid in students:
                students[sid].showAverageCompleted()
            else:
                print(" Student not found.")

        elif choice == "6":
            sid = int(input("Enter Student ID: "))
            course = input("Enter Course Name: ")
            if sid in students:
                students[sid].showCourseGrade(course)
            else:
                print(" Student not found.")

        elif choice == "7":
            print(" Exiting program. Goodbye!")
            break

        else:
            print(" Invalid choice, please try again.")

    except ValueError:
        print(" Please enter a valid number.")

    again = input("\nWould you like to perform another query? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
