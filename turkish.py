#!/usr/bin/python
# -*- coding: utf-8 -*-
from turkish_string import is_upper, make_lower, make_upper, concat, from_upper_or_lower, last_vowel, last_letter
from consonants import EXCEPTION_MISSING, HARD_CONSONANTS, MINOR_HARMONY, EXCEPTION_WORDS, \
    VOWELS, MINOR_HARMONY_FOR_FUTURE


def make_plural(parameter_word: str, **kwargs) -> str:
    word: str = parameter_word

    if 'proper_noun' in kwargs:
        word = f'{word}\''

    if last_vowel(word)['tone'] == 'front':
        return concat(word, 'lar')
    else:
        return concat(word, 'ler')

# -i hali
def make_accusative(parameter_word, **kwargs):  # not finished yet
    # firslty exceptions for o (he/she/it)
    word = parameter_word
    lower_word = make_lower(word)

    proper_noun = kwargs.get('proper_noun', False)

    if lower_word == 'o':
        if proper_noun:
            return_data = from_upper_or_lower('O\'nu', word)
        else:
            return_data = from_upper_or_lower('onu', word)
    else:
        if lower_word in EXCEPTION_MISSING and proper_noun == True:
            word = from_upper_or_lower(EXCEPTION_MISSING[lower_word], word)
            lower_word = make_lower(word)

        actual_last_letter = last_letter(word)
        actual_last_vowel = last_vowel(word)

        if proper_noun:
            word += '\''

        if 'vowel' in actual_last_letter:
            word = concat(word, 'y')
        elif 'discontinuous_hard_consonant' in actual_last_letter and proper_noun == False:
            if actual_last_vowel['vowel_count'] > 1:
                word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

        word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])

        return_data = word

    return return_data


# -e hali
def make_dative(parameter_word: str, **kwargs) -> str:
    # firstly exceptions for ben (I) and you (sen)
    word: str = parameter_word

    proper_noun = kwargs.get('proper_noun', False)

    lower_word = make_lower(word)

    if proper_noun:
        word += '\''

    if lower_word == 'ben' and proper_noun == False:
        return_data = from_upper_or_lower('bana', word)
    elif lower_word == 'sen' and proper_noun == False:
        return_data = from_upper_or_lower('sana', word)
    else:
        if lower_word in EXCEPTION_MISSING and proper_noun == False:
            word = from_upper_or_lower(EXCEPTION_MISSING[lower_word], word)
            lower_word = make_lower(word)

        actual_last_letter = last_letter(word)
        actual_last_vowel = last_vowel(word)

        if 'vowel' in actual_last_letter:
            word = concat(word, 'y')
        elif 'discontinuous_hard_consonant_for_suffix' in actual_last_letter:
            if actual_last_vowel['vowel_count'] > 1 and proper_noun == False:
                word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant_for_suffix'])

        if actual_last_vowel['tone'] == 'front':
            word = concat(word, 'a')
        else:
            word = concat(word, 'e')

        return_data = word

    if return_data.isupper():
        return_data = make_upper(return_data)

    return return_data


# -de hali
def make_genitive(parameter_word: str, **kwargs) -> str:
    word = parameter_word

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)

    lower_word = make_lower(word)
    proper_noun = kwargs.get('proper_noun', False)

    if proper_noun:
        word += '\''

    if lower_word in EXCEPTION_MISSING:
        word = from_upper_or_lower(EXCEPTION_MISSING[lower_word], word)
        lower_word = make_lower(word)

    if 'hard_consonant' in actual_last_letter:
        word = concat(word, 't')
    else:
        word = concat(word, 'd')

    if actual_last_vowel['tone'] == 'front' and not word in EXCEPTION_WORDS:
        word = concat(word, 'a')
    else:
        word = concat(word, 'e')

    return word


