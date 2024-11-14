def get_new_dictionary(input_dict_name, output_dict_name):
    with open(input_dict_name) as input_file:
        lines = input_file.read().splitlines()
    dict_drago_human = {}
    for i in range(1, len(lines)):
        human_word, drago_words = lines[i].split(' - ')
        drago_words = drago_words.split(', ')
        for drago_word in drago_words:
            dict_drago_human.setdefault(drago_word, []).append(human_word)

    with open(output_dict_name, 'w') as output_file:
        n = len(dict_drago_human.keys())
        output_file.write(str(n) + '\n')
        i = 0
        array_keys = list(dict_drago_human.keys())
        array_keys.sort()
        for key in array_keys:
            drago_word = key
            human_words = dict_drago_human[key]
            i += 1
            human_words_str = ', '.join(sorted(human_words))
            if i != n:
                buf = '{0} - {1}'.format(drago_word, human_words_str) + '\n'
                output_file.write(buf)
            else:
                buf = '{0} - {1}'.format(drago_word, human_words_str)
                output_file.write(buf)
