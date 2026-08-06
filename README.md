# PrepTrack — Placement Preparation Performance Analyzer


## Project Title
PrepTrack — Placement Preparation Performance Analyzer

## Project Overview
PrepTrack is a Python console application that analyzes a student's placement-preparation performance and determines readiness for a placement mock interview. The application collects student profile information (`student_name`, `registration_number`, `graduation_year`), attendance percentage (`attendance`), project completion status (`project_completed`), profile verification status (`profile_verified`), and seven daily coding-practice scores. It performs input validation, score classification, highest/lowest score tracking, and critical-score detection entirely without lists, tuples, or built-in aggregation functions. Finally, it displays a complete formatted report showing the practice summary, performance analysis, critical score information, and the final placement decision.

## Features Implemented
- **Student Details Processing**:
  - Non-empty student name input validation loop (`student_name`)
  - Registration number input collection (`registration_number`)
  - Graduation year input collection (`graduation_year`), evaluated later during eligibility checking
  - Attendance percentage validation loop enforcing range 0–100 with an "Attendance accepted." confirmation message (`attendance`)
  - Case-insensitive `yes`/`no` validation loops (using `.lower()`) converting inputs into Boolean flags for project completion (`project_completed`) and profile verification (`profile_verified`)

- **Practice & Score Processing**:
  - Seven-day practice loop processing (`for day in range(1, 8)`)
  - Score validation loop supporting `-1` for absence or `0–100` score range, with a "Score accepted." confirmation message
  - Absence handling with `absent_days` counter, a dedicated "Absent" result line, and `continue` control flow
  - Four-tier daily performance classification: Strong (75–100), Satisfactory (60–74), Needs Improvement (40–59), and Critical (0–39)
  - Tracking of practice engagement metrics: Attempted Days, Absent Days, Passed Days (score ≥ 60), and Failed Days (score < 60)
  - Detailed score category counts for Strong Days, Satisfactory Days, Needs Improvement Days, and Critical Days

- **Performance & Critical Score Analytics**:
  - Total score accumulation (`total_score`) and average score calculation (`average_score`) formatted to 2 decimal places with zero-division protection
  - List-free high/low score detection tracking `Highest Score`, `Highest Score Day`, `Lowest Score`, and `Lowest Score Day` using an initialization flag (`first_attempt_found`)
  - Fallback display handling ("Not Available") for highest/lowest metrics when no practice days were attempted
  - First critical score lock tracking (`Critical Score Found`, `First Critical Day`, `First Critical Score`) with fallback handling ("Not Applicable") when no critical score exists (score < 40)

- **Readiness Evaluation & Final Decision Report**:
  - Eight independent eligibility Boolean expressions (graduation year, attendance, practice count, average score, critical-score clearance, passed-days count, project completion, profile verification)
  - Combined `placement_ready` Boolean and explicit `Placement Ready` line in the report
  - Priority-based decision chain evaluating 9 status levels in order, so only the first major blocker is displayed
  - Determination of `Final Status`, `Primary Blocker`, and actionable `Next Action`
  - Clean formatted ASCII report terminal output (`PREPTRACK REPORT`) with structured sections (`PRACTICE SUMMARY`, `PERFORMANCE ANALYSIS`, `FINAL DECISION`)

## Python Concepts Used
- Basic Input / Output (`input()`, `print()`)
- Type Casting (`int()`, `float()`)
- Primitive Data Types & Variables (Strings, Integers, Floats, Booleans)
- Conditional Statements (`if`, `elif`, `else`)
- Boolean Operators & Logic (`and`, `not`)
- Loops (`while` for validation, `for` with `range(1, 8)`)
- Loop Control Keywords (`break`, `continue`)
- Increment Counters & Accumulators (`total_score`, `attempted_days`, `absent_days`, `passed_days`, `failed_days`, etc.)
- String Formatting & Precision Control (f-strings, `{attendance:.2f}`, `{average_score:.2f}`, inline ternary expressions)

## Instructions to Run the Program
To execute the application, run:

```bash
python main.py
```

or

```bash
python3 main.py
```

## Sample Output

```text
==================================================
              PREPTRACK APPLICATION
==================================================
Enter student name: Manoj
Enter registration number: PY24045
Enter graduation year: 2026
Enter attendance percentage: 82
Attendance accepted.
Has the student completed the required project? (yes/no): yes
Is the student profile verified? (yes/no): yes
Enter Day 1 score (0-100) or -1 for absent: 85
Score accepted.
Day 1 Performance : Strong
Enter Day 2 score (0-100) or -1 for absent: 78
Score accepted.
Day 2 Performance : Strong
Enter Day 3 score (0-100) or -1 for absent: 92
Score accepted.
Day 3 Performance : Strong
Enter Day 4 score (0-100) or -1 for absent: 60
Score accepted.
Day 4 Performance : Satisfactory
Enter Day 5 score (0-100) or -1 for absent: 35
Score accepted.
Day 5 Performance : Critical
Enter Day 6 score (0-100) or -1 for absent: -1
Score accepted.
Day 6 Result : Absent
Enter Day 7 score (0-100) or -1 for absent: 70
Score accepted.
Day 7 Performance : Satisfactory

==================================================
              PREPTRACK REPORT
==================================================
Student Name           : Manoj
Registration Number    : PY24045
Graduation Year        : 2026
Attendance             : 82.00%

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
Strong Days            : 3
Satisfactory Days      : 2
Needs Improvement Days : 0
Critical Days          : 1

Total Score            : 420
Average Score          : 70.00

Highest Score          : 92
Highest Score Day      : Day 3
Lowest Score           : 35
Lowest Score Day       : Day 5

First Critical Day     : Day 5
First Critical Score   : 35

FINAL DECISION
------------------
Placement Ready        : No

Final Status           : Critical Support Required
Primary Blocker        : Critical score found
Next Action            : Improve the first critical score.
==================================================
```


