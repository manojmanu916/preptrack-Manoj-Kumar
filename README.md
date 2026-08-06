# PrepTrack — Placement Preparation Performance Analyzer

# Project Title

**PrepTrack — Placement Preparation Performance Analyzer**

# Project Overview

PrepTrack is a Python console application designed to analyze student performance and determine placement interview readiness. The application collects student profile information (`student_name`, `registration_number`, `graduation_year`), attendance percentage (`attendance`), project completion status (`project_completed`), profile verification status (`profile_verified`), and seven daily coding-practice scores.

The program performs comprehensive input validation, score classification, highest and lowest score tracking, first critical score detection, average score calculation, placement eligibility evaluation, and final readiness analysis without using built-in list data structures. Finally, it generates a structured report displaying the student's practice summary, performance analysis, critical score information, placement readiness, primary blocker, and recommended next action.

# Features Implemented

### Student Details Processing

- Non-empty student name validation loop (`student_name`)
- Registration number input collection (`registration_number`)
- Graduation year input collection (`graduation_year`)
- Attendance percentage validation loop enforcing the range **0–100%** (`attendance`)
- Yes/No validation loop for project completion (`project_completed`)
- Yes/No validation loop for profile verification (`profile_verified`)

### Practice & Score Processing

- Seven-day practice processing using `for day in range(1, 8)`
- Score validation loop supporting **-1** for absent days or scores between **0 and 100**
- Absent day handling using the `continue` statement
- Daily score classification into:
  - Strong (75–100)
  - Satisfactory (60–74)
  - Needs Improvement (40–59)
  - Critical (0–39)
- Tracking:
  - Attempted Days
  - Absent Days
  - Passed Days
  - Failed Days
- Performance category counting:
  - Strong Days
  - Satisfactory Days
  - Needs Improvement Days
  - Critical Days

### Performance & Critical Score Analytics

- Total score accumulation (`total_score`)
- Average score calculation (`average_score`) with division-by-zero protection
- Highest score tracking (`highest_score`, `highest_score_day`)
- Lowest score tracking (`lowest_score`, `lowest_score_day`)
- Initialization using `first_attempt_found`
- First critical score tracking using:
  - `critical_score_found`
  - `first_critical_day`
  - `first_critical_score`
- Displays **Not Available** for highest and lowest scores when no practice is attempted
- Displays **Not Applicable** when no critical score exists

### Placement Readiness & Final Decision

- Placement eligibility evaluation using multiple conditions
- Priority-based decision logic
- Final Status generation
- Primary Blocker identification
- Next Action recommendation
- Placement Ready indicator
- Structured **PREPTRACK REPORT** generation

# Python Concepts Used

- Basic Input / Output (`input()`, `print()`)
- Type Casting (`int()`, `float()`)
- Variables
- Primitive Data Types
  - String
  - Integer
  - Float
  - Boolean
- Arithmetic Operators
- Comparison Operators
- Logical Operators (`and`, `or`, `not`)
- Conditional Statements (`if`, `elif`, `else`)
- Nested Conditions
- `while` Loop
- `for` Loop with `range()`
- Loop Control Statements (`break`, `continue`)
- Boolean Expressions
- Counters
- Accumulators
- Formatted Output using f-strings
- Precision Formatting (`{average_score:.2f}`)

# Instructions to Run the Program

To execute the application, run the following command:

```bash
python main.py
```

or

```bash
python3 main.py
```

## Steps to Run

1. Install Python 3.x on your system.
2. Open the project folder.
3. Open a terminal or command prompt.
4. Navigate to the project directory.
5. Execute the program using:

```bash
python main.py
```

6. Enter the required student details.
7. Enter the attendance percentage.
8. Enter project completion status (`yes` or `no`).
9. Enter profile verification status (`yes` or `no`).
10. Enter practice scores for all seven days (`0–100`) or `-1` for an absent day.
11. View the generated PrepTrack report.

# Sample Output

==================================================
              PREPTRACK APPLICATION
