def trace(filename, output):
    # open the results from runit
    inputfile = open(filename, "r")
    # store the traced memory results
    outputfile = open(output, "w")
    ipages = dict() #stores instruction accesses
    dpages = dict() #stores data accesses
    totali = 0
    totald = 0
    
    # get all occurances of S, M, L and I accesses
    for line in inputfile:
        if line.split(",")[1][0].upper() == "I":
            ipages[line[:-3]] = ipages.get(line[:-3], 0) + 1
            totali += 1
        elif line.split(",")[1][0].upper() == "S" or line.split(",")[1][0].upper() == "M" or \
             line.split(",")[1][0].upper() == "L":
            dpages[line[:-3]] = dpages.get(line[:-3], 0) + 1
            totald+=1
        
    outputfile.write("Instructions\n")
    # write the page table into a new file
    for key in ipages:
        outputfile.write(str(key) + ", " + str(ipages[key]) + "\n")
    outputfile.write("Data\n")
    for key in dpages:
        outputfile.write(str(key) + ", " + str(dpages[key]) + "\n")        
    outputfile.write("Total Instructions:" + str(totali) + "\nTotal Data:" + str(totald) + "\n")
    # close both files
    inputfile.close()
    outputfile.close()


if __name__ == "__main__":
    trace ("tr-heaploop.ref", "output_table.txt")
    trace ("tr-matmul.ref", "output_table_m.txt")
