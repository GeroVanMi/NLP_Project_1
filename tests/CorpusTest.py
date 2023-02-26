import unittest

from src.Corpus import Corpus

corpus = Corpus("./mock_data")


class CorpusTest(unittest.TestCase):
    def test_number_of_documents(self):
        expected_length = 451
        self.assertEqual(expected_length, len(corpus.documents))


if __name__ == '__main__':
    unittest.main()
