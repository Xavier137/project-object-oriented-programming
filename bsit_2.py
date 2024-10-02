class Bsit_2:
    def __init__(self, name, registration_number, course, year, semester):
        self.name = name
        self.registration_number = registration_number
        self.course = course
        self.year = year
        self.semester = semester

    def identify(self):
        student = {
            "name": self.name,
            "registration_number": self.registration_number,
            "course": self.course,
            "year": self.year,
            "semester": self.semester
        }
        return student

    def show(self):
        return {"student": self.identify()}

    def display_details(self):
        student_details = self.identify()
        details = (
            f"Name: {student_details['name']}\n"
            f"Registration Number: {student_details['registration_number']}\n"
            f"Course: {student_details['course']}\n"
            f"Year: {student_details['year']}\n"
            f"Semester: {student_details['semester']}\n"
        )
        return details

bsit_2 = Bsit_2("OKELLO JOHN", "S23B13/004", "BSIT", 2, 1)
print(bsit_2.display_details())