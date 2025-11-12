#  Parcels CRM Data Analysis Tool

##  Overview
This Python program is a simple **Customer Relationship Management (CRM) data analysis tool**   
It provides an interactive, menu-driven interface that allows users to explore customer issue data stored in a CSV file.

The tool helps visualize issue trends, resolution times, and regional performance using **Pandas** for data analysis and **Matplotlib** for data visualization.

---

##  Features

- **Main Menu Interface**  
  A text-based interface that allows users to choose from several reporting options.

- **Total Issues by Type**  
  Displays how many times each type of issue (e.g., delivery, account, service complaint) has been logged.

- **Average Resolution Time**  
  Calculates and visualizes the average number of days it takes to resolve each issue type using a bar chart.

- **Issues and Resolutions by Region**  
  Generates stacked bar charts to compare:
  - Number of issues by region and issue type  
  - Number of resolutions by region and resolution type  

- **Input Validation**  
  Ensures users enter valid numeric options before processing.

---

##  How It Works

1. The user selects a menu option (1–4).  
2. Depending on the choice:
   - **Option 1:** Prompts for an issue type, counts occurrences, and displays totals.  
   - **Option 2:** Calculates mean resolution times and plots them.  
   - **Option 3:** Groups data by region and plots issue and resolution breakdowns.  
   - **Option 4:** Exits the program gracefully.  
3. All data is read from `Task4a_data.csv`, which should contain columns such as:
   - `Issue Type`
   - `Days To Resolve`
   - `Region`
   - `How Resolved`

---

## Requirements

- Python 3.x  
- [pandas](https://pandas.pydata.org/)  
- [matplotlib](https://matplotlib.org/)

Install dependencies using:

```bash
pip install pandas matplotlib
