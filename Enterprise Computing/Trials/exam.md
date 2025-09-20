Of course. Here is an alternate HSC Enterprise Computing Trial Exam based on the provided practice paper and syllabus.

***

### **HSC Enterprise Computing Alternate Trial Exam**

**Time limit:** 2 hours and 20 minutes + 10 minutes reading time

---

#### **Section 1 - Multiple Choice (20 marks)**

**Instructions:** Answer all questions. For each question, select the best response.

**1. Which project management tool is best suited for documenting project progress, including tasks achieved, issues encountered, and reflective comments by team members? (1 mark)**

a) Gantt chart 

b) System flowchart

c) Process diary/logbook

d) Data flow diagram

**2. A new software version is released to a limited number of users to gather feedback on real-world usage before a full rollout. What is this testing method called? (1 mark)**

a) Volume testing

b) Acceptance testing

c) Functional testing

d) Beta testing

**3. What is the primary purpose of normalisation in a relational database? (1 mark)**

a) To increase query speed by adding redundant data.

b) To minimise data redundancy and improve data integrity.

c) To enforce a strict data format for all text fields.

d) To create a single, large table for ease of access.

**4. In a Data Flow Diagram (DFD), what does a circle or rounded rectangle represent? (1 mark)**

a) A data store

b) An external entity

c) A process

d) A data flow

**5. A company replaces its old accounting system with a new one. To minimise risk, they run both the old and the new systems simultaneously for a month to compare the results. Which implementation method is this? (1 mark)**

a) Phased implementation


b) Pilot implementation

c) Direct implementation

d) Parallel implementation

**6. Which of the following are examples of structured data? (Select all that apply) (2 marks)**
a) A transcript of a customer service call.
b) A table of sales figures in a database.
c) A collection of social media comments.
d) A spreadsheet containing employee names, IDs, and start dates.
e) A video interview with a job candidate.

**7. An expert system uses a set of rules to make decisions. What is the most common format for these rules? (1 mark)**
a) SQL queries
b) IF-THEN statements
c) Machine learning algorithms
d) Fuzzy logic sets

**8. Which of the following are significant ethical concerns when developing an intelligent system that automates loan approvals? (Select all that apply) (2 marks)**
a) The system might be too slow to process applications.
b) The system may perpetuate historical biases present in the training data.
c) The system requires significant computing power.
d) The lack of transparency in decision-making (a "black box" problem).
e) The system's user interface might be difficult to use.

**9. In a database schema for a library, the `Books` table has a `PublisherID` field, which corresponds to the primary key in the `Publishers` table. What is `PublisherID` in the `Books` table? (1 mark)**
a) Primary key
b) Secondary key
c) Foreign key
d) Composite key

**10. What is a key advantage of the Agile development methodology over the Waterfall model? (1 mark)**
a) It requires all requirements to be defined and finalised at the start.
b) It is more rigid and less adaptable to change.
c) It emphasises extensive documentation over working software.
d) It allows for iterative development and continuous feedback from stakeholders.

**11. Which of the following SQL clauses is used to sort the results of a query? (1 mark)**
a) `SORT BY`
b) `GROUP BY`
c) `ORDER BY`
d) `ARRANGE BY`

**12. A smart thermostat adjusts the temperature based on imprecise descriptions like 'cool', 'warm', or 'hot'. This is an application of: (1 mark)**
a) A neural network
b) An expert system
c) A data dictionary
d) Fuzzy logic

**13. Which system modelling tool is used to represent the flow of data through a system, including processes and devices? (1 mark)**
a) Storyboard
b) System flowchart
c) Gantt chart
d) Network diagram

**14. A company wants to create an interactive dashboard showing real-time sales data with maps, charts, and graphs that users can filter. Which software tool would be most suitable? (1 mark)**
a) A word processor
b) A presentation software like PowerPoint
c) A business intelligence tool like Microsoft Power BI or Tableau
d) A standard spreadsheet program with basic charting

