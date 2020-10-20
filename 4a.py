import hashlib
import itertools


# Intercept 6 characters of sha1
def MY24SHA(str_init):
    str_result = hashlib.sha1(str_init.encode('utf-8')).hexdigest()[0:6]
    return str_result


letter_array = [chr(letter).lower() for letter in range(65, 91)]  # Generate a-z character array
num_array = [str(num) for num in range(1, 10)]  # Generate 1-9 character array
character_array = letter_array + num_array  # Combine two character arrays
character_string = ''.join(character_array)  # Combine the character array into a string, ie ‘abcdefghijklmnopqrstuvwxyz123456789’

print(character_string)

character_list = []  # Array for storing character combinations
hash_dict = {}  # A dictionary that stores characters and their hash values


def find_collision_24():
    for i in range(1, 5):
        character_list = ["".join(x) for x in
                          itertools.product(character_string, repeat=i)]  # Use python itertools to generate all character combinations in the function length i
        for index, v in enumerate(character_list):  # Traverse character combinations to compare whether the hash value is the same as the existing hash value
            for k in hash_dict.keys():  # Traverse the hash dictionary
                if hash_dict[k] == MY24SHA(v):  # If the same, find the result
                    print(k, v)
                    return k, v
            hash_dict[v] = MY24SHA(v)  # If not found, add the character and its hash value to the hash dictionary
            print("Not Found")
    print(hash_dict.keys())


find_collision_24()
