#!/usr/bin/python
# -*- coding: utf-8 -*-
import turkish_suffix_library.turkish_string as turkish_string
import turkish_suffix_library.consonants as consonants


def make_plural(parameter_word: str, **kwargs) -> str:
    word: str = parameter_word

    if 'proper_noun' in kwargs:
        word = f'{word}\''

    if turkish_string.last_vowel(word)['tone'] == 'front':
        return turkish_string.concat(word, 'lar')
    else:
        return turkish_string.concat(word, 'ler')


# -i hali
def make_accusative(parameter_word: str, **kwargs) -> str:  # not finished yet
    # firstly exceptions for o (he/she/it)
    word = parameter_word
    lower_word = turkish_string.make_lower(word)

    proper_noun = kwargs.get('proper_noun', False)

    if lower_word == 'o':
        if proper_noun:
            return_data = turkish_string.from_upper_or_lower('O\'nu', word)
        else:
            return_data = turkish_string.from_upper_or_lower('onu', word)
    else:
        if lower_word in consonants.EXCEPTION_MISSING and proper_noun:
            word = turkish_string.from_upper_or_lower(consonants.EXCEPTION_MISSING[lower_word], word)

        actual_last_letter = turkish_string.last_letter(word)
        actual_last_vowel = turkish_string.last_vowel(word)

        if proper_noun:
            word += '\''

        if 'vowel' in actual_last_letter:
            word = turkish_string.concat(word, 'y')
        elif 'discontinuous_hard_consonant' in actual_last_letter and not proper_noun:
            word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])
        elif parameter_word in consonants.ARABIC_T:
            word = turkish_string.concat(word[0:len(word) - 1], 'd')

        word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])

        return_data = word

    return return_data


# -e hali
def make_dative(parameter_word: str, **kwargs) -> str:
    # firstly exceptions for ben (I) and you (sen)
    word: str = parameter_word

    proper_noun = kwargs.get('proper_noun', False)

    lower_word = turkish_string.make_lower(word)

    if proper_noun:
        word += '\''

    if lower_word == 'ben' and proper_noun == False:
        return_data = turkish_string.from_upper_or_lower('bana', word)
    elif lower_word == 'sen' and proper_noun == False:
        return_data = turkish_string.from_upper_or_lower('sana', word)
    else:
        if lower_word in consonants.EXCEPTION_MISSING and proper_noun == False:
            word = turkish_string.from_upper_or_lower(consonants.EXCEPTION_MISSING[lower_word], word)

        actual_last_letter = turkish_string.last_letter(word)
        actual_last_vowel = turkish_string.last_vowel(word)

        if 'vowel' in actual_last_letter:
            word = turkish_string.concat(word, 'y')
        elif 'discontinuous_hard_consonant_for_suffix' in actual_last_letter:
            if actual_last_vowel['vowel_count'] > 1 and proper_noun == False:
                word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant_for_suffix'])

        if actual_last_vowel['tone'] == 'front':
            word = turkish_string.concat(word, 'a')
        else:
            word = turkish_string.concat(word, 'e')

        return_data = word

    if return_data.isupper():
        return_data = turkish_string.make_upper(return_data)

    return return_data


# -de hali
def make_genitive(parameter_word: str, **kwargs) -> str:
    word = parameter_word

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)

    lower_word = turkish_string.make_lower(word)
    proper_noun = kwargs.get('proper_noun', False)

    if proper_noun:
        word += '\''

    if lower_word in consonants.EXCEPTION_MISSING:
        word = turkish_string.from_upper_or_lower(consonants.EXCEPTION_MISSING[lower_word], word)
        lower_word = turkish_string.make_lower(word)

    if 'hard_consonant' in actual_last_letter:
        word = turkish_string.concat(word, 't')
    else:
        word = turkish_string.concat(word, 'd')

    if actual_last_vowel['tone'] == 'front' and not word in consonants.MAJOR_HAMONY_EXCEPTIONS:
        word = turkish_string.concat(word, 'a')
    else:
        word = turkish_string.concat(word, 'e')

    return word


