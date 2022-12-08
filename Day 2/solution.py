file = open("Day 2/input.txt", "r").read().splitlines()

def part1():

    horizonalPosition = 0
    depth = 0
    total = 0

    for line in file:

        if "forward" in line:
            num = int(line.removeprefix("forward "))
            horizonalPosition += num
        elif "up" in line:
            num = int(line.removeprefix("up "))
            depth -= num
        elif "down" in line:
            num = int(line.removeprefix("down "))
            depth += num

    total = horizonalPosition * depth

    print(f"Part 1 answer : {total}")

def part2():

    aim = 0
    horizonalPosition = 0
    depth = 0
    total = 0

    for line in file:

        if "forward" in line:
            num = int(line.removeprefix("forward "))
            horizonalPosition += num
            depth += (aim * num)
        elif "up" in line:
            num = int(line.removeprefix("up "))
            aim -= num
        elif "down" in line:
            num = int(line.removeprefix("down "))
            aim += num

    total = horizonalPosition * depth

    print(f"Part 2 answer : {total}")

part1(), part2()