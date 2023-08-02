import hashlib

given_hash = '50425c8f663d3453ba3eaabb569baf42'
salt = 'f589082d0f14'

result = []

with open('./words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        test_hash = hashlib.md5((word + salt).encode('utf-8')).hexdigest()
        # print(test_hash)

        if test_hash == given_hash:
            result.append(word)

print(result)