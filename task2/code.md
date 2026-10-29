# 2. Progressive Electricity Billing System – Python Program

This B.Tech 1st-year assignment includes the problem statement, algorithm, flowchart, Python source code, sample input, sample output, and Mermaid flowchart code.

## 1. Problem Statement

Design a Python program to calculate household electricity bills based on monthly electricity consumption using progressive billing slabs. The system should calculate energy charges, fixed charges, surcharges, and rebates to determine the final bill amount. It should compare bills across several months and identify unusual increases in electricity bills.

Example billing rules used:

| Electricity consumption  | Rate per unit |
| ------------------------ | ------------- |
| First 100 units          | ₹2 per unit   |
| Next 100 units (101–200) | ₹3 per unit   |
| Above 200 units          | ₹5 per unit   |

Additional rules:

- Fixed charge: ₹50 per month.
- Surcharge: 5% of energy charges if consumption exceeds 200 units.
- Rebate: 5% of energy charges if consumption is at most 100 units.
- Unusual increase: the current month's final bill is more than 30% higher than the previous month's bill.

These are sample rules for the assignment, not official electricity tariff rates.

## 2. Algorithm

1. Start.
2. Input the number of months.
3. For each month, input the month name and electricity consumption in units.
4. Calculate energy charges using progressive slabs.
5. Add the fixed charge of ₹50.
6. If consumption exceeds 200 units, calculate a 5% surcharge on energy charges. Otherwise, if consumption is at most 100 units, calculate a 5% rebate on energy charges.
7. Calculate the final bill by adding the energy charges and fixed charge, then adding the surcharge or subtracting the rebate.
8. Store the monthly consumption and final bill.
9. Compare each month's bill with the previous month's bill.
10. If the bill increases by more than 30%, identify it as an unusual increase.
11. Display the monthly bills and comparison results.
12. Stop.

## 3. Flowchart

``` mermaid

flowchart TD
    A([START]) --> B[/Input number of months/]
    B --> C[/Input month name and units consumed/]
    C --> D[Calculate progressive energy charges]
    D --> E[Add fixed charges]
    E --> F{Units above 200?}
    F -- Yes --> G[Add 5% surcharge]
    F -- No --> H{Units at most 100?}
    H -- Yes --> I[Subtract 5% rebate]
    H -- No --> J[No surcharge or rebate]
    G --> K[Calculate and store final bill]
    I --> K
    J --> K
    K --> L{More months?}
    L -- Yes --> C
    L -- No --> M[Compare consecutive monthly bills]
    M --> N{Increase greater than 30%?}
    N -- Yes --> O[Display unusual increase alert]
    N -- No --> P[Display normal bill change]
    O --> Q[Display all monthly bills]
    P --> Q
    Q --> R([STOP])

    style A fill:#d9ead3,stroke:#38761d
    style R fill:#d9ead3,stroke:#38761d
    style F fill:#fff2cc,stroke:#bf9000
    style H fill:#fff2cc,stroke:#bf9000
    style N fill:#fff2cc,stroke:#bf9000
    style O fill:#f4cccc,stroke:#990000

```


## 5. Sample Input

```
Enter number of months: 3

Month 1
Enter month name: January
Enter units consumed: 80

Month 2
Enter month name: February
Enter units consumed: 120

Month 3
Enter month name: March
Enter units consumed: 250
```

## 6. Sample Output

```
Month 1
Energy charges: Rs. 160.0
Fixed charges: Rs. 50
Surcharge: Rs. 0
Rebate: Rs. 8.0
Final bill: Rs. 202.0

Month 2
Energy charges: Rs. 260.0
Fixed charges: Rs. 50
Surcharge: Rs. 0
Rebate: Rs. 0
Final bill: Rs. 310.0

Month 3
Energy charges: Rs. 750.0
Fixed charges: Rs. 50
Surcharge: Rs. 37.5
Rebate: Rs. 0
Final bill: Rs. 837.5

--- MONTHLY BILL COMPARISON ---
January - Rs. 202.0
February - Rs. 310.0
Bill increased by 53.47 %
March - Rs. 837.5
ALERT: Unusual increase of 170.16 %

Electricity billing process completed.
```

Explanation: January's bill is ₹202. February's bill increases by 53.47%, so the program identifies an unusual increase. March's bill also increases significantly, triggering another alert.




Important: The sample output above follows the code's billing rules. The 30% threshold is applied to the final bill compared with the immediately preceding month's final bill.
