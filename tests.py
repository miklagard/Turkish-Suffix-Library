from turkish_suffix_library.turkish import Turkish
import unittest


class TestSuffixes(unittest.TestCase):
    def test_adverb_verb_during_action(self):
        self.assertEqual(
            Turkish('it').present_continuous().adverb_verb_during_action().to_string(),
            'itiyorken'
        )

    def test_adverb_verb_after_action(self):
        self.assertEqual(
            Turkish('gül').adverb_verb_after_action(negative=True).to_string(),
            'gülmeyince'
        )


if __name__ == '__main__':
    unittest.main()