# -den hali
def make_ablative(parameter_word, **kwargs):
    word = parameter_word

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)
    proper_noun = kwargs.get('proper_noun', False)

    if proper_noun:
        word += '\''

    if actual_last_letter['letter'] in HARD_CONSONANTS:
        word = concat(word, 't')
    else:
        word = concat(word, 'd')

    if actual_last_vowel['tone'] == 'front':
        word = concat(word, 'an')
    else:
        word = concat(word, 'en')

    return_data = word

    return return_data


# -de hali
def make_locative(parameter_word, **kwargs):
    word = parameter_word

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)
    proper_noun = kwargs.get('proper_noun', False)

    if proper_noun:
        word += '\''

    if actual_last_letter['letter'] in HARD_CONSONANTS:
        word = concat(word, 't')
    else:
        word = concat(word, 'd')

    if actual_last_vowel['tone'] == 'front':
        word = concat(word, 'a')
    else:
        word = concat(word, 'e')

    return_data = word

    return return_data


# İyelik ekleri
def possessive_affix(parameter_word, **kwargs):
    position = kwargs.get('position', 1)
    word = parameter_word

    person = str(kwargs.get('person', 3))
    quantity = kwargs.get('quantity', 'singular')

    proper_noun = kwargs.get('proper_noun', False)

    if not (person == '3' and quantity == 'plural'):
        actual_last_letter = last_letter(word)
        actual_last_vowel = last_vowel(word)

        if proper_noun:
            word += '\''

        elif 'discontinuous_hard_consonant' in actual_last_letter:
            if actual_last_vowel['vowel_count'] > 1:
                word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])
           
            if make_lower(word) in EXCEPTION_MISSING:
                word = from_upper_or_lower(EXCEPTION_MISSING[make_lower(word)], word)

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)

    last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

    minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]

    if quantity == 'singular':
        if not last_letter_is_vowel:
            word = concat(word, minor_harmony_letter)

        if person == '1':
            word = concat(word, 'm')

        elif person == '2':
            word = concat(word, 'n')

        elif person == '3':
            word = concat(word, 's')
            word = concat(word, minor_harmony_letter)
    else:
        if person == '1':
            if not last_letter_is_vowel :
                word = concat(word, minor_harmony_letter)

            word = concat(word, 'm')
            word = concat(word, minor_harmony_letter)
            word = concat(word, 'z')

        elif person == '2':
            if not last_letter_is_vowel:
                word = concat(word, minor_harmony_letter)

            word = concat(word, 'n')
            word = concat(word, minor_harmony_letter)
            word = concat(word, 'z')
        else:

            if make_lower(word) == 'ism':
                word = from_upper_or_lower('isim', word)

            word = make_plural(word)
            word = concat(word, minor_harmony_letter)

    return word

