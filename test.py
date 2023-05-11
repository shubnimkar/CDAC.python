#FUNCTIONS DEFINITION

Teams={"Chennai Super Kings":[" Name=Chennai Super Kings\n","Owner=N. Srinivasan\n","Captain=M.S Dhoni\n","Sponsers=Vison 11\n","Support_staff=",["Coach:""Stephen Fleming"]],
"Mumbai Indians":[" Name=Mumbai Indians\n","owner=Mukesh Ambani\n","captain=Rohit Sharma\n","sponsers=Reliance Group\n","support_staff=Coach:""Mark Boucher"]
,"Kolkata Knight Riders":[" Name=Kolkata Knight Riders\n","Owner=Shahrukh Khan\n","Captain=Nitish Rana\n","Sponsers=TV9 Network\n","Support_staff=Coach:Chandrakant Pandit"]
,"Sun Risers Hyderabad":[ "Name=Sun Risers Hyderabad\n","Owner=Sun Group\n","Captain=Aiden Markram\n","Sponsers=FanCraze\n","Support_staff=Coach:Brian Lara"]
,"Punjab Kings":[" Name=Punjab Kings\n","Owner=Preity Zinta\n","Captain=Shikhar Dhawan\n","Sponsers=EbixCash\n","Support_staff=Coach:Trevor Bayliss"]
,"Lucknnow Super Giants":[" Name=Lucknnow Super Giants\n","Owner=RPSG Group\n","Captain=KL Rahul\n","Sponsers=My11Circle\n","Support_staff=Coach:Andy Flower"]
,"Delhi Capitals":[" Name=Delhi Capitals\n","Owner=JSW Group\n","Captain=David Warner\n","Sponsers=Viacom18\n","Support_staff=Coach:Ricky Ponting"]
,"Rajasthan Royals":[" Name=Rajasthan Royals\n","Owner=Manoj Badale\n","Captain=Sanju Samson\n","Sponsers=Luminous Power Technologies\n","Support_staff=Coach:Kumar Sangakkara"]
,"Royal Challengers Bangalore":[ "Name=Royal Challengers Bangalore\n","Owner=United Spirits\n","Captain=Faf du Plessis\n","Sponsers=Qatar Airways\n","Support_staff=Coach:Sanjay Bangar"]
,"Gujarat Titans":[" Name=Gujarat Titans\n","Owner=CVC Capital Partners\n","Captain=Hardik Pandya\n","Sponsers=Capri Global\n","Support_staff=Coach:Ashish Nehra"]}
list=["Chennai Super Kings","Kolkata Knight Riders","Mumbai Indians","Sun Risers Hyderabad","Punjab Kings","Lucknow Super Giants","Delhi Capitals","Rajasthan Royals","Royal Challengers Bangalore","Gujarat Titans"]

venue={"Ahmedabad":["Ahmedabad\n","\tLocation: Narendra Modi Stadium\n","\tCapacity: 132,000"],
       "Bengaluru":["Bengaluru\n","\tLocation: M. Chinnaswamy Stadium\n","\tCapacity: 40,000"],
       "Mumbai":["Mumbai\n","\tLocation: Wankhede Stadium\n","\tCapacity: 33,108"],
       "Hyderabad":["Hyderabad\n","\tLocation: Rajiv Gandhi International Cricket Stadium\n","\tCapacity: 55,000"],
       "Jaipur":["Jaipur\n","\tLocation: Sawai Mansingh Stadium\n","\tCapacity: 30,000"],
       "Delhi":["Delhi\n","\tLocation: Arun Jaitley Stadium\n","\tCapacity: 41,842"],
       "Mohali":["Mohali\n","\tLocation: Punjab Cricket Association Stadium\n","\tCapacity: 27,000"],
        "Chennai":["Chennai\n","\tLocation: M. A. Chidambaram Stadium\n","\tCapacity: 50,000"],
        "Navi Mumbai":["Navi Mumbai\n","\tLocation: D Y Patil Sports Stadium\n","\tCapacity: 55,000"] }

list2=['Ahmedabad','Bengaluru','Mumbai','Hyderabad','Jaipur','Delhi','Mohali','Chennai','Navi Mumbai']













#DISPLAY FUNCTIONS

#fixtures():
def fixtures():
    import random    

    team1=random.choices(list)
    team2=random.choices(list)
    if team1 != team2:
        print("\tTODAY'S MATCH")
        print("Match Number: ",random.randint(0,74))
        print("{} VS {}\n".format(*team1,*team2))    
    
    ven=print("Venue: ",*venue[random.choice(list2)][0:2])
    tim=["03.30 PM","07:30 PM"]
    print("Time:  ",random.choice(tim))
    
#Team data

def teams():
    inp=input("Enter the complete name of team to view data:")
    print("YOUR TEAM:\n",*Teams[inp])
    
    
#def players

def players():
    import csv

    file = open("IPL.csv", "r")
    data = list(csv.DictReader(file, delimiter=","))
    file.close()
    print(data)
    
    





# # winner_team=
while True:
    print("Welcome to IPL 2023")
    print("1. To know today's fixtures")
    print("2. To get information about teams")
    print("3. To know about players")
    
    choice=int(input("Enter your prefered choice: "))
    
    if choice==1 :
        print(fixtures())
    
    elif choice==2:
        print(teams())
    
    elif choice==3:
        print(players())    
        
