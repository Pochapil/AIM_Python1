def find_max_substring_occurrence(input_string):
    for i in range(1, len(input_string)):
        buf = input_string[0:i]
        if input_string == buf * (len(input_string) // len(input_string[0:i])):
            return (len(input_string) // len(input_string[0:i]))
    return 1
