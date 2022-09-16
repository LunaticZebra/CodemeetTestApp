from app import StringOperations, NumbersOperations

string_operations = StringOperations()
numbers_operations = NumbersOperations()

def test_is_palindrome_string_correct():
    my_string = "abccba"
    assert string_operations.is_palindrome(my_string), print("String is not a palindrome")

def test_is_palindrome_string_incorrect():
    my_string = "Maciej"
    assert not string_operations.is_palindrome(my_string), print("String should not be a palindrome")

def test_palindrome_string_empty():
    my_string = ""
    assert string_operations.is_palindrome(my_string)

def test_palindrome_array_of_numbers_correct():
    my_array = [1, 2, 3, 3, 2, 1]
    assert string_operations.is_palindrome(my_array)

def test_palindrome_array_of_numbers_incorrect():
    my_array = [1, 2, 4, 3, 2, 1]
    assert not string_operations.is_palindrome(my_array)

def test_is_number_between_correct():
    number = 100
    left = 10
    right = 200
    assert numbers_operations.check_if_number_between(left, right, number)

def test_is_number_between_check_right_boundary():
    number = 200
    left = 10
    right = 200
    assert not numbers_operations.check_if_number_between(left, right, number)

def test_is_number_between_check_left_boundary():
    number = 10
    left = 10
    right = 200
    assert not numbers_operations.check_if_number_between(left, right, number)

def test_is_number_between_incorrect():
    number = 100
    left = 10
    right = 20
    assert not numbers_operations.check_if_number_between(left, right, number)

def test_is_number_between_type_error():
    number = '10'
    left = 10
    right = 20
    try:
        assert numbers_operations.check_if_number_between(left, right, number)
    except TypeError:
        assert True

def test_is_number_divisable():
    divident = 10
    divisor = 5 #check for zero
    assert numbers_operations.check_if_dividable(divident, divisor)

