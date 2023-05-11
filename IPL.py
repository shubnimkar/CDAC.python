class Teams():
    def tm():
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
    def disp1():
        tm=("enter the name of team:")
        print("Team: ",Teams(tm))
# players(
#     attributes--> 
#     IV:name,baseprice,actual price,role,nationality,dob,misc-stats
#     Behaviors--> getters/setter/add
# )
# venues(
#     attributes-->
#     IV:name,location(city:,state:,country),capacity
#     Behaviors--> getters/setter/add
# )
# fixture(
# attributes-->
# IV: team1,team2,venue,time,winner team
# Behaviors--> getters/setter/add/outcome
# )
# ########################################################################################################################################################
# import random
# print("WELCOME TO IPL 2023")


# class Teams():
# Teams={"Chennai Super Kings":[" Name=Chennai Super Kings\n","Owner=N. Srinivasan\n","Captain=M.S Dhoni\n","Sponsers=Vison 11\n","Support_staff=",["Coach:""Stephen Fleming"]],
# "Mumbai Indians":[" Name=Mumbai Indians\n","owner=Mukesh Ambani\n","captain=Rohit Sharma\n","sponsers=Reliance Group\n","support_staff=Coach:""Mark Boucher"]
# ,"Kolkata Knight Riders":[" Name=Kolkata Knight Riders\n","Owner=Shahrukh Khan\n","Captain=Nitish Rana\n","Sponsers=TV9 Network\n","Support_staff=Coach:Chandrakant Pandit"]
# ,"Sun Risers Hyderabad":[ "Name=Sun Risers Hyderabad\n","Owner=Sun Group\n","Captain=Aiden Markram\n","Sponsers=FanCraze\n","Support_staff=Coach:Brian Lara"]
# ,"Punjab Kings":[" Name=Punjab Kings\n","Owner=Preity Zinta\n","Captain=Shikhar Dhawan\n","Sponsers=EbixCash\n","Support_staff=Coach:Trevor Bayliss"]
# ,"Lucknnow Super Giants":[" Name=Lucknnow Super Giants\n","Owner=RPSG Group\n","Captain=KL Rahul\n","Sponsers=My11Circle\n","Support_staff=Coach:Andy Flower"]
# ,"Delhi Capitals":[" Name=Delhi Capitals\n","Owner=JSW Group\n","Captain=David Warner\n","Sponsers=Viacom18\n","Support_staff=Coach:Ricky Ponting"]
# ,"Rajasthan Royals":[" Name=Rajasthan Royals\n","Owner=Manoj Badale\n","Captain=Sanju Samson\n","Sponsers=Luminous Power Technologies\n","Support_staff=Coach:Kumar Sangakkara"]
# ,"Royal Challengers Bangalore":[ "Name=Royal Challengers Bangalore\n","Owner=United Spirits\n","Captain=Faf du Plessis\n","Sponsers=Qatar Airways\n","Support_staff=Coach:Sanjay Bangar"]
# ,"Gujarat Titans":[" Name=Gujarat Titans\n","Owner=CVC Capital Partners\n","Captain=Hardik Pandya\n","Sponsers=Capri Global\n","Support_staff=Coach:Ashish Nehra"]}
# list=["Chennai Super Kings","Kolkata Knight Riders","Mumbai Indians","Sun Risers Hyderabad","Punjab Kings","Lucknnow Super Giants","Delhi Capitals","Rajasthan Royals","Royal Challengers Bangalore","Gujarat Titans"]
# print(*Teams[random.choice(list)])








# class  players():
#    name=
#    base_price=
#    actual_price=
#    role=
#    nationality=
#    DOB=
#    misc_stats=


# class venues():
#     def __init__(self):
#         venue={"Ahmedabad":["Ahmedabad","Narendra Modi Stadium",132,000],
#            "Bengaluru":["Bengaluru","M. Chinnaswamy Stadium",40,000],
#             "Mumbai":["Mumbai","Wankhede Stadium",33,108],
#            "Hyderabad":["Hyderabad","Rajiv Gandhi International Cricket Stadium",55,000],
#            "Jaipur":["Jaipur","Sawai Mansingh Stadium",30,000],
#            "Delhi":["Delhi","Arun Jaitley Stadium",41,842],
#            "Mohali":["Mohali","Punjab Cricket Association Stadium",27,000],
#            "Chennai":["Chennai","M. A. Chidambaram Stadium",50,000],
#            "Navi Mumbai":["Navi Mumbai","D Y Patil Sports Stadium",55,000],
#            "Chennai":["Chennai","M. A. Chidambaram Stadium",50,000]
#                    }

#     list=['Ahmedabad','Bengaluru','Mumbai','Hyderabad','Jaipur','Delhi','Mohali','Chennai','Navi Mumbai']
#     print(venue[input(random.choice(list))])

# class fixtures():
#     match no=
#     team1=
#     team2=
#     venue=
#     time=
#     winner_team=

def main():
    IPL=Teams()
    print(IPL)

tm1=("Enter")
main()