==================================================
Enter student name: Manoj Kumar
Enter registration number: KODJGP0D2
Enter graduation year: 2026
Enter attendance percentage: 90
Attendance accepted.
Has the student completed the required project? (yes/no): yes
Is the student profile verified? (yes/no): yes
Enter Day 1 score (0-100) or -1 for absent:98
Score accepted.
Day 1 Performance : Strong
Enter Day 2 score (0-100) or -1 for absent:89
Score accepted.
Day 2 Performance : Strong
Enter Day 3 score (0-100) or -1 for absent:87
Score accepted.
Day 3 Performance : Strong
Enter Day 4 score (0-100) or -1 for absent:75
Score accepted.
Day 4 Performance : Strong
Enter Day 5 score (0-100) or -1 for absent:-1
Score accepted.
Day 5 Result : Absent
Enter Day 6 score (0-100) or -1 for absent:68
Score accepted.
Day 6 Performance : Satisfactory
Enter Day 7 score (0-100) or -1 for absent:59
Score accepted.
Day 7 Performance : Needs Improvement

==================================================
              PREPTRACK REPORT
==================================================
Student Name           : Manoj Kumar
Registration Number    : KODJGP0D2
Graduation Year        : 2026
Attendance             : 90.00%

Project Completed      : Yes
Profile Verified       : Yes

PRACTICE SUMMARY
--------------------
Total Practice Days    : 7
Attempted Days         : 6
Absent Days            : 1
Passed Days            : 5
Failed Days            : 1

PERFORMANCE ANALYSIS
----------------------
Strong Days            : 4
Satisfactory Days      : 1
Needs Improvement Days : 1
Critical Days          : 0

Total Score            : 476
Average Score          : 79.33

Highest Score          : 98
Highest Score Day      : Day 1
Lowest Score           : 59
Lowest Score Day       : Day 7

First Critical Day     : Not Applicable
First Critical Score   : Not Applicable

FINAL DECISION
------------------
Placement Ready        : Yes

Final Status           : Ready for Mock Interview
Primary Blocker        : None
Next Action            : Proceed to the mock interview.
==================================================

# Test-Result Summary
<h1>Test-Result Summary</h1>

<table>
<tr>
<th>Test ID</th>
<th>Scenario</th>
<th>Expected Result</th>
<th>Actual Result</th>
<th>Status</th>
</tr>

<tr>
<td>TC-01</td>
<td>All eligibility conditions satisfied</td>
<td>Ready for Mock Interview</td>
<td>Ready for Mock Interview</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-02</td>
<td>One critical score (&lt;40)</td>
<td>Critical Support Required</td>
<td>Critical Support Required</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-03</td>
<td>Project not completed</td>
<td>Project Incomplete</td>
<td>Project Incomplete</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-04</td>
<td>Profile not verified</td>
<td>Profile Verification Pending</td>
<td>Profile Verification Pending</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-05</td>
<td>Attendance below minimum (75%)</td>
<td>Attendance Improvement Required</td>
<td>Attendance Improvement Required</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-06</td>
<td>Graduation year outside eligible range (2025–2027)</td>
<td>Graduation Not Eligible</td>
<td>Graduation Not Eligible</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-07</td>
<td>Empty student name</td>
<td>Prompted until a valid name is entered</td>
<td>Prompted until a valid name is entered</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-08</td>
<td>Invalid attendance (less than 0 or greater than 100)</td>
<td>Prompted until valid attendance is entered</td>
<td>Prompted until valid attendance is entered</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-09</td>
<td>Invalid project/profile input</td>
<td>Prompted until "yes" or "no" is entered</td>
<td>Prompted until "yes" or "no" is entered</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-10</td>
<td>Invalid practice score (&gt;100 or &lt;-1)</td>
<td>Prompted until a valid score is entered</td>
<td>Prompted until a valid score is entered</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-11</td>
<td>All seven practice days absent (-1)</td>
<td>Practice Not Evaluated</td>
<td>Practice Not Evaluated</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-12</td>
<td>Highest and lowest score tracking</td>
<td>Correct highest and lowest score with corresponding day displayed</td>
<td>Correct values displayed</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-13</td>
<td>Average score calculation</td>
<td>Average displayed with two decimal places</td>
<td>Average displayed correctly</td>
<td>✅ Pass</td>
</tr>

<tr>
<td>TC-14</td>
<td>Multiple blockers present</td>
<td>Highest-priority blocker displayed</td>
<td>Correct blocker displayed</td>
<td>✅ Pass</td>
</tr>

</table>

# Project Structure

