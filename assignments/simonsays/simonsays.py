lines = ["Simon says Jump over this log"]#raw_input()


for line in lines:
    printstring = ""
    if (line.startswith("simon says") or line.startswith("Simon says")):
        #should cut out "simon says"
        printList = line.split()[2:]
        for item in printList:
            printstring = printstring + item + " "   
    print(printstring)