# Mastar eski
def make_infinitive(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('negative', False):
        if last_vowel(word)['tone'] == 'front':
            return_data = concat(word, 'mamak')
        else:
            return_data = concat(word, 'memek')
    else:
        if last_vowel(word)['tone'] == 'front':
            return_data = concat(word, 'mak')
        else:
            return_data = concat(word, 'mek')

    return return_data


# Şimdiki zaman
#	   * arıyorum
#	   * For alternative usage of present continuous tense, check the function make_present_continuous_alternative
def make_present_continuous(parameter_word, **kwargs):
    word = parameter_word

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)

    last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

    if not kwargs.get('negative', False):
        # if 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
        #	word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

        if word == 'git':
            word = 'gid'

        if last_letter_is_vowel:
            word = concat(word[:-1], MINOR_HARMONY[word[-1]])
        else:
            word = concat(word, MINOR_HARMONY[actual_last_vowel['letter']])
    else:
        word = concat(word, 'm')
        word = concat(word, MINOR_HARMONY[actual_last_vowel['letter']])

    word = concat(word, 'yor')

    if kwargs.get('question', False):
        if kwargs.get('quantity', 'singular') == 'singular':
            if kwargs.get('person', 3) == 1:
                word = concat(word, ' muyum')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, ' musun')
            elif kwargs.get('person', 3) == 3:
                word = concat(word, ' mu')
        elif kwargs.get('quantity', 'singular') == 'plural':
            if kwargs.get('person', 3) == 1:
                word = concat(word, ' muyuz')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, ' musunuz')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
                word = concat(word, ' m')
                if last_vowel(word)['tone'] == 'front':
                    word = concat(word, 'ı')
                else:
                    word = concat(word, 'i')
    else:
        if kwargs.get('quantity', 'singular') == 'singular':
            if kwargs.get('person', 3) == 1:
                word = concat(word, 'um')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 'sun')
        elif kwargs.get('quantity', 'singular') == 'plural':
            if kwargs.get('person', 3) == 1:
                word = concat(word, 'uz')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 'sunuz')
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
        if last_vowel(word)['tone'] == 'front':
            word = concat(word, 'ma')
        else:
            word = concat(word, 'me')

    word = make_infinitive(word)

    if last_vowel(word)['tone'] == 'front':
        word = concat(word, 'ta')
    else:
        word = concat(word, 'te')

    if not kwargs.get('question', False):
        if kwargs.get('quantity', 'singular') == 'singular':
            if kwargs.get('person', 3) == 1:
                word = concat(word, 'y')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 's')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'n')
        elif kwargs.get('quantity', 'singular') == 'plural':
            if kwargs.get('person', 3) == 1:
                word = concat(word, 'y')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 's')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'n')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
    elif kwargs.get('question', False):
        if kwargs.get('quantity', 'singular') == 'singular':
            if kwargs.get('person', 3) == 1:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'y')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 's')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'n')
        elif kwargs.get('quantity', 'singular') == 'plural':
            if kwargs.get('person', 3) == 1:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'y')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 's')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'n')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])

    return word


# Geniş zaman
def make_present_simple(parameter_word, **kwargs):
    word = parameter_word
    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)

    last_letter_is_vowel = actual_last_letter['letter'] in VOWELS

    minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]
    minor_harmony_letterFF = MINOR_HARMONY_FOR_FUTURE[actual_last_vowel['letter']]
    minorHA = MINOR_HARMONY_FOR_FUTURE[minor_harmony_letter]

    if not kwargs.get('negative', False):
        if 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
            word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])
        if word == 'git':
            word = 'gid'

    if kwargs.get('question', False):
        if not kwargs.get('negative', False):
            if word in ['al', 'kal']:
                word = concat(word, 'ır')
            else:
                if not last_letter_is_vowel:
                    word = concat(word, minor_harmony_letterFF)

                word = concat(word, 'r')

            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'y')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 's')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'n')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
            elif kwargs.get('quantity', 'singular') == 'plural':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'y')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 's')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'n')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = make_plural(word)
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
        elif kwargs.get('negative', False) == True:
            actual_last_vowel = last_vowel(word)

            if last_vowel(word)['tone'] == 'front':
                minor_harmony_letterFF = 'a'
            else:
                minor_harmony_letterFF = 'e'

            word = concat(word, 'm')
            word = concat(word, minor_harmony_letterFF)
            word = concat(word, 'z')

            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'y')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 's')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'n')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
            elif kwargs.get('quantity', 'singular') == 'plural':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'y')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 's')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'n')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = make_plural(word)
                    word = concat(word, ' ')
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letter)
    elif not kwargs.get('question', False) :
        if not kwargs.get('negative', False):
            if word in ['al', 'kal']:
                word = concat(word, 'ır')
            else:
                if not last_letter_is_vowel:
                    word = concat(word, minor_harmony_letterFF)

                word = concat(word, 'r')

            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 's')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'n')
            elif kwargs.get('quantity', 'singular') == 'plural':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 's')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'n')
                    word = concat(word, minor_harmony_letter)
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = make_plural(word)
        elif kwargs.get('negative', False) == True:
            if last_vowel(word)['tone'] == 'front':
                minor_harmony_letterFF = 'a'
            else:
                minor_harmony_letterFF = 'e'

            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letterFF)
                    word = concat(word, 'm')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letterFF)
                    word = concat(word, 'z')
                    word = concat(word, 's')
                    word = concat(word, MINOR_HARMONY[minorHA])
                    word = concat(word, 'n')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letterFF)
                    word = concat(word, 'z')
            elif kwargs.get('quantity', 'singular') == 'plural':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letterFF)
                    word = concat(word, 'y')
                    word = concat(word, MINOR_HARMONY[minorHA])
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letterFF)
                    word = concat(word, 'z')
                    word = concat(word, 's')
                    word = concat(word, MINOR_HARMONY[minorHA])
                    word = concat(word, 'n')
                    word = concat(word, MINOR_HARMONY[minorHA])
                    word = concat(word, 'z')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'm')
                    word = concat(word, minor_harmony_letterFF)
                    word = concat(word, 'z')
                    word = make_plural(word)

    return word


