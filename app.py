class StringOperations:

    @staticmethod
    def check_if_sequence_is_palindrome(text) -> bool:
        for i in range(0, int(len(text)/2)):
            if text[i] != text[(len(text)-1) - i]:
                return False
        return True

    @staticmethod
    def concatenate_array(string_array: list[str]) -> str:
        string_to_return = ""
        for string in string_array:
            string_to_return += string + " "
        return string_to_return

    @staticmethod
    def delete_all_consonants(text: str) -> str:
        string_to_return = ""
        for letter in text:
            if letter in "aeiouAEIOU":
                string_to_return += letter
        return string_to_return

    @staticmethod
    def delete_all_vowes(text: str) -> str:
        string_to_return = ""
        for letter in text:
            if letter not in "aeiouAEIOU":
                string_to_return += letter
        return string_to_return

    @staticmethod
    def check_if_word_is_forbidden(word: str, ban_list: list[str]) -> bool:
        return word in ban_list

    @staticmethod
    def substitute_letters(word, ban_list, substitute_letter):
        for letter in word:
            if letter in ban_list:
                word.replace(letter, substitute_letter)


class NumbersOperations:

    @staticmethod
    def check_if_number_is_between(left: int, right: int, number: int) -> bool:
        return left < number < right

    @staticmethod
    def check_if_number_is_dividable(divident: float, divisor: float) -> bool:
        return divident % divisor == 0

