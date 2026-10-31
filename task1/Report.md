
# University Scholarship Allocation System – Python Program

This is a beginner-friendly B.Tech 1st-year Python assignment. It includes the problem statement, algorithm, flowchart, Python source code, sample input, sample output, and Mermaid flowchart code.

## 1. Problem Statement

Design a Python program to allocate university scholarships to students based on their aggregate marks, subject-wise minimum marks, attendance percentage, and family income. The program should check whether each student satisfies all the eligibility criteria. Eligible students must be ranked according to their aggregate marks in descending order. If two students have equal aggregate marks, ties should be resolved using higher attendance, then lower family income, and finally the student's name in alphabetical order. Display the eligible students in rank order and identify students who are not eligible.

Eligibility criteria used in this program:

- Aggregate marks: at least 75%.
- Minimum marks in every subject: 60%.
- Attendance: at least 75%.
- Annual family income: not more than ₹2,50,000.

These are example rules for the assignment and can be changed according to university requirements.

## 2. Algorithm

1. Start.
2. Read the number of students.
3. For each student, input name, aggregate percentage, subject marks, attendance percentage, and annual family income.
4. Check whether aggregate marks are at least 75%, every subject mark is at least 60%, attendance is at least 75%, and family income is at most ₹2,50,000.
5. If all conditions are satisfied, add the student to the eligible list. Otherwise, add the student to the ineligible list.
6. Sort eligible students by:
   - Higher aggregate marks first.
   - Higher attendance first if aggregate marks are equal.
   - Lower family income first if both are equal.
   - Alphabetical name if all previous criteria are equal.
7. Assign ranks to eligible students.
8. Display the eligible students with their ranks and the ineligible students with their reasons.
9. Stop.

## 3. Flowchart
``` mermaid

flowchart TD
    A([START]) --> B[/Input number of students/]
    B --> C[/Input student details and marks/]
    C --> D{Aggregate >= 75%, all subjects >= 60%, attendance >= 75%, income <= 250000?}
    D -- Yes --> E[Add student to eligible list]
    D -- No --> F[Record ineligible student and reason]
    E --> G{More students?}
    F --> G
    G -- Yes --> C
    G -- No --> H[Sort eligible students by tie-break rules]
    H --> I[Assign ranks and display results]
    I --> J([STOP])

    style A fill:#d9ead3,stroke:#38761d
    style J fill:#d9ead3,stroke:#38761d
    style D fill:#fff2cc,stroke:#bf9000
    style E fill:#d9ead3,stroke:#38761d
    style F fill:#f4cccc,stroke:#990000

```




## 5. Sample Input

Enter the following values when you run the program.

```
Enter number of students: 4

Enter details of student 1
Name: Anu
Aggregate marks (%): 85
Enter marks in 3 subjects:
Subject 1: 80
Subject 2: 90
Subject 3: 85
Attendance (%): 90
Annual family income (Rs.): 200000

Enter details of student 2
Name: Bala
Aggregate marks (%): 85
Enter marks in 3 subjects:
Subject 1: 75
Subject 2: 80
Subject 3: 90
Attendance (%): 95
Annual family income (Rs.): 220000

Enter details of student 3
Name: Chitra
Aggregate marks (%): 78
Enter marks in 3 subjects:
Subject 1: 65
Subject 2: 70
Subject 3: 80
Attendance (%): 80
Annual family income (Rs.): 150000

Enter details of student 4
Name: Deepa
Aggregate marks (%): 90
Enter marks in 3 subjects:
Subject 1: 58
Subject 2: 95
Subject 3: 90
Attendance (%): 95
Annual family income (Rs.): 180000
```

## 6. Sample Output

```
--- ELIGIBLE STUDENTS ---
1 Bala | Aggregate: 85.0 % | Attendance: 95.0 % | Income: Rs. 220000.0
2 Anu | Aggregate: 85.0 % | Attendance: 90.0 % | Income: Rs. 200000.0
3 Chitra | Aggregate: 78.0 % | Attendance: 80.0 % | Income: Rs. 150000.0

--- INELIGIBLE STUDENTS ---
Deepa - Subject mark below 60%

Scholarship allocation process completed.
```

Explanation: Bala gets Rank 1 because Bala and Anu have equal aggregate marks, but Bala has higher attendance. Deepa is ineligible because one subject mark is below 60%, even though the aggregate is 90%.


Note: The Python program uses three subject marks for simplicity. If your assignment specifies a different number of subjects or different scholarship eligibility rules, adjust those inputs and conditions accordingly.
