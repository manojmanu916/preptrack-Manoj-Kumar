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
