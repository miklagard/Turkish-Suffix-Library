from turkish_suffix_library import consonants


def is_upper(word):
    word = word.replace('ı', 'i').replace('İ', 'I').replace('ş', 's').replace('Ş', 'S').replace('ğ', 'g'). \
        replace('Ğ', 'G').replace('ü', '').replace('Ü', 'U').replace('ç', 'c').replace('Ç', 'C'). \
        replace('ö', 'o').replace('Ö', 'O')

    return word.isupper()


def make_lower(word):
    return word.replace('İ', 'i').replace('I', 'ı').lower()


def make_upper(word):
    return word.replace('i', 'İ').replace('ı', 'I').upper()


def concat(string_left, string_right):
    if is_upper(string_left):
        return_data = string_left + make_upper(string_right)
    else:
        return_data = string_left + string_right

    return return_data


def from_upper_or_lower(new_word, reference_word):
    if is_upper(reference_word[len(reference_word) - 1]):
        return_data = make_upper(new_word)
    else:
        if is_upper(reference_word[0]):
            return_data = make_upper(new_word[0]) + make_lower(new_word[1:])
        else:
            return_data = make_lower(new_word)

    return return_data


def last_vowel(word):
    word = make_lower(word)

    vowel_count = 0

    return_data = ''

    for letter in word:
        if letter in consonants.FRONT_VOWELS:
            vowel_count = vowel_count + 1
            return_data = {'letter': letter, 'tone': 'front'}
        elif letter in consonants.BACK_VOWELS:
            vowel_count = vowel_count + 1
            return_data = {'letter': letter, 'tone': 'back'}

    # fake return for exception behaviour in Turkish
    if word in consonants.MAJOR_HAMONY_EXCEPTIONS:
        if return_data['letter'] == 'o':
            return_data = {'letter': 'ö', 'tone': 'back'}
        elif return_data['letter'] == 'a':
            return_data = {'letter': 'e', 'tone': 'back'}
        elif return_data['letter'] == '':
            return_data = {'letter': 'ü', 'tone': 'back'}

    if return_data == '':
        return_data = {'letter': '', 'tone': 'back'}

    return_data['vowel_count'] = vowel_count

    return return_data


def change_last_letter(word, new_last_letter):
    return concat(word[0:len(word) - 1], new_last_letter)


def last_letter(word):
    word = make_lower(word)
    return_data = {}
    actual_last_letter = word[len(word) - 1]

    if actual_last_letter == '\'':
        actual_last_letter = word[len(word) - 2]

    return_data['letter'] = actual_last_letter

    if actual_last_letter in consonants.VOWELS:
        return_data['vowel'] = True
        if actual_last_letter in consonants.FRONT_VOWELS and word not in consonants.MAJOR_HAMONY_EXCEPTIONS:
            return_data['front_vowel'] = True
        else:
            return_data['back_vowel'] = True
    else:
        return_data['consonant'] = True

        if actual_last_letter in consonants.DISCONTINUOUS_HARD_CONSONANTS:
            return_data['discontinuous_hard_consonant'] = True
            actual_last_letter = consonants.SOFTEN_DHC[
                consonants.DISCONTINUOUS_HARD_CONSONANTS.index(actual_last_letter)
            ]
            return_data['soften_consonant'] = actual_last_letter

    actual_last_letter = word[len(word) - 1]

    if actual_last_letter == '\'':
        actual_last_letter = word[len(word) - 2]

    if actual_last_letter in consonants.HARD_CONSONANTS and word:
        return_data['hard_consonant'] = True

        if actual_last_letter in consonants.DISCONTINUOUS_HARD_CONSONANTS_AFTER_SUFFIX:
            return_data['discontinuous_hard_consonant_for_suffix'] = True
            actual_last_letter = consonants.SOFTEN_DHC_AFTER_SUFFIX[
                consonants.DISCONTINUOUS_HARD_CONSONANTS_AFTER_SUFFIX.index(actual_last_letter)
            ]
            return_data['soften_consonant_for_suffix'] = actual_last_letter

    return return_data


def soften(parameter_word, proper_noun=False, negative=False):
    word = parameter_word

    actual_last_letter = last_letter(word)
    actual_last_vowel = last_vowel(word)

    if proper_noun:
        word += '\''
    elif 'discontinuous_hard_consonant' in actual_last_letter:
        if actual_last_vowel['vowel_count'] > 1:
            if word not in consonants.ARABIC_K or actual_last_letter.get('letter') != 'k':
                if word in consonants.ARABIC_T or actual_last_letter.get('letter') != 't':
                    word = concat(
                        word[0:len(word) - 1],
                        actual_last_letter['soften_consonant']
                    )

    return word


def exception_missing(parameter_word, proper_noun=False):
    word = parameter_word

    if not proper_noun:
        if make_lower(word) in consonants.EXCEPTION_MISSING:
            word = from_upper_or_lower(
                consonants.EXCEPTION_MISSING[make_lower(word)],
                word
            )

    return word