# Gelecek zaman
def make_future(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('negative', False):
        if last_vowel(word)['tone'] == 'front':
            word = concat(word, 'ma')
        else:
            word = concat(word, 'me')

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)

    if 'vowel' in actual_last_letter:
        if word == 'de':
            word = 'di'
        elif word == 'ye':
            word = 'yi'

        word = concat(word, 'y')
    elif 'discontinuous_hard_consonant' in actual_last_letter \
            and actual_last_vowel['vowel_count'] > 1 \
            and not kwargs.get('negative', False):
        word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

    if not kwargs.get('negative', False):
        if word == 'git':
            word = 'gid'

    if kwargs.get('question', False):
        if last_vowel(word)['tone'] == 'front':
            if kwargs.get('person', 3) == 3 and kwargs.get('quantity', 'singular') == 'plural':
                word = concat(word, 'acaklar ')
            else:
                word = concat(word, 'acak ')

            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'mıyım')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'mısın')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'mı')
            elif kwargs.get('quantity', 'singular') == 'plural':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'mıyız')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'mısınız')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'mı')
        else:
            if kwargs.get('person', 3) == 3 and kwargs.get('quantity', 'singular') == 'plural':
                word = concat(word, 'ecekler ')
            else:
                word = concat(word, 'ecek ')

            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'miyim')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'misin')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'mi')
            elif kwargs.get('quantity', 'singular'):
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'miyiz')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'misiniz')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'mi')
    elif not kwargs.get('question', False):
        if last_vowel(word)['tone'] == 'front':
            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'acağım')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'acaksın')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'acak')
            elif kwargs.get('quantity', 'singular') == 'plural':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'acağız')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'acaksınız')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'acaklar')
        else:
            if kwargs.get('quantity', 'singular') == 'singular':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'eceğim')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'eceğiz')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'ecek')
            elif kwargs.get('quantity', 'plural') == 'plural':
                if kwargs.get('person', 3) == 1:
                    word = concat(word, 'eceğiz')
                elif kwargs.get('person', 3) == 2:
                    word = concat(word, 'eceksiniz')
                elif kwargs.get('person', 3) == 3:
                    word = concat(word, 'ecekler')

    return word


