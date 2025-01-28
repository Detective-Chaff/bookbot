
path_to_file = "books/frankenstein.txt"

def count_words(string_in):
    count = 0
    str_array = []

    str_array = string_in.split()
    count = len(str_array)

    return count

def char_count(string_in):
    new_dict = {}
    for item in string_in.lower():
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
        
    return new_dict

def sort_on(dict):
    return dict["num"]


def main():
    count = 0
    total_dict = {}
    dict_list = []
    num_key = "num"

    print(f"--- Begin report of {path_to_file} --- \n")

    with open(path_to_file) as file:
        file_contents = file.read()
        count = count_words(file_contents)
        total_dict = char_count(file_contents)
        #print(file_contents)
    print(f"{count} words were found in the document \n")

    for item in total_dict:
        char_dict = {}
        if type(item) is str and item.isalpha():
            char_dict[item] = item
            char_dict["num"] = total_dict[item]
            dict_list.append(char_dict)

    dict_list.sort(reverse=True, key=sort_on)

    for list_item in dict_list:
        for item in list_item:
            if item == "num":
                continue
            else:
                print(f"the '{item}' character was found {list_item[num_key]} times")

    print("--- End report ---")
    #print(count)
    #print(char_dict)

main()