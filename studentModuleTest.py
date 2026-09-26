# this python file is to test all functionality of the student class
# we are using this module for login/registration

from modules.student import studentclass


def main():
    # step 1: student registration test
    email = input("enter your email: ")
    password = input("enter your password: ")

    s1 = studentclass()
    s1.set_username_and_password(email, password)
    print("Student registered successfully.")

    full_name = input("enter your name: ")
    dob = input("enter your date of birth: ")
    gender = input("enter your gender: ")
    mobile_number = input("enter your mobile number: ")
    preferred_language = input("enter your preferred language: ")
    school_college_name = input("enter your school/college name: ")
    class_grade = input("enter your class/grade: ")
    board_curriculum = input("enter your board/curriculum: ")

    s1.set_personal_details(
        full_name,
        dob,
        gender,
        mobile_number,
        preferred_language,
        school_college_name,
        class_grade,
        board_curriculum,
    )
    print("Student profile updated successfully.")


if __name__ == "__main__":
    main()