# -den hali
def make_ablative(parameter_word, **kwargs):
    word = parameter_word

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)
    proper_noun = kwargs.get('proper_noun')

    if proper_noun:
        word += '\''

    if actual_last_letter['letter'] in consonants.HARD_CONSONANTS:
        word = turkish_string.concat(word, 't')
    else:
        word = turkish_string.concat(word, 'd')

    if actual_last_vowel['tone'] == 'front':
        word = turkish_string.concat(word, 'an')
    else:
        word = turkish_string.concat(word, 'en')

    return_data = word

    return return_data


# -de hali
def make_locative(parameter_word, **kwargs):
    word = parameter_word

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)
    proper_noun = kwargs.get('proper_noun', False)

    if proper_noun:
        word += '\''

    if actual_last_letter['letter'] in consonants.HARD_CONSONANTS:
        word = turkish_string.concat(word, 't')
    else:
        word = turkish_string.concat(word, 'd')

    if actual_last_vowel['tone'] == 'front':
        word = turkish_string.concat(word, 'a')
    else:
        word = turkish_string.concat(word, 'e')

    return_data = word

    return return_data


# İyelik ekleri
def possessive_affix(parameter_word, **kwargs):
    position = kwargs.get('position', 1)
    word = parameter_word

    person = str(kwargs.get('person', 3))
    plural = kwargs.get('plural')

    proper_noun = kwargs.get('proper_noun', False)

    if not (person == '3' and plural):
        actual_last_letter = turkish_string.last_letter(word)
        actual_last_vowel = turkish_string.last_vowel(word)

        if proper_noun:
            word += '\''

        elif 'discontinuous_hard_consonant' in actual_last_letter:
            if actual_last_vowel['vowel_count'] > 1:
                word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

            if turkish_string.make_lower(word) in consonants.EXCEPTION_MISSING:
                word = turkish_string.from_upper_or_lower(
                    consonants.EXCEPTION_MISSING[turkish_string.make_lower(word)],
                    word
                )

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)

    turkish_string.last_letter_is_vowel = actual_last_letter['letter'] in consonants.VOWELS

    minor_harmony_letter = consonants.MINOR_HARMONY[actual_last_vowel['letter']]

    if not plural:
        if not turkish_string.last_letter_is_vowel:
            word = turkish_string.concat(word, minor_harmony_letter)

        if person == '1':
            word = turkish_string.concat(word, 'm')

        elif person == '2':
            word = turkish_string.concat(word, 'n')

        elif person == '3':
            word = turkish_string.concat(word, 's')
            word = turkish_string.concat(word, minor_harmony_letter)
    else:
        if person == '1':
            if not turkish_string.last_letter_is_vowel:
                word = turkish_string.concat(word, minor_harmony_letter)

            word = turkish_string.concat(word, 'm')
            word = turkish_string.concat(word, minor_harmony_letter)
            word = turkish_string.concat(word, 'z')

        elif person == '2':
            if not turkish_string.last_letter_is_vowel:
                word = turkish_string.concat(word, minor_harmony_letter)

            word = turkish_string.concat(word, 'n')
            word = turkish_string.concat(word, minor_harmony_letter)
            word = turkish_string.concat(word, 'z')
        else:

            if turkish_string.make_lower(word) == 'ism':
                word = turkish_string.from_upper_or_lower('isim', word)

            word = make_plural(word)
            word = turkish_string.concat(word, minor_harmony_letter)

    return word


