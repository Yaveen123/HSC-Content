## HSC Software Engineering Practice Examination

---

**Question 1 (1 mark)**

Which of the following should take place during the requirements definition step when developing a software solution?
A. Identifying algorithms to be used
B. Documenting security vulnerabilities
C. Identifying potential security threats in the software
D. Documenting the needs and constraints of the software

---

**Question 2 (1 mark)**

Which of the following best describes SMTP?
A. A protocol for email transmission
B. A set of rules to securely transfer files across a network
C. A set of rules for securing communication between computers
D. A protocol used for synchronising communication across networks

---

**Question 3 (1 mark)**

A company conducts all of its consultations with its clients via its website.
Which of the following is the best way for the company to maintain the security of its clients' data?
A. Implement data encryption
B. Ensure that the software is user-friendly
C. Focus on software that incorporates metadata
D. Use software that allows for easy data integration with other platforms

---

**Question 4 (1 mark)**

Which of the following are benefits of collaborating with others when developing software solutions?
(More than one may be selected.)
A. Privacy is improved.
B. Security of data is increased.
C. Intellectual property is protected.
D. Different points of view can be considered.
E. Tasks can be delegated to those with expertise.

---

**Question 5 (1 mark)**

New systems can be implemented in a number of different ways.
Match the implementation methods to their characteristics by dragging them to their corresponding boxes.

**Implementation Methods:**
*   Direct
*   Parallel
*   Phased
*   Pilot

**Characteristics:**
*   [ ] The new system runs immediately with no delay.
*   [ ] The new system gradually replaces the old system.
*   [ ] The new system and the old system run at the same time.
*   [ ] The new system is trialled with a small group of users and then implemented entirely when ready.

---

**Question 6 (1 mark)**

A company is creating a new online application.
Which of the following is the least important consideration when choosing an open-source front-end web framework for the new application?
A. Popularity of the framework on social media
B. Quality of existing framework documentation
C. Knowledge of the framework within the company's development team
D. Compatibility of the framework with the company's existing technology

---

**Question 7 (1 mark)**

Consider the following Python code:
```python
for index in range(n):
  print(index)
```
Select the correct option to complete the equivalent pseudocode.

```
FOR index = [   ]
  Display index
NEXT index
```
Options for the blank:
A. 0 TO n
B. 1 TO n
C. 0 TO n-1
D. 1 TO n-1

---

**Question 8 (2 marks)**

The strategies listed below can be used to test the security of a web application that contains a database.
Classify each strategy as EITHER static application security testing (SAST) OR dynamic application security testing (DAST).

| Strategy                                                           | Static Application Security Testing (SAST) | Dynamic Application Security Testing (DAST) |
| :----------------------------------------------------------------- | :----------------------------------------: | :-----------------------------------------: |
| Simulate attacks on the web application                            |                                            |                                             |
| Check the way SQL queries are constructed                          |                                            |                                             |
| Test the web application used to interact with the database when it is running |                                            |                                             |
| Analyse the code for connecting to the database to identify security vulnerabilities |                                            |                                             |

---

**Question 9 (2 marks)**

Place the following steps of a number guessing algorithm in the correct order by dragging the steps into position.

```
BEGIN GuessingGame
  Set guess = -1
  [ ]
  [ ]
  [ ]
  [ ]
  [ ]
  [ ]
END GuessingGame
```

**Steps to place:**
*   ::Display "Guess a number between 0 and 100:"
*   ::Display "Well Done"
*   ::Set number = random integer between 0 and 100
*   ::ENDWHILE
*   ::WHILE guess <> number
*   ::Get guess

---

**Question 10 (2 marks)**

This structure chart describes an online ordering system for a café.

**(Note: Structure chart from image would be displayed here. It shows a 'Café online ordering system' with sub-modules for 'Customer record', 'Order number', 'Confirm cart', 'Display order'. 'Customer record' has 'Loyalty account login' and 'Enter user details and validate'. 'Order number' has 'Browse menu', 'Add items to order', 'Apply loyalty bonus'. Arrows indicate data flow like 'record' and 'confirmed', and control flow like 'Until valid', 'Until cart confirmed'.)**

Which of the following statements are TRUE about this structure chart?
(More than one may be selected.)
A. Confirm cart is Boolean.
B. Order number is a control variable.
C. A valid loyalty account is not required for online ordering.
D. The order cannot be displayed until the cart is confirmed.
E. A choice is repeatedly offered between Browse menu and Add items to order.

---

**Question 11 (3 marks)**

Consider the following algorithm:

```
BEGIN responsiveScreen
  Get ScreenSize
  IF ScreenSize >= 1024 THEN
    Viewport = 'Desktop'
  ELSEIF ScreenSize >= 768 THEN
    Viewport = 'Tablet'
  ELSE
    Viewport = 'Phone'
  ENDIF
  Display "Display set to ", Viewport
END responsiveScreen
```

Provide a set of test data that will thoroughly test the algorithm. Include the expected outputs and reasons for inclusion. You may assume that all input data are valid.

