# call after successfully login:

from os import name
import usefulLinks
import profile
import friend
import friendList


def mainPage(nameofuser):
    global name
    name = nameofuser

    friend.has_pending_requests(nameofuser)
    
    kbInput = '-1'

    while (kbInput != '0'):
        print("")
        print("*************")
        print("* InCollege *")
        print("*************")
        print("")
        print("Main page")
        print("------------------------------------")
        print("| '1' to find someone you know      |")
        print("| '2' for learn new skill           |")
        print("| '3' for job search/ internship    |")
        print("| '4' for useful links              |")
        print("| '5' to go to your profile         |")
        print("| '6' to show your network          |")
        print("| '7' to show your friendList       |")
        print("| '0' to return to login            |")
        print("-------------------------------------")
        print("")
        kbInput = input("Enter page you want to go to: ")

        if (kbInput == '1'):
            peopleSearchPage()
        elif (kbInput == '2'):
            skillsPage()
        elif (kbInput == '3'):
            jobSearchPage()
        elif (kbInput == '4'):
            usefulLinks.menu()
        elif (kbInput == '5'):
            profile.profileMenu(name)
        elif (kbInput == '6'):
            friend.friendMenu(name)
        elif (kbInput == '7'):
            friendList.friendList1(name)
        elif (kbInput == '0'):
            return
        else:
            print("Please enter an available option!!\n")


def postNewJob():
    select = "x"
    print("-----------------------------------")
    print(" Welcome to the Job Creation Page! ")
    print("-----------------------------------")
    while (select != 'y' and select != 'Y' and select != 'n' and select != "N"):
        select = input("Would you like to create a job? ('y' or 'n'): ")
        if (select == 'y' or select == 'Y'):
            if (has_max_jobs()):
                mainPage()
            createNewJob()
        elif (select == 'n' or select == 'N'):
            mainPage()
        else:
            print("Invalid input please try again.")


def has_max_jobs():
    count = 0
    for line in open("jobs.txt", "r"): count += 1
    if count == 10 or count > 10:
        print("All permitted jobs have been posted(10 jobs), please come back later." + "\n")
        return True
    return False


def createNewJob():
    print("")
    title = input("Enter the title for your job: ")
    description = input("Enter the description for your job: ")
    employer = input("Enter the employer for your job: ")
    location = input("Enter the location for your job: ")
    salary = input("Enter the salary for your job: ")

    saveJob(name, title, description, employer, location, salary)

    print("\nyour job has been saved")
    mainPage(name)


def saveJob(n, t, d, e, l, s):
    file4 = open("jobs.txt", "a")
    file4.write(n + "\t" + t + "\t" + d + "\t" + e + "\t" + l + "\t" + s + "\n")
    file4.close()


def peopleSearchPage():
    a = -1
    print("----------------------------")
    print(" Welcome to Contact Search! ")
    print("----------------------------")

    file3 = open("accounts.txt", "r")

    firstname = input("Enter the first name of the contact you're looking for: ")
    lastname = input("Enter the last name of the contact you're looking for: ")
    name = firstname + " " + lastname

    from login import find_contacts

    if (find_contacts(name)):
        print("")
        print("They are a part of the InCollege system." + "\n")
        mainPage()
    else:
        print("")
        print("They are not a part of the InCollege system" + "\n")
        mainPage()
    a = input("Press '0' to return.")
    if int(a) == 0:
        mainPage()

    file3.close()


def skillsPage():
    kbInput = "6"

    while (kbInput != "1" and kbInput != "2"
           and kbInput != "3" and kbInput != "4" and kbInput != "5" and kbInput != "b"):
        print("--------------------------------------------------------")
        print("Available skills to learn:")
        print("Enter the Coressponding Number with a skill to learn it today:")
        print(" 1. LeaderShip")
        print(" 2. Basic programming in Python")
        print(" 3. Make an outstanding resume")
        print(" 4. Professional writing")
        print(" 5. Microsoft Excel basics")
        kbInput = input(" Or enter b for return to mainPage\n")

        if (kbInput != "1" and kbInput != "2"
                and kbInput != "3" and kbInput != "4" and kbInput != "5" and kbInput != "b"):
            print("Please enter the available options")
        elif (kbInput != "b"):
            print("Page under construction.")
            a = input("Press '0' to return")
            if int(a) == 0:
                mainPage(name)

    if (kbInput == "b"):
        mainPage(name)

def appliedJob():
    print("applied jobs")
def notAppliedJob():
    print("not applied jobs:")

def jobApplication(title):

    print("----------JOB APPLICATION----------")
    g = input("Enter your graduation date Ex:(mm/dd/yyyy): ")
    s = input("Enter the day you can start Ex:(mm/dd/yyyy): ")
    d = input("Describe why you feel fit for the job: ")
    
    saveJobApp(title, g, s, d)
    

def saveJobApp(title, g, s, d):
    file5 = open("appliedJobs.txt", "a")
    file5.write(title + "\t" + g + "\t" + s + "\t" + d + "\n" )
    file5.close()




def jobSearchPage():
    print("\n")
    print("Job Search/ Internship")
    print("------------")
    print("List of all jobs")
    print("------------")
    a = "x"

    jobFile = open("jobs.txt",'r')
    jobList = []
    for line in jobFile:
        if line != '\n':
            n, t, d, e, l, s = line.split('\t')
            jobList.append(t)

    #jobList = set(jobList)
    '''
    jobOptionInput = input("Enter 'a' to see list of applied jobs or 'n' for list of jobs that you have not applied: ")
    
    if jobOptionInput == "a":
        appliedJob()
    elif jobOptionInput == "n":
        notAppliedJob()
    '''

    
    print(*jobList, sep="\t")
    print("------------------------------------------------------------")
    j=0
    #Just a start Ill come back in a few
    while(j!=1):
        selection = input("Type the name of the job that you would like to apply for (Case Sensitive): ")
        if (selection == t):
            jobApplication(t)
            j=1
        
            

    
    while (a != "0" and a != "1"):
        a = input("Press '0' to return or 1 to post a new job.")
        if a == "0":
            mainPage(name)
        elif (a == "1"):
            postNewJob()
        else:
            print("Please enter an available option!!\n")
    





#saveJob(name, title, description, employer, location, salary)
#jobSearchPage()

    


def pageUnderConstruction():
    print("")
    print("--------------------------------------------------------")
    print("Page under construction")