# Mastar eski
def make_infinitive(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('negative', False):
        if turkish_string.last_vowel(word)['tone'] == 'front':
            return_data = turkish_string.concat(word, 'mamak')
        else:
            return_data = turkish_string.concat(word, 'memek')
    else:
        if turkish_string.last_vowel(word)['tone'] == 'front':
            return_data = turkish_string.concat(word, 'mak')
        else:
            return_data = turkish_string.concat(word, 'mek')

    return return_data


# Şimdiki zaman
#	   * arıyorum
#	   * For alternative usage of present continuous tense, check the function make_present_continuous_alternative
def make_present_continuous(parameter_word, **kwargs):
    word = parameter_word

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)

    turkish_string.last_letter_is_vowel = actual_last_letter['letter'] in consonants.VOWELS

    if not kwargs.get('negative', False):
        # if 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
        #	word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

        if word == 'git':
            word = 'gid'

        if turkish_string.last_letter_is_vowel:
            word = turkish_string.concat(word[:-1], consonants.MINOR_HARMONY[word[-1]])
        else:
            word = turkish_string.concat(word, consonants.MINOR_HARMONY[actual_last_vowel['letter']])
    else:
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, consonants.MINOR_HARMONY[actual_last_vowel['letter']])

    word = turkish_string.concat(word, 'yor')

    if kwargs.get('question'):
        if not kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, ' muyum')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, ' musun')
            elif kwargs.get('person', 3) == 3:
                word = turkish_string.concat(word, ' mu')
        elif kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, ' muyuz')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, ' musunuz')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
                word = turkish_string.concat(word, ' m')
                if turkish_string.last_vowel(word)['tone'] == 'front':
                    word = turkish_string.concat(word, 'ı')
                else:
                    word = turkish_string.concat(word, 'i')
    else:
        if not kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, 'um')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 'sun')
        elif kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, 'uz')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 'sunuz')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)

    return word


def make_present_continuous_alternative(parameter_word, **kwargs):
    # There are two ways to express 'present continuous tense in Turkish '
    # This kind is not common in daily Turkish usage anymore
    #	   * aramaktayım
    #	   * yapmaktayım
    word = parameter_word

    if kwargs.get('negative', False):
        if turkish_string.last_vowel(word)['tone'] == 'front':
            word = turkish_string.concat(word, 'ma')
        else:
            word = turkish_string.concat(word, 'me')

    word = make_infinitive(word)

    if turkish_string.last_vowel(word)['tone'] == 'front':
        word = turkish_string.concat(word, 'ta')
    else:
        word = turkish_string.concat(word, 'te')

    if not kwargs.get('question', False):
        if not kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, 'y')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'n')
        elif kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, 'y')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'n')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
    elif kwargs.get('question', False):
        if not kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'y')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'n')
        elif kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'y')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'n')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])

    return word


# Geniş zaman
def make_present_simple(parameter_word, **kwargs):
    word = parameter_word
    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)

    turkish_string.last_letter_is_vowel = actual_last_letter['letter'] in consonants.VOWELS

    minor_harmony_letter = consonants.MINOR_HARMONY[actual_last_vowel['letter']]
    minor_harmony_letterFF = consonants.MINOR_HARMONY_FOR_FUTURE[actual_last_vowel['letter']]
    minorHA = consonants.MINOR_HARMONY_FOR_FUTURE[minor_harmony_letter]

    if not kwargs.get('negative', False):
        if 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
            word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])
        if word == 'git':
            word = 'gid'

    if kwargs.get('question', False):
        if not kwargs.get('negative', False):
            if word in ['al', 'kal']:
                word = turkish_string.concat(word, 'ır')
            else:
                if not turkish_string.last_letter_is_vowel:
                    word = turkish_string.concat(word, minor_harmony_letterFF)

                word = turkish_string.concat(word, 'r')

            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'y')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'n')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
            elif kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'y')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'n')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = make_plural(word)
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
        elif kwargs.get('negative', False) == True:
            actual_last_vowel = turkish_string.last_vowel(word)

            if turkish_string.last_vowel(word)['tone'] == 'front':
                minor_harmony_letterFF = 'a'
            else:
                minor_harmony_letterFF = 'e'

            word = turkish_string.concat(word, 'm')
            word = turkish_string.concat(word, minor_harmony_letterFF)
            word = turkish_string.concat(word, 'z')

            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'y')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'n')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
            elif kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'y')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'n')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = make_plural(word)
                    word = turkish_string.concat(word, ' ')
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letter)
    elif not kwargs.get('question', False):
        if not kwargs.get('negative', False):
            if word in ['al', 'kal']:
                word = turkish_string.concat(word, 'ır')
            else:
                if not turkish_string.last_letter_is_vowel:
                    word = turkish_string.concat(word, minor_harmony_letterFF)

                word = turkish_string.concat(word, 'r')

            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'n')
            elif kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'n')
                    word = turkish_string.concat(word, minor_harmony_letter)
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = make_plural(word)
        elif kwargs.get('negative', False) == True:
            if turkish_string.last_vowel(word)['tone'] == 'front':
                minor_harmony_letterFF = 'a'
            else:
                minor_harmony_letterFF = 'e'

            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letterFF)
                    word = turkish_string.concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letterFF)
                    word = turkish_string.concat(word, 'z')
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, consonants.MINOR_HARMONY[minorHA])
                    word = turkish_string.concat(word, 'n')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letterFF)
                    word = turkish_string.concat(word, 'z')
            elif kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letterFF)
                    word = turkish_string.concat(word, 'y')
                    word = turkish_string.concat(word, consonants.MINOR_HARMONY[minorHA])
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letterFF)
                    word = turkish_string.concat(word, 'z')
                    word = turkish_string.concat(word, 's')
                    word = turkish_string.concat(word, consonants.MINOR_HARMONY[minorHA])
                    word = turkish_string.concat(word, 'n')
                    word = turkish_string.concat(word, consonants.MINOR_HARMONY[minorHA])
                    word = turkish_string.concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'm')
                    word = turkish_string.concat(word, minor_harmony_letterFF)
                    word = turkish_string.concat(word, 'z')
                    word = make_plural(word)

    return word


