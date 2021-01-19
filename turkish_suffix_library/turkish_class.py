import turkish_suffix_library.turkish_string as tr
import turkish_suffix_library.consonants as con


class TurkishClass:
    def __init__(self, parameter_word: str, **kwargs):
        self.word = parameter_word
        self.stem = kwargs.get('stem', parameter_word)
        self.history = kwargs.get('history', [])

    def __str__(self):
        return self.word

    def to_string(self):
        return self.word

    def to_json(self):
        return {
            'result': self.word,
            'stem': self.stem,
            'history': self.history
        }

    def last_word(self):
        return self.word.lower().split(' ')[-1]

    def other_words_but_not_last(self):
        return ' '.join(self.word.lower().split(' ')[:-1])

    def make_plural(self):
        self.concat(f'l{self.letter_a()}r')

        return self.word

    def apostrophes(self, **kwargs):
        if kwargs.get('proper_noun'):
            self.word += "'"
            return True
        else:
            return False

    def last_vowel(self):
        return tr.last_vowel(self.word)

    def letter_d(self):
        if self.last_letter_is_vowel() or not self.last_letter_is_hard():
            return 'd'
        else:
            return 't'

    def letter_a(self):
        if self.last_vowel().get('tone') == 'front':
            return 'a'
        else:
            return 'e'

    def minor(self):
        return con.MINOR_HARMONY.get(self.last_vowel().get('letter'), 'a')

    def letter_i(self):
        if self.last_vowel().get('tone') == 'front':
            return 'ı'
        else:
            return 'i'

    def last_letter(self):
        return tr.last_letter(self.last_word())

    def last_letter_is_vowel(self):
        return self.last_letter().get('letter') in con.VOWELS

    def last_letter_is_hard(self):
        return self.last_letter().get('letter') in con.HARD_CONSONANTS

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

    def from_upper_or_lower(self, new_word):
        self.word = tr.from_upper_or_lower(new_word, self.word)
        return self.word

    def is_from_able(self):
        if len(self.history):
            action = self.history[-1].get('action')
            auxiliary = self.history[-1].get('kwargs', {}).get('auxiliary')

            if action == 'unify_verbs' and auxiliary == 'bil':
                return True

        return False

    def is_from_passive(self):
        if len(self.history):
            action = self.history[-1].get('action')

            if action == 'passive':
                return True

        return False

    def ng_change(self):
        word = self.lower()

        for noun in con.NK_G_CHANGE:
            if word.endswith(noun):
                return self.from_upper_or_lower(
                    word[:-len(noun)] + con.NK_G_CHANGE.get(noun, self.word)
                )

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
        word = self.last_word()

        return word in con.VERB_MINOR_HARMONY_EXCEPTIONS

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

    def harmony_for_present_first(self):
        vowel = self.last_vowel()['letter'].lower()

        return con.HARMONY_FOR_PRESENT_FIRST.get(vowel, vowel)

    def count_syllable(self):
        vowel = self.last_vowel()

        return vowel['vowel_count']

    def if_condition(self, person, plural, *args):
        for arg in args:
            person_param = arg[0]
            plural_param = arg[1]
            suffix = arg[2]

            if person == person_param and plural_param == plural:
                self.concat(suffix)
                return self.word

        return self.word