**15. What is the primary function of an actuator in a computer-controlled system? (1 mark)**
a) To measure a physical quantity from the environment.
b) To perform a physical action based on a signal from the control system.
c) To store data about the system's state.
d) To process data and make decisions.

**16. Which of the following should be considered when evaluating the potential for bias in a dataset? (Select all that apply) (2 marks)**
a) The size of the dataset.
b) The source from which the data was collected.
c) The method used for data collection.
d) The file format in which the data is stored.
e) The age of the data and whether it reflects current realities.

---

#### **Section 2 – Short Answer Questions (40 marks)**

**Question 17 (8 marks)**

The following Data Flow Diagram (DFD) models a simple system for a university's course enrolment.

**(Diagram of a DFD shows an external entity 'Student' providing 'Enrolment Request' to a process 'Process Enrolment'. This process gets 'Course Details' from a data store 'Courses' and checks 'Student Record' from a data store 'Students'. The process then sends 'Enrolment Confirmation' back to the 'Student' and updates the 'Students' data store with 'Updated Record'.)**

a) Identify the four main components of a DFD and provide one example of each from the diagram above. (4 marks)

b) The 'Process Enrolment' process must also verify that the student has paid their fees before confirming enrolment. The fee status is held in a 'Finance' data store. Describe the changes needed in the DFD to include this requirement. (4 marks)

**Question 18 (10 marks)**

A technology store uses the following spreadsheet to track its inventory.

| | A | B | C | D | E |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1**| **Product ID** | **Product Name** | **Unit Price** | **Quantity in Stock** | **Stock Value** |
| **2**| P101 | Gaming Mouse | 85 | 25 | |
| **3**| P102 | Keyboard | 120 | 15 | |
| **4**| P103 | Webcam | 95 | 0 | |
| **5**| P104 | Monitor | 350 | 10 | |

a) Write the formula for cell **E2** to calculate the stock value for the Gaming Mouse. This formula should be able to be filled down to cell E5. (2 marks)

b) The store manager wants the `Stock Value` column to display "Out of Stock" if the `Quantity in Stock` is 0. Write an `IF` statement for cell **E4** that achieves this. (3 marks)

c) The manager wants to use conditional formatting to highlight any product with a `Quantity in Stock` of less than 15. Describe the rule that would need to be applied to the range D2:D5. (2 marks)

d) What is the function of a pivot table, and how could it be used with this data? (3 marks)

**Question 19 (10 marks)**

A real estate company uses a database to manage its properties and agents. The database has two tables: `Agent` and `Property`.

**Agent Table**
*   `AgentID` (Primary Key)
*   `FirstName`
*   `LastName`
*   `CommissionRate`

**Property Table**
*   `PropertyID` (Primary Key)
*   `Address`
*   `ListPrice`
*   `AgentID` (Foreign Key)

a) Describe the relationship between the `Agent` and `Property` tables. (2 marks)

b) Write an SQL query to display the `Address` and `ListPrice` of all properties listed for more than $500,000. (3 marks)

c) Write an SQL query that displays the `FirstName` and `LastName` of the agent, and the `Address` of the property they are assigned to, for all properties. (5 marks)

**Question 20 (12 marks)**

A project manager is planning the development of a new mobile application. The Gantt chart below shows the main tasks.

**(Image of a Gantt chart. Task A "Market Research" is 2 weeks. Task B "UI Design" starts after A, lasts 3 weeks. Task C "Backend Dev" starts after A, lasts 4 weeks. Task D "App Coding" starts after B and C, lasts 5 weeks. Task E "Testing" starts after D, lasts 2 weeks.)**

a) Identify which task(s) can be performed in parallel with Task B "UI Design". (2 marks)

b) What is a "dependent task"? Provide one example of a dependent task from the chart and explain the dependency. (3 marks)

c) The "Backend Dev" (Task C) was delayed and took 6 weeks instead of 4. Explain the impact this delay would have on the project's timeline and the start date of Task E "Testing". (4 marks)

d) Define what a project milestone is and suggest a suitable milestone for this project. (3 marks)

