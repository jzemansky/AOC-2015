def square_footage(string):
    num = string.rstrip().split('x')
    lw = int(num[0]) * int(num[1])
    hw = int(num[1]) * int(num[2])
    hl = int(num[2]) * int(num[0])
    
    smallest = min(lw, hw, hl)

    return 2*lw + 2*hw + 2*hl + smallest

def ribbon(string):
    total_ribbon = 0
    list = string.rstrip().split('x')
    num = [int(x) for x in list]
    num.sort()
    total_ribbon += num[0] * 2 + num[1] * 2
    total_ribbon += num[0] * num[1] * num[2]
    
    return total_ribbon
    

def main():
    sf_count = 0
    ribbon_count = 0
    with open('2.txt') as file:
        for line in file:
            sf_count += square_footage(line)
            ribbon_count += ribbon(line)
    print(f'Total square footage: {sf_count}')
    print(f'Total ribbon: {ribbon_count}')
main()