| Test data (ScreenSize) | Expected output (Viewport) | Reason for inclusion |
| :--------------------- | :------------------------- | :------------------- |
|                        |                            |                      |
|                        |                            |                      |
|                        |                            |                      |
|                        |                            |                      |

---

**Question 12 (6 marks)**

(a) Explain how a web developer could test a website for cross-platform compatibility. (3 marks)
(b) Explain how the load time of a web page can be improved using a progressive web app (PWA). (3 marks)

---

**Question 13 (3 marks)**

Describe the function of protocols in the transfer of data. In your answer, refer to a specific web protocol.

---

**Question 14 (3 marks)**

PseudoPizza creates and sells custom-designed pizzas.
The price of a small pizza is $10. The following costs are added, depending on the size of the pizza base and the number of toppings chosen.
*   Medium size: $2
*   Large size: $4
*   Each topping: $1.50

An algorithm is needed to calculate the cost of pizzas ordered for a customer.
The algorithm should calculate and display:
*   the cost of each pizza
*   the total cost of the order

Write the algorithm using pseudocode. Include at least one subroutine in your answer. You may assume that all inputs are valid.

---

**Question 15 (3 marks)**

Describe how machine learning algorithms can be used in data analysis.

---

**Question 16 (3 marks)**

A developer added a cascading style sheet (CSS) to their company's website.
The developer had expected the HTML code to display Image 1, but Image 2 is being displayed.

**Image 1:** Software (normal font)
**Image 2:** Software (italic, bold)

The following code was used by the developer.

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Software</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    <h1>Software</h1>
    <p><span id="se_item">Software</span> includes code.</p>
</body>
</html>
```

**main.css**
```css
body {
    font-family: Arial;
}

h1 {
    font-weight: bold;
    text-align: center;
}

