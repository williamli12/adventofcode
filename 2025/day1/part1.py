import csv



curr_val = 50
counter = 0

# look into relative directory
with open("part1input.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        val = row[0]
        letter = val[0]
        number = int(val[1:])
        

        #when file was created or saved by excel, the first line
        #looks like this \efeffL49 and not L49
        #print(repr(val)) # use this line to see this
        # therefore to strip the BOM when opening the file
        # use utf-8-sig encoding which is a param above

        print(letter)
        
        print(number)




        if (letter == 'R'):
            curr_val = (curr_val + number) % 100
            
        else:
            curr_val = (curr_val - number) % 100
        
        if (curr_val == 0):
                counter += 1
print(counter)



