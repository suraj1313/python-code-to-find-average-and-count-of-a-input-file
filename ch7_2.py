fname = input('enter the file name : ')
avg = 0
count = 0
try:
    fh = open(fname)

except:
    print('code is wrong')
    quit()

for line in fh :
    if  line.startswith("X-DSPAM-Confidence: ") :
        pos = line.find(' ')
        val = line[pos:].rstrip()
        gd = float(val)
        count = count + 1
        avg = avg + gd
print('Average spam confidence: ', avg/count)
