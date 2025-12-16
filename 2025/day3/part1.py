'''
max(input) to find the largest max single int
find the index it is and then find max from index + 1 to the end
if the orignial max is last index then we can index from start to index - 1 and append the new things

'''


with open("input.txt") as inp:
    lines = inp.read().splitlines()

    # lines[i] string row 
    # lines[i][j] char digit

result = 0

for row in lines:
    max_row = 0
    index = -1

    for i in range(len(row)):
        curr = int(row[i])

        if curr > max_row:
            max_row = curr
            index = i


    #make the str word right now
    word = str(max_row)

    max_row = 0


    if index == len(row) - 1:
        #do the stuff from start to index - 1
        for i in range(0, index):
            curr = int(row[i])
            if curr > max_row:
                max_row = curr

        word = str(max_row) + word
            
    else:

        # find the other digit from index + 1 to end

        for i in range(index + 1, len(row)):
            curr = int(row[i])

            if curr > max_row:
                max_row = curr

        word = word + str(max_row)


    word = int(word)
    result += word
    #print(result)


    
print(result)
