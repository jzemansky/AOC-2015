import hashlib

def part_1(string):
    num = 0
    while True:
        md5_hash = get_md5_hash(string + str(num))
        if md5_hash[:5] == '00000':
            break
        num += 1
    return num

def part_2(string):
    num = 0
    while True:
        md5_hash = get_md5_hash(string + str(num))
        if md5_hash[:6] == '000000':
            break
        num += 1
    return num

def get_md5_hash(string):
    encoded_string = string.encode('utf-8')
    md5_hash = hashlib.md5(encoded_string).hexdigest()
    return md5_hash

def main():
    secret_key = 'yzbqklnj'
    
    print(f'Part 1 num: {part_1(secret_key)}')
    print(f'Part 2 num: {part_2(secret_key)}')

main()