# Gelecek zaman
def make_future(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('negative', False):
        if turkish_string.last_vowel(word)['tone'] == 'front':
            word = turkish_string.concat(word, 'ma')
        else:
            word = turkish_string.concat(word, 'me')

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)

    if 'vowel' in actual_last_letter:
        if word == 'de':
            word = 'di'
        elif word == 'ye':
            word = 'yi'

        word = turkish_string.concat(word, 'y')
    elif 'discontinuous_hard_consonant' in actual_last_letter \
            and actual_last_vowel['vowel_count'] > 1 \
            and not kwargs.get('negative', False):
        word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

    if not kwargs.get('negative', False):
        if word == 'git':
            word = 'gid'

    if kwargs.get('question', False):
        if turkish_string.last_vowel(word)['tone'] == 'front':
            if kwargs.get('person', 3) == 3 and kwargs.get('plural'):
                word = turkish_string.concat(word, 'acaklar ')
            else:
                word = turkish_string.concat(word, 'acak ')

            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'mıyım')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'mısın')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'mı')
            elif kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'mıyız')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'mısınız')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'mı')
        else:
            if kwargs.get('person', 3) == 3 and kwargs.get('plural'):
                word = turkish_string.concat(word, 'ecekler ')
            else:
                word = turkish_string.concat(word, 'ecek ')

            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'miyim')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'misin')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'mi')
            else:
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'miyiz')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'misiniz')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'mi')
    elif not kwargs.get('question', False):
        if turkish_string.last_vowel(word)['tone'] == 'front':
            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'acağım')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'acaksın')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'acak')
            elif kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'acağız')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'acaksınız')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'acaklar')
        else:
            if not kwargs.get('plural'):
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'eceğim')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'eceğiz')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'ecek')
            else:
                if kwargs.get('person', 3) == 1:
                    word = turkish_string.concat(word, 'eceğiz')
                elif kwargs.get('person', 3) == 2:
                    word = turkish_string.concat(word, 'eceksiniz')
                elif kwargs.get('person', 3) == 3:
                    word = turkish_string.concat(word, 'ecekler')

    return word


# Not the same with English past perfect tense
# This usage is for past tense of an action which is learned but not witnessed.
# mişli geçmiş zaman veya öğrenilen geçmiş zaman
def make_past_perfect(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('negative', False):
        word = turkish_string.concat(word, 'm')

        if turkish_string.last_vowel(word)['tone'] == 'front':
            word = turkish_string.concat(word, 'a')
        else:
            word = turkish_string.concat(word, 'e')

    actual_last_vowel = turkish_string.last_vowel(word)
    minor_harmony_letter = consonants.MINOR_HARMONY[actual_last_vowel['letter']]

    word = turkish_string.concat(word, 'm')
    word = turkish_string.concat(word, minor_harmony_letter)
    word = turkish_string.concat(word, 'ş')

    if not kwargs.get('question', False):
        if not kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'n')
        elif kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'n')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
    elif kwargs.get('question'):
        if not kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'y')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'n')
            elif kwargs.get('person', 3) == 3:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor_harmony_letter)
        elif kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'y')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 's')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'n')
                word = turkish_string.concat(word, minor_harmony_letter)
                word = turkish_string.concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor_harmony_letter)

    return word