## Test-Result Summary

| Test ID | Scenario | Expected Result | Actual Result | Status |
|---------|----------|-----------------|---------------|--------|
| TC-01 | All requirements satisfied | Ready for Mock Interview | Ready for Mock Interview | ✅ Pass |
| TC-02 | One score below 40 | Critical Support Required | Critical Support Required | ✅ Pass |
| TC-03 | Fewer than six attempted days | Practice Incomplete | Practice Incomplete | ✅ Pass |
| TC-04 | Fewer than four passed days | Practice Improvement Required | Practice Improvement Required | ✅ Pass |
| TC-05 | Average score below 70 | Practice Improvement Required | Practice Improvement Required | ✅ Pass |
| TC-06 | Attendance below 75 | Attendance Improvement Required | Attendance Improvement Required | ✅ Pass |
| TC-07 | Graduation year not eligible | Graduation Not Eligible | Graduation Not Eligible | ✅ Pass |
| TC-08 | Project incomplete | Project Incomplete | Project Incomplete | ✅ Pass |
| TC-09 | Profile not verified | Profile Verification Pending | Profile Verification Pending | ✅ Pass |
| TC-10 | All seven days absent | Practice Not Evaluated | Practice Not Evaluated | ✅ Pass |
| TC-11 | Invalid score below -1 | Input rejected, re-prompted | Input rejected, re-prompted | ✅ Pass |
| TC-12 | Invalid score above 100 | Input rejected, re-prompted | Input rejected, re-prompted | ✅ Pass |
| TC-13 | Exact boundary scores | Correct classifications | Correct classifications | ✅ Pass |
| TC-14 | Multiple blockers present | First major blocker displayed | First major blocker displayed | ✅ Pass |

## Individual Contribution
Name: Manoj Kumar

Repository URL: https://github.com/manojmanu916/preptrack-Manoj-Kumar.git

My main contribution: Implemented the complete execution flow in main.py — building input validation loops for all profile fields, constructing the seven-day practice analysis loop, tracking score metrics without any prohibited data structures, and establishing the priority-based final decision chain.

Features I implemented: Interactive input validation loops (student_name, attendance, project_input, profile_input, score); daily score classification and category counting; list-free tracking for highest_score and lowest_score; first critical score locking logic; eight eligibility Boolean expressions and a combined placement_ready flag; a 9-tier if-elif-else priority decision chain; and formatted terminal report rendering.

Python Concepts I used: while loops, for loops with range(), break, continue, if-elif-else structures, Boolean expressions, accumulators, type casting, and formatted f-strings.

Most difficult logic: Tracking highest_score and lowest_score across iterations without using lists, arrays, or built-in max()/min() functions, while correctly excluding absent days (-1) from every comparison.

Problem I faced: Making sure an absent day (-1) never got compared against lowest_score or added into total_score and average_score.

How I solved it: Placed the `if score == -1` check immediately after score validation to increment absent_days and trigger continue, skipping all classification and comparison logic for that day. Used the first_attempt_found flag to set the initial highest/lowest values on the first attempted day, then applied `>` and `<` comparisons only on subsequent attempted days.

## Code Review Completed

Reviewed Member: [Teammate name]

Repository URL:
[Teammate repository link]

What Was Done Well:
- The absent-day check (`if score == -1`) runs immediately after score validation and before any classification logic, so `continue` correctly skips highest/lowest comparison, total_score accumulation, and passed/failed counting for that day.
- The highest/lowest score logic uses the `first_attempt_found` flag to seed both values from the first attempted day instead of defaulting to 0, which correctly avoids a false low score when a student's actual scores are all above 0.

Issue Identified:
- The `final_status` strings do not exactly match the status table in Part 24 of the PRD. "Practice Improvement Required" is reused for both the "fewer than four passed days" condition and the "average below 70" condition, even though the PRD defines these as two distinct statuses ("Insufficient Passed Practices" and "Practice Improvement Required"). Similarly, "Graduation Not Eligible", "Project Incomplete", and "Profile Verification Pending" don't match the PRD's specified wording ("Graduation Criteria Not Met" and "Application On Hold" for both the project and profile cases).

Suggested Improvement:
- Update each `final_status` assignment in the priority decision chain to use the exact status text from the Part 24 table, so the report output matches the PRD specification precisely and passed/failed test cases can be verified against the exact expected strings.

## Feedback Received

Reviewed By:
[Reviewer name]

Feedback Received:
The final_status labels in the priority decision chain don't match the exact wording required by the PRD's Part 24 status table — specifically the passed-days case, the graduation case, and the project/profile cases all use different text than what's specified.

Was the Feedback Valid?
Yes

Change Made:
Updated the `final_status` values in the priority decision chain: changed the fewer-than-four-passed-days branch to "Insufficient Passed Practices", the graduation branch to "Graduation Criteria Not Met", and both the project-incomplete and profile-not-verified branches to "Application On Hold", so every status now matches the PRD's Part 24 table exactly.

Commit Message Used:
Apply peer review improvement - align final status labels with PRD

## Improvement Made After Review
Corrected the `final_status` string values inside the priority-ordered `if`/`elif` decision chain in Section 6 (Determine Final Status) of `main.py`, so that the fewer-than-four-passed-days, graduation-not-eligible, project-incomplete, and profile-not-verified branches now display the exact status text defined in the PRD's Part 24 table instead of the previously reused or reworded labels. Re-ran TC-04, TC-07, TC-08, and TC-09 afterward to confirm the corrected labels appear in the final report.