---

#### **Section 3 - Extended Response (40 marks)**

**Question 21 (10 marks)**

A hospital is developing a new intelligent system to assist doctors in diagnosing patient illnesses. The system will analyse patient symptoms, medical history, and lab results to suggest possible diagnoses.

Discuss the social and ethical issues that must be considered during the development and implementation of this system. In your answer, refer to **bias, privacy, and accountability**.

**Question 22 (12 marks)**

A large retail company wants to create a new online learning platform for its 10,000 employees. The system needs to be highly interactive, and the company expects that new features and training modules will need to be added frequently after the initial launch.

Compare and contrast the suitability of the **Agile** and **Waterfall** development methodologies for this project. Justify which methodology you would recommend and why.

**Question 23 (8 marks)**

Outsourcing development work to external companies is a common practice.

a) Describe two potential benefits for a company that chooses to outsource the development of its new customer relationship management (CRM) system. (4 marks)

b) Describe two potential risks or drawbacks of outsourcing the development of the same CRM system. (4 marks)



**Question 24 (10 marks)**

A logistics company uses a fleet of delivery trucks that are equipped with various technologies. Each truck has:
1.  A GPS unit to track its location.
2.  A temperature monitor inside its refrigerated compartment.
3.  A mechanism that can automatically lock the cargo doors.

a) For each of the three numbered items, identify whether its primary component is a **sensor** or an **actuator**, and justify your choice. (6 marks)
> A GPS unit is primarly a sensor, as it collects data about it's environment and does not actually have physical components that move. 
> A temperature monitor is a sensor as it records data about the env. temp. is doesn't have physical moving components
> A locking mechanism is an actuator as it has functional components that move to lock the component into place. 


b) The company wants to use this data to tell a story about delivery efficiency. Describe how a data visualisation could be used to demonstrate how delivery times are affected by traffic patterns throughout the day. (4 marks)
> Delivery efficiency from these datasets can show the time for each delivery truck to arrive to it's destination. This can be visualised in a map with heated path indicator to show common routes, along with common chokepoints so trucks can use faster routes. Furthermore, through column graphs, the time taken 

how long each delivery truck takes to load/unload. 

***

### **HSC Enterprise Computing Alternate Trial Exam [ANSWERS]**

---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---

#### **Section 1 - Multiple Choice (20 marks)**

1.  **c) Process diary/logbook** - This is the specific tool used for detailed, regular progress documentation.
2.  **d) Beta testing** - This involves releasing software to a limited, external audience for real-world testing.
3.  **b) To minimise data redundancy and improve data integrity.** - This is the core purpose of normalisation.
4.  **c) A process** - A circle/rounded rectangle represents a process that transforms inputs into outputs.
5.  **d) Parallel implementation** - This method involves running the old and new systems side-by-side.
6.  **b) A table of sales figures in a database.** and **d) A spreadsheet containing employee names, IDs, and start dates.** - Both are organised in rows and columns with a defined schema.
7.  **b) IF-THEN statements** - This is the fundamental structure of a rule-based expert system.
8.  **b) The system may perpetuate historical biases present in the training data.** and **d) The lack of transparency in decision-making (a "black box" problem).** - These are key ethical concerns in AI.
9.  **c) Foreign key** - It is a key used to link two tables together.
10. **d) It allows for iterative development and continuous feedback from stakeholders.** - This flexibility is a core principle of Agile.
11. **c) `ORDER BY`** - This is the correct SQL clause for sorting results.
12. **d) Fuzzy logic** - This deals with reasoning that is approximate rather than precise.
13. **b) System flowchart** - This shows the flow of data as well as the devices involved.
14. **c) A business intelligence tool like Microsoft Power BI or Tableau** - These tools are designed for creating interactive data visualisations and dashboards.
15. **b) To perform a physical action based on a signal from the control system.** - Sensors detect, actuators act.
16. **b) The source from which the data was collected.**, **c) The method used for data collection.**, and **e) The age of the data and whether it reflects current realities.** - These factors can all introduce bias.

---

#### **Section 2 – Short Answer Questions (40 marks)**

**Question 17 (8 marks)**
a)
1.  **External Entity:** A source or destination of data outside the system. Example: `Student`.
2.  **Process:** An activity that transforms data. Example: `Process Enrolment`.
3.  **Data Store:** A repository of data. Example: `Courses` or `Students`.
4.  **Data Flow:** The movement of data between other components. Example: `Enrolment Request` or `Enrolment Confirmation`.

b)
A new data store named `Finance` would be added to the diagram. A data flow arrow, labelled `Fee Status`, would go from the `Finance` data store to the `Process Enrolment` process. This shows the process is retrieving the fee information to verify payment before it sends the `Enrolment Confirmation` to the student.

**Question 18 (10 marks)**
a) `=C2*D2`
b) `=IF(D4=0, "Out of Stock", C4*D4)`
c) The rule would be: "Format cells that are LESS THAN 15". This rule would be applied to the range D2:D5, and a formatting style (e.g., red fill) would be chosen.
d) A pivot table is a tool used to summarise, group, and analyse large amounts of data from a table or spreadsheet. With this data, a pivot table could be used to quickly calculate the total stock value for all products or find the average unit price without needing to write individual formulas.

**Question 19 (10 marks)**
a) The relationship is **one-to-many**. One agent can be assigned to many properties, but one property can only be assigned to one agent. The `AgentID` foreign key in the `Property` table establishes this link.

b)
```sql
SELECT Address, ListPrice
FROM Property
WHERE ListPrice > 500000;
```

c)
```sql
SELECT Agent.FirstName, Agent.LastName, Property.Address
FROM Agent
JOIN Property ON Agent.AgentID = Property.AgentID;
```

**Question 20 (12 marks)**
a) Task C "Backend Dev" can be performed in parallel with Task B "UI Design".

b) A dependent task is a task that cannot begin until one or more other tasks have been completed. For example, Task D "App Coding" is a dependent task. It cannot start until both Task B "UI Design" and Task C "Backend Dev" are finished.

c) If Task C takes 6 weeks, it will now finish at the end of week 8 (2 weeks for Task A + 6 weeks for Task C). Since Task D depends on both B and C, it cannot start until the latest predecessor is complete. Task B finishes at the end of week 5, but Task C now finishes at the end of week 8. Therefore, Task D cannot start until the beginning of week 9. This pushes the entire project back by 2 weeks. The start date of Task E will also be delayed by 2 weeks.

d) A project milestone is a specific point in a project's lifecycle used to measure progress. It is an event, not a task, and has zero duration. A suitable milestone would be "All Development Complete", placed after Task D is finished, or "Project Kick-off" before Task A.

---

#### **Section 3 - Extended Response (40 marks)**

**Question 21 (10 marks)**
**SAMPLE ANSWER:**
Developing an AI diagnostic system for a hospital raises significant social and ethical issues.
**Bias** is a primary concern. If the system is trained on historical medical data that underrepresents certain demographics (e.g., specific ethnicities or genders), its diagnostic accuracy for those groups could be dangerously low. This could perpetuate and even amplify existing health disparities, leading to misdiagnoses for minority patients. The data used must be carefully audited for representativeness.
**Privacy** is crucial as the system handles highly sensitive patient health information (PHI). There must be robust security measures to prevent data breaches, adhering to health regulations like HIPAA. Patients must give informed consent for their data to be used by the system, and the data should be anonymised wherever possible to protect patient identity. The potential for data misuse or unauthorised access is a major ethical risk.
**Accountability** presents a complex challenge. If the AI system provides an incorrect diagnosis that leads to patient harm, who is responsible? Is it the hospital, the doctors who used the system, or the developers who created the software? Clear lines of accountability must be established. The system should be treated as a decision-support tool, with the final clinical judgment and responsibility remaining with the human doctor, who must understand the system's limitations.

