import hashlib



# The tortoise and the rabbit actually represent two 15-digit strings, and the value space of the characters coincides with the first 15 digits of sha1.
# In other words, 15 characters correspond to a 15-bit hash value. Unless there is a one-to-one correspondence, there must be two characters corresponding to the same hash value, that is, there is a ring, which is the core of the algorithm


# The MY60SHA function
def MY60SHA(str_init):
    str_result = hashlib.sha1(str_init.encode('utf-8')).hexdigest()[0:15]
    return str_result


# Set the starting point of the tortoise and the hare race as'abcdef123456789', a for the tortoise and b for the hare
a = 'abcdef123456789'
b = 'abcdef123456789'

# Let the tortoise and the hare start to run until they meet
while True:
    a = MY60SHA(a)  # Each time the turtle runs one step, it uses MY60SHA() to hash once
    b = MY60SHA(MY60SHA(b))  # Each time the hace runs two steps, it uses MY60SHA() to hash twice
    if a == b:  # a and b are equal, which means they meet and break out of the loop
        break
    else:
        print('Still Run1')

# After meeting, let the tortoise return to the starting point, the rabbit at the meeting point, at the same speed, let them meet, and the meeting point is where the ring starts.
a = 'abcdef123456789'  # Turtle back to the beginning

# Respectively represent the previous step of a and the previous step of b
a_previous = a
b_previous = b

# Run until you meet, and the meeting point is where the ring begins. The beginning of the ring is the hash value of the two strings. Take their previous step respectively, which is the result
while True:
    a_previous = a  # Record the previous position of the turtle
    b_previous = b  # Record the position of the rabbit's previous step
    a = MY60SHA(a)  # Tortoise runs a step
    b = MY60SHA(b)  # Hace are also run a step
    if a == b:  # Equality means meeting, out of the loop
        break
    else:
        print("Still Run2")

print('result:', a_previous, b_previous)
