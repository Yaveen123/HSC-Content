Of course. Here is an alternative Higher School Certificate practice examination for Software Engineering, designed to be slightly more challenging than the example provided.

This examination has been generated with reference to the core themes of the NSW Education Standards Authority (NESA) Software Engineering 11-12 Syllabus (2022), which is first examined in the 2025 HSC. It focuses on areas such as secure software architecture, software automation, machine learning, programming for the web, and the object-oriented paradigm.

---
# <span style="color:red">Continue from **Q11** onwards</span>
### **HSC Software Engineering Practice Examination (Alternative)**

**General Instructions:**
*   Reading time – 10 minutes
*   Working time – 2 hours and 30 minutes
*   This is an online examination.
*   This paper has 25 questions.

---

#### **Section I: Multiple Choice & Short Answer (Total marks: 46)**

**Question 1 (1 mark)**

A software team is developing a banking application. A requirement that "the system must process 500 transactions per second" would be classified as which of the following?

A. Functional requirement ⬅️
B. Non-functional requirement
C. System constraint
D. User interface requirement

---

**Question 2 (1 mark)**

Which protocol is essential for establishing a secure, encrypted link between a web server and a browser, ensuring that all data passed between them remains private?

A. SMTP
B. FTP
C. HTTP ⬅️
D. TLS/SSL

---

**Question 3 (1 mark)**

A developer is building a system that handles sensitive medical records. To ensure data is unreadable both when stored in the database and while being transmitted to a client's browser, which combination of security measures is most appropriate?

A. Encryption at rest and two-factor authentication 
B. A web application firewall (WAF) and encryption in transit
C. Encryption at rest and encryption in transit (e.g., TLS) ⬅️
D. Input validation and rate limiting

---

**Question 4 (1 mark)**

In an Agile software development environment, what is a primary challenge of collaboration that is less prevalent in a Waterfall model?

(More than one may be selected.)

A. Difficulty in adapting to changing requirements. 
B. Ensuring consistent documentation throughout the project. ⬅️
C. Integrating work from different developers in short cycles. ⬅️
D. A lack of customer involvement during development.
E. Rigidly defined roles for team members.

---

**Question 5 (1 mark)**

A large national retail chain plans to replace its outdated point-of-sale (POS) system with a new, cloud-based solution. The company cannot afford any system-wide downtime but wants to gather real-world performance data before a full rollout.

Which implementation method is most suitable for this scenario?

A. Direct
B. Parallel ⬅️
C. Phased
D. Pilot

---

**Question 6 (1 mark)**

When choosing a third-party open-source library for handling user authentication, which of the following is the MOST critical consideration from a security perspective?

A. The number of downloads or stars the library has on GitHub.
B. The clarity and completeness of the library's documentation.
C. The license under which the library is distributed (e.g., MIT vs. GPL).
D. The library's history of security vulnerabilities and the frequency of security patches. ⬅️

---

**Question 7 (1 mark)**

Consider the following Python code snippet:
```python
i = 0
while i < len(items):
  print(items[i])
  i += 2
```
Select the correct option to complete the equivalent pseudocode.

```
i = 0
WHILE [   ]
  Display items[i]
  i = i + 2
ENDWHILE
```
Options for the blank:
A. i <= LENGTH(items)
B. i < LENGTH(items) ⬅️
C. i > LENGTH(items) 
D. i <> LENGTH(items) - 1

---

**Question 8 (2 marks)**

A security audit is performed on a new e-commerce website. Classify the following activities as either relating to **coupling** or **cohesion** in the context of secure software design.

| Activity | Coupling | Cohesion |
| :--- | :---: | :---: |
| A module responsible for payment processing also handles user profile updates. |  | 💠 |
| The user authentication module directly queries the inventory database. | 💠 | |
| All functions related to shipping logistics are contained within a single class. | | 💠 |
| A change to the logging module requires changes in the product, cart, and payment modules. | 💠 | |

---

**Question 9 (2 marks)**

Place the following steps of a binary search algorithm in the correct logical order. The algorithm searches for a `target` value within a sorted `array`.

```
my answer:

BEGIN BinarySearch(array, target)
  Set low = 0
  Set high = LENGTH(array) - 1

*   ::WHILE low <= high
    *   ::Set mid = (low + high) / 2
    *   ::IF array[mid] == target THEN RETURN mid
    *   ::IF array[mid] < target THEN Set low = mid + 1
    *   ::ELSE Set high = mid - 1
*   ::ENDWHILE

END BinarySearch
```

**Steps to place:**
*   ::Set mid = (low + high) / 2
*   ::IF array[mid] < target THEN Set low = mid + 1
*   ::WHILE low <= high
*   ::ELSE Set high = mid - 1
*   ::ENDWHILE
*   ::IF array[mid] == target THEN RETURN mid


---

**Question 10 (2 marks)**

Analyse the provided structure chart for a university enrolment system.

