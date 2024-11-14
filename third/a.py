import random
import itertools
import copy


class BatchGenerator:

    def __init__(self, list_of_sequences, batch_size, shuffle=False):
        """
        :param list_of_sequences: Список списков или numpy.array одинаковой длины
        :param batch_size: Размер батчей, на которые нужно разбить входные последовательности.
            Батчи последнего элемента генератора могут быть короче чем batch_size
        :param shuffle: Флаг, позволяющий перемешивать порядок элементов в последовательностях
        """

        list_of_sequences_copy = copy.deepcopy(list_of_sequences)
        # list_of_sequences_copy = list_of_sequences
        if shuffle:

            orderlist = list(range(len(list_of_sequences_copy[0])))
            random.shuffle(orderlist)
            for i, arr in enumerate(list_of_sequences_copy):
                list_of_sequences_copy[i] = [list_of_sequences_copy[i][j] for j in orderlist]

                # random.shuffle(arr)

        # def generator_function(list_of_sequences_copy):
        #     for i in range(len(list_of_sequences_copy[0]) // batch_size + 1 if len(
        #             list_of_sequences_copy[0]) % batch_size != 0 else 0):
        #         yield list_of_sequences_copy[0][i * batch_size:(i + 1) * batch_size]

        def generator_function(list_of_sequences_copy):
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

        self.generator = generator_function(list_of_sequences_copy)

    def __next__(self):
        return self.generator.__next__()
        # return self.generator

    def __iter__(self):
        # return self.generator
        return self


bg = BatchGenerator(
    list_of_sequences=[
        [1, 2, 3, 5, 1, 'a', 3],
        [0, 0, 1, 1, 0, 1, 4]
    ], batch_size=2, shuffle=True
)

list_of_sequences = [
    [1, 2, 3, 5, 1, 'a'],
    [0, 0, 1, 1, 0, 1]
]
batch_size = 2
# print(list_of_sequences[0][0 * batch_size:(0 + 1) * batch_size])

for elem in bg:
    print(elem)

# [item for row in matrix for item in row]

# def flatten_extend(matrix):
#     flat_list = []
#     for row in matrix:
#         flat_list.extend(row)
#     return flat_list
