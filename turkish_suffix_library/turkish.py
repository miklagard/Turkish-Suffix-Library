#!/usr/bin/python
# -*- coding: utf-8 -*-
import inspect

from turkish_suffix_library.turkish_string import make_lower, \
    make_upper, concat, from_upper_or_lower, \
    last_vowel, last_letter, soften, exception_missing, change_last_letter

from turkish_suffix_library.consonants import HARD_CONSONANTS, \
    MINOR_HARMONY, VOWELS, MINOR_HARMONY_FOR_FUTURE, N_CONNECTOR, VERBS_LOSING_VOWELS, \
    VERBS_HARDEN, PASSIVE_EXCEPTION, NK_G_CHANGE


class Turkish:
    def __init__(self, parameter_word: str, **kwargs):
        self.word = parameter_word
        self.stem = kwargs.get('stem', parameter_word)
        self.history = kwargs.get('history', [])

    def proceed_letters(func):
        def wrapper(self, *args, **kwargs):
            kwargs['last_vowel'] = last_vowel(self.word)
            if kwargs['last_vowel']['tone'] == 'front':
                kwargs['ae'] = 'a'
                kwargs['letter_i'] = 'ı'
            else:
                kwargs['ae'] = 'e'
                kwargs['letter_i'] = 'i'

            kwargs['last_letter'] = last_letter(self.word)
            kwargs['last_letter_is_vowel'] = kwargs['last_letter']['letter'] in VOWELS
            kwargs['lower_word'] = make_lower(self.word)

            return func(self, *args, **kwargs)

        return wrapper

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

    def common_return(self, **kwargs):
        self.history.append({
            'action': inspect.stack()[1][3],
            'current': self.word,
            'kwargs': kwargs
        })

        return Turkish(
            self.word,
            stem=self.stem,
            history=self.history
        )

    @proceed_letters
    def plural(self, **kwargs):
        ae = kwargs.get('ae')
        self.word = concat(self.word, f'l{ae}r')

        return self.common_return(**{})

    @proceed_letters
    def accusative(self, **kwargs):
        """
            -i hali
            (not finished yet)
        """

        proper_noun = kwargs.get('proper_noun')

        if proper_noun:
            self.word += '\''
        else:
            self.word = exception_missing(self.word, proper_noun)

        actual_last_letter = last_letter(self.word)

        if 'vowel' in actual_last_letter:
            if kwargs.get('lower_word') in N_CONNECTOR:
                self.word = concat(self.word, 'n')
            else:
                self.word = concat(self.word, 'y')

        self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)
        self.word = soften(self.word)

        self.word = concat(
            self.word,
            MINOR_HARMONY[last_vowel(self.word)['letter']]
        )

        return self.common_return(**kwargs)

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
        else:
            self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)
            self.word = exception_missing(self.word, proper_noun)

            actual_last_letter = last_letter(self.word)
            actual_last_vowel = last_vowel(self.word)

            if 'vowel' in actual_last_letter:
                if lower_word in N_CONNECTOR:
                    self.word = concat(self.word, 'n')
                else:
                    self.word = concat(self.word, 'y')

            self.word = soften(self.word)

            if actual_last_vowel['tone'] == 'front':
                self.word = concat(self.word, 'a')
            else:
                self.word = concat(self.word, 'e')

        if self.word.isupper():
            self.word = make_upper(self.word)

        return self.common_return(**kwargs)

    @proceed_letters
    def ablative(self, **kwargs):
        """
            -den hali
        """
        proper_noun = kwargs.get('proper_noun')
        ae = kwargs['ae']

        if proper_noun:
            self.word += '\''

        if kwargs.get('lower_word') in N_CONNECTOR:
            self.word = concat(self.word, 'n')

        if kwargs.get('last_letter')['letter'] in HARD_CONSONANTS:
            self.word = concat(self.word, 't')
        else:
            self.word = concat(self.word, 'd')

        self.word = concat(self.word, f'{ae}n')

        return self.common_return(**kwargs)

    @proceed_letters
    def locative(self, **kwargs):
        """
            -de hali
        """
        proper_noun = kwargs.get('proper_noun')
        ae = kwargs['ae']

        if proper_noun:
            self.word += '\''

        if kwargs['lower_word'] in N_CONNECTOR:
            self.word = concat(self.word, 'n')

        if kwargs['last_letter']['letter'] in HARD_CONSONANTS:
            self.word = concat(self.word, 't')
        else:
            self.word = concat(self.word, 'd')

        self.word = concat(self.word, ae)

        return self.common_return(**kwargs)

    @proceed_letters
    def genitive(self, **kwargs):
        """
            Iyelik aitlik eki
            Ayakkabinin
            Elif'in
        """

        proper_noun = kwargs.get('proper_noun')
        minor_harmony_letter = MINOR_HARMONY[kwargs['last_vowel']['letter']]

        if proper_noun:
            self.word += '\''

            if kwargs['last_letter_is_vowel']:
                self.word = concat(self.word, 'n')
        else:
            self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)

            if kwargs['last_letter_is_vowel']:
                self.word = concat(self.word, 'n')
            else:
                self.word = soften(self.word)

                self.word = exception_missing(self.word, proper_noun)

        self.word = concat(self.word, f'{minor_harmony_letter}n')

        return self.common_return(**kwargs)

    @proceed_letters
    def equalative(self, **kwargs):
        """
            Ismin esitlik hali: -ce, -ca etc.
        """

        ae = kwargs.get('ae')

        if kwargs['last_letter']['letter'] in HARD_CONSONANTS:
            self.word = concat(self.word, f'ç{ae}')
        else:
            self.word = concat(self.word, f'c{ae}')

        return self.common_return(**kwargs)

    @proceed_letters
    def instrumental(self, **kwargs):
        """
            Ismin vasıta hali: -le, -la, -yle, -yla
        """
        if kwargs.get('proper_noun'):
            self.word += '\''

        ae = kwargs.get('ae')

        if kwargs['last_letter_is_vowel']:
            self.word = concat(self.word, f'y')

        self.word = concat(self.word, f'l{ae}')

        return self.common_return(**kwargs)

    def possessive(self, **kwargs):
        """
            Iyelik tamlanan eki
            Ayakkabısı
        """
        person = str(kwargs.get('person', 3))

        is_plural = kwargs.get('plural', False)

        proper_noun = kwargs.get('proper_noun', False)

        if not (person == '3' and is_plural):
            if proper_noun:
                self.word += '\''
            else:
                self.word = soften(self.word)

                self.word = exception_missing(self.word, proper_noun)

        actual_last_letter = last_letter(self.word)
        actual_last_vowel = last_vowel(self.word)

        last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

        minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]

        if not is_plural:
            if person == '1':
                self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)

                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, 'm')

            elif person == '2':
                self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)

                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, 'n')

            elif person == '3':
                self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)

                if last_letter_is_vowel:
                    self.word = concat(self.word, 's')

                self.word = concat(self.word, minor_harmony_letter)
        else:
            if person == '1':
                self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)

                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, f'm{minor_harmony_letter}z')

            elif person == '2':
                self.word = NK_G_CHANGE.get(make_lower(self.word), self.word)

                if not last_letter_is_vowel:
                    self.word = concat(self.word, minor_harmony_letter)

                self.word = concat(self.word, f'n{minor_harmony_letter}z')
            else:
                if make_lower(self.word) == 'ism':
                    self.word = from_upper_or_lower('isim', self.word)

                self.word = self.plural().to_string()
                self.word = concat(self.word, minor_harmony_letter)

        return self.common_return(**kwargs)

    @proceed_letters
    def infinitive(self, **kwargs):
        """
            Mastar eki
        """

        ae = kwargs.get('ae')

        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{ae}')

        self.word = concat(self.word, f'm{ae}k')

        return self.common_return(**kwargs)

    @proceed_letters
    def present_continuous(self, **kwargs):
        """
            Şimdiki zaman
            Example: arıyorum
            Note: For alternative usage of present continuous tense, check the function
                    present_continuous_alternative
        """

        if not kwargs.get('negative', False):
            self.word = VERBS_HARDEN.get(self.word, self.word)

            if kwargs['last_letter_is_vowel']:
                self.word = change_last_letter(self.word, MINOR_HARMONY[self.word[-1]])
            else:
                self.word = concat(
                    self.word,
                    MINOR_HARMONY[kwargs['last_vowel']['letter']]
                )
        else:
            self.word = concat(self.word, 'm')
            self.word = concat(
                self.word,
                MINOR_HARMONY[kwargs['last_vowel']['letter']]
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

        return self.common_return(**kwargs)

    @proceed_letters
    def present_continuous_alternative(self, **kwargs):
        """
            There are two ways to express 'present continuous tense in Turkish '
            This kind is not common in daily Turkish usage anymore
            Example:
                * aramaktayım
                * yapmaktayım
        """
        ae = kwargs.get('ae')
        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{ae}')

        self.word = self.infinitive().to_string()

        self.word = concat(self.word, f't{ae}')

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
                    self.word = concat(self.word, ' m')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'y')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'm')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' m')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'n')
            else:  # plural
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, ' m')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'y')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, ' m')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 's')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'n')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])
                    self.word = concat(self.word, 'z')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
                    self.word = concat(self.word, ' m')
                    self.word = concat(self.word, MINOR_HARMONY[last_vowel(self.word)['letter']])

        return self.common_return(**kwargs)

    @proceed_letters
    def present_simple(self, **kwargs):
        """
            Geniş zaman
        """
        minor = MINOR_HARMONY[kwargs['last_vowel']['letter']]
        minor_harmony_letter_for_future = MINOR_HARMONY_FOR_FUTURE[kwargs['last_vowel']['letter']]
        minor_harmony_for_future = MINOR_HARMONY_FOR_FUTURE[minor]

        if not kwargs.get('negative', False):
            self.word = soften(self.word)

            self.word = VERBS_HARDEN.get(self.word, self.word)

        if kwargs.get('question', False):
            if not kwargs.get('negative', False):
                if self.word in ['al', 'kal']:
                    self.word = concat(self.word, 'ır')
                else:
                    if not kwargs['last_letter_is_vowel']:
                        self.word = concat(self.word, minor_harmony_letter_for_future)

                    self.word = concat(self.word, 'r')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, f' m{minor}y{minor}m')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, f' m{minor}s{minor}n')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, f' m{minor}')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, f' m{minor}y{minor}z')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, f' m{minor}s{minor}n{minor}z')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, f' m{minor}')
            elif kwargs.get('negative', False):
                if last_vowel(self.word)['tone'] == 'front':
                    minor_harmony_letter_for_future = 'a'
                else:
                    minor_harmony_letter_for_future = 'e'

                self.word = concat(self.word, f'm{minor_harmony_letter_for_future}z')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, f' m{minor}y{minor}m')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, f' m{minor}s{minor}n')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, f' m{minor}')
                elif kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, f' m{minor}y{minor}z')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, f' m{minor}s{minor}n{minor}z')
                    elif kwargs.get('person', 3) == 3:
                        self.word = self.plural().to_string()
                        self.word = concat(self.word, f' m{minor}')
        elif not kwargs.get('question', False):
            if not kwargs.get('negative', False):
                if self.word in ['al', 'kal']:
                    self.word = concat(self.word, 'ır')
                else:
                    if not kwargs['last_letter_is_vowel']:
                        self.word = concat(self.word, minor_harmony_letter_for_future)

                    self.word = concat(self.word, 'r')

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, f'{minor}m')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, f's{minor}n')
                else:
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, f'{minor}z')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, f's{minor}n{minor}z')
                    elif kwargs.get('person', 3) == 3:
                        self.word = self.plural().to_string()
            elif kwargs.get('negative', False):
                if last_vowel(self.word)['tone'] == 'front':
                    minor_harmony_letter_for_future = 'a'
                else:
                    minor_harmony_letter_for_future = 'e'

                if not kwargs.get('plural', False):
                    if kwargs.get('person', 3) == 1:
                        self.word = concat(self.word, f'm{minor_harmony_letter_for_future}m')
                    elif kwargs.get('person', 3) == 2:
                        self.word = concat(self.word, 'm')
                        self.word = concat(self.word, minor_harmony_letter_for_future)
                        self.word = concat(self.word, 'z')
                        self.word = concat(self.word, 's')
                        self.word = concat(self.word, MINOR_HARMONY[minor_harmony_for_future])
                        self.word = concat(self.word, 'n')
                    elif kwargs.get('person', 3) == 3:
                        self.word = concat(self.word, f'm{minor_harmony_letter_for_future}z')
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
                        self.word = concat(self.word, f'm{minor_harmony_letter_for_future}z')
                        self.word = self.plural().to_string()

        return self.common_return(**kwargs)

    @proceed_letters
    def future(self, **kwargs):
        """
            Gelecek zaman
        """
        ae = kwargs['ae']

        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{ae}')

        if 'vowel' in kwargs['last_letter']:
            self.word = VERBS_LOSING_VOWELS.get(self.word, self.word)
            self.word = concat(self.word, 'y')

        self.word = soften(self.word)

        if not kwargs.get('negative', False):
            self.word = VERBS_HARDEN.get(self.word, self.word)

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

        return self.common_return(**kwargs)

    @proceed_letters
    def learned_past(self, **kwargs):
        """
            Not the same with English past perfect tense
            This usage is for past tense of an action which is heared/learned but not witnessed.
            mişli geçmiş zaman veya öğrenilen geçmiş zaman
        """

        ae = kwargs['ae']
        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{ae}')

        minor = MINOR_HARMONY[kwargs['last_vowel']['letter']]

        self.word = concat(self.word, f'm{minor}ş')

        if not kwargs.get('question', False):
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, f'{minor}m')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, f's{minor}n')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, f'{minor}z')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, f's{minor}n{minor}z')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
        elif kwargs.get('question', False):
            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, f' m{minor}y{minor}m')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, f' m{minor}s{minor}n')
                elif kwargs.get('person', 3) == 3:
                    self.word = concat(self.word, f' m{minor}')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, f' m{minor}y{minor}z')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, f' m{minor}s{minor}n{minor}z')
                elif kwargs.get('person', 3) == 3:
                    self.word = self.plural().to_string()
                    self.word = concat(self.word, f' m{minor}')

        return self.common_return(**kwargs)

    @proceed_letters
    def unify_verbs(self, **kwargs):
        """
            Unified verbs (Birleşik fiiler) (Not a suffix but for 'can-bil' modal verb, this is necessary)
            Ability - Yeterlilik: kızabil (bil) (English modal auxiliary verb: Can)
            Swiftness - Tezlik: koşuver (ver)
            Continuity - Süreklilik: gidedur, bakakal, alıkoy (dur, kal, gel, koy)
            Approach - Yaklaşma: (yaz) düzeyaz
        """
        self.word = VERBS_LOSING_VOWELS.get(self.word, self.word)

        minor = MINOR_HARMONY[kwargs['last_vowel']['letter']]

        if kwargs['last_letter_is_vowel']:
            self.word = concat(self.word, 'y')

        self.word = soften(self.word)
        ae = kwargs['ae']

        self.word = VERBS_HARDEN.get(self.word, self.word)

        if not kwargs.get('negative', False):
            if kwargs.get('auxiliary') in ['ver', 'koy']:
                self.word = concat(self.word, minor)
            else:
                self.word = concat(self.word, ae)

            self.word = concat(self.word, kwargs.get('auxiliary'))
        if kwargs.get('negative', False):
            if kwargs.get('auxiliary') == 'bil':
                self.word = concat(self.word, f'{ae}m{ae}')
            else:
                if kwargs.get('auxiliary') in ['ver', 'koy']:
                    self.word = concat(self.word, minor)
                else:
                    self.word = concat(self.word, ae)

                self.word = concat(self.word, kwargs.get('auxiliary'))

                self.word = concat(self.word, ae)

        return self.common_return(**kwargs)

    @proceed_letters
    def must(self, **kwargs):
        """
            Gereklilik kipi
        """

        letter_a = kwargs['ae']
        letter_i = kwargs['letter_i']

        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{letter_a}')

        self.word = concat(self.word, f'm{letter_a}l{letter_i}')
        
        if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
            self.word = self.plural().to_string()

        if kwargs.get('question', False):
            self.word = concat(self.word, f' m{letter_i}')

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, f'y{letter_i}m')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, f's{letter_i}n')
        else:
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, f'y{letter_i}z')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, f's{letter_i}n{letter_i}z')

        return self.common_return(**kwargs)

    @proceed_letters
    def wish_condition(self, **kwargs):
        """
            Dilek - Şart kipi (-se, -sa)
        """
        letter_a = kwargs['ae']
        letter_i = kwargs['letter_i']

        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{letter_a}')

        self.word = concat(self.word, f's{letter_a}')

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'm')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, 'n')
        else:  # Plural
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, 'k')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, f'n{letter_i}z')
            elif kwargs.get('person', 3) == 3:
                self.word = self.plural().to_string()

        if kwargs.get('question', False):
            self.word = concat(self.word, f' m{letter_i}')

        return self.common_return(**kwargs)

    @proceed_letters
    def wish(self, **kwargs):
        """
            İstek kipi (geleyim, gelesin, gele, gelelim, gelesiniz, geleler)
        """
        letter_a = kwargs['ae']
        letter_i = kwargs['letter_i']

        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{letter_a}y{letter_a}')
        else:
            self.word = VERBS_LOSING_VOWELS.get(self.word, self.word)

            self.word = VERBS_HARDEN.get(self.word, self.word)

            if kwargs['last_letter_is_vowel']:
                self.word = concat(self.word, 'y')

            self.word = soften(self.word)

            self.word = concat(self.word, letter_a)

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, f'y{letter_i}m')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, f's{letter_i}n')
        else:
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, f'l{letter_i}m')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, f's{letter_i}n{letter_i}z')
            elif kwargs.get('person', 3) == 3:
                self.word = self.plural().to_string()

        if kwargs.get('question', False):
            self.word = concat(self.word, f' m{letter_i}')

        return self.common_return(**kwargs)

    @proceed_letters
    def command(self, **kwargs):
        """
            Make the verb command
            Usage: do it, break it, come!
            As different from English, command optative mood is valid also for 3rd person in Turkish
                but never for 1st person.
            For the second person, there is no suffix
        """

        ae = kwargs['ae']

        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{ae}')

        minor = MINOR_HARMONY[kwargs['last_vowel']['letter']]

        if not kwargs.get('plural', False):
            if kwargs.get('person', 2) == 3:
                self.word = concat(self.word, f's{minor}n')

                if kwargs.get('question', False):
                    self.word = concat(self.word, f' m{minor}')
        else:  # Plural
            if kwargs.get('person', 2) == 2:
                self.word = VERBS_LOSING_VOWELS.get(self.word, self.word)

                if kwargs['last_letter_is_vowel']:
                    self.word = concat(self.word, 'y')

                self.word = soften(self.word, False, kwargs.get('negative', False))

                self.word = VERBS_HARDEN.get(self.word, self.word)

                self.word = concat(self.word, f'{minor}n')

                if kwargs.get('formal', False):
                    self.word = concat(self.word, f'{minor}z')
            elif kwargs.get('person', 2) == 3:
                self.word = concat(self.word, f's{minor}n')
                self.word = self.plural().to_string()
                if kwargs.get('question', False):
                    self.word = concat(self.word, f' m{minor}')

        return self.common_return(**kwargs)

    @proceed_letters
    def past(self, **kwargs):
        """
            Past tense
            -di'li geçmiş zaman
        """
        
        ae = kwargs['ae']

        if kwargs.get('negative', False):
            self.word = concat(self.word, f'm{ae}')

        actual_last_letter = last_letter(self.word)
        minor = MINOR_HARMONY[last_vowel(self.word)['letter']]

        if 'hard_consonant' not in actual_last_letter or 'vowel' in actual_last_letter:
            ps = 'd'
        else:
            ps = 't'

        if not kwargs.get('plural', False):
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, f'{ps}{minor}m')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, f'{ps}{minor}n')
            elif kwargs.get('person', 3) == 3:
                self.word = concat(self.word, f'{ps}{minor}')
        else:  # plural
            if kwargs.get('person', 3) == 1:
                self.word = concat(self.word, f'{ps}{minor}k')
            elif kwargs.get('person', 3) == 2:
                self.word = concat(self.word, f'{ps}{minor}n{minor}z')
            elif kwargs.get('person', 3) == 3:
                self.word = concat(self.word, f'{ps}{minor}')
                self.word = self.plural().to_string()

        if kwargs.get('question', False):
            actual_last_vowel = last_vowel(self.word)
            minor = MINOR_HARMONY[last_vowel(self.word)['letter']]

            self.word = concat(self.word, f' m{minor}')

        return self.common_return(**kwargs)

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

            self.word = concat(self.word, ' m')

            if last_vowel(self.word)['tone'] == 'front':
                self.word = concat(self.word, 'ı')
            else:
                self.word = concat(self.word, 'i')
        else:
            self.word = self.past(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()

        return self.common_return(**kwargs)

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

            self.word = concat(self.word, f' m{letter}yd{letter}')

            if not kwargs.get('plural', False):
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'm')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, 'n')
            else:
                if kwargs.get('person', 3) == 1:
                    self.word = concat(self.word, 'k')
                elif kwargs.get('person', 3) == 2:
                    self.word = concat(self.word, f'n{letter}z')

        return self.common_return(**kwargs)

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

        return self.common_return(**kwargs)

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

                self.word = concat(self.word, f' m{minor}ym{minor}ş')
            else:
                minor = MINOR_HARMONY[last_vowel(self.word)['letter']]
                self.word = concat(self.word, f' m{minor}y')
                self.word = self.learned_past(
                    person=kwargs.get('person', 3),
                    plural=kwargs.get('plural', False)
                ).to_string()

        return self.common_return(**kwargs)

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

        return self.common_return(**kwargs)

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

        return self.common_return(**kwargs)

    @proceed_letters
    def ordinal(self, **kwargs):
        """
            Ordinal numbers: One->First, Two->Second etc.

            bir-i-nci, iki-nci...

            This rule is also valid for words:
            * son (last) -> sonuncu
            * ilk (first) -> ilkinci (ilk already means "first" but you can still put this suffix)
        """

        minor_harmony_letter = MINOR_HARMONY[kwargs['last_vowel']['letter']]

        last_letter_is_vowel = kwargs['last_letter']['letter'] in VOWELS

        if kwargs.get('proper_noun'):
            self.word += '\''
        elif kwargs['last_letter'].get('letter') == 't':
            self.word = change_last_letter(self.word, 'd')

        if not last_letter_is_vowel:
            self.word = concat(self.word, f'{minor_harmony_letter}')

        self.word = concat(self.word, f'nc{minor_harmony_letter}')

        return self.common_return(**kwargs)

    @proceed_letters
    def distributive(self, **kwargs):
        """
            Distributive numbers: One->One each, Two->Two each.

            bir-er, iki-şer...
        """

        ae = kwargs.get('ae')

        if kwargs.get('proper_noun'):
            self.word += '\''
        elif kwargs['last_letter'].get('letter') == 't':
            self.word = change_last_letter(self.word, 'd')

        if kwargs.get('last_letter_is_vowel'):
            self.word = concat(self.word, f'ş')

        self.word = concat(self.word, f'{ae}r')

        return self.common_return(**kwargs)

    @proceed_letters
    def passive(self, **kwargs):
        """
            Turns verb into passive (edilgen):

            Kirdim -> Kirildim
            I brake -> I am broken

            Use passive always before conjuncting the verb with tense and person

            Example:
            Turkish('ver').passive().present_continuous_alternative(person=1)
            verilmekteyim
        """
        self.word = VERBS_HARDEN.get(self.word, self.word)

        minor = MINOR_HARMONY[kwargs['last_vowel']['letter']]

        if kwargs['lower_word'] in PASSIVE_EXCEPTION:
            self.word = PASSIVE_EXCEPTION.get(kwargs['lower_word'])
        else:
            if kwargs['last_letter_is_vowel']:
                self.word = concat(self.word, f'n')

            self.word = concat(self.word, f'{minor}l')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_during_action(self, **kwargs):
        """
            Giderken etc. (iken)

            Generates adverb-verb for "while", doing two things together:

            He was smoking while sipping vodka.
            Sigara icerken vodka yudumluyordu.

            Use this method after conjuncting the verb with tense and person

            Person should be always 3rd person plural or 3rd person singular

            Example:
            Turkish('ver').present_continuous_alternative(person=3).adverb_during_action()
        """
        if kwargs['last_letter_is_vowel']:
            self.word = concat(self.word, f'y')

        self.word = concat(self.word, f'ken')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_continuity(self, **kwargs):
        """
            Git -> Gide gide etc. (-e)

            Use this method without conjuncting
        """
        ae = kwargs.get('ae')

        if kwargs.get('negative'):
            self.word = concat(self.word, f'm{ae}y')
        else:
            self.word = VERBS_HARDEN.get(self.word, self.word)

            if kwargs['last_letter_is_vowel']:
                self.word = concat(self.word, f'y')

        self.word = concat(self.word, f'{ae}')

        self.word = f'{self.word} {self.word}'

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_repeatedly(self, **kwargs):
        """
            Git -> Gide gide etc. (-e)

            Use this method without conjuncting
        """
        ae = kwargs.get('ae')

        self.word = self.past(
            negative=kwargs.get('negative'),
            person=1,
            plural=True
        ).to_string()

        self.word = concat(self.word, f'ç{ae}')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_after_action(self, **kwargs):
        """
            Gidince etc. (-nca)

            Generates adverb-verb for "after"

            Use this method without any conjuncting
        """

        ae = kwargs['ae']
        letter_i = kwargs['letter_i']
        minor = MINOR_HARMONY[kwargs['last_vowel']['letter']]
        self.word = VERBS_HARDEN.get(self.word, self.word)

        if kwargs.get('negative'):
            self.word = concat(self.word, f'm{ae}y{letter_i}')
        elif kwargs['last_letter_is_vowel']:
            self.word = concat(self.word, f'y{minor}')
        else:
            self.word = concat(self.word, f'{minor}')

        self.word = concat(self.word, f'nc{ae}')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_after_action_alternative(self, **kwargs):
        """
            Gidip etc. (-p)

            Generates adverb-verb for "after"

            Use this method without any conjuncting
        """

        ae = kwargs['ae']
        minor = MINOR_HARMONY[kwargs['last_vowel']['letter']]

        if kwargs.get('negative'):
            self.word = concat(self.word, f'm{ae}y')
        elif kwargs['last_letter_is_vowel']:
            self.word = concat(self.word, f'y')
        else:
            self.word = VERBS_HARDEN.get(self.word, self.word)

        self.word = concat(self.word, f'{minor}p')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_without_action(self, **kwargs):
        """
            Gitmeden etc. (-madan)

            Generates adverb-verb for "without action"

            Use this method without any conjuncting
        """

        ae = kwargs['ae']
        self.word = concat(self.word, f'm{ae}d{ae}n')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_without_action_alternative(self, **kwargs):
        """
            Gitmeksizin etc. (-meksizin)

            Generates adverb-verb for "without action"

            Use this method without any conjuncting
        """

        letter_i = kwargs['letter_i']
        self.word = self.infinitive().to_string()
        self.word = concat(self.word, f's{letter_i}z{letter_i}n')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_by_action(self, **kwargs):
        """
            Giderek etc. (-erek)

            Generates adverb-verb for "by action"

            Use this method without any conjuncting
        """

        ae = kwargs['ae']
        if kwargs.get('negative'):
            self.word = concat(self.word, f'm{ae}y')
        else:
            self.word = VERBS_HARDEN.get(self.word, self.word)

            if kwargs['last_letter_is_vowel']:
                self.word = concat(self.word, 'y')

        self.word = concat(self.word, f'{ae}r{ae}k')

        return self.common_return(**kwargs)

    @proceed_letters
    def adverb_since_action(self, **kwargs):
        """
            Gideli etc. (-eli)

            Generates adverb-verb for "since action"

            Use this method without any conjuncting
        """

        ae = kwargs['ae']
        letter_i = kwargs['letter_i']

        if kwargs.get('negative'):
            self.word = concat(self.word, f'm{ae}y')
        else:
            self.word = VERBS_HARDEN.get(self.word, self.word)

            if kwargs['last_letter_is_vowel']:
                self.word = concat(self.word, 'y')

        self.word = concat(self.word, f'{ae}l{letter_i}')

        return self.common_return(**kwargs)