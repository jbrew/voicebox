from .corpus import Corpus


class Voicebox(object):

    def __init__(self, texts):
        self.texts = texts

    def build(self):
        corpus = Corpus('. '.join(self.texts))

        voicebox = {}

        for ngram, ngram_data in corpus.tree.iteritems():
            voicebox[ngram] = {
                u'frequency': float(ngram_data.count) / float(corpus.wordcount)
            }

            voicebox[ngram][u'after'] = ngram_data.after
            for index, after in enumerate(ngram_data.after):
                ngram_after_total = sum([ngram_after_count for _, ngram_after_count in after.iteritems()])
                for ngram_after, ngram_after_count in after.iteritems():
                    voicebox[ngram][u'after'][index][ngram_after] = float(ngram_after_count) / float(ngram_after_total)

        voicebox[u'wordcount'] = corpus.wordcount

        return voicebox
