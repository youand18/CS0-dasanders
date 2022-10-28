lines = raw_input()


for line in lines:
    printstring = ""
    if (line.startswith("simon says") or line.startswith("Simon says")):
        #should cut out "simon says"
        printstring = " " + str(line.split()[2:])   
    print(printstring)