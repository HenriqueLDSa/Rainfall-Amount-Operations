rainfall_values_dict = {}


def rainfall_amounts():
    for i in range(20):
        values = float(input('Enter rainfall amount: '))
        if values >= 0:
            rainfall_values_dict[i] = float(values)

        else:
            print('Invalid input! Please try again.')
            rainfall_amounts()
            break


def total_rainfall():
    values = rainfall_values_dict.values()
    total = float(sum(values))
    return total


def average_rainfall():
    result = float(total_rainfall() / len(rainfall_values_dict))
    return result


def largest_smallest():
    largest_value = float(max(rainfall_values_dict.values()))
    smallest_value = float(min(rainfall_values_dict.values()))
    return largest_value, smallest_value


rainfall_amounts()
peak_values = list(largest_smallest())

print('The total rainfall for the 20 days is {:.2f}.'.format(total_rainfall()))
print('The average rainfall for the 20 days is {:.2f}.'.format(average_rainfall()))
print('The largest rainfall amount is {}, and the smallest is {}.'.format(peak_values[0], peak_values[1]))
