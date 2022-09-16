class StringOperations:

    def is_palindrome(self, text):
        for i in range(0, int(len(text)/2)):
            if text[i] != text[(len(text)-1) - i]:
                return False
        return True

    def concatenate_array(self, string_array):
        string_to_return = ""
        for string in string_array:
            string_to_return += string+" "
        return string_to_return

    def delete_all_consonants(self, text):
        string_to_return = ""
        for letter in text:
            if letter in "aeiouAEIOU":
                string_to_return += letter
        return string_to_return

    def delete_all_vowes(self, text):
        string_to_return = ""
        for letter in text:
            if letter not in "aeiouAEIOU":
                string_to_return += letter
        return string_to_return

    def check_if_word_is_forbidden(self, word, ban_list, substitute_word):
        return word in ban_list

    def substitute_letters(self, word, ban_list, substitute_letter):
        for letter in word:
            if letter in ban_list:
                word.replace(letter, substitute_letter)

class NumbersOperations:

    def check_if_number_between(self, left, right, number):
        return left < number < right

    def check_if_dividable(self, divident, divisor):
        return divident % divisor == 0

