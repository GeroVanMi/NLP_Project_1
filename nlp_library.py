from src.gero.nlp_workbench.Corpus import Corpus


def main():
    corpus = Corpus('tests/mock_data/')
    print(corpus)
    corpus.generate_word_cloud()


if __name__ == '__main__':
    main()
