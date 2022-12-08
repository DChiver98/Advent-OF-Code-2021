file = open("Day 1\input.txt", "r").read().splitlines()

def part1():
    
    count = 0

    for measurement in range(len(file) - 1):
        test = file[measurement : measurement + 2]
        if int(test[1]) > int(test[0]): 
            count += 1

    print(f"Part 1 answer : {count}")

def part2():

    count = 0

    for measurement in range(len(file) - 2):
        firstMeasurement = [int(x) for x in file[measurement : measurement + 3]]
        secondMeasurement = [int(x) for x in file[measurement + 1 : measurement + 4]]
        if sum(secondMeasurement) > sum(firstMeasurement): 
            count += 1 

    print(f"Part 2 answer : {count}")

part1(), part2()