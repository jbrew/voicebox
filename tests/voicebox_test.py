from __future__ import absolute_import

import unittest

from voicebox.voicebox import Voicebox


class VoiceboxTest(unittest.TestCase):
    def test_build_voicebox_multiple_texts(self):
        voicebox = Voicebox(texts=[
            u'a penny saved is a penny earned',
            u'a penny for your thoughts'
        ])

        self.maxDiff = None
        self.assertDictEqual(
            voicebox.build(),
            {
                u'wordcount': 12,
                u'a': {
                    u'after': [{u'penny': 1.0}, {u'earned': 1.0 / 3.0, u'saved': 1.0 / 3.0, u'for': 1.0 / 3.0}],
                    u'frequency': 3.0 / 12.0
                },
                u'a penny': {
                    u'after': [
                        {u'earned': 1.0 / 3.0, u'saved': 1.0 / 3.0, u'for': 1.0 / 3.0},
                        {u'is': 0.5, u'your': 0.5}
                    ],
                    u'frequency': 3.0 / 12.0
                },
                u'earned': {
                    u'after': [],
                    u'frequency': 1.0 / 12.0
                },
                u'is': {
                    u'after': [{u'a': 1.0}, {u'penny': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'is a': {
                    u'after': [{u'penny': 1.0}, {u'earned': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'penny': {
                    u'after': [{u'for': 1.0 / 3.0, u'earned': 1.0 / 3.0, u'saved': 1.0 / 3.0},
                               {u'is': 0.5, u'your': 0.5}],
                    u'frequency': 3.0 / 12.0
                },
                u'penny earned': {
                    u'after': [],
                    u'frequency': 1.0 / 12.0
                },
                u'penny saved': {
                    u'after': [{u'is': 1.0}, {u'a': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'saved': {
                    u'after': [{u'is': 1.0}, {u'a': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'saved is': {
                    u'after': [{u'a': 1.0}, {u'penny': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'for': {
                    u'after': [{u'your': 1.0}, {u'thoughts': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'your': {
                    u'after': [{u'thoughts': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'thoughts': {
                    u'after': [],
                    u'frequency': 1.0 / 12.0
                },
                u'penny for': {
                    u'after': [{u'your': 1.0}, {u'thoughts': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'for your': {
                    u'after': [{u'thoughts': 1.0}],
                    u'frequency': 1.0 / 12.0
                },
                u'your thoughts': {
                    u'after': [],
                    u'frequency': 1.0 / 12.0
                }
            }
        )

    # TODO: Should a two-gram frequency be based off of number of two-grams?
    # TODO: (i.e. 6 two-grams for 7 words) word_count - (n - 1) for n-gram
    def test_make_voicebox(self):
        voicebox = Voicebox(texts=[u'a penny saved is a penny earned'])

        self.assertDictEqual(
            voicebox.build(),
            {
                u'wordcount': 7,
                u'a': {
                    u'after': [{u'penny': 1.0}, {u'earned': 0.5, u'saved': 0.5}],
                    u'frequency': 2.0 / 7.0
                },
                u'a penny': {
                    u'after': [{u'earned': 0.5, u'saved': 0.5}, {u'is': 1.0}],
                    u'frequency': 2.0 / 7.0
                },
                u'earned': {
                    u'after': [],
                    u'frequency': 1.0 / 7.0
                },
                u'is': {
                    u'after': [{u'a': 1.0}, {u'penny': 1.0}],
                    u'frequency': 1.0 / 7.0
                },
                u'is a': {
                    u'after': [{u'penny': 1.0}, {u'earned': 1.0}],
                    u'frequency': 1.0 / 7.0
                },
                u'penny': {
                    u'after': [{u'earned': 0.5, u'saved': 0.5}, {u'is': 1.0}],
                    u'frequency': 2.0 / 7.0
                },
                u'penny earned': {
                    u'after': [],
                    u'frequency': 1.0 / 7.0
                },
                u'penny saved': {
                    u'after': [{u'is': 1.0}, {u'a': 1.0}],
                    u'frequency': 1.0 / 7.0
                },
                u'saved': {
                    u'after': [{u'is': 1.0}, {u'a': 1.0}],
                    u'frequency': 1.0 / 7.0
                },
                u'saved is': {
                    u'after': [{u'a': 1.0}, {u'penny': 1.0}],
                    u'frequency': 1.0 / 7.0
                }
            }
        )
