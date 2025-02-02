def part1(content):
    count = 0
    for i in content:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    return count

def part2(content):
    count = 0
    position = 0

    for i in content:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        position += 1
        
        if count == -1:
            return position

def main():
    content = ''
    with open('1.txt', 'r') as file:
        content = file.read()
    print(f'Part 1: {part1(content)}')
    print(f'Part 2: {part2(content)}')
main()