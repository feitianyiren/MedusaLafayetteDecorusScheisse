import sys

fr = open(sys.argv[1], "r")
fw = open(sys.argv[2], "w")

pline = ""
fw.write(fr.readline())        # pop out first line (Id,Prediction)
for line in fr:
    data = line.strip(" \n").split(",")
    instance = data[0].rsplit("_", 1)
    s_id = instance[0]
    index = int(instance[1])
    phone = data[1]
    if index == 1:
        ppphone = phone
        fw.write(pline)     # Before new sentence starts, write previous sentence's last line
        fw.write(line)      # Write new sentence's first line
    elif index == 2:
        pphone = phone
    else:
        if pphone != ppphone and phone != pphone:
            pphone = ppphone
        fw.write(s_id + "_" + str(index - 1) + "," + pphone + "\n")
        ppphone = pphone
        pphone = phone
    pline = line
fw.write(pline)         # Write the last sentence's last line
