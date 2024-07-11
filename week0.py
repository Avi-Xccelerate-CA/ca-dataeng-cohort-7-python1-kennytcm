# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    pro =['HP','Attack','Defense','Special Attack','special Defense','Speed']
    b = []
    sum = 0
    max = 0
    for i in range(len(pro)):
        sum += needs[i]
        max = needs[i]
        if sum >= 500:
            return('No medicine given')
        if max >= 250:
            return('No medicine given')
        if int(needs[i]) == 0:
            c = 0,0
            b.append(c)
        elif int(needs[i])%10 == 0:
            c = int(needs[i]/10),0
            b.append(c)
        else:
            c = int(needs[i]/10)+1,10-int(needs[i])%10
            b.append(c)
    return(b)

    #YOUR SOLUTION ENDS HERE