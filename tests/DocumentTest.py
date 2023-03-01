import unittest

from gero.nlp_workbench.Document import Document

document = Document('mock_data/roses.txt')


class DocumentTest(unittest.TestCase):

    def test_number_of_characters(self):
        """
        Number of characters
        :return:
        """
        self.assertEqual(62, document.get_character_amount())

    def test_find(self):
        """
        Full text search for a substring (e.g. with Knuth-Morris-Pratt algorithm)
        :return:
        """
        location = document.find('Roses')
        self.assertEqual(0, location)

    def test_words_tokenization(self):
        """
        Split the text into words (using e.g. split() or nltk.Tokenizer)
        :return:
        """
        expected_words = [
            "Roses", "are", "red",
            "Violets", "are", "blue", ",",
            "Sugar", "is", "sweet",
            "And", "so", "are", "you", "."
        ]
        self.assertListEqual(expected_words, document.words)

    def test_number_of_words(self):
        """
        Number of words
        :return:
        """
        expected_length = 15
        self.assertEqual(expected_length, document.number_of_words())

    def test_unique_words(self):
        """
        Unique words
        :return:
        """
        expected_unique_words = {
            "Roses", "are", "red",
            "Violets", "are", "blue", ",",
            "Sugar", "is", "sweet",
            "And", "so", "are", "you", "."
        }
        self.assertSetEqual(expected_unique_words, document.get_unique_words())

    def test_number_of_unique_words(self):
        """
        Number of different words
        :return:
        """
        # "are" appears 3 times, so the total length is reduced by 2
        expected_length = 13
        self.assertEqual(expected_length, document.number_of_unique_words())

    def test_inverted_index(self):
        """
        # An inverted index that, for given word, outputs the positions of the word in the text
        :return:
        """
        expected_location_of_are = [1, 4, 12]
        self.assertEqual(expected_location_of_are, document.get_inverted_index()['are'])

    def test_character_set(self):
        """
        Character set
        :return:
        """
        expected_set = set("Roses are red Violets are blue, Sugar is sweet And so are you.")
        self.assertSetEqual(expected_set, document.get_character_set())

    def test_character_occurrences(self):
        """
        Number of occurrences for each character
        TODO: Should we only work with lower-case characters? At the moment "A" and "a" are stored separately.
        :return:
        """
        expected_occurrences_of_a = 4
        self.assertEqual(expected_occurrences_of_a, document.get_character_occurrences()['a'])


if __name__ == '__main__':
    unittest.main()
