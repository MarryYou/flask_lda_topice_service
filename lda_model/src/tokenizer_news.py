from gensim import corpora, models




fr = open('../data/train_words.txt', 'r', encoding='utf8')

train = []

for line in fr.readlines():
    line = [word.strip() for word in line.split(' ')]
    train.append(line)

dictionary = corpora.Dictionary(train)

corpus = [dictionary.doc2bow(text) for text in train]

lda = models.LdaModel(corpus=corpus, id2word=dictionary, iterations=400, num_topics=10)
topic_list = lda.print_topics(10)
print("10个主题的单词分布为：\n")
for topic in topic_list:
    print(topic)