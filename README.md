# automated_plot_test

This project is a demo of how to automate python scripts with Windows Task Scheduler and Gthub Actions.
The plot below is updated daily with the script.

![Final plott](https://github.com/martingeew/automated_plot_test/blob/main/demo_data/stock_plot_2024-10-13_13-15-06.png?raw=true)

## Instructions to Set Up and Run the Project with Windows Task Scheduler

### Step 1: Clone or Download the Project
Download or clone this project to your local machine.

### Step 2: Modify the `.bat` File to Point to Your Local Project Directory

This project includes a `.bat` file that helps automate the process of activating the virtual environment and running the Python script. Before running the `.bat` file, you need to modify the paths to match the location where you saved the project on your local machine.

#### Instructions to Update the `.bat` File:

1. **Locate the `schedule.bat` file**:
   - The file is located in the root directory of the project.

2. **Update the Project Path**:
   - Open the `.bat` file in any text editor or code editor.
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