'''
Написати функцію, яка буде повертати унікальний ідентифікатор
'''

# id = 0

# def generate_unique_id():
#     global id
#     id += 1
#     return id

# for i in range(5):
#     print(generate_unique_id())

def generate_unique_id():
    id = 0
    def calculate_next_id():
        nonlocal id
        id += 1
        return id
    return calculate_next_id

numbers_generator = generate_unique_id()
print(numbers_generator())
print(numbers_generator())
print(numbers_generator())
print(numbers_generator())

number_generator_two = generate_unique_id()
print(number_generator_two())
print(number_generator_two())
print(number_generator_two())
print(number_generator_two())