**Question 22 (12 marks)**
**SAMPLE ANSWER:**
When developing an online learning platform for a large company with evolving needs, the choice of development methodology is critical.

The **Waterfall methodology** is a linear, sequential approach where each phase (requirements, design, implementation, testing) must be completed before the next begins.
*   **Suitability for this project:** This model would be poorly suited. Its rigidity means all requirements must be defined upfront. For a dynamic learning platform where new features are expected frequently, this is impractical. If the company wanted to add a new type of quiz or a social feature mid-development, it would be difficult and costly to go back and change the specifications.
*   **Contrast:** The key drawback is its inflexibility and the late stage at which a working product is delivered to stakeholders for feedback.

The **Agile methodology** is an iterative approach where the project is broken down into small cycles or "sprints." A small, functional piece of the product is developed in each sprint and demonstrated to stakeholders.
*   **Suitability for this project:** This model is highly suitable. It allows for continuous feedback from the company's training department, ensuring the platform meets their needs as it evolves. New features can be prioritised and added to the backlog for future sprints, making the system adaptable. For instance, the first version might only include basic video modules, with interactive quizzes and discussion forums added in subsequent iterations based on user feedback.
*   **Contrast:** Unlike Waterfall, Agile embraces change and prioritises stakeholder collaboration and a working product over comprehensive documentation.

**Recommendation:**
I would strongly recommend the **Agile methodology**. Its iterative nature is perfect for a project where requirements are expected to change and expand. It allows the development team to deliver value quickly and adapt to the needs of the 10,000 employees and the training department. This flexibility reduces the risk of building a platform that doesn't meet user needs and ensures the final product is both useful and engaging.

**Question 23 (8 marks)**
**SAMPLE ANSWER:**
a) **Benefits of Outsourcing:**
1.  **Access to Specialised Expertise:** The company can hire an external firm that specialises in building CRM systems. This provides access to experienced developers, project managers, and business analysts who have deep knowledge of best practices, which the company's in-house IT team may lack. This can lead to a higher quality product.
2.  **Cost Reduction and Focus on Core Business:** Outsourcing can be cheaper than hiring, training, and retaining a specialised in-house development team, especially for a one-off project. It converts a fixed cost (salaries) into a variable cost (project contract). This also allows the company to focus its own resources and employees on its primary business activities rather than on a complex IT project.

b) **Risks of Outsourcing:**
1.  **Loss of Control and Communication Challenges:** The company gives up direct day-to-day control over the development process. Time zone differences, language barriers, and cultural differences can lead to miscommunication, misunderstandings of requirements, and delays. Ensuring the final product meets the precise business needs can be difficult.
2.  **Data Security and Privacy Risks:** The company must share sensitive customer data with the external vendor. This creates a significant security risk. If the outsourced company has poor security practices, it could lead to a data breach, damaging the company's reputation and potentially leading to legal penalties. A thorough vetting of the vendor's security protocols is essential.

**Question 24 (10 marks)**
**SAMPLE ANSWER:**
a)
1.  **GPS unit:** This is a **sensor**. Its function is to receive signals from satellites to determine and measure its physical geographic location. It is detecting information from the environment.
2.  **Temperature monitor:** This is a **sensor**. Its purpose is to measure the physical property of temperature within the refrigerated compartment. It detects the current state.
3.  **Mechanism to automatically lock cargo doors:** This is an **actuator**. Based on a signal from the control system (e.g., a command from the driver or an automated trigger), it performs a physical action: moving the lock into place. It is acting on the environment.

b)
To tell a story about delivery efficiency, a data visualisation could combine GPS and traffic data on an interactive map. One could use a **heatmap layer** over the city map, where colors represent traffic density (e.g., red for heavy, green for light). A **line chart** could be synchronized with the map, plotting average delivery times against the time of day. By animating the map and chart over a 24-hour period, the company could clearly demonstrate how high-traffic periods (visible as red areas on the map) directly correlate with spikes in delivery times on the chart. This visual story would effectively argue for scheduling more deliveries during off-peak hours to improve efficiency.