import unittest

from gero.nlp_workbench.Corpus import Corpus

corpus = Corpus("./mock_data")


class CorpusTest(unittest.TestCase):
    def test_number_of_documents(self):
        expected_length = 451
        self.assertEqual(expected_length, len(corpus.documents))

    def test_corpus_inverted_index(self):
        index = corpus.generate_inverted_index()
        self.assertIn('Roses', index)


if __name__ == '__main__':
    unittest.main()
