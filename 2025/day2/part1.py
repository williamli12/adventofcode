'''
brainstorming:
    - if the num has even number of digits, we can split it into 2 parts
    - one can have two pointers that start at 0 and then at midpoint and observe
    - if odd length, it is not possible to have the same 2 repeating digits so we skip

heuristics:
    - we dont necessarily need to parse through everything in the interval
    - we can (this is on the even number of digits problem) find all possible pattern (incrementally) of the first half, and then we can concatenate the first half with a repeat of itself onto the second half and see if that is less than the upper limit of the interval
    - for odd numbers, we can skip all the odd numbers by going to raise 10 to the length of the odd number 
    - ex: anything in the 100-999, the next even length number is 1000 which is 10^3 aka the length of 100-999
'''





with open("input.txt") as inp:
    line = inp.read().strip()

intervals = line.split(",")

count = 0

for interval in intervals:
    start, end = interval.split("-")

    start = int(start)
    end = int(end)
    #print(start)
    #print(end)
    
    #now do a loop that parses through and we will manipulate the pointer
    while start <= end:

        #check the length by turning it back to a str
        str_ver = str(start)
        if (len(str_ver) % 2 == 1):
            # odd

            start = 10 ** (len(str_ver))
            continue
        
        # even so we split
        str_ver = str_ver[:(len(str_ver) // 2)]

        str_pattern = str_ver + str_ver


        if len(str_pattern) == 0:
            str_int = 0
        else:
            str_int = int(str_pattern)
        
        #print(str_int)

        if str_int < start:
            str_ver = int(str_ver)
            str_ver += 1
            str_ver = str(str_ver) + str(str_ver)
            str_int = int(str_ver)

        
        if str_int <= end:
            count += str_int
            start = str_int + 1

         #   print(count)

        else:
            break


        '''
        problem i just thought about:
        - if we just let the loop continue here, then it would double count
        - ex: 11 is obviously a pattern but using out logic, 12 would count it also by doing 11 again. so we have to adjust our lower bound and check against it as well
        
        - another optimization: we dont even need to parse through every number, we just need to increase the pointer by the rightmost value of the first half
        '''
print(count)


