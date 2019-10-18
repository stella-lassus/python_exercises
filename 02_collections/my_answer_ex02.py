name=["Bill","Anne","Angy","Cony","Daniel","Occhan"]
for i in range(0,5):
    if(name[i]!="Angy"):
        print("{}.{} is my classmate".format(i+1,name[i]))
    else:
        print("{}.My name is {}".format(i+1,name[i]))
