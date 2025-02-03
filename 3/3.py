def robo_directions(content):
    santa_horizontal = 0
    santa_vertical = 0
    robo_horizontal = 0
    robo_vertical = 0
    directions = [[0, 0]]
    for i in range(0, len(content)):
        if i % 2 == 0:
            if content[i] == '>':
                robo_horizontal += 1
            elif content[i] == '<':
                robo_horizontal -= 1
            elif content[i] == '^':
                robo_vertical += 1
            elif content[i] == 'v':
                robo_vertical -= 1
            if not [robo_horizontal, robo_vertical] in directions:
                directions.append([robo_horizontal, robo_vertical])
        else: 
            if content[i] == '>':
                santa_horizontal += 1
            elif content[i] == '<':
                santa_horizontal -= 1
            elif content[i] == '^':
                santa_vertical += 1
            elif content[i] == 'v':
                santa_vertical -= 1
            if not [santa_horizontal, santa_vertical] in directions:
                directions.append([santa_horizontal, santa_vertical])
    return len(directions)

def main_directions(content):
    horizontal = 0
    vertical = 0
    directions = [[0, 0]]
    for i in content:
        if i == '>':
            horizontal += 1
        elif i == '<':
            horizontal -= 1
        elif i == '^':
            vertical += 1
        elif i == 'v':
            vertical -= 1
        if not [horizontal, vertical] in directions:
            directions.append([horizontal, vertical])
    return len(directions)

def main():
    with open('3.txt') as file:
        content = file.read()
        directions = main_directions(content)
        print(f'There were {directions} houses visited by Santa') 
        directions =  robo_directions(content)
        print(f'There were {directions} houses visited by Santa and Robo-Santa')  

main()