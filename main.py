# ==================================================
# PREPTRACK — BOILERPLATE CODE
# Complete every section marked TODO.
# ==================================================

print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------

# Student Name
while True:
    student_name = input("Enter student name: ")

    if student_name != "":
        break

    print("Student name cannot be empty.")

# Registration Number
registration_number = input("Enter registration number: ")

# Graduation Year
graduation_year = int(input("Enter graduation year: "))

# Attendance
while True:
    attendance = float(input("Enter attendance percentage: "))

    if attendance >= 0 and attendance <= 100:
        print("Attendance accepted.")
        break

    print("Invalid attendance. Enter a value between 0 and 100.")

# Project Completed
while True:
    project_input = input(
        "Has the student completed the required project? (yes/no): "
    ).lower()

    if project_input == "yes" or project_input == "no":
        break

    print("Invalid input. Enter only yes or no.")

if project_input == "yes":
    project_completed = True
else:
    project_completed = False

# Profile Verified
while True:
    profile_input = input(
        "Is the student profile verified? (yes/no): "
    ).lower()

    if profile_input == "yes" or profile_input == "no":
        break

    print("Invalid input. Enter only yes or no.")

if profile_input == "yes":
    profile_verified = True
else:
    profile_verified = False

# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND VARIABLES
# --------------------------------------------------

total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0

# --------------------------------------------------
# 3. PROCESS SEVEN PRACTICE DAYS
# --------------------------------------------------

for day in range(1, 8):

    # ----------------------------
    # Score Validation
    # ----------------------------
    while True:

        score = int(
            input(
                f"Enter Day {day} score (0-100) or -1 for absent:"
            )
        )

        if score == -1 or (0 <= score <= 100):
            print("Score accepted.")
            break

        print("Invalid score. Enter -1 or a value between 0 and 100.")

    # ----------------------------
    # Handle Absent Day
    # ----------------------------
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result : Absent")
        continue

    # ----------------------------
    # Attempted Days & Total Score
    # ----------------------------
    attempted_days += 1
    total_score += score

    # ----------------------------
    # Highest & Lowest Score
    # ----------------------------
    if not first_attempt_found:

        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True

    else:

        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # ----------------------------
    # Score Classification
    # ----------------------------
    if score >= 75:
        strong_days += 1
        print(f"Day {day} Performance : Strong")

    elif score >= 60:
        satisfactory_days += 1
        print(f"Day {day} Performance : Satisfactory")

    elif score >= 40:
        improvement_days += 1
        print(f"Day {day} Performance : Needs Improvement")

    else:
        critical_days += 1
        print(f"Day {day} Performance : Critical")

    # ----------------------------
    # Passed / Failed
    # ----------------------------
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

    # ----------------------------
    # First Critical Score
    # ----------------------------
    if score < 40:

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

# --------------------------------------------------
# 4. CALCULATE THE AVERAGE
# --------------------------------------------------

if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0


# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------

graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)


# --------------------------------------------------
# 6. DETERMINE FINAL STATUS
# --------------------------------------------------

if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice attempted"
    next_action = "Complete at least one practice day."

elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = "Critical score found"
    next_action = "Improve the first critical score."

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Less than six practice attempts"
    next_action = "Complete at least six practice days."

elif passed_days < 4:
    final_status = "Practice Improvement Required"
    primary_blocker = "Less than four passed days"
    next_action = "Pass at least four practice days."

elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score below 70"
    next_action = "Improve the average score."

elif attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance below 75%"
    next_action = "Maintain attendance above 75%."

elif not graduation_eligible:
    final_status = "Graduation Not Eligible"
    primary_blocker = "Graduation year not eligible"
    next_action = "Check graduation eligibility."

elif not project_completed:
    final_status = "Project Incomplete"
    primary_blocker = "Project not completed"
    next_action = "Complete the required project."

elif not profile_verified:
    final_status = "Profile Verification Pending"
    primary_blocker = "Profile not verified"
    next_action = "Verify the student profile."

else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to the mock interview."


# --------------------------------------------------
# 7. DISPLAY FINAL REPORT
# --------------------------------------------------

print()
print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)

print(f"Student Name           : {student_name}")
print(f"Registration Number    : {registration_number}")
print(f"Graduation Year        : {graduation_year}")
print(f"Attendance             : {attendance:.2f}%")

print()
print(f"Project Completed      : {'Yes' if project_completed else 'No'}")
print(f"Profile Verified       : {'Yes' if profile_verified else 'No'}")

print()
print("PRACTICE SUMMARY")
print("-" * 20)

print("Total Practice Days    : 7")
print(f"Attempted Days         : {attempted_days}")
print(f"Absent Days            : {absent_days}")
print(f"Passed Days            : {passed_days}")
print(f"Failed Days            : {failed_days}")

print()
print("PERFORMANCE ANALYSIS")
print("-" * 22)

print(f"Strong Days            : {strong_days}")
print(f"Satisfactory Days      : {satisfactory_days}")
print(f"Needs Improvement Days : {improvement_days}")
print(f"Critical Days          : {critical_days}")

print()

print(f"Total Score            : {total_score}")
print(f"Average Score          : {average_score:.2f}")

print()

if attempted_days > 0:
    print(f"Highest Score          : {highest_score}")
    print(f"Highest Score Day      : Day {highest_score_day}")

    print(f"Lowest Score           : {lowest_score}")
    print(f"Lowest Score Day       : Day {lowest_score_day}")
else:
    print("Highest Score          : Not Available")
    print("Highest Score Day      : Not Available")

    print("Lowest Score           : Not Available")
    print("Lowest Score Day       : Not Available")

print()

if critical_score_found:
    print(f"First Critical Day     : Day {first_critical_day}")
    print(f"First Critical Score   : {first_critical_score}")
else:
    print("First Critical Day     : Not Applicable")
    print("First Critical Score   : Not Applicable")

print()
print("FINAL DECISION")
print("-" * 18)


print(f"Placement Ready        : {'Yes' if placement_ready else 'No'}")

print()
print(f"Final Status           : {final_status}")
print(f"Primary Blocker        : {primary_blocker}")
print(f"Next Action            : {next_action}")

print("=" * 50)