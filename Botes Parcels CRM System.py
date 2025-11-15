import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Time taken to resolve issue")
        print("### 3. Issue and resolution based on region")
        print("### 4. Exit")

        choice = input('Enter your number selection here: ')

        if choice in ['1','2','3','4']:
            print("choice accepted")
            flag = False
            return choice
        else:
            print("please enter a number from 1-3")


            
    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')
        
        if choice in ['1','2','3','4']:
            print("choice accepted")
            flag = False
        else:
            print("please enter a number from 1-4")

        
        choice = int(choice)


    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg
######################################### option 2 #############################################

def data_issue_time():
    
    df = pd.read_csv("Task_data.csv")
    
    df1 = df.groupby('Issue Type')['Days To Resolve'].mean().sort_values()
    print(df1)

    df1.plot(kind="bar",color='green',title='Avarage resolution time wtih issue')


    plt.xlabel("Issue")
    plt.ylabel("days to resolve")
    plt.tight_layout()
    plt.show()   

######################################### option3 ##############################################

def issue_by_region():

    df = pd.read_csv("Task_data.csv")
    df1 = df.groupby(['Region','Issue Type']).size().unstack(fill_value=0)

    print(df1)

    df1.plot(kind="bar",stacked=True,figsize=(10,6),colormap='Set2',title='issue by region')
    plt.ylabel("number of issues")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    resolution = df.groupby(['Region','How Resolved']).size().unstack(fill_value=0)
    print(resolution)
    
    resolution.plot(kind="bar",stacked=True,figsize=(10,6),colormap='Set3',title='resolutions by region')

    plt.ylabel("num of resolutions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

######################################## selection for menu choice #################################   

main_menu_choice = main_menu()
if main_menu_choice ==  "1":
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))
elif main_menu_choice == "2":
    plot_data_2 = data_issue_time()
    print(plot_data_2)
elif main_menu_choice == "3":
    plot_data_3 = issue_by_region()
    print(plot_data_3)
else:
    print("you have exited the program goodbye !!!!")
    quit 