# Not the same with English past perfect tense
# This usage is for past tense of an action which is heared/learned but not witnessed.
# mişli geçmiş zaman veya öğrenilen geçmiş zaman
def make_past_perfect(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('negative', False):
        word = concat(word, 'm')

        if last_vowel(word)['tone'] == 'front':
            word = concat(word, 'a')
        else:
            word = concat(word, 'e')

    actual_last_vowel = last_vowel(word)
    minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]

    word = concat(word, 'm')
    word = concat(word, minor_harmony_letter)
    word = concat(word, 'ş')

    if not kwargs.get('question', False):
        if kwargs.get('quantity', 'singular') == 'singular':
            if kwargs.get('person', 3) == 1:
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 's')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'n')
        elif kwargs.get('quantity', 'singular') == 'plural':
            if kwargs.get('person', 3) == 1:
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 's')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'n')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
    elif kwargs.get('question', False):
        if kwargs.get('quantity', 'singular') == 'singular':
            if kwargs.get('person', 3) == 1:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'y')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 's')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'n')
            elif kwargs.get('person', 3) == 3:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor_harmony_letter)
        elif kwargs.get('quantity', 'singular') == 'plural':
            if kwargs.get('person', 3) == 1:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'y')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 's')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'n')
                word = concat(word, minor_harmony_letter)
                word = concat(word, 'z')
            elif kwargs.get('person', 3) == 3:
                word = make_plural(word)
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor_harmony_letter)

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

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)
    get_aux_last_vowel = last_vowel(kwargs.get('auxiliary'))
    minor_harmony_letter = MINOR_HARMONY[actual_last_vowel['letter']]
    actual_last_letter = last_letter(word)

    if 'vowel' in actual_last_letter:
        word = concat(word, 'y')
    elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
        word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

    if not kwargs.get('negative', False):
        if kwargs.get('auxiliary') in ['ver', 'koy']:
            word = concat(word, minor_harmony_letter)
        elif actual_last_vowel['tone'] == 'front':
            word = concat(word, 'a')
        else:
            word = concat(word, 'e')

        word = concat(word, kwargs.get('auxiliary'))
    if kwargs.get('negative', False):
        if kwargs.get('auxiliary') == 'bil':
            if actual_last_vowel['tone'] == 'front':
                word = concat(word, 'ama')
            else:
                word = concat(word, 'eme')
        else:
            if kwargs.get('auxiliary') in ['ver', 'koy']:
                word = concat(word, minor_harmony_letter)
            elif actual_last_vowel['tone'] == 'front':
                word = concat(word, 'a')
            else:
                word = concat(word, 'e')

            word = concat(word, kwargs.get('auxiliary'))

            if get_aux_last_vowel['tone'] == 'front':
                word = concat(word, 'a')
            else:
                word = concat(word, 'e')

    return word


# Gereklilik kipi (-meli, -malı)
def make_must(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = last_vowel(word)

    if actual_last_vowel['tone'] == 'front':
        letterA = 'a'
        letterI = 'ı'
    else:
        letterA = 'e'
        letterI = 'i'

    if kwargs.get('negative', False):
        word = concat(word, 'm')
        word = concat(word, letterA)

    word = concat(word, 'm')
    word = concat(word, letterA)
    word = concat(word, 'l')
    word = concat(word, letterI)

    if kwargs.get('person', 3) == 3 and kwargs.get('quantity', 'singular') == 'plural':
        word = make_plural(word)

    if kwargs.get('question', False):
        word = concat(word, ' ')
        word = concat(word, 'm')
        word = concat(word, letterI)

    if kwargs.get('quantity', 'singular') == 'singular':
        if kwargs.get('person', 3) == 1:
            word = concat(word, 'y')
            word = concat(word, letterI)
            word = concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, 's')
            word = concat(word, letterI)
            word = concat(word, 'n')
    elif kwargs.get('quantity', 'singular') == 'plural':
        if kwargs.get('person', 3) == 1:
            word = concat(word, 'y')
            word = concat(word, letterI)
            word = concat(word, 'z')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, 's')
            word = concat(word, letterI)
            word = concat(word, 'n')
            word = concat(word, letterI)
            word = concat(word, 'z')

    return word


# Dilek - Şart kipi (-se, -sa)
def make_wish_condition(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = last_vowel(word)

    if actual_last_vowel['tone'] == 'front':
        letterA = 'a'
        letterI = 'ı'
    else:
        letterA = 'e'
        letterI = 'i'

    if kwargs.get('negative', False):
        word = concat(word, 'm')
        word = concat(word, letterA)

    word = concat(word, 's')
    word = concat(word, letterA)

    if kwargs.get('quantity', 'singular') == 'singular':
        if kwargs.get('person', 3) == 1:
            word = concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, 'n')
    else:  # Plural
        if kwargs.get('person', 3) == 1:
            word = concat(word, 'k')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, 'n')
            word = concat(word, letterI)
            word = concat(word, 'z')
        elif kwargs.get('person', 3) == 3:
            word = make_plural(word)

    if kwargs.get('question', False):
        word = concat(word, ' ')
        word = concat(word, 'm')
        word = concat(word, letterI)

    return word


