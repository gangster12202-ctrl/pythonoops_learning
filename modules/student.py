class StudentClass:
    def __init__(self):
        self.full_name = None
        self.date_of_birth = None
        self.age = None
        self.gender = None
        self.mobile_number = None
        self.email_address = None
        self.password = None
        self.preferred_language = None
        self.school_college_name = None
        self.class_grade = None
        self.board_curriculum = None
        self.academic_year = None
        self.tuition_subjects = []
        self.subject_levels = {}
        self.topics_needing_help = []
        self.parent_guardian_name = None
        self.parent_guardian_relationship = None
        self.parent_guardian_mobile_number = None
        self.parent_guardian_email_address = None
        self.preferred_communication_method = None

    def set_username_and_password(self, email_address, password):
        self.email_address = email_address
        self.password = password
        return self

    def set_personal_details(
        self,
        full_name,
        date_of_birth,
        gender,
        mobile_number,
        preferred_language,
        school_college_name,
        class_grade,
        board_curriculum,
    ):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.mobile_number = mobile_number
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        return self


studentclass = StudentClass