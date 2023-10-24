def display_main_menu():
    print("Enter some numbers seperated by commas (eg. 5, 67, 32)")


def get_user_input():
    input_text = input()
    text_list = input_text.split(",")
    # print(text_list)

    # float_list = [float(ele) for ele in text_list]
    float_list = list(map(float, text_list))
    # both of these float_list functions work in converting list of strings to list of floats

    print("User Input: " + str(float_list))
    return float_list


def calc_average(float_list):
    if not float_list:
        return None  # Return None for an empty list to avoid division by zero error

    total = sum(float_list)
    average = total / len(float_list)
    print("The average temperature is: " + str(average))
    return average


def find_min_max(float_list):
    min_value = min(float_list)
    max_value = max(float_list)

    result = [min_value, max_value]
    print("The min and max temperatures are: " + str(result))
    return result


def sort_temperature(float_list):
    float_list.sort()  # Sorts the list in-place
    print("Sorted list (ascending):", float_list)


def calc_median_temperature(float_list):
    sorted_list = sorted(float_list)
    n = len(sorted_list)

    if n % 2 == 1:
        # If the list has an odd number of elements, the median is the middle element
        median = sorted_list[n // 2]
    else:
        # If the list has an even number of elements, the median is the average of the two middle elements
        middle1 = sorted_list[n // 2 - 1]
        middle2 = sorted_list[n // 2]
        median = (middle1 + middle2) / 2
    print("The median temperature is " + str(median))
    return median


def main():
    print("ET0435 (DevOps for AIOT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_temperature(num_list)
    calc_median_temperature(num_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
