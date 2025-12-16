
'''
brainstorming:
    - if the num has even number of digits, we can split it into 2 parts
    - one can have two pointers that start at 0 and then at midpoint and observe


    - if odd length, we can apply the same logic as even numbers but ignore the middle element

heuristics:
    - we dont necessarily need to parse through everything in the interval
    - we can (this is on the even number of digits problem) find all possible pattern (incrementally) of the first half, and then we can concatenate the first half with a repeat of itself onto the second half and see if that is less than the upper limit of the interval
    


    - nvm this wont work for part 2.
    ex: 1212121212 where splitting this is even but they dont match


    part2 logic:

    - we can get the length of the current curr
    - find all possibe divisors as they are our only repeat pattern lengths
    - we can calculate the next candidate for each chunk size and the winner is next invalid ID

    - concretely: take the first k digits of current number 
    - repeat them to fill length
    - if result is smaller than curr num then increment the k digits by 1 and repeat again
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
        candidates = []
        length = len(str_ver)

        # find all poss valid chunk sizes

        chunks = []

        for i in range(1, (length // 2) + 1):
            if length % i == 0:
                chunks.append(i)


        # if no chuncks exists (except 1 )
        if not chunks:
            start = 10 #why
            continue

        for i in chunks:
            base = str_ver[:i]

            repeat = length // i

            full = base * repeat
            val = int(full)

        
            # if val is smaller than curr then incrment 
            if val < start:
                next_base = str(int(base) + 1)

                val = int(next_base * repeat)

            candidates.append(val)

        best = min(candidates)
        print(best)
        if best <= end:
            count += best

            start = best + 1
        else:
            break

    


print(count)
