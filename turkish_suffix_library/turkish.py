#!/usr/bin/python
# -*- coding: utf-8 -*-
from turkish_suffix_library.turkish_string import is_upper, make_lower, \
    make_upper, concat, from_upper_or_lower, \
    last_vowel, last_letter

from turkish_suffix_library.consonants import EXCEPTION_MISSING, HARD_CONSONANTS, \
    MINOR_HARMONY, MAJOR_HAMONY_EXCEPTIONS, \
    VOWELS, MINOR_HARMONY_FOR_FUTURE


class Turkish:
    def __init__(self, parameter_word: str):
        self.word = parameter_word

    def to_string(self):
        return self.word

    def __str__(self):
        return self.word

    def plural(self, **kwargs):
        if 'proper_noun' in kwargs:
            self.word = f'{self.word}\''

        if last_vowel(self.word)['tone'] == 'front':
            self.word = concat(self.word, 'lar')
        else:
            self.word = concat(self.word, 'ler')

        return Turkish(self.word)

    def accusative(self, **kwargs):
        """
            -i hali
            (not finished yet)
        """

        # firstly exceptions for o (he/she/it)
        lower_word = make_lower(self.word)

        proper_noun = kwargs.get('proper_noun', False)

        if lower_word == 'o':
            if proper_noun:
                self.word = from_upper_or_lower('O\'nu', self.word)
            else:
                self.word = from_upper_or_lower('onu', self.word)
        elif lower_word == 'bu' and not proper_noun:
            self.word = from_upper_or_lower('bunu', self.word)
        elif lower_word == 'şu' and not proper_noun:
            self.word = from_upper_or_lower('şunu', self.word)
        else:
            if lower_word in EXCEPTION_MISSING and proper_noun == True:
                self.word = from_upper_or_lower(
                    EXCEPTION_MISSING[lower_word],
                    self.word
                )

            actual_last_letter = last_letter(self.word)
            actual_last_vowel = last_vowel(self.word)

            if proper_noun:
                self.word += '\''

            if 'vowel' in actual_last_letter:
                self.word = concat(self.word, 'y')
            elif 'discontinuous_hard_consonant' in actual_last_letter \
                    and not proper_noun:
                if actual_last_vowel['vowel_count'] > 1:
                    self.word = concat(
                        self.word[0:len(self.word) - 1],
                        actual_last_letter['soften_consonant']
                    )

            self.word = concat(
                self.word,
                MINOR_HARMONY[last_vowel(self.word)['letter']]
            )

        return Turkish(self.word)

    def dative(self, **kwargs):
        """
            -e hali
        """

        # firstly exceptions for ben (I) and you (sen)

        proper_noun = kwargs.get('proper_noun', False)

        lower_word = make_lower(self.word)

        if proper_noun:
            self.word += '\''

        if lower_word == 'ben' and not proper_noun:
            self.word = from_upper_or_lower('bana', self.word)
        elif lower_word == 'sen' and not proper_noun:
            self.word = from_upper_or_lower('sana', self.word)
        elif lower_word == 'o' and not proper_noun:
            if proper_noun:
                self.word = from_upper_or_lower('O\'na', self.word)
            else:
                self.word = from_upper_or_lower('ona', self.word)
        elif lower_word == 'bu' and not proper_noun:
            self.word = from_upper_or_lower('buna', self.word)
        elif lower_word == 'şu' and not proper_noun:
            self.word = from_upper_or_lower('şuna', self.word)
        else:
            if lower_word in EXCEPTION_MISSING and not proper_noun:
                self.word = from_upper_or_lower(
                    EXCEPTION_MISSING[lower_word],
                    self.word
                )

            actual_last_letter = last_letter(self.word)
            actual_last_vowel = last_vowel(self.word)

            if 'vowel' in actual_last_letter:
                self.word = concat(self.word, 'y')
            elif 'discontinuous_hard_consonant_for_suffix' in actual_last_letter:
                if actual_last_vowel['vowel_count'] > 1 and not proper_noun:
                    self.word = concat(
                        self.word[0:len(self.word) - 1],
                        actual_last_letter['soften_consonant_for_suffix']
                    )

            if actual_last_vowel['tone'] == 'front':
                self.word = concat(self.word, 'a')
            else:
                self.word = concat(self.word, 'e')

        if self.word.isupper():
            self.word = make_upper(self.word)

        return Turkish(self.word)

    def ablative(self, **kwargs):
        """
            -den hali
        """
        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)
        proper_noun = kwargs.get('proper_noun', False)
        lower_word = make_lower(self.word)

        if lower_word == 'o' and not proper_noun:
            if proper_noun:
                self.word = from_upper_or_lower('O\'ndan', self.word)
            else:
                self.word = from_upper_or_lower('ondan', self.word)
        elif lower_word == 'bu' and not proper_noun:
            self.word = from_upper_or_lower('bundan', self.word)
        elif lower_word == 'şu' and not proper_noun:
            self.word = from_upper_or_lower('şundan', self.word)
        else:
            if proper_noun:
                self.word += '\''

            if actual_last_letter['letter'] in HARD_CONSONANTS:
                self.word = concat(self.word, 't')
            else:
                self.word = concat(self.word, 'd')

            if actual_last_vowel['tone'] == 'front':
                self.word = concat(self.word, 'an')
            else:
                self.word = concat(self.word, 'en')

        return Turkish(self.word)

    def locative(self, **kwargs):
        """
            -de hali
        """
        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)
        proper_noun = kwargs.get('proper_noun', False)

        if proper_noun:
            self.word += '\''

        if actual_last_letter['letter'] in HARD_CONSONANTS:
            self.word = concat(self.word, 't')
        else:
            self.word = concat(self.word, 'd')

        if actual_last_vowel['tone'] == 'front':
            self.word = concat(self.word, 'a')
        else:
            self.word = concat(self.word, 'e')

        return Turkish(self.word)

    def genitive(self, **kwargs):
        """
            Iyelik aitlik eki
            Ayakkabinin
            Elif'in
        """

        proper_noun = kwargs.get('proper_noun', False)
        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)
        minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]

        last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

        if proper_noun:
            self.word += '\''

            if last_letter_is_vowel:
                self.word = concat(self.word, 'n')

        else:
            if last_letter_is_vowel:
                self.word = concat(self.word, 'n')
            else:
                if 'discontinuous_hard_consonant' in actual_last_letter:
                    if actual_last_vowel['vowel_count'] > 1:
                        self.word = concat(
                            self.word[0:len(self.word) - 1],
                            actual_last_letter['soften_consonant']
                        )

                if make_lower(self.word) in EXCEPTION_MISSING:
                    self.word = from_upper_or_lower(
                        EXCEPTION_MISSING[make_lower(self.word)],
                        self.word
                    )

        self.word = concat(self.word, minor_harmony_letter)
        self.word = concat(self.word, 'n')

        return Turkish(self.word)

    def possessive(self, **kwargs):
        """
            Iyelik tamlanan eki
            Ayakkabısı
        """
        person = str(kwargs.get('person', 3))

        is_plural = kwargs.get('plural', False)

        proper_noun = kwargs.get('proper_noun', False)

        if not (person == '3' and is_plural):
            actual_last_letter = last_letter(self.word)
            actual_last_vowel = last_vowel(self.word)

            if proper_noun:
                self.word += '\''

            elif 'discontinuous_hard_consonant' in actual_last_letter:
                if actual_last_vowel['vowel_count'] > 1:
                    self.word = concat(
                        self.word[0:len(self.word) - 1],
                        actual_last_letter['soften_consonant']
                    )

                if make_lower(self.word) in EXCEPTION_MISSING:
                    self.word = from_upper_or_lower(
                        EXCEPTION_MISSING[make_lower(self.word)],
                        self.word
                    )

        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)

        last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

        minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]

        if not is_plural:
            if person == '1':
                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, 'm')

            elif person == '2':
                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, 'n')

            elif person == '3':
                if last_letter_is_vowel:
                    self.word = concat(self.word, 's')

                self.word = concat(self.word, minor_harmony_letter)
        else:
            if person == '1':
                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, 'm')
                self.word = concat(self.word, minor_harmony_letter)
                self.word = concat(self.word, 'z')

            elif person == '2':
                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, 'n')
                self.word = concat(self.word, minor_harmony_letter)
                self.word = concat(self.word, 'z')
            else:
                if make_lower(self.word) == 'ism':
                    self.word = from_upper_or_lower('isim', self.word)

                self.word = self.plural().to_string()
                self.word = concat(self.word, minor_harmony_letter)

        return Turkish(self.word)

    def infinitive(self, **kwargs):
        """
            Mastar eki
        """
        if kwargs.get('negative', False):
            if last_vowel(self.word)['tone'] == 'front':
                self.word = concat(self.word, 'mamak')
            else:
                self.word = concat(self.word, 'memek')
        else:
            if last_vowel(self.word)['tone'] == 'front':
                self.word = concat(self.word, 'mak')
            else:
                self.word = concat(self.word, 'mek')

        return Turkish(self.word)

    def present_continuous(self, **kwargs):
        """
            Şimdiki zaman
            Example: arıyorum
            Note: For alternative usage of present continuous tense, check the function
                    present_continuous_alternative
        """
        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)

        last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

        if not kwargs.get('negative', False):
            # if 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
            #	word = concat(self.word[0:len(self.word) - 1], actual_last_letter['soften_consonant'])

            if self.word == 'git':
                self.word = 'gid'

            if last_letter_is_vowel:
                self.word = concat(
                    self.word[:-1],
                    MINOR_HARMONY[self.word[-1]]
                )
            else:
                self.word = concat(
                    self.word,
                    MINOR_HARMONY[actual_last_vowel['letter']]
                )
        else:
            self.word = concat(self.word, 'm')
            self.word = concat(
                self.word,
                MINOR_HARMONY[actual_last_vowel['letter']]
            )

        self.word = concat(self.word, 'yor')

        if kwargs.get('question', False):
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, ' muyum')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' musun')
                elif kwargs.get('person', 3) == 3:
                    self.word = concat(self.word, ' mu')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, ' muyuz')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' musunuz')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
                    self.word = concat(self.word, ' m')
                    if last_vowel(self.word)['tone'] == 'front':
                        self.word = concat(self.word, 'ı')
                    else:
                        self.word = concat(self.word, 'i')
        else:
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'um')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 'sun')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'uz')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 'sunuz')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()

        return Turkish(self.word)

    def present_continuous_alternative(self, **kwargs):
        """
            There are two ways to express 'present continuous tense in Turkish '
            This kind is not common in daily Turkish usage anymore
            Example:
                * aramaktayım
                * yapmaktayım
        """
        if kwargs.get('negative', False):
            if last_vowel(self.word)['tone'] == 'front':
                self.word = concat(self.word, 'ma')
            else:
                self.word = concat(self.word, 'me')

        self.word = self.infinitive().to_string()

        if last_vowel(self.word)['tone'] == 'front':
            self.word = concat(self.word, 'ta')
        else:
            self.word = concat(self.word, 'te')

        if not kwargs.get('question', False):
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'y')
                    self.word = concat(
                        self.word,
                        MINOR_HARMONY[last_vowel(self.word)['letter']]
                    )
                    self.word = concat(self.word, 'm')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 's')
                    self.word = concat(
                        self.word,
                        MINOR_HARMONY[last_vowel(self.word)['letter']]
                    )
                    self.word = concat(self.word, 'n')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'y')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'n')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
        elif kwargs.get('question', False):
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'y')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'm')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'n')
            else:  # plural
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'y')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'n')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])

        return Turkish(self.word)

    def present_simple(self, **kwargs):
        """
            Geniş zaman
        """
        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)

        last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

        minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]
        minor_harmony_letter_for_future = MINOR_HARMONY_FOR_FUTURE[actual_last_vowel['letter']]
        minor_harmony_for_future = MINOR_HARMONY_FOR_FUTURE[minor_harmony_letter]

        if not kwargs.get('negative', False):
            if 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
                self.word = concat(
                    self.word[0:len(self.word) - 1],
                    actual_last_letter['soften_consonant']
                )
            if self.word == 'git':
                self.word = 'gid'

        if kwargs.get('question', False):
            if not kwargs.get('negative', False):
                if self.word in ['al', 'kal']:
                    self.word = concat(self.word, 'ır')
                else:
                    if not last_letter_is_vowel:
                        self.word = concat(self.word, minor_harmony_letter_for_future)

                    self.word = concat(self.word, 'r')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'y')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'm')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'n')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'y')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'n')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 3:
                        self.word = self.plural().to_string()
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
            elif kwargs.get('negative', False):
                actual_last_vowel = last_vowel(self.word)

                if last_vowel(self.word)['tone'] == 'front':
                    minor_harmony_letter_for_future = 'a'
                else:
                    minor_harmony_letter_for_future = 'e'

                self.word = concat(self.word, 'm')
                self.word = concat(self.word, minor_harmony_letter_for_future)
                self.word = concat(self.word, 'z')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'y')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'm')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'n')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                elif kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'y')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'n')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 3:
                        self.word = self.plural().to_string()
                        self.word = concat(self.word, ' ')
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter)
        elif not kwargs.get('question', False):
            if not kwargs.get('negative', False):
                if self.word in ['al', 'kal']:
                    self.word = concat(self.word, 'ır')
                else:
                    if not last_letter_is_vowel:
                        self.word = concat(self.word, minor_harmony_letter_for_future)

                    self.word = concat(self.word, 'r')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'm')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'n')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'n')
                        self.word = concat(self.word, minor_harmony_letter)
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 3:
                        self.word = self.plural().to_string()
            elif kwargs.get('negative', False):
                if last_vowel(self.word)['tone'] == 'front':
                    minor_harmony_letter_for_future = 'a'
                else:
                    minor_harmony_letter_for_future = 'e'

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter_for_future)
                        self.word = concat(self.word, 'm')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter_for_future)
                        self.word = concat(self.word, 'z')
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, MINOR_HARMONY[minor_harmony_for_future])
                        self.word = concat(self.word, 'n')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter_for_future)
                        self.word = concat(self.word, 'z')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter_for_future)
                        self.word = concat(self.word, 'y')
                        self.word = concat(self.word, MINOR_HARMONY[minor_harmony_for_future])
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter_for_future)
                        self.word = concat(self.word, 'z')
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, MINOR_HARMONY[minor_harmony_for_future])
                        self.word = concat(self.word, 'n')
                        self.word = concat(self.word, MINOR_HARMONY[minor_harmony_for_future])
                        self.word = concat(self.word, 'z')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter_for_future)
                        self.word = concat(self.word, 'z')
                        self.word = self.plural().to_string()

        return Turkish(self.word)

    def future(self, **kwargs):
        """
            Gelecek zaman
        """
        if kwargs.get('negative', False):
            if last_vowel(self.word)['tone'] == 'front':
                self.word = concat(self.word, 'ma')
            else:
                self.word = concat(self.word, 'me')

        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)

        if 'vowel' in actual_last_letter:
            if self.word == 'de':
                self.word = 'di'
            elif self.word == 'ye':
                self.word = 'yi'

            self.word = concat(self.word, 'y')
        elif 'discontinuous_hard_consonant' in actual_last_letter \
                and actual_last_vowel['vowel_count'] > 1 \
                and not kwargs.get('negative', False):
            self.word = concat(self.word[0:len(self.word) - 1], actual_last_letter['soften_consonant'])

        if not kwargs.get('negative', False):
            if self.word == 'git':
                self.word = 'gid'

        if kwargs.get('question', False):
            if last_vowel(self.word)['tone'] == 'front':
                if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
                    self.word = concat(self.word, 'acaklar ')
                else:
                    self.word = concat(self.word, 'acak ')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'mıyım')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'mısın')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'mı')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'mıyız')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'mısınız')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'mı')
            else:
                if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
                    self.word = concat(self.word, 'ecekler ')
                else:
                    self.word = concat(self.word, 'ecek ')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'miyim')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'misin')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'mi')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'miyiz')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'misiniz')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'mi')
        elif not kwargs.get('question', False):
            if last_vowel(self.word)['tone'] == 'front':
                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'acağım')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'acaksın')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'acak')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'acağız')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'acaksınız')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'acaklar')
            else:
                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'eceğim')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'eceğiz')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'ecek')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, 'eceğiz')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'eceksiniz')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, 'ecekler')

        return Turkish(self.word)

    def learned_past(self, **kwargs):
        """
            Not the same with English past perfect tense
            This usage is for past tense of an action which is heared/learned but not witnessed.
            mişli geçmiş zaman veya öğrenilen geçmiş zaman
        """

        if kwargs.get('negative', False):
            self.word = concat(self.word, 'm')

            if last_vowel(self.word)['tone'] == 'front':
                self.word = concat(self.word, 'a')
            else:
                self.word = concat(self.word, 'e')

        actual_last_vowel = last_vowel(self.word)
        minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]

        self.word = concat(self.word, 'm')
        self.word = concat(self.word, minor_harmony_letter)
        self.word = concat(self.word, 'ş')

        if not kwargs.get('question', False):
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'm')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'n')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'n')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
        elif kwargs.get('question', False):
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'y')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'm')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'n')
                elif kwargs.get('person', 3) == 3:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor_harmony_letter)
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'y')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'n')
                    self.word = concat(self.word, minor_harmony_letter)
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor_harmony_letter)

        return Turkish(self.word)

    def unify_verbs(self, **kwargs):
        """
            Unified verbs (Birleşik fiiler) (Not a suffix but for 'can-bil' modal verb, this is necessary)
            Ability - Yeterlilik: kızabil (bil) (English modal auxiliary verb: Can)
            Swiftness - Tezlik: koşuver (ver)
            Continuity - Süreklilik: gidedur, bakakal, alıkoy (dur, kal, gel, koy)
            Approach - Yaklaşma: (yaz) düzeyaz
        """
        if self.word == 'de':
            self.word = 'di'
        elif self.word == 'ye':
            self.word = 'yi'

        actual_last_vowel = last_vowel(self.word)
        get_aux_last_vowel = last_vowel(kwargs.get('auxiliary'))
        minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]
        actual_last_letter = last_letter(self.word)

        if 'vowel' in actual_last_letter:
            self.word = concat(self.word, 'y')
        elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
            self.word = concat(self.word[0:len(self.word) - 1], actual_last_letter['soften_consonant'])

        if not kwargs.get('negative', False):
            if kwargs.get('auxiliary') in ['ver', 'koy']:
                self.word = concat(self.word, minor_harmony_letter)
            elif actual_last_vowel['tone'] == 'front':
                self.word = concat(self.word, 'a')
            else:
                self.word = concat(self.word, 'e')

            self.word = concat(self.word, kwargs.get('auxiliary'))
        if kwargs.get('negative', False):
            if kwargs.get('auxiliary') == 'bil':
                if actual_last_vowel['tone'] == 'front':
                    self.word = concat(self.word, 'ama')
                else:
                    self.word = concat(self.word, 'eme')
            else:
                if kwargs.get('auxiliary') in ['ver', 'koy']:
                    self.word = concat(self.word, minor_harmony_letter)
                elif actual_last_vowel['tone'] == 'front':
                    self.word = concat(self.word, 'a')
                else:
                    self.word = concat(self.word, 'e')

                self.word = concat(self.word, kwargs.get('auxiliary'))

                if get_aux_last_vowel['tone'] == 'front':
                    self.word = concat(self.word, 'a')
                else:
                    self.word = concat(self.word, 'e')

        return Turkish(self.word)

    def must(self, **kwargs):
        """
            Gereklilik kipi
        """
        actual_last_vowel = last_vowel(self.word)

        if actual_last_vowel['tone'] == 'front':
            letterA = 'a'
            letterI = 'ı'
        else:
            letterA = 'e'
            letterI = 'i'

        if kwargs.get('negative', False):
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, letterA)

        self.word = concat(self.word, 'm')
        self.word = concat(self.word, letterA)
        self.word = concat(self.word, 'l')
        self.word = concat(self.word, letterI)

        if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
            self.word = self.plural().to_string()

        if kwargs.get('question', False):
            self.word = concat(self.word, ' ')
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, letterI)

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'y')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'm')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, 's')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'n')
        else:
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'y')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'z')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, 's')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'n')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'z')

        return Turkish(self.word)

    def wish_condition(self, **kwargs):
        """
            Dilek - Şart kipi (-se, -sa)
        """
        actual_last_vowel = last_vowel(self.word)

        if actual_last_vowel['tone'] == 'front':
            letterA = 'a'
            letterI = 'ı'
        else:
            letterA = 'e'
            letterI = 'i'

        if kwargs.get('negative', False):
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, letterA)

        self.word = concat(self.word, 's')
        self.word = concat(self.word, letterA)

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'm')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, 'n')
        else:  # Plural
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'k')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, 'n')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'z')
            elif kwargs.get('person', 3) == 3:
                self.word = self.plural().to_string()

        if kwargs.get('question', False):
            self.word = concat(self.word, ' ')
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, letterI)

        return Turkish(self.word)

    def wish(self, **kwargs):
        """
            İstek kipi (geleyim, gelesin, gele, gelelim, gelesiniz, geleler)
        """
        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)

        if actual_last_vowel['tone'] == 'front':
            letterA = 'a'
            letterI = 'ı'
        else:
            letterA = 'e'
            letterI = 'i'

        if kwargs.get('negative', False):
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, letterA)
            self.word = concat(self.word, 'y')
            self.word = concat(self.word, letterA)
        else:
            if self.word == 'de':
                self.word = 'di'
            elif self.word == 'ye':
                self.word = 'yi'

            if self.word == 'git':
                self.word = 'gid'

            if 'vowel' in actual_last_letter:
                self.word = concat(self.word, 'y')
            elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
                self.word = concat(self.word[0:len(self.word) - 1], actual_last_letter['soften_consonant'])

            self.word = concat(self.word, letterA)

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'y')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'm')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, 's')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'n')
        else:
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'l')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'm')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, 's')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'n')
                self.word = concat(self.word, letterI)
                self.word = concat(self.word, 'z')
            elif kwargs.get('person', 3) == 3:
                self.word = self.plural().to_string()

        if kwargs.get('question', False):
            self.word = concat(self.word, ' ')
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, letterI)

        return Turkish(self.word)

    def command(self, **kwargs):
        """
            Make the verb command
            Usage: do it, break it, come!
            As different from English, command optative mood is valid also for 3rd person in Turkish
                but never for 1st person.
            For the second person, there is no suffix
        """
        actual_last_vowel = last_vowel(self.word)

        # MINOR_HARMONY[last_vowel(self.word)['letter']]

        if kwargs.get('negative', False):
            self.word = concat(self.word, 'm')
            if actual_last_vowel['tone'] == 'front':
                self.word = concat(self.word, 'a')
            else:
                self.word = concat(self.word, 'e')

        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)
        minor = MINOR_HARMONY[last_vowel(self.word)['letter']]

        if not kwargs.get('plural', False):
            if kwargs.get('person', 2) == 3:
                self.word = concat(self.word, 's')
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'n')

                if kwargs.get('question', False):
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor)
        else:  # Plural
            if kwargs.get('person', 2) == 2:
                if self.word == 'de':
                    self.word = 'di'
                elif self.word == 'ye':
                    self.word = 'yi'

                if 'vowel' in actual_last_letter:
                    self.word = concat(self.word, 'y')
                elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel[
                    'vowel_count'] > 1 and kwargs.get(
                    'negative', False) == False:
                    self.word = concat(self.word[0:len(self.word) - 1], actual_last_letter['soften_consonant'])

                if self.word == 'git':
                    self.word = 'gid'

                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'n')

                if kwargs.get('formal', False):
                    self.word = concat(self.word, minor)
                    self.word = concat(self.word, 'z')
            elif kwargs.get('person', 2) == 3:
                self.word = concat(self.word, 's')
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'n')
                self.word = self.plural().to_string()
                if kwargs.get('question', False):
                    self.word = concat(self.word, ' ')
                    self.word = concat(self.word, 'm')
                    self.word = concat(self.word, minor)

        return Turkish(self.word)

    def past(self, **kwargs):
        """
            Past tense
            -di'li geçmiş zaman
        """
        actual_last_vowel = last_vowel(self.word)

        if kwargs.get('negative', False):
            self.word = concat(self.word, 'm')
            if actual_last_vowel['tone'] == 'front':
                self.word = concat(self.word, 'a')
            else:
                self.word = concat(self.word, 'e')

        actual_last_letter = last_letter(self.word)
        minor = MINOR_HARMONY[last_vowel(self.word)['letter']]

        if 'hard_consonant' not in actual_last_letter or 'vowel' in actual_last_letter:
            ps = 'd'
        else:
            ps = 't'

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, ps)
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'm')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, ps)
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'n')
            elif kwargs.get('person', 3) == 3:
                self.word = concat(self.word, ps)
                self.word = concat(self.word, minor)
        else:  # plural
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, ps)
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'k')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, ps)
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'n')
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'z')
            elif kwargs.get('person', 3) == 3:
                self.word = concat(self.word, ps)
                self.word = concat(self.word, minor)
                self.word = self.plural().to_string()

        if kwargs.get('question', False):
            actual_last_vowel = last_vowel(self.word)
            minor = MINOR_HARMONY[last_vowel(self.word)['letter']]

            self.word = concat(self.word, ' ')
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, minor)

        return Turkish(self.word)

    def past_past(self, **kwargs):
        """
            Bilinen geçmiş zamanın hikayesi
            yaptıydım, yaptıydın, yaptıydı, yaptıydık, yaptıydınız, yaptıydılar
            yaptı mıydım, yaptı mıydın, yaptı mıydı, yaptı mıydık, yaptı mıydınız, yaptılar mıydı
        """

        if kwargs.get('person', 3) == 3 \
                and kwargs.get('question', False) \
                and kwargs.get('plural', False):
            self.word = self.past(
                person=3,
                plural=False,
                negative=kwargs.get('negative', False),
            ).to_string()
        else:
            self.word = self.past(
                person=3,
                plural=False,
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False)
            ).to_string()

            self.word = concat(self.word, 'y')

        if kwargs.get('person', 3) == 3 \
                and kwargs.get('question', False) \
                and kwargs.get('plural', False):
            self.word = self.plural().to_string()

            self.word = concat(self.word, ' ')
            self.word = concat(self.word, 'm')

            if last_vowel(self.word)['tone'] == 'front':
                self.word = concat(self.word, 'ı')
            else:
                self.word = concat(self.word, 'i')
        else:
            self.word = self.past(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()

        return Turkish(self.word)

    def past_condition(self, **kwargs):
        """
            Bilinen geçmiş zamanın şartı
                durduysam, durduysan, durduysa, durduysak, durduysanız, durdularsa
                dursa mıydım, dursa mıydın, dursa mıydı, dursa mıydık, dursalar mıydı
        """

        if not kwargs.get('question', False):
            self.word = self.past(
                person=3,
                negative=kwargs.get('negative', False)
            ).to_string()

            self.word = concat(self.word, 'y')

            self.word = self.wish_condition(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()
        else:
            self.word = self.wish_condition(
                person=3,
                negative=kwargs.get('negative', False)
            ).to_string()

            if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
                self.word = self.plural().to_string()

            if last_vowel(self.word)['tone'] == 'front':
                letter = 'ı'
            else:
                letter = 'i'

            self.word = concat(self.word, ' ')
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, letter)
            self.word = concat(self.word, 'y')
            self.word = concat(self.word, 'd')
            self.word = concat(self.word, letter)

            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'm')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 'n')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'k')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 'n')
                    self.word = concat(self.word, letter)
                    self.word = concat(self.word, 'z')

        return Turkish(self.word)

    def past_learned_past(self, **kwargs):
        """
            Öğrenilen geçmiş zamanın hikayesi
            Yapmışlardı (-miş -di)
            Example: It is heard by someone that somebody did something in the past
        """

        if kwargs.get('person') == 3 and kwargs.get('plural', False) and kwargs.get('question', False):
            self.word = self.learned_past(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False),
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()
        else:
            self.word = self.learned_past(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False),
            ).to_string()

        if kwargs.get('question', False):
            self.word = concat(self.word, 'y')

        if kwargs.get('person') == 3 and kwargs.get('plural', False) and kwargs.get('question', False):
            self.word = self.past(person=kwargs.get('person', 3)).to_string()
        else:
            self.word = self.past(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()

        return Turkish(self.word)

    def learned_past_learned_past(self, **kwargs):
        """
            Öğrenilen geçmiş zamanın rivayeti
            Duymuşmuşum Duymuşmuşsun Duymuşmuş Duymuşmuşuz Duymuşmuşunuz Duymuşmuşlar
            Duymuş mumuymuşum? Duymuş mumuymuşsun? Duymuş mumuymuş? Duymuş mumuymuşuz?
            Duymuş mumuymuşsunuz Duymuşlar mıymış?
        """

        self.word = self.learned_past(negative=kwargs.get('negative', False)).to_string()

        if not kwargs.get('question', False):
            self.word = self.learned_past(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False),
                question=kwargs.get('question', False)
            ).to_string()
        else:
            if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
                self.word = self.plural().to_string()
                minor = MINOR_HARMONY[last_vowel(self.word)['letter']]

                self.word = concat(self.word, ' ')
                self.word = concat(self.word, 'm')
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'y')
                self.word = concat(self.word, 'm')
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'ş')
            else:
                minor = MINOR_HARMONY[last_vowel(self.word)['letter']]
                self.word = concat(self.word, ' ')
                self.word = concat(self.word, 'm')
                self.word = concat(self.word, minor)
                self.word = concat(self.word, 'y')
                self.word = self.learned_past(
                    person=kwargs.get('person', 3),
                    plural=kwargs.get('plural', False)
                ).to_string()

        return Turkish(self.word)

    def learned_past_future(self, **kwargs):
        """
            Gelecek zamanın rivayeti
            Yapacaklardı (-acak -mış)
            Example: It is heard by someone that somebody will do something in the past
        """

        if kwargs.get('person') == 3 and kwargs.get('plural', False) and kwargs.get('question', False):
            self.word = self.future(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False),
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()
        else:
            self.word = self.future(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False),
            ).to_string()

        if kwargs.get('person') == 3 and kwargs.get('plural', False) and kwargs.get('question', False):
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
            self.word = concat(self.word, 'y')
            self.word = self.learned_past(person=kwargs.get('person', 3)).to_string()
        else:
            if kwargs.get('question', False):
                self.word = concat(self.word, 'y')

            self.word = self.learned_past(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()

        return Turkish(self.word)

    def past_future(self, **kwargs):
        """
            Gelecek zamanın hikayesi
                Yapacaklardı (-acak -tı)
                Example: Somebody will do something in the past
        """

        if kwargs.get('person') == 3 and kwargs.get('plural', False) and kwargs.get('question', False):
            self.word = self.future(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False),
                person=kwargs.get('person', 3),
                pplural=kwargs.get('plural', False)
            ).to_string()
        else:
            self.word = self.future(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False)
            ).to_string()

        if kwargs.get('person') == 3 and kwargs.get('plural', False) and kwargs.get('question', False):
            self.word = concat(self.word, 'm')
            self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
            self.word = concat(self.word, 'y')
            self.word = self.past(person=kwargs.get('person', 3)).to_string()
        else:
            if kwargs.get('question', False):
                self.word = concat(self.word, 'y')

            self.word = self.past(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()

        return Turkish(self.word)