# İstek kipi (geleyim, gelesin, gele, gelelim, gelesiniz, geleler)
def make_wish(parameter_word, **kwargs):
    word = parameter_word
    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)

    if actual_last_vowel['tone'] == 'front':
        letterA = 'a'
        letterI = 'ı'
    else:
        letterA = 'e'
        letterI = 'i'

    if kwargs.get('negative', False):
        word = concat(word, 'm')
        word = concat(word, letterA)
        word = concat(word, 'y')
        word = concat(word, letterA)
    else:
        if word == 'de':
            word = 'di'
        elif word == 'ye':
            word = 'yi'

        if word == 'git':
            word = 'gid'

        if 'vowel' in actual_last_letter:
            word = concat(word, 'y')
        elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1:
            word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

        word = concat(word, letterA)

    if kwargs.get('quantity', 'singular') == 'singular':
        if kwargs.get('person', 3) == 1:
            word = concat(word, 'y')
            word = concat(word, letterI)
            word = concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, 's')
            word = concat(word, letterI)
            word = concat(word, 'n')
    else:
        if kwargs.get('person', 3) == 1:
            word = concat(word, 'l')
            word = concat(word, letterI)
            word = concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, 's')
            word = concat(word, letterI)
            word = concat(word, 'n')
            word = concat(word, letterI)
            word = concat(word, 'z')
        elif kwargs.get('person', 3) == 3:
            word = make_plural(word)

    if kwargs.get('question', False):
        word = concat(word, ' ')
        word = concat(word, 'm')
        word = concat(word, letterI)

    return word


# Make the verb command
# Usage: do it, break it, come!
# As different from English, command optative mood is valid also for 3rd person in Turkish
#    but never for 1st person.
# For the second person, there is no suffix
def make_command(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = last_vowel(word)

    # MINOR_HARMONY[last_vowel(word)['letter']]

    if kwargs.get('negative', False):
        word = concat(word, 'm')
        if actual_last_vowel['tone'] == 'front':
            word = concat(word, 'a')
        else:
            word = concat(word, 'e')

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)
    minor = MINOR_HARMONY[last_vowel(word)['letter']]

    if kwargs.get('quantity', 'singular') == 'singular':
        if kwargs.get('person', 2) == 3:
            word = concat(word, 's')
            word = concat(word, minor)
            word = concat(word, 'n')

            if kwargs.get('question', False):
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor)
    else:  # Plural
        if kwargs.get('person', 2) == 2:
            if word == 'de':
                word = 'di'
            elif word == 'ye':
                word = 'yi'

            if 'vowel' in actual_last_letter:
                word = concat(word, 'y')
            elif 'discontinuous_hard_consonant' in actual_last_letter and actual_last_vowel['vowel_count'] > 1 and kwargs.get(
                    'negative', False) == False:
                word = concat(word[0:len(word) - 1], actual_last_letter['soften_consonant'])

            if word == 'git':
                word = 'gid'

            word = concat(word, minor)
            word = concat(word, 'n')

            if kwargs.get('formal', False):
                word = concat(word, minor)
                word = concat(word, 'z')
        elif kwargs.get('person', 2) == 3:
            word = concat(word, 's')
            word = concat(word, minor)
            word = concat(word, 'n')
            word = make_plural(word)
            if kwargs.get('question', False):
                word = concat(word, ' ')
                word = concat(word, 'm')
                word = concat(word, minor)

    return word


