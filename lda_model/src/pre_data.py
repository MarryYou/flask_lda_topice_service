import jieba, re

def stopwordlist(filename):

    stopwords = [ list.strip() for list in open(filename, encoding='utf8').readlines()]
    return stopwords



def get_data( tmp_obj):
    tmp_arr = []
    for obj in tmp_obj:
       tmp_arr.append(obj['content'])

    return tmp_arr

def seg_depart(sentence, filename):
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordlist(filename)
    out_str = ''
    for word in sentence_depart:
        if word not in stopwords:
            out_str += word
            out_str += " "

    return out_str

def out_put(lines, outfilename, filename):
    out_puts = open( outfilename, 'w', encoding='utf8')
    for line in lines:
        line = re.sub(r'[^\u4e00-\u9fa5]+','',line)
        line_seg = seg_depart(line.strip(), filename)
        out_puts.write(line_seg.strip() + '\n')

    out_puts.close()
    print('分词成功')