# Unified verbs (Birleşik fiiler) (Not a suffix but for 'can-bil' modal verb, this is necessary)
# Ability - Yeterlilik: kızabil (bil) (English modal auxiliary verb: Can)
# Swiftness - Tezlik: koşuver (ver)
# Continuity - Süreklilik: gidedur, bakakal, alıkoy (dur, kal, gel, koy)
# Approach - Yaklaşma: (yaz) düzeyaz
def unify_verbs(parameter_word, **kwargs):
    word = parameter_word

    if word == 'de':
        word = 'di'
    elif word == 'ye':
        word = 'yi'

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)
    get_aux_turkish_string.last_vowel = turkish_string.last_vowel(kwargs.get('auxiliary'))
    minor_harmony_letter = consonants.MINOR_HARMONY[actual_last_vowel['letter']]
    actual_last_letter = turkish_string.last_letter(word)

    if 'vowel' in actual_last_letter:
        word = turkish_string.concat(word, 'y')
    elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
        word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

    if not kwargs.get('negative', False):
        if kwargs.get('auxiliary') in ['ver', 'koy']:
            word = turkish_string.concat(word, minor_harmony_letter)
        elif actual_last_vowel['tone'] == 'front':
            word = turkish_string.concat(word, 'a')
        else:
            word = turkish_string.concat(word, 'e')

        word = turkish_string.concat(word, kwargs.get('auxiliary'))
    if kwargs.get('negative', False):
        if kwargs.get('auxiliary') == 'bil':
            if actual_last_vowel['tone'] == 'front':
                word = turkish_string.concat(word, 'ama')
            else:
                word = turkish_string.concat(word, 'eme')
        else:
            if kwargs.get('auxiliary') in ['ver', 'koy']:
                word = turkish_string.concat(word, minor_harmony_letter)
            elif actual_last_vowel['tone'] == 'front':
                word = turkish_string.concat(word, 'a')
            else:
                word = turkish_string.concat(word, 'e')

            word = turkish_string.concat(word, kwargs.get('auxiliary'))

            if get_aux_turkish_string.last_vowel['tone'] == 'front':
                word = turkish_string.concat(word, 'a')
            else:
                word = turkish_string.concat(word, 'e')

    return word


# Gereklilik kipi (-meli, -malı)
def make_must(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = turkish_string.last_vowel(word)

    if actual_last_vowel['tone'] == 'front':
        letterA = 'a'
        letterI = 'ı'
    else:
        letterA = 'e'
        letterI = 'i'

    if kwargs.get('negative', False):
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, letterA)

    word = turkish_string.concat(word, 'm')
    word = turkish_string.concat(word, letterA)
    word = turkish_string.concat(word, 'l')
    word = turkish_string.concat(word, letterI)

    if kwargs.get('person', 3) == 3 and kwargs.get('plural'):
        word = make_plural(word)

    if kwargs.get('question', False):
        word = turkish_string.concat(word, ' ')
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, letterI)

    if not kwargs.get('plural'):
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, 'y')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, 's')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'n')
    elif kwargs.get('plural'):
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, 'y')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'z')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, 's')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'n')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'z')

    return word


# Dilek - Şart kipi (-se, -sa)
def make_wish_condition(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = turkish_string.last_vowel(word)

    if actual_last_vowel['tone'] == 'front':
        letterA = 'a'
        letterI = 'ı'
    else:
        letterA = 'e'
        letterI = 'i'

    if kwargs.get('negative', False):
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, letterA)

    word = turkish_string.concat(word, 's')
    word = turkish_string.concat(word, letterA)

    if not kwargs.get('plural'):
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, 'n')
    else:  # Plural
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, 'k')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, 'n')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'z')
        elif kwargs.get('person', 3) == 3:
            word = make_plural(word)

    if kwargs.get('question', False):
        word = turkish_string.concat(word, ' ')
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, letterI)

    return word


