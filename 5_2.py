largest = None
smallest = None
#n=0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fv = float(num)
    except:
        print('Invalid input')
        continue
    #n=n+1
    if largest is None:
        largest = float(num)
    elif float(num)>largest:
        largest = float(num)
    if smallest is None:
        smallest = float(num)
    elif float(num)<smallest:
        smallest =float(num)
    #print (n,largest, smallest)
print("Maximum is", int(largest))
print("Minimum is", int(smallest))