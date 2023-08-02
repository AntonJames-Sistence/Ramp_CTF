import hashlib

given_hash = 'b1fb3f9555820af69626dc561da4cadf'
salt = 'd958bc7dc5d2'

result = []

with open('./words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        test_hash = hashlib.md5((word + salt).encode('utf-8')).hexdigest()
        # print(test_hash)

        if test_hash == given_hash:
            result.append(word)

print(result)