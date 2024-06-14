from bs4 import BeautifulSoup
import requests
import json

def upcoming_contests():
    response = requests.get("https://codeforces.com/contests")
    soup = BeautifulSoup(response.content, 'html5lib')
    contest_lists = []
    upcoming_list=[]
    upcoming_contest = soup.find_all("div", {"class":"datatable"})[0].find_all("tr")

    for contest in upcoming_contest:
        coloums = contest.find_all("td")
        if(len(coloums)==6):
            name = (
                coloums[0].text.strip().replace("Enter"," " ).replace("Virtual participation", " ")
            )
            start_dur = coloums[2].text.strip()
            length = coloums[3].text.strip()
        
            upcoming_list.append(
                {"name" : name,
                "start duration":start_dur,
                "length": length
            })
    contest_lists.append({"upcoming contest": upcoming_list})
    contest_lists = json.dumps(contest_lists,indent=2)
    print(contest_lists)
    return contest_lists

    
def past_Contest():
    response = requests.get("https://codeforces.com/contests")
    soup = BeautifulSoup(response.content, 'html5lib')
    contest_lists = []
    past_contest_list=[]
    past_contest = soup.find_all("div", {"class":"datatable"})[1].find_all("tr")

    for contest in past_contest:
        coloums = contest.find_all("td")
        if(len(coloums)==6):
            name = (
                coloums[0].text.strip().replace("Enter"," " ).replace("Virtual participation", " ").replace("\u00bb", " ")
            )
            start_dur = coloums[2].find("span", class_="format-date").text.strip()
            length = coloums[3].text.strip()
            name = " ".join(line.strip() for line in name.splitlines() if line.strip()) 
            past_contest_list.append(
                {"name" : name,
                "start duration":start_dur,
                "length": length
            })
    contest_lists.append({"past contest": past_contest_list})
    contest_lists = json.dumps(contest_lists,indent=2)
    print(contest_lists)
    return contest_lists


def user(handle:str):
    response = requests.get(f'https://codeforces.com/profile/{handle}')
    
    soup = BeautifulSoup(response.content, 'html5lib')
    
    user={}
    information_user = soup.find("div", {"class":"main-info"})
    user["handle"] = information_user.find("a").text.strip()
    info_string = information_user.find("div", style="margin-top: 0.5em;").text.strip()
    info_string = info_string.split(",")
    if(info_string[0].startswith("From")):
        user["username"] = ""
    else :user["username"] = info_string[0]
    try:
        user["City"] = info_string[1].replace(" ", "")
    except:
        user["City"] = ""
    try:
        location=info_string[2].split("From")
        user["Country"] = location[0].strip()
        user["Organization"] = location[1].replace(" ", "")
    except:
        user["Country"] = ""
        user["Organization"] = ""
    
    information_contest = soup.find("div",{"class":"info"}).find_all("li")[0].text.strip()
    information_contest = " ".join(i.strip() for i in information_contest.splitlines() if i.strip())
    test = information_contest.split()
    user["Contest rating"] = test[2]
    user["Max rating"] = test[5].replace(")","")
    user["Max rank"] = test[4].replace(",","")
    
    information_contri = soup.find("div",{"class":"info"}).find_all("li")[1].text.strip()
    information_contri = " ".join(i.strip() for i in information_contri.splitlines() if i.strip())
    test = information_contri.split()
    user["Contribution"] = test[1]
    
    information_freinds = soup.find("div",{"class":"info"}).find_all("li")[2].text.strip()
    information_freinds = " ".join(i.strip() for i in information_freinds.splitlines() if i.strip())
    test = information_freinds.split()
    user["Friend"] = test[2]
    
    information_last_Visit = soup.find("div",{"class":"info"}).find_all("li")[3].text.strip()
    information_last_Visit= " ".join(i.strip() for i in information_last_Visit.splitlines() if i.strip())
    test = information_last_Visit.split()
    if(test[3]!=None):
        user["Last visit"] = test[2] + test[3]
    else:
        user["Last visit"] = test[2] + " "  
    
    information_prblm = soup.find("div",{"class":"_UserActivityFrame_footer"}).text.strip()
    information_prblm= " ".join(i.strip() for i in information_prblm.splitlines() if i.strip())
    test = information_prblm.split()
    user["Total Problems"] = test[0]
    user["Total Problems Solved Last Year"] = test[6]
    user["Total Problems Solved in a Row Max"] = test[20]
    print(json.dumps(user,indent=1))
    return user



def user_compare(handle_of_first:str, handle_of_second:str):
    response1 = requests.get(f'https://codeforces.com/profile/{handle_of_first}')
    response2 = requests.get(f'https://codeforces.com/profile/{handle_of_second}')
    soup1 = BeautifulSoup(response1.content, 'html5lib')
    soup2 = BeautifulSoup(response2.content, 'html5lib')
    user={}
    user1={}
    user2={}
    
    information_user = soup1.find("div", {"class":"main-info"})
    user1["handle"] = information_user.find("a").text.strip()
    
    information_contest = soup1.find("div",{"class":"info"}).find_all("li")[0].text.strip()
    information_contest = " ".join(i.strip() for i in information_contest.splitlines() if i.strip())
    test = information_contest.split()
    user1["Contest rating"] = test[2]
    user1["Max rating"] = test[5].replace(")","")
    user1["Max rank"] = test[4].replace(",","")
    
    information_contri = soup1.find("div",{"class":"info"}).find_all("li")[1].text.strip()
    information_contri = " ".join(i.strip() for i in information_contri.splitlines() if i.strip())
    test = information_contri.split()
    user1["Contribution"] = test[1]
    
    information_prblm = soup1.find("div",{"class":"_UserActivityFrame_footer"}).text.strip()
    information_prblm= " ".join(i.strip() for i in information_prblm.splitlines() if i.strip())
    test = information_prblm.split()
    user1["Total Problems"] = test[0]
    user1["Total Problems Solved Last Year"] = test[6]
    user1["Total Problems Solved in a Row Max"] = test[20]
    
    information_user = soup2.find("div", {"class":"main-info"})
    user2["handle"] = information_user.find("a").text.strip()
    
    information_contest = soup2.find("div",{"class":"info"}).find_all("li")[0].text.strip()
    information_contest = " ".join(i.strip() for i in information_contest.splitlines() if i.strip())
    test = information_contest.split()
    user2["Contest rating"] = test[2]
    user2["Max rating"] = test[5].replace(")","")
    user2["Max rank"] = test[4].replace(",","")
    
    information_contri = soup2.find("div",{"class":"info"}).find_all("li")[1].text.strip()
    information_contri = " ".join(i.strip() for i in information_contri.splitlines() if i.strip())
    test = information_contri.split()
    user2["Contribution"] = test[1]
    
    information_prblm = soup2.find("div",{"class":"_UserActivityFrame_footer"}).text.strip()
    information_prblm= " ".join(i.strip() for i in information_prblm.splitlines() if i.strip())
    test = information_prblm.split()
    user2["Total Problems"] = test[0]
    user2["Total Problems Solved Last Year"] = test[6]
    user2["Total Problems Solved in a Row Max"] = test[20]
    
    user = {"User 1": user1, 
            "User 2": user2}
    user = json.dumps(user, indent=1)
    print(user)
    

# upcoming_contests()
# past_Contest()
# user("Give Handle here")
# user_compare("Give handle for first user", "Give handle for second user")  