**(Note: A more complex structure chart would be displayed. It shows a root module 'Process Enrolment'. It has sub-modules 'Validate Student ID', 'Check Course Availability', and 'Finalise Enrolment'. 'Validate Student ID' passes 'student_status' up. 'Check Course Availability' takes 'course_code' and 'student_status' and passes 'is_available' up. 'Finalise Enrolment' takes 'student_id', 'course_code' and passes 'confirmation_details' up. A loop exists around 'Check Course Availability' labelled 'Until valid course selected'.)**

Which of the following statements are TRUE?
(More than one may be selected.)

A. `is_available` is a control flag. ⬅️
B. High cohesion is demonstrated by the 'Validate Student ID' module. ⬅️
C. The system exhibits tight coupling between the 'Validate Student ID' and 'Check Course Availability' modules. 
D. A student's status must be validated before checking if a course is available. ⬅️
E. `course_code` is passed by reference to the 'Check Course Availability' module. 

---

**Question 11 (3 marks)**

Consider the following algorithm designed to determine a user's discount level based on their account type and years of membership.

```
BEGIN calculateDiscount
  Get accountType, membershipYears
  IF accountType == 'Premium' AND membershipYears >= 5 THEN
    discount = 0.20
  ELSEIF accountType == 'Premium' AND membershipYears < 5 THEN
    discount = 0.15
  ELSEIF accountType == 'Standard' AND membershipYears >= 10 THEN
    discount = 0.10
  ELSE
    discount = 0.0
  ENDIF
  Display "Discount is ", discount
END calculateDiscount
```
Provide a set of test data that uses equivalence partitioning and boundary value analysis to thoroughly test the algorithm.

| Test Data (accountType, membershipYears) | Expected Output (discount) | Reason for Inclusion (e.g., Boundary, Equivalence Class) |
| :--- | :--- | :--- |
| | | |
| | | |
| | | |
| | | |

---

**Question 12 (6 marks)**

(a) Compare Server-Side Rendering (SSR) and Client-Side Rendering (CSR) in the context of a content-heavy news website. Your answer should refer to initial page load time, SEO, and server load. (3 marks)

(b) Explain how a Content Delivery Network (CDN) can be used to improve the performance and availability of such a website, regardless of whether it uses SSR or CSR. (3 marks)

---

**Question 13 (3 marks)**

Describe the three-way handshake process used by the Transmission Control Protocol (TCP) to establish a reliable connection.

---

**Question 14 (4 marks)**

A movie streaming service offers the following subscription plans:
*   **Basic:** $9.99/month
*   **Standard:** $15.99/month
*   **Premium:** $21.99/month

Customers who opt for an annual subscription receive a 15% discount on the total yearly cost. An algorithm is needed to calculate a customer's subscription cost.

Write an algorithm in pseudocode to solve this problem. The algorithm must:
*   Accept the plan type ('Basic', 'Standard', 'Premium') and billing cycle ('Monthly', 'Annual') as inputs.
*   Use a subroutine to calculate the total cost based on the inputs.
*   Display the final calculated cost, formatted to two decimal places.

---

**Question 15 (3 marks)**

Explain the difference between supervised, unsupervised, and reinforcement learning. For each type, provide a specific software engineering example where it might be applied.

---

**Question 16 (3 marks)**

A web developer wants the main heading on a page to be blue, but it is appearing red.

**index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Styling Issue</title>
    <link rel="stylesheet" href="style.css">
    <style>
        h1 {
            color: blue;
            font-size: 24px;
        }
    </style>
</head>
<body>
    <h1 id="main-heading" class="title">Welcome</h1>
</body>
</html>
```

**style.css**
```css
.title {
    font-weight: bold;
}

#main-heading {
    color: red;
}
```

(a) Referring to the Cascading Style Sheets (CSS) rules of precedence, explain why the heading is red instead of blue. (2 marks)

(b) What is one advantage of using an external stylesheet (`style.css`) over an internal stylesheet (using the `<style>` tag)? (1 mark)

---

**Question 17 (4 marks)**

A university database has the following tables to track student enrolments in various courses.

**Students**
| StudentID | FirstName | LastName | Major |
| :--- | :--- | :--- | :--- |
| S101 | Alice | Smith | CompSci |
| S102 | Bob | Jones | Engineering |
| S103 | Charlie | Brown | CompSci |

**Courses**
| CourseID | CourseName | Credits |
| :--- | :--- | :--- |
| CS101 | Intro to Python | 10 |
| CS205 | Data Structures | 10 |
| EN100 | Intro to Eng | 15 |

**Enrolments**
| EnrolmentID | StudentID | CourseID | Semester |
| :--- | :--- | :--- | :--- |
| E1 | S101 | CS101 | Sem1_2025 |
| E2 | S101 | CS205 | Sem1_2025 |
| E3 | S102 | EN100 | Sem1_2025 |
| E4 | S103 | CS101 | Sem1_2025 |

(a) Write an SQL query to list the `FirstName` and `LastName` of all students majoring in 'CompSci' who are enrolled in the 'Intro to Python' course. (2 marks)

(b) Write an SQL query to find the number of students enrolled in each course. The output should display the `CourseName` and the `StudentCount`. (2 marks)

---

#### **Section II: Extended Answer (Total marks: 44)**

**Question 18 (6 marks)**

A social media platform requires users to set a password that meets the following criteria:
1.  Minimum 12 characters.
2.  At least one uppercase letter.
3.  At least one lowercase letter.
4.  At least one number.
5.  At least one special character from the set `!@#$%`.

