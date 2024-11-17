# COMP 125
# Assignment 2 
# Harmanjit Singh 300212091


# Used python to write this code because I already did python in my COMP150( Intorduction of Programming) and COMP155 (Object Oriented Programming) courses.

def calculate_grade_and_points(score):
    # Define the grade and quality points mapping
    grade_points = [
        (90, "A+", 4.33),
        (85, "A", 4.00),
        (80, "A-", 3.67),
        (77, "B+", 3.33),
        (73, "B", 3.00),
        (70, "B-", 2.67),
        (67, "C+", 2.33),
        (63, "C", 2.00),
        (60, "C-", 1.67),
        (50, "D", 1.00),
        (0, "F", 0.00),
    ]

    # Find the grade and quality points for the score
    for threshold, grade, points in grade_points:
        if score >= threshold:
            return grade, points


def main():
    # Get a valid user name
    while True:
        user_name = input("Enter your name: ").strip()  # used strip to remove the space from the beginning and the end
        if user_name.replace(" ", "").isalpha():   # after replacing space, used isalpha to ensure that the user enter the alphabets only
            break
        else:
            print("Invalid name. Please enter alphabetic characters only.")

    # Get a valid program name
    while True:
        program_name = input("Enter your program name: ").strip()  # used strip to remove the space from the beginning and the end
        if program_name:  # Check if it's non-empty
            break
        else:
            print("Invalid program name. Please enter a valid program name.")

    semesters = []
    while True:
        try:
            num_semesters = int(input("Enter the number of semesters: "))
            if 0 < num_semesters <= 20:
                break
            else:
                print("Enter a valid number between 1 and 20.")
        except ValueError:
            print("Enter valid number only.")

    for semester_num in range(1, num_semesters + 1):
        print(f"\n  Starting semester {semester_num}...")
        courses = []
        total_credits = 0
        entered_courses = set()  # Set to track entered course codes

        while total_credits <= 20:
            print(f"Current total credits: {total_credits}")
            action = input("Type 'a' to add a new course, 'd' to finish this semester: ").lower()

            if action == 'd':
                if total_credits < 9:
                    print("Error: At least 9 credits are required to calculate GPA.")
                else:
                    break
            elif action == 'a':
                while True:
                    course_code = input("Enter course code (e.g., COMP230): ").strip()
                    if course_code in entered_courses:
                        print("Error: This course has already been entered. Please enter a different course.")
                    else:
                        entered_courses.add(course_code)
                        break

                while True:
                    try:
                        score = float(input("Enter your score for the course (0-100): "))
                        if 0 <= score <= 100:
                            break
                        else:
                            print("Score must be between 0 and 100.")
                    except ValueError:
                        print("Enter a valid score.")

                grade, quality_points = calculate_grade_and_points(score)

                while True:
                    try:
                        credits = int(input("Enter the number of credits for the course (3 or 4): "))
                        if credits in [3, 4]:
                            break
                        else:
                            print("Credits must be either 3 or 4.")
                    except ValueError:
                        print("Enter a valid number of credits.")

                if total_credits + credits > 20:
                    print("Error: Total credits cannot exceed 20.")
                else:
                    courses.append({
                        "course_code": course_code,
                        "score": score,
                        "grade": grade,
                        "quality_points": quality_points * credits,
                        "credits": credits
                    })
                    total_credits += credits
            else:
                print("Invalid action. Please try again.")

        semesters.append(courses)

    total_quality_points_overall = 0
    total_credits_overall = 0

    for semester_num, courses in enumerate(semesters, start=1):
        print(f"\n  Results for Semester {semester_num}:\n")
        total_quality_points = 0
        total_credits = 0

        for course in courses:
            print(f"Course: {course['course_code']} "
                  f"    |   Credits: {course['credits']} "
                  f"    |   Score: {course['score']} "
                  f"    |   Grade: {course['grade']} "
                  f"    |   Quality Points: {course['quality_points']}")
            total_quality_points += course['quality_points']
            total_credits += course['credits']

        semester_gpa = total_quality_points / total_credits if total_credits > 0 else 0
        print(f"\nTotal Credits: {total_credits}    |   Total Quality Points: {total_quality_points}    |   GPA for Semester {semester_num}: {semester_gpa:.2f}")

        total_quality_points_overall += total_quality_points
        total_credits_overall += total_credits

    print("\n       Overall Results:\n")
    print(f"Total Credits: {total_credits_overall}  |   Total Quality Points: {total_quality_points_overall}", end=", ")

    if total_credits_overall > 0:
        cgpa = total_quality_points_overall / total_credits_overall
        print(f"    |   CGPA: {cgpa:.2f}\n")
    else:
        print("CGPA cannot be calculated.")


if __name__ == "__main__":
    main()
