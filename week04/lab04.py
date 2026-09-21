def find_common_elements(list1, list2):
    common = set(list1) & set(list2)
    return list(common)

def find_user_by_name(users, name):
    for user in users:
        if user['name'] == name:
            return user
    return None

def get_list_of_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers