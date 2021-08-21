from inspect import getouterframes, currentframe


def get_recursion(list_to_search):
    my_dict = {}

    def recursive_count(list_to_search):
        f_level = (len(getouterframes(currentframe()))) - 3
        for element in list_to_search:
            if isinstance(element, int):
                if f_level in my_dict:
                    my_dict[f_level] = my_dict.get(f_level, 0) + element
                else:
                    my_dict.update({f_level: element})
            else:
                recursive_count(element)

    recursive_count(list_to_search)
    return my_dict


print(get_recursion([[1,2,3, [1,2,3, [2,[2, 5, 6, [[1,2,3, [1,2,3, [2,[2,[[1,2,3, [1,2,3, [2,[2, 5, 6, [[1,2,3, [1,2,3, [2,[2, 5, 6],2,3]]], [2,3,8], [2,36,6,[2,36,6]], [2,36,6]]],2,3]]], [2,3,8], [2,36,6,[2,36,6]], [2,36,6]], 5, 6],2,3]]], [2,3,8], [2,36,6,[2,36,6]], [2,36,6]]],2,3]]], [2,3,8], [2,36,6,[2,36,6]], [2,36,6]]))