#sec_item {
    font-style: italic;
    font-weight: bold;
}
```

(a) Referring to the code, what is the cause of the problem? (1 mark)
A. Font family is missing.
B. Attribute of `<span>` has not been defined.
C. main.css has not been correctly referenced.
D. The id "se_item" has not been correctly referenced.

(b) Outline TWO benefits of adding CSS to the company's website. (2 marks)

---

**Question 17 (3 marks)**

A shop uses an online database for recording its stock. The database contains a Products table and a Suppliers table. The prices are in dollars and the masses are in grams.

**Products**
| ProductID | Name            | Price | Mass | Producer   | SupplierID |
| :-------- | :-------------- | :---- | :--- | :--------- | :--------- |
| PID001    | TruffleSway     | 1.00  | 30   | Yumtreats  | SID001     |
| PID002    | PeanutPop       | 1.00  | 35   | Yumtreats  | SID001     |
| PID003    | Carameluxe      | 2.20  | 50   | Yumtreats  | SID003     |
| PID004    | BerryBlend      | 1.25  | 50   | Yumtreats  | SID001     |
| PID005    | Chocolate Cascade | 1.25  | 52   | Yumtreats  | SID002     |
| PID006    | Hazelnut Symphony | 2.50  | 50   | Sugaryum   | SID003     |
| PID007    | Caramel Delight | 2.50  | 40   | Treatopia  | SID002     |
| PID008    | ChocoGlow       | 2.50  | 55   | Treatopia  | SID002     |

**Suppliers**
| SupplierID | Name          |
| :--------- | :------------ |
| SID001     | The Lolly Pop |
| SID002     | Sugar Rush Hour |
| SID003     | Sweet Retreat |

The shop wants to identify all the products with a mass of at least 50 grams that are produced by Yumtreats.
(a) Write an SQL query for the above requirement.

Write an SQL query to display the product names and supplier names, in descending order by product name.
(b) Write an SQL query for the above requirement.

---

**Question 18 (6 marks)**

An online site requires its users to create accounts. These accounts are created using a ‘Create Profile’ web form. This web form includes fields such as username, password, first name, last name, mobile number and date of birth.

Each username must satisfy the following rules:
1.  It must be at least 8 characters long.
2.  It must start with an uppercase letter.
3.  The second character must be a lowercase letter.
4.  The last character must be numeric.

An example of a valid username is NESA24C3.

(a) Explain how defensive data input handling practices can be implemented for this website. (3 marks)
(b) Write a function with Python that will check whether a username satisfies the rules. (3 marks)

---

**Question 19 (4 marks)**

An app is being developed for use in a school. It will allow teachers to upload and assign work, and track student homework. Students can download work and upload their completed responses for marking.

Explain how authentication and authorisation could be applied to this app.

---

**Question 20 (4 marks)**

Consider the following decision tree of a trained machine learning model that determines whether to purchase a mobile phone.

**(Note: Decision tree diagram from image would be displayed here. It shows a tree with initial split on 'Memory > 200 GB'. Branches lead to 'Foldable' and 'AI Assistant' further down, with final outcomes of 'Buy' or 'Do not buy'.)**

(a) Using the decision tree, determine the outcome of each of the following situations. (1 mark)
*   Memory = >200 GB, AI Assistant = Yes, Accessory inclusions = No
*   Memory = 128 GB, AI Assistant = No, Accessory inclusions = Yes
*   Foldable = Yes, AI Assistant = No, Accessory inclusions = No

(b) The decision tree can be simplified without compromising its logic. Redraw the decision tree to reduce the number of branches. (3 marks)
**(Note: A drawing tool would be available here in the digital exam.)**

---

**Question 21 (6 marks)**

At a school, each student studies five subjects. The school timetable has five periods each day so that each subject will appear in all five periods during the week.

An example of a student timetable is shown.

| Period | Monday    | Tuesday   | Wednesday | Thursday  | Friday    |
| :----- | :-------- | :-------- | :-------- | :-------- | :-------- |
| 1      | English   | Sport     | Science   | Drama     | Software  |
| 2      | Software  | English   | Sport     | Science   | Drama     |
| 3      | Drama     | Software  | English   | Sport     | Science   |
| 4      | Science   | Drama     | Software  | English   | Sport     |
| 5      | Sport     | Science   | Drama     | Software  | English   |

In this example, the student studies English, Software, Drama, Science and Sport. From Monday to Friday, English is held in Period 1, Period 2, Period 3 and Period 4. Software is held in Period 2, Period 3, Period 4, Period 5 and then Period 1. A similar pattern can be observed for the other subjects.

You are required to write a Python program to print out the timetable in the following format:
```
Monday
Period 1: English
Period 2: Software
Period 3: Drama
Period 4: Science
Period 5: Sport
and so on...
```
Start your program with `subjects = ["English", "Software", "Drama", "Science", "Sport"]`
Different students may study different subjects.
The program will be used by different students to print out their timetable by changing the subjects listed in the first line of code.

(a) If the timetable is stored as a 2D array, what is the correct Python snippet for accessing the subject that is on Monday Period 3? (1 mark)
A. `Timetable[2]`
B. `Timetable[1,4]`
C. `Timetable[2][0]`
D. `Timetable[0][2]`

(b) Write the Python program using subroutines. (5 marks)

---

**Question 22 (5 marks)**

An online relational database is used to keep track of students at a coding club. The contents of the database are shown.

**Students**
| StudentID | FirstName | Surname  | Attended | Level        |
| :-------- | :-------- | :------- | :------- | :----------- |
| Student1  | John      | Doe      | 5        | Beginner     |
| Student2  | Jane      | Smith    | 4        | Intermediate |
| Student3  | David     | Kim      | 3        | Beginner     |
| Student4  | Sarah     | Lee      | 2        | Expert       |
| Student5  | Emma      | Wilson   | 1        | Beginner     |
| Student6  | Michael   | Johnson  | 0        | Intermediate |
| Student7  | Olivia    | Davis    | 2        | Beginner     |
| Student8  | Ethan     | Martinez | 3        | Intermediate |
| Student9  | Sophia    | Choi     | 4        | Expert       |
| Student10 | Noah      | Moore    | 5        | Beginner     |
| Student11 | Isabella  | Garcia   | 1        | Intermediate |
| Student12 | Liam      | Vo       | 2        | Expert       |

(a) Complete the SQL query to generate the number of students at each level. (2 marks)
```sql
SELECT Level, [  ]
FROM Students
GROUP BY [  ]
ORDER BY [  ]
```

(b) Race conditions have been identified as a potential issue for this database.
Provide an example of when a race condition may occur in this scenario and outline how secure code could be implemented to prevent it. (3 marks)

---

**Question 23 (6 marks)**

(a) How can the effects of human bias be minimised when training machine learning algorithms? (3 marks)
(b) Compare linear regression and K-nearest neighbour. (3 marks)

---

**Question 24 (4 marks)**

A train company wants a class diagram that models the relationship between long-distance train trips and passengers.

The long-distance train has:
*   a unique trip identifier (e.g. AL456)
*   a model code for the train engine (e.g. E67) and a model code (e.g. P9754) for each of the passenger cars
*   two different areas (‘Standard’ and ‘Executive’). The Executive area has 20 seats and there are 400 seats in the Standard area.

Each passenger:
*   has contact details including an email address and phone number
*   purchases a ‘Standard’ or ‘Executive’ ticket and is given a seat number (e.g. 250)
*   may be a frequent traveller.

Create a class diagram for the train company.
**(Note: A drawing tool would be available here in the digital exam.)**

---

**Question 25 (8 marks)**

A telecommunications company had a recent security breach which prompted a review to improve the security of its systems.
It has contracted QuidantCon to propose security enhancements to its systems.

**QuidantCon’s Proposal highlights the following areas:**

*   **Robotic Process Automation (RPA) Enhancement**
    *   Intelligent task automation: Optimise workflows with ML, ensuring compliance with security processes.
    *   Threat prediction: Use ML to predict and prevent security threats.

*   **Business Process Automation (BPA) Security**
    *   Predictive analysis: Identify vulnerabilities in business processes and automate risk mitigation.
    *   Automated compliance monitoring: Ensure continuous compliance with security regulations through ML.

*   **DevOps Integration**
    *   Automated Security Testing: Integrate machine learning (ML) powered tools for automated code scanning and vulnerability testing.
    *   Anomaly Detection: Use ML to monitor logs and traffic.

Discuss QuidantCon’s proposal for security enhancements to the company’s systems.