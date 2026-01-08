# Student Gradebook CLI: A guide 
A simple Python command-line application to manage a student gradebook, demonstrates Python's data structures, file handling and basic calculations
The project was written on Python 3.14.0 IDLE.
## Requirements:
- Python 3.14.0 including IDLE or any code editing software (like VSCode, PyCharm)
- A text editor to gain access to .json file.
## Project features: 
- **Add a course**: Enter course code, name, credits, semester, and score.
- **Update a course**: Modify existing course details.
- **Delete a course**: Remove a course from the gradebook.
- **View gradebook**: Display all courses in a tabular format.
- **GPA Calculation**: Compute overall weighted GPA and semester GPA.
- **Persistent storage**: Data is saved in gradebook.json and loaded automatically on startup.
- **Input validation**: Prevents invalid scores, duplicate course codes and missing fields.
## Install & open the project
- Inside the Google Drive file, download both of the .py and .json file.
- In the download menu, select a file that will contains both of the files.
- Install both of the files. 
- Once installed,open the .py file in Python IDLE and run the project.
OR:
You can execute the .py by open the file containing the program on terminal (this will open Command Prompt) and type the following:
```python
python gradebook.py
```
## Use the menu
- You will see the list of actions and type the number of the option in which action you desire:

Gradebook Menu:
1. Add course
2. Update course
3. Delete course
4. View gradebook
5. Calculate GPA
6. Exit
- Input example:
|Code|Name|Credits|Semester|Score|
|-|-|-|-|-|
|AU005.1|Introduction to IT|3|2025|67.0|
- All data will be stored in gradebook.json.
## Notes
- You can directly edit the data in .json file.
- The output will follow the GPA scale below: 
93–100: 4.0
90-93: 3.7
87-89: 3.3
83-86: 3.0
80-82: 2.7
77-79: 2.3
73-76: 2.0
70-72: 1.7
67-69: 1.3
63-66: 1.0
60-62: 0.7
Below 60: 0.0
- Always run the program from the same folder as the .json file.