# İstek kipi (geleyim, gelesin, gele, gelelim, gelesiniz, geleler)
def make_wish(parameter_word, **kwargs):
    word = parameter_word
    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)

    if actual_last_vowel['tone'] == 'front':
        letterA = 'a'
        letterI = 'ı'
    else:
        letterA = 'e'
        letterI = 'i'

    if kwargs.get('negative', False):
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, letterA)
        word = turkish_string.concat(word, 'y')
        word = turkish_string.concat(word, letterA)
    else:
        if word == 'de':
            word = 'di'
        elif word == 'ye':
            word = 'yi'

        if word == 'git':
            word = 'gid'

        if 'vowel' in actual_last_letter:
            word = turkish_string.concat(word, 'y')
        elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
            word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

        word = turkish_string.concat(word, letterA)

    if not kwargs.get('plural', False):
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, 'y')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, 's')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'n')
    else:
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, 'l')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, 's')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'n')
            word = turkish_string.concat(word, letterI)
            word = turkish_string.concat(word, 'z')
        elif kwargs.get('person', 3) == 3:
            word = make_plural(word)

    if kwargs.get('question', False):
        word = turkish_string.concat(word, ' ')
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, letterI)

    return word


# Make the verb command
# Usage: do it, break it, come!
# As different from English, command optative mood is valid also for 3rd person in Turkish
#    but never for 1st person.
# For the second person, there is no suffix
def make_command(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = turkish_string.last_vowel(word)

    # consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']]

    if kwargs.get('negative', False):
        word = turkish_string.concat(word, 'm')
        if actual_last_vowel['tone'] == 'front':
            word = turkish_string.concat(word, 'a')
        else:
            word = turkish_string.concat(word, 'e')

    actual_last_letter = turkish_string.last_letter(word)
    actual_last_vowel = turkish_string.last_vowel(word)
    minor = consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']]

    if not kwargs.get('plural'):
        if kwargs.get('person', 2) == 3:
            word = turkish_string.concat(word, 's')
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'n')

            if kwargs.get('question', False):
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor)
    else:  # Plural
        if kwargs.get('person', 2) == 2:
            if word == 'de':
                word = 'di'
            elif word == 'ye':
                word = 'yi'

            if 'vowel' in actual_last_letter:
                word = turkish_string.concat(word, 'y')
            elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel[
                'vowel_count'] > 1 and kwargs.get(
                'negative', False) == False:
                word = turkish_string.concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

            if word == 'git':
                word = 'gid'

            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'n')

            if kwargs.get('formal', False):
                word = turkish_string.concat(word, minor)
                word = turkish_string.concat(word, 'z')
        elif kwargs.get('person', 2) == 3:
            word = turkish_string.concat(word, 's')
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'n')
            word = make_plural(word)
            if kwargs.get('question', False):
                word = turkish_string.concat(word, ' ')
                word = turkish_string.concat(word, 'm')
                word = turkish_string.concat(word, minor)

    return word


# Past tense
# -di'li geçmiş zama
def make_past(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = turkish_string.last_vowel(word)
    actual_last_letter = turkish_string.last_letter(word)
    minor = consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']]

    if kwargs.get('negative', False):
        word = turkish_string.concat(word, 'm')
        if actual_last_vowel['tone'] == 'front':
            word = turkish_string.concat(word, 'a')
        else:
            word = turkish_string.concat(word, 'e')

    actual_last_vowel = turkish_string.last_vowel(word)
    actual_last_letter = turkish_string.last_letter(word)
    minor = consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']]

    if 'hard_consonant' not in actual_last_letter or 'vowel' in actual_last_letter:
        ps = 'd'
    else:
        ps = 't'

    if not kwargs.get('plural'):
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, ps)
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, ps)
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'n')
        elif kwargs.get('person', 3) == 3:
            word = turkish_string.concat(word, ps)
            word = turkish_string.concat(word, minor)
    else:  # plural
        if kwargs.get('person', 3) == 1:
            word = turkish_string.concat(word, ps)
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'k')
        elif kwargs.get('person', 3) == 2:
            word = turkish_string.concat(word, ps)
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'n')
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'z')
        elif kwargs.get('person', 3) == 3:
            word = turkish_string.concat(word, ps)
            word = turkish_string.concat(word, minor)
            word = make_plural(word)

    if kwargs.get('question', False):
        actual_last_vowel = turkish_string.last_vowel(word)
        minor = consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']]

        word = turkish_string.concat(word, ' ')
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, minor)

    return word


