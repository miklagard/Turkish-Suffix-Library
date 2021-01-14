import inspect

from turkish_suffix_library.turkish_string import make_lower, \
    concat, from_upper_or_lower, \
    last_vowel, last_letter, soften, exception_missing, change_last_letter

from turkish_suffix_library.consonants import HARD_CONSONANTS, \
    MINOR_HARMONY, VOWELS, VERB_MINOR_HARMONY_EXCEPTIONS, N_CONNECTOR, VERBS_LOSING_VOWELS, \
    VERBS_HARDEN, NK_G_CHANGE


class TurkishClass:
    def __init__(self, parameter_word: str, **kwargs):
        self.word = parameter_word
        self.stem = kwargs.get('stem', parameter_word)
        self.history = kwargs.get('history', [])

    def last_vowel(self):
        return last_vowel(self.word)

    def letter_a(self):
        if self.last_vowel()['tone'] == 'front':
            return 'a'
        else:
            return 'e'

    def minor(self):
        return MINOR_HARMONY[self.last_vowel()['letter']]

    def letter_i(self):
        if self.last_vowel()['tone'] == 'front':
            return 'ı'
        else:
            return 'i'

    def last_letter(self):
        return last_letter(self.word)

    def last_letter_is_vowel(self):
        return self.last_letter()['letter'] in VOWELS

    def concat_if_ends_with_vowel(self, concat_text):
        vowel = self.last_letter_is_vowel()

        if vowel:
            self.concat(concat_text)

        return vowel

    def last_letter_is_hard(self):
        return self.last_letter()['letter'] in HARD_CONSONANTS

    def if_ends_with_hard(self, concat_1, concat_2):
        if self.last_letter_is_hard():
            self.concat(concat_1)
        else:
            self.concat(concat_2)

    def lower(self):
        return make_lower(self.word)

    def soften(self):
        self.word = soften(self.word)
        return self.word

    def concat(self, concat_string):
        self.word = concat(self.word, concat_string)
        return concat(self.word, concat_string)

    def exception_missing(self, proper_noun):
        return exception_missing(self.word, proper_noun)

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
        self.word = from_upper_or_lower(new_word, self.word)
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
        self.word = NK_G_CHANGE.get(self.lower(), self.word)
        return self.word

    def change_last_letter(self, letter):
        self.word = change_last_letter(self.word, letter)
        return self.word

    def ends_with(self, letter):
        return self.last_letter().get('letter') == letter

    def if_ends_with(self, old_letter, new_letter):
        if self.ends_with(old_letter):
            self.change_last_letter(new_letter)

    def verb_in_minor_harmony_exception(self):
        lower = self.lower()

        for verb in VERB_MINOR_HARMONY_EXCEPTIONS:
            if lower.endswith(verb):
                return True

        return False

    def harden_verb(self):
        lower = self.lower()

        for hard in VERBS_HARDEN:
            if lower.endswith(hard):
                self.word = concat(self.word[:-len(hard)], VERBS_HARDEN[hard])

        return self.word

    def verbs_losing_vowels(self):
        self.word = self.from_upper_or_lower(VERBS_LOSING_VOWELS.get(self.lower(), self.word))
        return self.word

    def n_connector(self):
        return self.lower() in N_CONNECTOR
