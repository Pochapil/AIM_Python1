import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

args = (1.2, 3, 5.9)
for arg in args:
    arg = round(arg)
print(args)

batch_size = 2


def generator_function(list_of_sequences_copy, batch_size):
    for i in range(len(list_of_sequences_copy[0]) // batch_size):
        res = []
        for j in range(len(list_of_sequences_copy)):
            res.append(list_of_sequences_copy[j][i * batch_size:(i + 1) * batch_size])
        yield res
    if (i + 1) * batch_size < len(list_of_sequences_copy[0]):
        res = []
        for j in range(len(list_of_sequences_copy)):
            res.append(list_of_sequences_copy[j][(i + 1) * batch_size:])
        yield res


list_of_sequences = [
    [1, 2, 3, 5, 1, 'a'],
    [0, 0, 1, 1, 0, 1]
]


def generator_function1():
    for i in range(10):
        yield i


c = generator_function1()
# print(next(c))

# print(list_of_sequences[:, 2:4])

b = generator_function(list_of_sequences, 2)
# print(next(b))
# print(list(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
