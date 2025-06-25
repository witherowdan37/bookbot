def word_count(str_input):
    tmp_list = []
    tmp_list = str_input.split()
    count = len(tmp_list)

    return count

def char_count(str_input):
    str_cpy = str_input.lower()
    char_dict = {}
    tmp_list = str_cpy.split()
    sub_list = []

    for i in range(0,len(tmp_list)):
        sub_list = list(tmp_list[i])

        for k in range(0,len(sub_list)):

          if sub_list[k] not in char_dict:
              char_dict[sub_list[k]] = 1

          elif sub_list[k] in  char_dict:
              char_dict[sub_list[k]] += 1
  
    return char_dict

def sorted_list(dictionary_input):
    new_list = []
    

    for dictionary_input, chars in dictionary_input.items():
        tmp_dict = {"char": '', "num": 0}
        tmp_dict["char"] = dictionary_input
        tmp_dict["num"] = chars
        new_list.append(tmp_dict)

    new_list.sort(reverse=True, key=lambda tmp_dict: tmp_dict["num"])
    return new_list