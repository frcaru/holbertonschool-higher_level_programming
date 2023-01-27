#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    result = 0
    list_result = []
    for a in range(list_length):
        try:
            result = my_list_1[a] / my_list_2[a]
            list_result.append(result)

        except (TypeError, AttributeError):
            print("wrong type")
            list_result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            list_result.append(0)
        except IndexError:
            print("out of range")
            list_result.append(0)

        finally:
            pass
    return list_result