# Past tense
# -di'li geçmiş zama
def make_past(parameter_word, **kwargs):
    word = parameter_word
    actual_last_vowel = last_vowel(word)
    actual_last_letter = last_letter(word)
    minor = MINOR_HARMONY[last_vowel(word)['letter']]

    if kwargs.get('negative', False):
        word = concat(word, 'm')
        if actual_last_vowel['tone'] == 'front':
            word = concat(word, 'a')
        else:
            word = concat(word, 'e')

    actual_last_vowel = last_vowel(word)
    actual_last_letter = last_letter(word)
    minor = MINOR_HARMONY[last_vowel(word)['letter']]

    if 'hard_consonant' not in actual_last_letter or 'vowel' in actual_last_letter:
        ps = 'd'
    else:
        ps = 't'

    if kwargs.get('quantity', 'singular') == 'singular':
        if kwargs.get('person', 3) == 1:
            word = concat(word, ps)
            word = concat(word, minor)
            word = concat(word, 'm')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, ps)
            word = concat(word, minor)
            word = concat(word, 'n')
        elif kwargs.get('person', 3) == 3:
            word = concat(word, ps)
            word = concat(word, minor)
    else:  # plural
        if kwargs.get('person', 3) == 1:
            word = concat(word, ps)
            word = concat(word, minor)
            word = concat(word, 'k')
        elif kwargs.get('person', 3) == 2:
            word = concat(word, ps)
            word = concat(word, minor)
            word = concat(word, 'n')
            word = concat(word, minor)
            word = concat(word, 'z')
        elif kwargs.get('person', 3) == 3:
            word = concat(word, ps)
            word = concat(word, minor)
            word = make_plural(word)

    if kwargs.get('question', False) :
        actual_last_vowel = last_vowel(word)
        minor = MINOR_HARMONY[last_vowel(word)['letter']]

        word = concat(word, ' ')
        word = concat(word, 'm')
        word = concat(word, minor)

    return word


