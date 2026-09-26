class studentclass:
    def __init__(
        self,
        full_name,
        date_of_birth,
        age,
        gender,
        mobile_number,
        email_address,
        preferred_language,
        school_name,
        class_grade,
        board,
        academic_year,
        subjects,
        current_level_by_subject,
        areas_of_help,
        parent_guardian=None,
    ):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.preferred_language = preferred_language
        self.school_name = school_name
        self.class_grade = class_grade
        self.board = board
        self.academic_year = academic_year
        self.subjects = subjects
        self.current_level_by_subject = current_level_by_subject
        self.areas_of_help = areas_of_help
        self.parent_guardian = parent_guardian

    def display(self):
        print(f"Student Name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.class_grade}")
        print(f"Subjects: {self.subjects}")
