# School department

## Vision

“School department” is web-application which allows users to record information about students, teachers and the lessons.

Application should provide:
* Storing teachers, students and classes in a database;
* Display list of teachers;
* Updating the list of teachers (adding, editing, removing);
* Display list of students;
* Updating the list of students (adding, editing, removing);
* Display list of classes;
* Updating the list of classes (adding, editing, removing);
* Display number of the classes for students;
* Filtering by date for students;
* Filtering by classes for students.

## 1. Teachers
### 1.1  Display list of teachers

This mode is intended for viewing and editing the teachers list.

Main scenario:
* User selects item “teachers”;
* Application displays list of teachers;

<img src="..\..\SchoolAPI\documentation\img\teachers_table.png"/></img>
Pic. 1.1 Teacher table.

The list displays the following columns:
* First name – teacher`s first name;
* Last name – teacher`s last name;
* Sex – teacher`s sex;
* Year of birth - teacher`s date birthday;
* Country - teacher`s country;
* City - teacher`s city;
* Class teacher - number and char class taught by the teacher;

### 1.2 Add teacher

Main scenario:
* User clicks the “Add” button in the teacher`s list view mode;
* Application displays form to enter teacher`s data;
* User enters teacher`s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If new teacher record is successfully added, then list of teacher`s with added records is displaying.


Cancel operation scenario:
* User clicks the “Add” button in the teachers list view mode;
* Application displays form to enter teacher`s data;
* User enters teacher`s data and presses “Cancel” button;
* Data don’t save in data base, then list of teachers records is displaying to user.
* If the user selects the menu item "Teachers”, ”Classes” or "Students", the data will not be saved to the
database and the corresponding form with updated data will be opened.

<img src="..\..\SchoolAPI\documentation\img\teacher_add_table.png"/></img>
Pic. 1.2 Add teacher.

When adding a teacher, the following details are entered:
* Teacher name – teacher’s name;
* Teacher lastname – teacher’s lastname;
* Sex – user can select choose between male and female;
* Year of birth – integer year of birth;
* Country - country from teacher`s;
* City - city from teacher`s;
* Class teacher - selected existing class;

Constraints for data validation:

* Teacher name – maximum length of 45 characters;
* Teacher lastname – maximum length of 45 characters;
* Sex - required field.
* Country and City - maximum length of 45 characters
* Year of birth – teacher’s year of birth in format dd/mm/yyyy;
* Class teacher – field сan be empty;

### 1.3 Edit teacher

Main scenario:
* User clicks the “Edit” button in the teachers list view mode;
* Application displays form to enter client data;
* User enters teacher’s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is added to database;
* If error occurs, then error message is displaying;
* If teacher’s record is successfully edited, then list of teachers with added records is displaying.

Cancel operation scenario:

* User clicks the “Edit” button in the teachers list view mode;
* Application displays form to enter teacher data;
* User enters teacher data and presses “Cancel” button;
* Data don’t save in data base, then list of teachers records is displaying to user.
* If the user selects the menu item "Teachers”, ”Classes” or "Students", the data will not be saved to the
database and the corresponding form with updated data will be opened

<img src="..\..\SchoolAPI\documentation\img\teacher_edit_table.png"/></img>
Pic.1.3 Edit teacher.

### 1.4 Removing teacher

Main scenario:
* The user, while in the list of clients mode, presses the "Delete" button in the selected teacher line;
* Application displays confirmation dialog “Please confirm delete teacher?”;
* The user confirms the removal of the teacher;
* Record is deleted from database;
* If error occurs, then error message displays;
* If teacher record is successfully deleted, then list of teachers without deleted records is displaying.

Cancel operation scenario:
* User is in display mode of teachers list and press “Delete” button;
* Application displays confirmation dialog “Please confirm delete teacher?”;

## 2. Students

### 2.1  Display list of students

This mode is intended for viewing and editing the Students list.

Main scenario:
* User selects item “Students”;
* Application displays list of Students;

<img src="..\..\SchoolAPI\documentation\img\students_table.png"/></img>
Pic. 2.1 Student table.

The list displays the following columns:
* Id student - Unique student id
* First name – student`s first name;
* Last name – student`s last name;
* Sex – student`s sex;
* Year of birth - student`s date birthday;
* Country - student`s country;
* City - student`s city;
* Class name - number and char class taught by the student;
* Class teacher - name teacher who teaches the student;

### 2.2 Add student

Main scenario:
* User clicks the “Add” button in the student`s list view mode;
* Application displays form to enter student`s data;
* User enters student`s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If new student record is successfully added, then list of student`s with added records is displaying.


Cancel operation scenario:
* User clicks the “Add” button in the student list view mode;
* Application displays form to enter student`s data;
* User enters student`s data and presses “Cancel” button;
* Data don’t save in database, then list of students records is displaying to user.
* If the user selects the menu item "Teachers”, ”Classes” or "Students", the data will not be saved to the
database and the corresponding form with updated data will be opened.