# Bilinen geçmiş zamanın hikayesi
# yaptıydım, yaptıydın, yaptıydı, yaptıydık, yaptıydınız, yaptıydılar
# yaptı mıydım, yaptı mıydın, yaptı mıydı, yaptı mıydık, yaptı mıydınız, yaptılar mıydı
def make_past_past(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('person', 3) == 3 \
            and kwargs.get('question', False) \
            and kwargs.get('quantity', 'singular') == 'plural':
        word = make_past(word,
            person=3,
            quantity='singular',
            negative=kwargs.get('negative', False),
        )
    else:
        word = make_past(word,
            person=3,
            quantity='singular',
            negative=kwargs.get('negative', False),
            question=kwargs.get('question', False)
        )

        word = concat(word, 'y')

    if kwargs.get('person', 3) == 3 \
            and kwargs.get('question', False) \
            and kwargs.get('quantity', 'singular') == 'plural':
        word = make_plural(word)

        word = concat(word, ' ')
        word = concat(word, 'm')
        if last_vowel(word)['tone'] == 'front':
            word = concat(word, 'ı')
        else:
            word = concat(word, 'i')
    else:
        word = make_past(word,
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
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

        word = concat(word, 'y')

        word = make_wish_condition(word,
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
        )
    else:
        word = make_wish_condition(word,
            person=3,
            negative=kwargs.get('negative', False)
        )

        if kwargs.get('person', 3) == 3 and kwargs.get('quantity', 'singular') == 'plural':
            word = make_plural(word)

        if last_vowel(word)['tone'] == 'front':
            letter = 'ı'
        else:
            letter = 'i'

        word = concat(word, ' ')
        word = concat(word, 'm')
        word = concat(word, letter)
        word = concat(word, 'y')
        word = concat(word, 'd')
        word = concat(word, letter)

        if kwargs.get('quantity', 'singular') == 'singular':
            if kwargs.get('person', 3) == 1:
                word = concat(word, 'm')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 'n')
        else:
            if kwargs.get('person', 3) == 1:
                word = concat(word, 'k')
            elif kwargs.get('person', 3) == 2:
                word = concat(word, 'n')
                word = concat(word, letter)
                word = concat(word, 'z')
    return word


# Öğrenilen geçmiş zamanın hikayesi
# Yapmışlardı (-miş -di)
# Example: It is heard by someone that somebody did something in the past
def make_past_past_perfect(parameter_wrod, **kwargs):
    word = parameter_wrod

    if kwargs.get('person') == 3 and kwargs.get('quantity') == 'plural' and kwargs.get('question', False):
        word = make_past_perfect(word,
            negative=kwargs.get('negative', False),
            question=kwargs.get('question', False),
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
        )
    else:
        word = make_past_perfect(word,
            negative=kwargs.get('negative', False),
            question=kwargs.get('question', False),
        )

    if kwargs.get('question', False):
        word = concat(word, 'y')

    if kwargs.get('person') == 3 and kwargs.get('quantity') == 'plural' and kwargs.get('question', False):
        word = make_past(word,
            person=kwargs.get('person', 3)
        )
    else:
        word = make_past(word,
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
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
            quantity=kwargs.get('quantity', 'singular'),
            question=kwargs.get('question', False)
        )
    else:
        if kwargs.get('person', 3) == 3 and kwargs.get('quantity', 'singular') == 'plural':
            word = make_plural(word)
            minor = MINOR_HARMONY[last_vowel(word)['letter']]

            word = concat(word, ' ')
            word = concat(word, 'm')
            word = concat(word, minor)
            word = concat(word, 'y')
            word = concat(word, 'm')
            word = concat(word, minor)
            word = concat(word, 'ş')
        else:
            minor = MINOR_HARMONY[last_vowel(word)['letter']]
            word = concat(word, ' ')
            word = concat(word, 'm')
            word = concat(word, minor)
            word = concat(word, 'y')
            word = make_past_perfect(word,
                person=kwargs.get('person', 3),
                quantity=kwargs.get('quantity', 'singular')
            )
    return word


# Gelecek zamanın rivayeti
# Yapacaklardı (-acak -mış)
# Example: It is heard by someone that somebody will do something in the past
def make_past_perfect_future(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('person') == 3 and kwargs.get('quantity') == 'plural' and kwargs.get('question', False):
        word = make_future(word,
            negative=kwargs.get('negative', False),
            question=kwargs.get('question', False),
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
        )
    else:
        word = make_future(word,
            negative=kwargs.get('negative', False),
            question=kwargs.get('question', False),
        )

    if kwargs.get('person') == 3 and kwargs.get('quantity') == 'plural' and kwargs.get('question', False):
        word = concat(word, 'm')
        word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
        word = concat(word, 'y')
        word = make_past_perfect(word,
            person=kwargs.get('person', 3)
        )
    else:
        if kwargs.get('question', False):
            word = concat(word, 'y')

        word = make_past_perfect(word,
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
        )

    return word


# Gelecek zamanın hikayesi
# Yapacaklardı (-acak -tı)
# Example: Somebody will do something in the past
def make_past_future(parameter_word, **kwargs):
    word = parameter_word

    if kwargs.get('person') == 3 and kwargs.get('quantity') == 'plural' and kwargs.get('question', False):
        word = make_future(word,
            negative=kwargs.get('negative', False),
            question=kwargs.get('question', False),
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
        )
    else:
        word = make_future(word,
            negative=kwargs.get('negative', False),
            question=kwargs.get('question', False)
        )

    if kwargs.get('person') == 3 and kwargs.get('quantity') == 'plural' and kwargs.get('question', False):
        word = concat(word, 'm')
        word = concat(word, MINOR_HARMONY[last_vowel(word)['letter']])
        word = concat(word, 'y')
        word = make_past(word,
            person=kwargs.get('person', 3)
        )
    else:
        if kwargs.get('question', False):
            word = concat(word, 'y')

        word = make_past(word,
            person=kwargs.get('person', 3),
            quantity=kwargs.get('quantity', 'singular')
        )

    return word

