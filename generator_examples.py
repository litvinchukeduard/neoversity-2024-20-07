'''
Написати функцію-генератор, яка буде генерувати унікальне значення
'''

def generate_unique_id():
    id = 1
    while True:
        yield id
        id += 1
        if id > 3:
            break

generator = generate_unique_id()

next_user_id = next(generator)

# print(next_user_id)
# user_dict = {'id': next_user_id, 'name': 'John'}
# print(user_dict)

# ...
# ...

# next_user_id = next(generator)

# print(next_user_id)
# user_dict = {'id': next_user_id, 'name': 'John'}
# print(user_dict)
# try:
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))
#     print(next(generator))  # Ctrl C
# except StopIteration:
#     print("Iteration stopped")
# for i in generator:
#     print(i)

for i in range(1, 3):
    print(i)


