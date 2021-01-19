from turkish_suffix_library.turkish import Turkish
import unittest


class Adverb(unittest.TestCase):
    def test_adverb_during_action(self):
        self.assertEqual(
            Turkish('it').present_continuous_simple().adverb_during_action().to_string(),
            'itiyorken'
        )

        self.assertEqual(
            Turkish('it').present_continuous_simple(negative=True).adverb_during_action().to_string(),
            'itmiyorken'
        )

    def test_adverb_after_action(self):
        self.assertEqual(
            Turkish('gül').adverb_after_action().to_string(),
            'gülünce'
        )

        self.assertEqual(
            Turkish('gül').adverb_after_action(negative=True).to_string(),
            'gülmeyince'
        )

    def test_adverb_after_action_alternative(self):
        self.assertEqual(
            Turkish('git').adverb_after_action_alternative().to_string(),
            'gidip'
        )

        self.assertEqual(
            Turkish('git').adverb_after_action_alternative(negative=True).to_string(),
            'gitmeyip'
        )

    def test_adverb_without_action(self):
        self.assertEqual(
            Turkish('et').adverb_without_action().to_string(),
            'etmeden'
        )

    def test_adverb_without_action_alternative(self):
        self.assertEqual(
            Turkish('yürü').adverb_without_action_alternative().to_string(),
            'yürümeksizin'
        )

    def test_adverb_by_action(self):
        self.assertEqual(
            Turkish('ata').adverb_by_action(negative=True).to_string(),
            'atamayarak'
        )

        self.assertEqual(
            Turkish('ata').adverb_by_action().to_string(),
            'atayarak'
        )

    def test_adverb_continuity(self):
        self.assertEqual(
            Turkish('anlat').adverb_continuity().to_string(),
            'anlata anlata'
        )

        self.assertEqual(
            Turkish('anlat').adverb_continuity(negative=True).to_string(),
            'anlatmaya anlatmaya'
        )

    def test_adverb_repeatedly(self):
        self.assertEqual(
            Turkish('vur').adverb_repeatedly().to_string(),
            'vurdukça'
        )

        self.assertEqual(
            Turkish('vur').adverb_repeatedly(negative=True).to_string(),
            'vurmadıkça'
        )

    def test_adverb_since_action(self):
        self.assertEqual(
            Turkish('ara').adverb_since_action().to_string(),
            'arayalı'
        )

        self.assertEqual(
            Turkish('ara').adverb_since_action(negative=True).to_string(),
            'aramayalı'
        )


class Noun(unittest.TestCase):
    def test_dative(self):
        self.assertEqual(
            Turkish('araba').dative().to_string(),
            'arabaya'
        )

        self.assertEqual(
            Turkish('renk').dative().to_string(),
            'renge'
        )

        self.assertEqual(
            Turkish('bank').dative().to_string(),
            'banka'
        )

    def test_ablative(self):
        self.assertEqual(
            Turkish('sebep').ablative().to_string(),
            'sebepten'
        )

    def test_accusative(self):
        self.assertEqual(
            Turkish('sebep').accusative().to_string(),
            'sebebi'
        )

        self.assertEqual(
            Turkish('ecdat').accusative().to_string(),
            'ecdadı'
        )

    def test_instrumental(self):
        self.assertEqual(
            Turkish('kedi').instrumental().to_string(),
            'kediyle'
        )

    def test_possessive(self):
        self.assertEqual(
            Turkish('aparat').possessive(person=2).to_string(),
            'aparatın'
        )

        self.assertEqual(
            Turkish('batak').possessive(person=3).to_string(),
            'batağı'
        )

        self.assertEqual(
            Turkish('idrak').possessive(person=1, plural=True).to_string(),
            'idrakımız'
        )

        self.assertEqual(
            Turkish('ok').possessive(person=2, plural=True).to_string(),
            'okunuz'
        )

        self.assertEqual(
            Turkish('çanta').possessive(person=3, plural=True).to_string(),
            'çantaları'
        )

    def test_genitive_possessive(self):
        self.assertEqual(
            f'{Turkish("Elif").genitive(proper_noun=True)} {Turkish("Öküz").possessive(person=3)}',
            'Elif\'in Öküzü'
        )

    def test_ordinal(self):
        self.assertEqual(
            Turkish('dört').ordinal().to_string(),
            'dördüncü'
        )

    def test_distributive(self):
        self.assertEqual(
            Turkish('yedi').distributive().to_string(),
            'yedişer'
        )


class Verb(unittest.TestCase):
    def test_passive(self):
        self.assertEqual(
            Turkish('al').passive().present_continuous_simple(person=2, negative=True).to_string(),
            'alınılmıyorsun'
        )

negative = False
verb = 'et'
question = False
print(Turkish(verb).simple_tense(negative=negative, question=question, person=1, plural=False))
print(Turkish(verb).simple_tense(negative=negative, question=question, person=2, plural=False))
print(Turkish(verb).simple_tense(negative=negative, question=question, person=3, plural=False))
print(Turkish(verb).simple_tense(negative=negative, question=question, person=1, plural=True))
print(Turkish(verb).simple_tense(negative=negative, question=question, person=2, plural=True))
print(Turkish(verb).simple_tense(negative=negative, question=question, person=3, plural=True))

if __name__ == '__main__':
    unittest.main()