# Bilinen geçmiş zamanın hikayesi
# yaptıydım, yaptıydın, yaptıydı, yaptıydık, yaptıydınız, yaptıydılar
# yaptı mıydım, yaptı mıydın, yaptı mıydı, yaptı mıydık, yaptı mıydınız, yaptılar mıydı
def make_past_past(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('person', 3) == 3 \
            and kwargs.get('question', False) \
            and kwargs.get('plural'):
        word = make_past(word,
                         person=3,
                         plural=False,
                         negative=kwargs.get('negative', False),
                         )
    else:
        word = make_past(word,
                         person=3,
                         plural=False,
                         negative=kwargs.get('negative', False),
                         question=kwargs.get('question', False)
                         )

        word = turkish_string.concat(word, 'y')

    if kwargs.get('person', 3) == 3 \
            and kwargs.get('question', False) \
            and kwargs.get('plural'):
        word = make_plural(word)

        word = turkish_string.concat(word, ' ')
        word = turkish_string.concat(word, 'm')
        if turkish_string.last_vowel(word)['tone'] == 'front':
            word = turkish_string.concat(word, 'ı')
        else:
            word = turkish_string.concat(word, 'i')
    else:
        word = make_past(word,
                         person=kwargs.get('person', 3),
                         plural=kwargs.get('plural')
                         )

    return word


# Bilinen geçmiş zamanın şartı
# durduysam, durduysan, durduysa, durduysak, durduysanız, durdularsa
# dursa mıydım, dursa mıydın, dursa mıydı, dursa mıydık, dursalar mıydı
def make_past_condition(parameter_word, **kwargs):
    word = parameter_word

    if not kwargs.get('question', False):
        word = make_past(word,
                         person=3,
                         negative=kwargs.get('negative', False)
                         )

        word = turkish_string.concat(word, 'y')

        word = make_wish_condition(word,
                                   person=kwargs.get('person', 3),
                                   plural=kwargs.get('plural')
                                   )
    else:
        word = make_wish_condition(word,
                                   person=3,
                                   negative=kwargs.get('negative', False)
                                   )

        if kwargs.get('person', 3) == 3 and kwargs.get('plural'):
            word = make_plural(word)

        if turkish_string.last_vowel(word)['tone'] == 'front':
            letter = 'ı'
        else:
            letter = 'i'

        word = turkish_string.concat(word, ' ')
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, letter)
        word = turkish_string.concat(word, 'y')
        word = turkish_string.concat(word, 'd')
        word = turkish_string.concat(word, letter)

        if not kwargs.get('plural'):
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 'n')
        else:
            if kwargs.get('person', 3) == 1:
                word = turkish_string.concat(word, 'k')
            elif kwargs.get('person', 3) == 2:
                word = turkish_string.concat(word, 'n')
                word = turkish_string.concat(word, letter)
                word = turkish_string.concat(word, 'z')
    return word


# Öğrenilen geçmiş zamanın hikayesi
# Yapmışlardı (-miş -di)
# Example: It is heard by someone that somebody did something in the past
def make_past_past_perfect(parameter_wrod, **kwargs):
    word = parameter_wrod

    if kwargs.get('person') == 3 and kwargs.get('plural') and kwargs.get('question'):
        word = make_past_perfect(word,
                                 negative=kwargs.get('negative', False),
                                 question=kwargs.get('question', False),
                                 person=kwargs.get('person', 3),
                                 plural=kwargs.get('plural')
                                 )
    else:
        word = make_past_perfect(word,
                                 negative=kwargs.get('negative', False),
                                 question=kwargs.get('question', False),
                                 )

    if kwargs.get('question', False):
        word = turkish_string.concat(word, 'y')

    if kwargs.get('person') == 3 and kwargs.get('plural') and kwargs.get('question', False):
        word = make_past(word,
                         person=kwargs.get('person', 3)
                         )
    else:
        word = make_past(word,
                         person=kwargs.get('person', 3),
                         plural=kwargs.get('plural')
                         )

    return word


