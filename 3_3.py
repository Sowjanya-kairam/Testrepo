score = input("Enter Score: ")
sr =float(score)
if(sr>0.0):
    if(sr<=1.0):
        if(sr<0.6):
            print("F")
        elif (sr>=0.9):
            print("A")
        elif(sr>=0.8):
            print("B")
        elif(sr>=0.7):
            print("C")
        elif(sr>=0.6):
            print("D")
    else:
        print("error score should be less than or equal 1.0")
else:
    print("error score should be greater than 0.0")
            
