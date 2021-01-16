import turkish_suffix_library.turkish_string as tr
import turkish_suffix_library.consonants as con


class TurkishClass:
    def __init__(self, parameter_word: str, **kwargs):
        self.word = parameter_word
        self.stem = kwargs.get('stem', parameter_word)
        self.history = kwargs.get('history', [])

    def plural(self):
        self.concat(f'l{self.letter_a()}r')

        return self.word

    def apostrophes(self, **kwargs):
        if kwargs.get('proper_noun'):
            self.concat("'")
            return True
        else:
            return False

    def last_vowel(self):
        return tr.last_vowel(self.word)

    def letter_a(self):
        if self.last_vowel()['tone'] == 'front':
            return 'a'
        else:
            return 'e'

    def minor(self):
        return con.MINOR_HARMONY[self.last_vowel()['letter']]

    def letter_i(self):
        if self.last_vowel()['tone'] == 'front':
            return 'ı'
        else:
            return 'i'

    def last_letter(self):
        return tr.last_letter(self.word)

    def last_letter_is_vowel(self):
        return self.last_letter()['letter'] in con.VOWELS

    def last_letter_is_hard(self):
        return self.last_letter()['letter'] in con.HARD_CONSONANTS

    def if_ends_with_hard(self, concat_1, concat_2):
        if self.last_letter_is_hard():
            self.concat(concat_1)
        else:
            self.concat(concat_2)

    def if_ends_with_vowel(self, concat_text):
        if self.last_letter_is_vowel():
            self.concat(concat_text)

    def lower(self):
        return tr.make_lower(self.word)

    def soften(self):
        self.word = tr.soften(self.word)
        return self.word

    def concat(self, concat_string):
        self.word = tr.concat(self.word, concat_string)
        return self.word

    def exception_missing(self, proper_noun):
        return tr.exception_missing(self.word, proper_noun)

    def to_string(self):
        return self.word

    def to_json(self):
        return {
            'result': self.word,
            'stem': self.stem,
            'history': self.history
        }

    def __str__(self):
        return self.word

    def from_upper_or_lower(self, new_word):
        self.word = tr.from_upper_or_lower(new_word, self.word)
        return self.word

    def is_from_able(self):
        if len(self.history):
            action = self.history[-1]['action']
            auxiliary = self.history[-1]['kwargs'].get('auxiliary')

            if action == 'unify_verbs' and auxiliary == 'bil':
                return True

        return False

    def is_from_passive(self):
        if len(self.history):
            action = self.history[-1]['action']

            if action == 'passive':
                return True

        return False

    def ng_change(self):
        self.word = con.NK_G_CHANGE.get(self.lower(), self.word)
        return self.word

    def change_last_letter(self, letter):
        self.word = tr.change_last_letter(self.word, letter)
        return self.word

    def ends_with(self, letter):
        return self.last_letter().get('letter') == letter

    def if_ends_with(self, old_letter, new_letter):
        if self.ends_with(old_letter):
            self.change_last_letter(new_letter)

    def verb_in_minor_harmony_exception(self):
        lower = self.lower()

        for verb in con.VERB_MINOR_HARMONY_EXCEPTIONS:
            if lower.endswith(verb):
                return True

        return False

    def harden_verb(self):
        lower = self.lower()

        for hard in con.VERBS_HARDEN:
            if lower.endswith(hard):
                self.word = tr.concat(
                    self.word[:-len(hard)], con.VERBS_HARDEN[hard]
                )

        return self.word

    def verbs_losing_vowels(self):
        self.word = self.from_upper_or_lower(
            con.VERBS_LOSING_VOWELS.get(self.lower(), self.word)
        )
        return self.word

    def n_connector(self):
        return self.lower() in con.N_CONNECTOR

    def harmony_for_present(self):
        vowel = self.last_vowel()['letter'].lower()

        return con.HARMONY_FOR_PRESENT.get(vowel, vowel)

    def count_syllable(self):
        vowel = self.last_vowel()

        return vowel['vowel_count']
