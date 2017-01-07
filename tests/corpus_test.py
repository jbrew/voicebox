from __future__ import absolute_import

import unittest

from voicebox.ngram import Ngram
from voicebox.corpus import Corpus

from tests import test_data


class CorpusTests(unittest.TestCase):
    @staticmethod
    def _build_ngram(token, after, count):
        ngram = Ngram(token)
        ngram.after = after
        ngram.count = count
        return ngram

    def test_get_sentences__with_unicode_string(self):
        corpus = Corpus(text=test_data.text_unicode)

        sentences = corpus.get_sentences()
        self.assertEqual(sentences, [[u'hey', u'look'], [u'i\'m', u'unicode']])

    def test_make_tree__with_small_text(self):
        corpus = Corpus(text=u'a hit is a hit',
                        sentence_start_token=u'#')

        self.assertDictEqual(
            corpus.tree,
            {
                u'a': self._build_ngram(
                    token=u'a',
                    after=[{u'hit': 2}, {u'is': 1}],
                    count=2
                ),
                u'hit': self._build_ngram(
                    token=u'hit',
                    after=[{u'is': 1}, {u'a': 1}],
                    count=2
                ),
                u'is': self._build_ngram(
                    token=u'is',
                    after=[{u'a': 1}, {u'hit': 1}],
                    count=1
                ),
                u'a hit': self._build_ngram(
                    token=u'a hit',
                    after=[{u'is': 1}, {u'a': 1}],
                    count=2
                ),
                u'hit is': self._build_ngram(
                    token=u'hit is',
                    after=[{u'a': 1}, {u'hit': 1}],
                    count=1
                ),
                u'is a': self._build_ngram(
                    token=u'is a',
                    after=[{u'hit': 1}],
                    count=1
                )
            }
        )


if __name__ == '__main__':
    unittest.main()
