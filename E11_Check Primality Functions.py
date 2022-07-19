def get_number():
    return int(input('please select a number: '))


def calculate_prime(selected_number):
    prime = False
    for number in range(2, selected_number):
        if selected_number % number == 0:
            prime = False
            break
        else:
            prime = True
    return prime


selected_number = get_number()
if calculate_prime(selected_number):
    print(f'{selected_number}  is a prime number')
else:
    print(f'{selected_number} is not a prime number')
print('this is a new screen')
print('new button')