<img src="..\..\SchoolAPI\documentation\img\students_add_table.png"/></img>
Pic. 2.2 Add student.

When adding a student, the following details are entered:
* Student name – student’s name;
* Student lastname – student’s lastname;
* Sex – user can select choose between male and female;
* Year of birth – integer year of birth;
* Country - country from student`s;
* City - city from student`s;
* Class name - selected existing class;
* Class teacher - name teacher who teaches the student;

Constraints for data validation:

* Student name – maximum length of 45 characters;
* Teacher lastname – maximum length of 45 characters;
* Sex - required field.
* Country and City - maximum length of 45 characters
* Year of birth – student’s year of birth in format dd/mm/yyyy;
* Class name - required field;
* Class teacher – required field;

### 2.3 Edit student

Main scenario:
* User clicks the “Edit” button in the students list view mode;
* Application displays form to enter student data;
* User enters student’s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is added to database;
* If error occurs, then error message is displaying;
* If student’s record is successfully edited, then list of students with added records is displaying.

Cancel operation scenario:

* User clicks the “Edit” button in the student list view mode;
* Application displays form to enter student data;
* User enters student data and presses “Cancel” button;
* Data don’t save in database, then list of students records is displaying to user.
* If the user selects the menu item "Teachers”, ”Classes” or "Students", the data will not be saved to the
database and the corresponding form with updated data will be opened

<img src="..\..\SchoolAPI\documentation\img\students_edit_table.png"/></img>
Pic.2.3 Edit student.

### 2.4 Removing student

Main scenario:
* The user, while in the list of student mode, presses the "Delete" button in the selected student line;
* Application displays confirmation dialog “Please confirm delete student?”;
* The user confirms the removal of the student;
* Record is deleted from database;
* If error occurs, then error message displays;
* If student record is successfully deleted, then list of students without deleted records is displaying.

Cancel operation scenario:
* User is in display mode of students list and press “Delete” button;
* Application displays confirmation dialog “Please confirm delete student?”;

## 3. Classes

### 3.1  Display list of classes

This mode is intended for viewing and editing the classes list.

Main scenario:
* User selects item “Classes”;
* Application displays list of Classes;

<img src="..\..\SchoolAPI\documentation\img\class_table.drawio.png"/></img>
Pic. 3.1 Class table.

The list displays the following columns:
* Id сlass - Unique сlass id
* Class name – Classe`s name (Int and char);
* Year_start - date start class;
* Year_finish - date finish class;
* Teacher_name - teacher`s name;
* Class student - list of students;

### 3.2 Add classes

Main scenario:
* User clicks the “Add” button in the classes list view mode;
* Application displays form to enter classes data;
* User enters student`s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If new class record is successfully added, then list of classes with added records is displaying.


Cancel operation scenario:
* User clicks the “Add” button in the class list view mode;
* Application displays form to enter classes data;
* User enters classes data and presses “Cancel” button;
* Data don’t save in database, then list of classes records is displaying to user.
* If the user selects the menu item "Teachers”, ”Classes” or "Students", the data will not be saved to the
database and the corresponding form with updated data will be opened.

<img src="..\..\SchoolAPI\documentation\img\class_add_table.png"/></img>
Pic. 3.2 Add class.

When adding a student, the following details are entered:
* Class name – Classe`s name (Int and char);
* Year_start - date start class;
* Year_finish - date finish class;
* Teacher_name - teacher`s name;
* Class student - list of students;

Constraints for data validation:

* Class name – required field (select 1 name from list);
* Year_start - year when started teach in format dd/mm/yyyy;
* Year_finish - year when finished teach in format dd/mm/yyyy;
* Teacher_name - required field (select 1 name teacher`s from existing list);
* Class student - required field (select 1 name student`s from existing list);

### 3.3 Edit class

Main scenario:
* User clicks the “Edit” button in the class list view mode;
* Application displays form to enter class data;
* User enters classes data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited data is added to database;
* If error occurs, then error message is displaying;
* If class record is successfully edited, then list of classes with added records is displaying.

Cancel operation scenario:

* User clicks the “Edit” button in the class list view mode;
* Application displays form to enter class data;
* User enters class data and presses “Cancel” button;
* Data don’t save in database, then list of classes records is displaying to user.
* If the user selects the menu item "Teachers”, ”Classes” or "Students", the data will not be saved to the
database and the corresponding form with updated data will be opened.

<img src="..\..\SchoolAPI\documentation\img\class_edit_table.png"/></img>
Pic.3.3 Edit class.

### 2.4 Removing student

Main scenario:
* The user, while in the list of class mode, presses the "Delete" button in the selected class line;
* Application displays confirmation dialog “Please confirm delete class?”;
* The user confirms the removal of the class;
* Record is deleted from database;
* If error occurs, then error message displays;
* If class record is successfully deleted, then list of classes without deleted records is displaying.

Cancel operation scenario:
* User is in display mode of classes list and press “Delete” button;
* Application displays confirmation dialog “Please confirm delete class?”;