lines = ["Simon says dance."]#raw_input()


for line in lines:
    printstring = ""
    if (line.startswith("simon says") or line.startswith("Simon says")):
        #should cut out "simon says"
        printstring = line.split()[2:]   
    print(printstring)