# public-sector-quiz-app-summative-two-ifcs
A Quiz Application Developed Using Streamlit and Python. Tests knowledge on the public sector, covering key topics such as security and data sensitivity.

## Introduction
Working as a degree apprentice within IBM Consulting involves solving problems and delivering technological solutions to clients. As a data scientist on a public sector consulting project, I am working in an environment where security, data sensitivity, and integrity are critical. In this type of work environment, employees are expected to maintain strong awareness of strict organisational procedures/ policies, ethics and operational expectations. This helps keep the public sector secure and prevents any official sensitive data from being exploited or leaked.
However, serious incidents can occur when employees accidentally expose confidential public sector information due to knowledge gaps regarding organisational policies and consequences.
Hence, I am developing a quiz application which will test the core knowledge of employees entering/ working in the public sector through a multiple-choice quiz. The quiz will have 10 questions covering crucial topics like cybersecurity and data sensitivity. The purpose of this quiz will be to test the "must-have"/ essential knowledge of public sector practices and identify any employee knowledge gaps. As a result, the quiz can also be used to reinforce knowledge of core public sector behaviours and strengthen any weak points of knowledge. To summarise, this application is designed with the intention of mitigating public sector incidents through proper education and quizzing.
I will be using Python and the Streamlit framework to develop my application as a minimum viable product (MVP). Developing an MVP will allow me to implement and validate core functionality quickly. Alongside rapid development, having an MVP will enable smoother application scaling in the future.

**Key features of my MVP application include:** <br>
-10 Multiple-choice questions <br>
-A CSV file to store pre-defined questions + answers <br>
-Input validation <br>
-Results screen showing score, pass/fail rating and visualisations. <br>

When developed, my quiz will act as a model/ proof-of-concept for how training courses and learning plans could be structured to help current employees and new joiners develop awareness of organisational policies and operations.

## Design

### GUI Designs:

Below are Figma designs of the Graphical User Interface (GUI) of my quiz application.
The user interface design is simple and linear user journey designed to make the quiz easy to understand and navigate. The flow comprises the following screens:

![alt text](image-3.png)
*Screen 1: Welcome screen. This is the first page that the user sees when they load up the quiz. It has an input box for the user to enter their name and an OK button.*

![alt text](image-8.png)

![alt text](image-27.png)
*Screen 2: Instructions screen. This is the next page that the user sees. This screen displays information about the quiz structure, the number of questions, the pass mark, and the assessed topics. There is a ready button to start the questions.*

![alt text](image-11.png)
*Question Screens: Every question is presented on a new screen. The question is at the top with the multiple choice answers underneath. Next to each option, there is a small circle which can be clicked to finalise the answer. At the bottom, there's a "Next" button which takes the user to the next question.*

![alt text](image-12.png)

![alt text](image-14.png)
*Screen 4: Results Page. This displays the user's score along with a pass or fail rating. Visualisations are also displayed which show the number of correct and incorrect questions. This page also displays the incorrectly answered questions along with correct responses. A 'Retry' button is presented to those who fail.*

![alt text](image-15.png)

*Below are screen designs for handling invalid user inputs (unhappy pathway):*
![alt text](image-17.png)

![alt text](image-18.png)
*Error Messagebox (Empty name field). If the user leaves the name field empty, this error messagebox is displayed.*

![alt text](image-19.png)

![alt text](image-20.png)
*Error Messagebox (Invalid Characters). If the user inputs invalid characters in the name field, this error messagebox is displayed.*

Figma Designs Prototype Link: <br>
```https://www.figma.com/proto/8pMmDQwf51MyWRiGa8xm4e/Summative-2-Quiz-Design?node-id=0-1&t=DFJ5UlcQQq93g9qx-1```

<br>

### User Journey Map:
![alt text](image-22.png)

<br>

### Quiz Flowchart - User Journey:
The following diagram displays the flow of the application from start to finish and helps visualise the journey that users take when they interact with the program. It shows the different pathways of the application based on certain conditions or situations.

![alt text](image-26.png)

<br>

### Functional and Non-Functional Requirements:
Functional Requirements (FR) define what the application must do, guiding the development of specific features and functionality.
Non-Functional requirements (NFR) define key attributes of the application such as usability and maintainability, guiding effective and efficient development.

<br>

**Functional Requirements (Data) Table:**

| ID   | Requirement                                                                 | Category              |
|------|-----------------------------------------------------------------------------|---------------------------------|
| FR1  | System must display "Welcome" screen when quiz application is run          | User Interface/ User Flow      |
| FR2  | System must allow users to enter name                                       | Input                           |
| FR3  | System must validate name input                                            | Input Validation                |
| FR4  | System must display screen with custom welcome message and quiz information | User Interface/ Output         |
| FR5  | System must read 10 questions and multiple-choice answers from CSV file    | Data Management                 |
| FR6  | System must display one question at a time and present all multiple choice answers to user | User Interface/ Output |
| FR7  | System must allow user to select one multiple-choice answer                | Input                           |
| FR8  | System must track and store live user score in CSV file                    | Scoring Mechanism/ Data Management |
| FR9  | System must track and keep a list of incorrectly answered questions in CSV file | Data Management/ Scoring |
| FR10 | System must detect all button clicks and respond appropriately             | User Interface/ Output         |
| FR11 | System must calculate pass/ fail rating based on user score              | Scoring/ Data Management       |
| FR12 | System must display "Results" screen at the end and output a final score accompanied by a pass/ fail rating | User Interface/ Output |
| FR13 | System must output score visualisations and incorrectly answered questions along with their correct responses on the "Results" page | User Interface/ Output |
| FR14 | System must display a "Retry" button on the "Results" page for users who fail the quiz | User Interface/ Output |
<br>

**Non-Functional Requirements (Data) Table:**

| ID   | Requirement                                                                 | Description + Justification              |
|------|-----------------------------------------------------------------------------|---------------------------------|
| NFR1  | Clear User Interface          | The UI must be well-organised with easily understandable layouts. Each screen must have consistent spacing between elements, and buttons must be noticeable. This reduces user errors and makes the application easy to interact with.     |
| NFR2  | Usability                                       | The application must be simple, easy to understand, yet intuitive. This makes the quiz easy to use and suitable for users from different backgrounds.                           |
| NFR3  | Accessibility                                            | The application must be simple. Text must be readable through appropriate font size. The colour scheme should be high contrast. UI elements must be clearly visible. This makes the application easily accessible to users with difficulties like blurry vision and colour blindness.                |
| NFR4  | Performance and Fast Response Times | The questions must be displayed instantly to the user as well as the end results. There must be no visible delay in these processes. This improves the user experience.         |
| NFR5  | Maintainability    | Code must be structured using the OOP (object-oriented programming) paradigm and pure functions. Code must follow standard Python conventions. This supports future modifications and development.                |
| NFR6  | Reliable data storage  | The quiz should store and track user progress/ scores without crashing. This prevents the loss of results. |
| NFR7  | Portability                | The application must run on all devices which have Python and the required dependencies installed. This allows users to take the quiz from any machine. |
<br>

### Tech Stack Outline
Programming Language: Python <br>
GUI toolkit: Streamlit <br>
Data Storage (questions, answers and scores): CSV files <br>
Testing: pytest framework <br>
Version Control: GitHub <br>
Continuous Integration (CI/CD): GitHub Actions - Python Application <br>

### Code Design - OOP



## Development
