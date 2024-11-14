def get_new_dictionary(input_dict_name, output_dict_name):
    with open(input_dict_name) as input_file:
        lines = input_file.read().splitlines()
    dict_drago_human = {}
    for i in range(1, len(lines)):
        human_word, drago_words = lines[i].split(' - ')
        drago_words = drago_words.split(', ')
        for drago_word in drago_words:
            dict_drago_human.setdefault(drago_word, []).append(human_word)

    with open(output_dict_name, 'w', encoding='utf-8') as output_file:
        n = len(dict_drago_human.keys())
        output_file.write(str(n) + '\n')
        i = 0
        sorted_dict = dict(sorted(dict_drago_human.items()))
        for drago_word, human_words in sorted_dict.items():
            i += 1
            human_words_str = ', '.join(human_words)
            if i != n:
                output_file.write('{0} - {1}'.format(drago_word, human_words_str) + '\n')
                # output_file.write(f'{drago_word} - {human_words_str}' + '\n')
            else:
                output_file.write('{0} - {1}'.format(drago_word, human_words_str))
                # output_file.write(f'{drago_word} - {human_words_str}')