(a) Explain how regular expressions can be used to implement a robust and efficient server-side validation for these password rules. (3 marks)

(b) Write a Python function `is_password_valid(password)` that takes a password string as input and returns `True` if it meets all the criteria, and `False` otherwise. Do not use the `re` (regex) module. (3 marks)

---

**Question 19 (4 marks)**

An online learning platform wants to allow students to log in using their existing Google accounts to simplify registration and access.

Explain how the OAuth 2.0 authorisation framework would facilitate this process. Your answer should refer to the roles of the **Resource Owner**, **Client**, **Authorisation Server**, and **Resource Server**.

---

**Question 20 (4 marks)**

(a) The following dataset shows user engagement with a video streaming app. Based on the data, construct a simple decision tree that predicts whether a user will `Renew` their subscription. Your tree should make the most logical first split. (3 marks)

| Hours Watched / Month | Devices Used | Ad-free Plan | Renew |
| :--- | :--- | :--- | :--- |
| > 20 | 3 | Yes | Yes |
| < 10 | 1 | No | No |
| > 20 | 2 | Yes | Yes |
| > 20 | 1 | No | No |
| < 10 | 2 | Yes | No |
| > 20 | 4 | Yes | Yes |

**(Note: A drawing tool would be available here in the digital exam.)**

(b) Identify one potential ethical issue with using such a model to make business decisions. (1 mark)

---

**Question 21 (6 marks)**

A program is required to manage a software project's task list. Tasks are stored in a data structure, where each task has a `name`, a `priority` (1-5, where 5 is highest), and a `status` ('Pending', 'In Progress', 'Complete').

The data is stored as a list of dictionaries in Python:
```python
tasks = [
    {'name': 'Setup Database', 'priority': 5, 'status': 'Complete'},
    {'name': 'Design UI', 'priority': 4, 'status': 'In Progress'},
    {'name': 'Develop Auth', 'priority': 5, 'status': 'Pending'},
    {'name': 'Write Tests', 'priority': 3, 'status': 'Pending'},
]
```
Write a Python program that does the following:
1.  Defines a function `display_pending_tasks(task_list)` that takes the list of tasks as an argument.
2.  The function should sort the pending tasks by `priority` in descending order (highest priority first).
3.  The function should then print the names of only the 'Pending' tasks in their sorted order.

---

**Question 22 (5 marks)**

A financial services company uses a database to process stock trades. Multiple brokers can attempt to execute trades on behalf of the same client simultaneously.

(a) Describe how a race condition could occur in this scenario, leading to an incorrect client account balance. (2 marks)

(b) Explain how a database transaction with a specific isolation level (e.g., `SERIALIZABLE`) can be used as a secure coding practice to prevent this issue. (3 marks)

---

**Question 23 (6 marks)**

(a) Explain the machine learning concepts of **overfitting** and **underfitting**. In your answer, describe a technique that could be used to mitigate overfitting. (3 marks)

(b) Compare the use of a K-nearest neighbour (KNN) algorithm with a logistic regression algorithm for a classification task, such as predicting customer churn (whether a customer will leave a service). (3 marks)

---

**Question 24 (5 marks)**

A local library wants to model its book lending system.
*   The system has **Members** and **Books**.
*   A **Book** has an `ISBN`, `title`, and `author`. A **Book** can also be a special type of book called a **ReferenceBook**, which cannot be borrowed.
*   A **Member** has a `memberID`, `name`, and can borrow multiple books. The relationship is that one Member can borrow many Books.
*   The system also models the loan itself. A **Loan** object is created when a book is borrowed. It has a `dueDate` and links a specific **Member** to a specific **Book**.

Create a UML class diagram that models this system, showing classes, attributes, and the relationships between them (including inheritance and multiplicity).

**(Note: A drawing tool would be available here in the digital exam.)**

---

**Question 25 (8 marks)**

A fast-growing e-commerce startup is deciding on its future software architecture. The current system is a **monolithic application**, where the user interface, product catalog, shopping cart, and payment processing are all part of a single, large codebase.

The lead architect has proposed migrating to a **microservices architecture**, where each of these components would become a separate, independently deployable service that communicates via APIs.

Discuss the trade-offs of this proposed migration from a monolithic to a microservices architecture. In your answer, you must evaluate the impact on:
*   **Scalability:** How easily the system can handle increased load.
*   **Maintainability & Development Speed:** The ease of updating, fixing, and adding new features.
*   **System Complexity & Security:** The overall difficulty in managing the system and the potential security implications.