# Öğrenilen geçmiş zamanın rivayeti
# Duymuşmuşum Duymuşmuşsun Duymuşmuş Duymuşmuşuz Duymuşmuşunuz Duymuşmuşlar
# Duymuş mumuymuşum? Duymuş mumuymuşsun? Duymuş mumuymuş? Duymuş mumuymuşuz? Duymuş mumuymuşsunuz Duymuşlar mıymış?
def make_past_perfect_past_perfect(paramater_word, **kwargs):
    word = paramater_word

    word = make_past_perfect(word, negative=kwargs.get('negative', False))

    if not kwargs.get('question', False):
        word = make_past_perfect(word,
                                 person=kwargs.get('person', 3),
                                 plural=kwargs.get('plural'),
                                 question=kwargs.get('question', False)
                                 )
    else:
        if kwargs.get('person', 3) == 3 and kwargs.get('plural'):
            word = make_plural(word)
            minor = consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']]

            word = turkish_string.concat(word, ' ')
            word = turkish_string.concat(word, 'm')
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'y')
            word = turkish_string.concat(word, 'm')
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'ş')
        else:
            minor = consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']]
            word = turkish_string.concat(word, ' ')
            word = turkish_string.concat(word, 'm')
            word = turkish_string.concat(word, minor)
            word = turkish_string.concat(word, 'y')
            word = make_past_perfect(word,
                                     person=kwargs.get('person', 3),
                                     plural=kwargs.get('plural')
                                     )
    return word


# Gelecek zamanın rivayeti
# Yapacaklardı (-acak -mış)
# Example: It is heard by someone that somebody will do something in the past
def make_past_perfect_future(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('person') == 3 and kwargs.get('plural') and kwargs.get('question'):
        word = make_future(word,
                           negative=kwargs.get('negative', False),
                           question=kwargs.get('question', False),
                           person=kwargs.get('person', 3),
                           plural=kwargs.get('plural')
                           )
    else:
        word = make_future(word,
                           negative=kwargs.get('negative', False),
                           question=kwargs.get('question', False),
                           )

    if kwargs.get('person') == 3 and kwargs.get('plural') and kwargs.get('question'):
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
        word = turkish_string.concat(word, 'y')
        word = make_past_perfect(word,
                                 person=kwargs.get('person', 3)
                                 )
    else:
        if kwargs.get('question', False):
            word = turkish_string.concat(word, 'y')

        word = make_past_perfect(word,
                                 person=kwargs.get('person', 3),
                                 plural=kwargs.get('plural')
                                 )

    return word


# Gelecek zamanın hikayesi
# Yapacaklardı (-acak -tı)
# Example: Somebody will do something in the past
def make_past_future(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('person') == 3 and kwargs.get('plural') and kwargs.get('question', False):
        word = make_future(word,
                           negative=kwargs.get('negative', False),
                           question=kwargs.get('question', False),
                           person=kwargs.get('person', 3),
                           plural=kwargs.get('plural')
                           )
    else:
        word = make_future(word,
                           negative=kwargs.get('negative', False),
                           question=kwargs.get('question', False)
                           )

    if kwargs.get('person') == 3 and kwargs.get('plural') and kwargs.get('question', False):
        word = turkish_string.concat(word, 'm')
        word = turkish_string.concat(word, consonants.MINOR_HARMONY[turkish_string.last_vowel(word)['letter']])
        word = turkish_string.concat(word, 'y')
        word = make_past(word,
                         person=kwargs.get('person', 3)
                         )
    else:
        if kwargs.get('question', False):
            word = turkish_string.concat(word, 'y')

        word = make_past(word,
                         person=kwargs.get('person', 3),
                         plural=kwargs.get('plural')
                         )

    return word
