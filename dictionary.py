alphabet = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'

# Remove spaces and split the string into individual letters
letters = alphabet.replace(" ", "").split(',')

# Create the dictionary using dictionary comprehension
alphabet_dict = {letter: index + 1 for index, letter in enumerate(letters)}

print(alphabet_dict)