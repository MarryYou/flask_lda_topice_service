from app import db
from lda_model.src.tokenizer_news import *


if __name__ == '__main__':
    outfilename = './lda_model/data/train_words.txt'
    tmp_obj = db['train'].find({})
    lines = get_data(tmp_obj)
    out_put(lines, outfilename)


