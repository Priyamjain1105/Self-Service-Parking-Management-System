# Self-Service-Parking-Management-System
I have developed this personal project called the “Self Service Parking Management System" to gain practical experience and enhance my programming skills.

This Project Aim is to enhance the process of parking entry and exit with more security and  efficient data management for highly important and secured areas such as government buildings or military areas or religiously or culturally reserved areas and many more .The aim is not to  exchange the jobs but to enhance the security of these places moreover it can only work with coordination of security personals and managing personals. With this system, parking attendants can easily register entries, verify exits, manage the records, and generate accurate bills for the parked vehicles. It eliminates the need for manual paperwork and reduces the chances of errors, resulting in smoother operations and improved customer service.

Through this project, I have honed my programming abilities, particularly in areas such as data handling, file management, user input validation, and time/date calculations. By using essential programming concepts and libraries like datetime, pickle, csv, and os, I have implemented various functionalities that contribute to the overall efficiency of the system.

Moreover, this project has provided me with a practical understanding of how to design and develop a software application from scratch. It has allowed me to apply my knowledge of programming principles and problem-solving techniques in a meaningful way.

In summary, the Parking Bill Management System showcases my commitment to expanding my programming skills and acquiring practical knowledge. It serves as evidence of my ability to develop functional applications that automate complex processes and contribute to increased efficiency. 

I would like to express my heartfelt appreciation to Mr. Ritesh Sahu for his invaluable guidance in teaching me the Python programming language. His comprehensive instruction and insightful explanations have equipped me with the necessary skills to independently develop this project.

Flow of the program:-

The Program follows a structured flow, beginning with the main menu screen. The main menu presents different options based on the user's needs. 

ENTRY SCREEN:  Choosing the "Entry" option leads to the entry screen, where users input their name and phone number. The system verifies the phone number, records the entry time, and assigns a unique serial number for each entry. Once the entry is validated, a permit is granted to the user.

EXIT SCREEN:  On the other hand, selecting the "Exit" option displays the exit screen. Users can verify their serial number, record the exit time, and generate a parking bill receipt. The receipt includes crucial details like the serial number, name, verified phone number, date, entry time, and exit time.

MANGER: Additionally, the system offers a "Manager" option for parking attendants or administrators to oversee various aspects of the parking system. The manager screen provides functionalities such as viewing all previous parking records (both entry and exit), manually adding an entry record, updating existing records (prior to exit), deleting records (prior to exit), viewing present entries, backing up data, and removing empty lists from the entry records.

In summary, the Parking Bill Management System provides a clear flow where users can enter and exit the parking lot, while managers have access to comprehensive management features. This streamlined approach ensures efficient parking management and facilitates the smooth operation of the system.

Functions:-
The provided code is an implementation of a self-service parking management system. It allows users to enter and exit a parking lot and generates bills for their parking duration. Here's an explanation of the code:
The code begins with importing necessary modules such as time, pickle, csv, datetime, and os. These modules provide functionality for time manipulation, data serialization, CSV file handling, and operating system-related operations.

The code defines several functions:

date(): Retrieves the current date and returns it as a string.
ptime(): Retrieves the current time and returns it as a string.
main(): Displays the main menu and handles user input for different operations (entry, exit, managing, quit).
write_heading(): Writes the header for three files (entry records, exit records, bill records).
entry(): Handles the entry process, collects user information (name, phone number), and stores the entry record.
exitn(): Handles the exit process, verifies the user's entry record, collects the exit time, and generates a bill.
deco(): Prints a decorative line separator.
manager(): Displays the management menu and handles different management operations (view records, add entry manually, update record, delete record, view present entries, backup data, remove empty lists, return to main menu).
sno(): Generates a unique serial number for the entry record.
checks(s): Checks if the given serial number exists in the entry records and verifies that the user has not already exited
read(): Reads and displays all previous parking records (entry and exit).
write(): Manually adds an entry record by collecting user information and storing it.
backup(): Creates a backup of the entry records.
delete(sno): Deletes a specific record by serial number from the entry records.
delete_empty_list(): Deletes any empty lists from the entry records.
update(): Updates a specific record in the entry records with new information.
readp(): Reads and displays all present entry records.



