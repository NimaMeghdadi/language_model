def remove_new_line():
    x_train = open("./train.txt", "r", encoding="utf8")
    corpus = x_train.read().lower()
    corpus = corpus.replace('\n', '')
    # corpus.replace('\n', " ")
    print(type(corpus))
    with open('./o.txt', 'w', encoding="utf8") as f:
        f.write(corpus)
        f.close()


def split(x_train):
    corpus = x_train.read().lower().split('.')
    print(len(corpus))
    print(type(corpus))
    print(corpus[:2])


def abc():
    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_seqs = token_list[:i+1]
            input_sequences.append(n_gram_seqs)
    print(len(input_sequences))
    print(input_sequences[:10])


if __name__ == '__main__':
    x_train = open("./train.txt", "r", encoding="utf8")
    split(x_train)
