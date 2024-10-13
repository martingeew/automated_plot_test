# automated_plot_test

## Instructions to Set Up and Run the Project with Windows Task Scheduler

### Step 1: Clone or Download the Project
Download or clone this project to your local machine.

### Step 2: Modify the `.bat` File to Point to Your Local Project Directory

This project includes a `.bat` file that helps automate the process of activating the virtual environment and running the Python script. Before running the `.bat` file, you need to modify the paths to match the location where you saved the project on your local machine.

#### Instructions to Update the `.bat` File:

1. **Locate the `.bat` file**:
   - The file is located in the root directory of the project (e.g., `run_project.bat`).

2. **Update the Project Path**:
   - Open the `.bat` file in any text editor (such as Notepad).
   - Replace `C:\path\to\your\project` with the actual path where you saved the project.

3. **Modify These Paths in the `.bat` File**:
   - Update the **path to the project directory**:
     ```bat
     cd C:\path\to\your\project\automated_plot_test
     ```
   - Update the **path to the virtual environment activation script**:
     ```bat
     call C:\path\to\your\project\automated_plot_test\.venv\Scripts\activate.bat
     ```
   - Update the **path to the Python script** you want to run:
     ```bat
     python C:\path\to\your\project\automated_plot_test\generate_report.py
     ```