```text
preptrack-Manoj-Kumar/
│
├── main.py
├── README.md
└── output.txt
```
# Individual Contribution

**Name:** Manoj Kumar

**Repository URL:** *(Add your GitHub repository URL here)*

### My Main Contribution

Implemented the complete execution flow in `main.py`, including student profile validation, attendance validation, project and profile verification, seven-day practice score processing, performance classification, placement eligibility evaluation, and generation of the final PrepTrack report.

### Features I Implemented

- Student information validation
- Attendance validation
- Project completion validation
- Profile verification validation
- Seven-day practice score processing
- Practice score validation
- Absent day handling using `continue`
- Highest score tracking
- Lowest score tracking
- Performance classification
- Passed and failed day counting
- First critical score detection
- Total score calculation
- Average score calculation
- Placement eligibility evaluation
- Final decision generation
- Placement readiness evaluation
- Complete formatted report generation

### Python Concepts I Used

- Variables
- Integer, Float, String and Boolean Data Types
- Input and Output
- Type Casting
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Assignment Operators
- `if`, `elif`, `else`
- Nested Conditions
- `while` Loop
- `for` Loop
- `range()`
- `break`
- `continue`
- Boolean Expressions
- Counters
- Accumulators
- Formatted Output using f-strings

### Most Difficult Logic

The most challenging part of the project was implementing the highest score and lowest score tracking without using lists, arrays, or built-in functions such as `max()` and `min()`. Another challenge was correctly storing only the first critical score while continuing to process the remaining practice days.

### Problem I Faced

Initially, it was difficult to ensure that absent practice days (`-1`) were excluded from total score calculation, average score calculation, highest score tracking, and lowest score tracking. Maintaining accurate counters while processing all seven practice days also required careful control flow.

### How I Solved It

I handled absent days immediately after score validation by incrementing `absent_days` and using the `continue` statement to skip further processing for that day. I also used the `first_attempt_found` flag to initialize the first valid score before comparing subsequent scores, ensuring accurate highest and lowest score tracking.

# Code Review Completed

**Reviewed Member:** ______________________

**Repository URL:** ______________________

### What Was Done Well

- Student information validation was implemented correctly.
- Attendance and practice score validation loops effectively handled invalid inputs.
- Absent practice days were correctly excluded from score calculations.
- Highest and lowest score tracking worked accurately without using lists or built-in functions.
- The final report was well structured, readable, and easy to understand.

### Issue Identified

The validation messages displayed during attendance and practice score input could provide clearer guidance about the accepted input values.

### Suggested Improvement

Display more descriptive validation messages to improve the user experience.

Examples:

- **Attendance:** `Enter a value between 0 and 100.`
- **Practice Score:** `Enter -1 for absent or a value between 0 and 100.`

These improvements make the application easier to use without changing the program logic.

# Feedback Received

**Reviewed By:** ______________________

### Feedback Received

The overall program logic is correct and follows the project requirements. The report formatting is clear, and the implementation is easy to understand. However, the validation messages can be made more descriptive so users immediately know the acceptable input range.

### Was the Feedback Valid?

**Yes**

### Change Made

Updated the attendance validation message to clearly specify the accepted range (**0 to 100**) and updated the practice score validation message to indicate that users should enter **-1 for an absent day** or **a value between 0 and 100**. The report formatting was also reviewed to maintain consistency throughout the application.

### Commit Message Used

```text
Improve input validation messages and report formatting based on peer review
```

# Improvement Made After Review

Based on the peer review feedback, the input validation messages were improved to provide clearer guidance during user input. The attendance validation now clearly specifies the accepted range (**0 to 100**), and the practice score validation explicitly states that users should enter **-1 for an absent day** or **a value between 0 and 100**.

After implementing these improvements, the application was tested again to verify that the validation logic, score processing, performance calculations, placement eligibility evaluation, and final report generation continued to work correctly without affecting the existing functionality.

# Acknowledgement

This project was developed as part of the **PrepTrack – Placement Preparation Performance Analyzer** assignment. It provided practical experience in applying Python fundamentals such as input validation, conditional statements, loops, counters, accumulators, Boolean logic, and formatted report generation. The project also helped strengthen problem-solving skills and reinforced the importance of writing structured, readable, and maintainable code.