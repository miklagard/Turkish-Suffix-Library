import inspect
from turkish_suffix_library.turkish_class import TurkishClass


class Turkish(TurkishClass):
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

    def plural(self, **kwargs):
        self.concat(f'l{self.letter_a()}r')

        return self.common_return(**kwargs)

    def accusative(self, **kwargs):
        """
            -i hali
            (not finished yet)
        """

        proper_noun = kwargs.get('proper_noun')

        if not self.apostrophes(**kwargs):
            self.word = self.exception_missing(proper_noun)

        if self.last_letter_is_vowel():
            if self.n_connector():
                self.concat('n')
            else:
                self.concat('y')

        if not proper_noun:
            self.ng_change()
            self.soften()

        self.concat(self.minor())

        return self.common_return(**kwargs)

    def dative(self, **kwargs):
        """
            -e hali
        """

        # firstly exceptions for ben (I) and you (sen)

        lower_word = self.lower()
        letter_a = self.letter_a()

        self.apostrophes(**kwargs)
        proper_noun = kwargs.get('proper_noun')

        if lower_word == 'ben' and not proper_noun:
            self.word = self.from_upper_or_lower('bana')
        elif lower_word == 'sen' and not proper_noun:
            self.word = self.from_upper_or_lower('sana')
        else:
            if not proper_noun:
                self.ng_change()
                self.word = self.exception_missing(proper_noun)

            if self.last_letter_is_vowel():
                if self.n_connector():
                    self.concat('n')
                else:
                    self.concat('y')

            if not proper_noun:
                self.soften()

            self.concat(letter_a)

        return self.common_return(**kwargs)

    def ablative(self, **kwargs):
        """
            -den hali
        """
        ae = self.letter_a()
        self.apostrophes(**kwargs)

        if self.n_connector():
            self.concat('n')

        self.if_ends_with_hard('t', 'd')

        self.concat(f'{ae}n')

        return self.common_return(**kwargs)

    def locative(self, **kwargs):
        """
            -de hali
        """
        letter_a = self.letter_a()

        self.apostrophes(**kwargs)

        if self.n_connector():
            self.concat('n')

        self.if_ends_with_hard('t', 'd')

        self.concat(letter_a)

        return self.common_return(**kwargs)

    def genitive(self, **kwargs):
        """
            Iyelik aitlik eki
            Ayakkabinin
            Elif'in
        """

        last_letter_is_vowel = self.last_letter_is_vowel()
        minor = self.minor()
        proper_noun = self.apostrophes(**kwargs)

        if proper_noun:
            if last_letter_is_vowel:
                self.concat('n')
        else:
            self.ng_change()

            if last_letter_is_vowel:
                self.concat('n')
            else:
                self.soften()

                self.exception_missing(proper_noun)

        self.concat(f'{minor}n')

        return self.common_return(**kwargs)

    def equalative(self, **kwargs):
        """
            Ismin esitlik hali: -ce, -ca etc.
        """

        letter_a = self.letter_a()
        self.if_ends_with_hard('ç', 'c')
        self.concat(letter_a)

        return self.common_return(**kwargs)

    def instrumental(self, **kwargs):
        """
            Ismin vasıta hali: -le, -la, -yle, -yla
        """
        is_vowel = self.last_letter_is_vowel()

        ae = self.letter_a()

        self.apostrophes(**kwargs)

        if is_vowel:
            self.concat('y')

        self.concat(f'l{ae}')

        return self.common_return(**kwargs)

    def possessive(self, **kwargs):
        """
            Iyelik tamlanan eki
            Ayakkabısı
        """
        person = str(kwargs.get('person', 3))
        plural = kwargs.get('plural', False)

        minor = self.minor()

        proper_noun = self.apostrophes(**kwargs)

        if not (person == '3' and plural):
            if not proper_noun:
                self.ng_change()

                self.soften()

                self.exception_missing(proper_noun)

        if not plural:
            if person == '1':
                if not self.last_letter_is_vowel():
                    self.concat(minor)

                self.concat('m')

            elif person == '2':
                if not self.last_letter_is_vowel():
                    self.concat(minor)

                self.concat('n')

            elif person == '3':
                if self.last_letter_is_vowel():
                    self.concat('s')

                self.concat(minor)
        else:
            if person == '1':
                if not self.last_letter_is_vowel():
                    self.concat(minor)

                self.concat(f'm{minor}z')

            elif person == '2':
                if not self.last_letter_is_vowel():
                    self.concat(minor)

                self.concat(f'n{minor}z')
            else:
                if self.lower() == 'ism':
                    self.from_upper_or_lower('isim')

                self.concat(f'l{self.letter_a()}r')
                self.concat(self.minor())

        return self.common_return(**kwargs)

    def relative_pronoun(self, **kwargs):
        proper_noun = kwargs.get('proper_noun', False)
        self.genitive(proper_noun=proper_noun)
        self.concat('ki')

        return self.common_return(**kwargs)

    def privative(self, **kwargs):
        minor = self.minor()
        self.concat(f's{minor}z')
        return self.common_return(**kwargs)

    def ordinal(self, **kwargs):
        """
            Ordinal numbers: One->First, Two->Second etc.

            bir-i-nci, iki-nci...

            This rule is also valid for words:
            * son (last) -> sonuncu
            * ilk (first) -> ilkinci (ilk already means "first" but you can still put this suffix)
        """

        minor = self.minor()

        self.if_ends_with('t', 'd')

        if not self.last_letter_is_vowel():
            self.concat(minor)

        self.concat(f'nc{minor}')

        return self.common_return(**kwargs)

    def distributive(self, **kwargs):
        """
            Distributive numbers: One->One each, Two->Two each.

            bir-er, iki-şer...
        """

        ae = self.letter_a()

        self.if_ends_with('t', 'd')

        if self.last_letter_is_vowel():
            self.concat('ş')

        self.concat(f'{ae}r')

        return self.common_return(**kwargs)

    def copula_present(self, **kwargs):
        """
            kedidir
            kedi degildir
        """

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)

        if negative:
            self.concat(' değil')

            if question:
                self.concat(' mi')

            letter_y = ''
            if self.last_letter_is_vowel():
                letter_y = 'y'

            self.if_condition(
                person, plural,
                [1, False, f'{letter_y}im'],
                [2, False, 'sin'],
                [3, False, 'dir'],
                [1, True, f'{letter_y}iz'],
                [2, True, 'siniz'],
                [3, True, 'ler'],
            )
        else:
            if question:
                self.concat(f' m{self.minor()}')
            else:
                if not self.apostrophes(**kwargs):
                    if person == 1 and not plural:
                        self.soften()
                    elif person == 1 and plural:
                        self.soften()

            letter_y = ''

            if self.last_letter_is_vowel():
                letter_y = 'y'

            self.if_condition(
                person, plural,
                [1, False, f'{letter_y}{self.minor()}m'],
                [2, False, f's{self.minor()}n'],
                [3, False, f'{self.letter_d()}{self.minor()}r'],
                [1, True, f'{letter_y}{self.minor()}z'],
                [2, True, f's{self.minor()}n{self.minor()}z'],
                [3, True, f'{self.letter_d()}{self.minor()}r'],
            )

        return self.common_return(**kwargs)

    def copula_definite_past(self, **kwargs):
        """
            kediydi
            kedi degildi
        """

        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        if negative:
            self.concat(' değil')

            if question:
                self.concat(' miy')
        else:
            if question:
                self.concat(f' m{self.minor()}')
            else:
                self.apostrophes(**kwargs)

            self.if_ends_with_vowel('y')

        self.concat(f'{self.letter_d()}{self.minor()}')

        self.if_condition(
            person, plural,
            [1, False, 'm'],
            [2, False, 'n'],
            [1, True, 'k'],
            [2, True, f'n{self.minor()}z'],
            )

        return self.common_return(**kwargs)

    def copula_indefinite_past(self, **kwargs):
        """
            kediymis
            kedi degilmis
        """

        negative = kwargs.get('negative')
        question = kwargs.get('question')
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        if negative:
            if question:
                self.concat(' değil miymiş')
            else:
                self.concat(' değilmiş')
        else:
            if question:
                self.concat(f' m{self.minor()}')
            else:
                self.apostrophes(**kwargs)

            self.if_ends_with_vowel('y')

            self.concat(f'm{self.minor()}ş')

        self.if_condition(
            person, plural,
            [1, False, 'im'],
            [2, False, 'sin'],
            [1, True, 'iz'],
            [2, True, 'tiniz'],
        )
        return self.common_return(**kwargs)

    def infinitive(self, **kwargs):
        """
            Mastar eki
        """

        ae = self.letter_a()

        from_able = self.is_from_able()

        if kwargs.get('negative', False) and not from_able:
            self.concat(f'm{ae}')

        self.concat(f'm{ae}k')

        return self.common_return(**kwargs)
    
    def present_continuous_simple(self, **kwargs):
        """
            Şimdiki zaman
            Example: arıyorum
            Note: For alternative usage of present continuous tense, check the function
                    present_continuous_simple_alternative
        """
        from_able = self.is_from_able()
        negative = kwargs.get('negative', False)
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        question = kwargs.get('question', False)

        if not negative:
            self.harden_verb()
            minor = self.minor()

            if self.last_letter_is_vowel():
                self.word = self.word[:-1]
                self.concat(minor)
            else:
                self.concat(minor)
        else:
            minor = self.minor()

            if not from_able:
                self.concat('m')
            else:
                self.word = self.word[:-1]

            self.concat(minor)

        self.concat('yor')

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        if question:
            self.concat(f' m{self.minor()}')

            self.if_condition(
                person, plural,
                [1, False, f'y{self.minor()}m'],
                [2, False, f's{self.minor()}n'],
                [1, True, f'y{self.minor()}z'],
                [2, True, f's{self.minor()}n{self.minor()}z'],
            )
        else:
            self.if_condition(
                person, plural,
                [1, False, f'{self.minor()}m'],
                [2, False, f's{self.minor()}n'],
                [1, True, f'{self.minor()}z'],
                [2, True, f'{self.minor()}n{self.minor()}z']
            )

        return self.common_return(**kwargs)
    
    def present_continuous_simple_alternative(self, **kwargs):
        """
            There are two ways to express 'present continuous tense in Turkish '
            This kind is not common in daily Turkish usage anymore
            Example:
                * aramaktayım
                * yapmaktayım
        """
        letter_a = self.letter_a()

        from_able = self.is_from_able()

        if kwargs.get('negative', False) and not from_able:
            self.concat(f'm{letter_a}')

        self.word = self.infinitive().to_string()

        self.concat(f't{letter_a}')

        question = kwargs.get('question', False)
        plural = kwargs.get('plural', False)
        person = kwargs.get('person', 3)

        if question and not (person == 3 and plural):
            self.concat(f' m{self.minor()}')

        self.if_condition(
            person, plural,
            [1, False, f'y{self.minor()}m'],
            [2, False, f's{self.minor()}n'],
            [1, True, f'y{self.minor()}z'],
            [2, True, f's{self.minor()}n{self.minor()}z'],
            [3, True, f'l{letter_a}r']
        )

        if question and person == 3 and plural:
            self.concat(f' m{self.minor()}')

        return self.common_return(**kwargs)
    
    def simple_tense(self, **kwargs):
        """
            Geniş zaman (aorist)
        """
        from_able = self.is_from_able()
        question = kwargs.get('question', False)
        negative = kwargs.get('negative', False)
        plural = kwargs.get('plural', False)
        person = kwargs.get('person', 3)

        letter_a = self.letter_a()

        if not negative:
            self.soften()
            self.harden_verb()

            if not self.last_letter_is_vowel():
                if self.verb_in_minor_harmony_exception():
                    self.concat(self.minor())
                elif self.count_syllable() > 1:
                    self.concat(self.minor())
                else:
                    self.concat(self.harmony_for_present_first())

            self.concat('r')

            if question:
                self.if_condition(
                    person, plural,
                    [1, False, f' m{self.minor()}y'],
                    [2, False, f' m{self.minor()}'],
                    [1, True, f' m{self.minor()}y'],
                    [2, True, f' m{self.minor()}'],
                )

            self.if_condition(
                person, plural,
                [1, False, self.minor()],
                [1, True, self.minor()],
            )
        else:
            if not from_able:
                self.concat(f'm{letter_a}')

            if question:
                self.if_condition(
                    person, plural,
                    [2, False, f'z m{self.minor()}'],
                    [3, False, 'z'],
                    [1, True, f'z m{self.minor()}y{self.minor()}'],
                    [2, True, f'z m{self.minor()}'],
                )
            else:
                self.if_condition(
                    person, plural,
                    [2, False, 'z'],
                    [3, False, 'z'],
                    [1, True, f'y{self.minor()}'],
                    [2, True, 'z']
                )

        if person == 3 and plural:
            if negative:
                self.concat('z')
            self.concat(f'l{letter_a}r')

        self.if_condition(
            person, plural,
            [1, False, f'm'],
            [2, False, f's{self.minor()}n'],
            [1, True, 'z'],
            [2, True, f's{self.minor()}n{self.minor()}z'],
        )

        if question:
            if negative:
                self.if_condition(
                    person, plural,
                    [1, False, f' m{self.minor()}']
                )

            self.if_condition(
                person, plural,
                [3, False, f' m{self.minor()}'],
                [3, True, f' m{self.minor()}']

            )

        return self.common_return(**kwargs)

    def past_definite(self, **kwargs):
        """
            Past tense
            -di'li geçmiş zaman
        """

        letter_a = self.letter_a()

        from_able = self.is_from_able()

        if kwargs.get('negative', False) and not from_able:
            self.concat(f'm{letter_a}')

        minor = self.minor()

        if self.last_letter_is_vowel() or not self.last_letter_is_hard():
            letter_d = 'd'
        else:
            letter_d = 't'

        plural = kwargs.get('plural', False)
        person = kwargs.get('person', 3)

        self.if_condition(
            person, plural,
            [1, False, f'{letter_d}{minor}m'],
            [2, False, f'{letter_d}{minor}n'],
            [3, False, f'{letter_d}{minor}'],
            [1, True, f'{letter_d}{minor}k'],
            [2, True, f'{letter_d}{minor}n{minor}z'],
            [3, True, f'{letter_d}{self.minor()}l{letter_a}r'],
        )

        if kwargs.get('question', False):
            minor = self.minor()

            self.concat(f' m{minor}')

        return self.common_return(**kwargs)

    def past_progressive_dubitative(self, **kwargs):
        person = kwargs.get('person', 3)
        negative = kwargs.get('negative', False)
        plural = kwargs.get('plural', False)
        question = kwargs.get('question', False)

        self.word = self.present_continuous_simple(
            person=3,
            negative=negative,
        ).to_string()

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')
            plural = False

        if question:
            self.concat(f' m{self.minor()}')

        self.if_ends_with_vowel('y')

        self.word = self.indefinite_past(
            person=person,
            plural=plural
        ).to_string()

        return self.common_return(**kwargs)

    def past_progressive_alternative_dubitative(self, **kwargs):
        person = kwargs.get('person', 3)
        plural = person == 3 and kwargs.get('plural')

        self.word = self.present_continuous_simple_alternative(
            person=3,
            plural=plural,
            question=kwargs.get('question', False),
            negative=kwargs.get('negative', False)
        ).to_string()

        self.if_ends_with_vowel('y')

        if person == 3 and kwargs.get('plural'):
            plural = False
        else:
            plural = kwargs.get('plural', False)

        self.word = self.indefinite_past(
            person=person,
            plural=plural
        ).to_string()

        return self.common_return(**kwargs)

    def indefinite_past(self, **kwargs):
        """
            Past Aorist
            Not the same with English past perfect tense
            This usage is for past tense of an action which is heared/learned but not witnessed.
            mişli geçmiş zaman veya öğrenilen geçmiş zaman
        """

        letter_a = self.letter_a()
        from_able = self.is_from_able()

        if kwargs.get('negative', False) and not from_able:
            self.concat(f'm{letter_a}')

        minor = self.minor()

        self.concat(f'm{minor}ş')

        question = kwargs.get('question', False)
        plural = kwargs.get('plural', False)
        person = kwargs.get('person', 3)

        if not question:
            self.if_condition(
                person, plural,
                [1, False, f'{minor}m'],
                [2, False, f's{minor}n'],
                [1, True, f'{minor}z'],
                [2, True, f's{minor}n{minor}z'],
                [3, True, f'l{letter_a}r']
            )
        else:
            self.if_condition(
                person, plural,
                [1, False, f' m{minor}y{minor}m'],
                [2, False, f' m{minor}s{minor}n'],
                [3, False, f' m{minor}'],
                [1, True, f'{minor}z'],
                [2, True, f' m{minor}y{minor}z'],
                [3, True, f'l{letter_a}r m{minor}']
            )

        return self.common_return(**kwargs)

    def past_progressive_narrative(self, **kwargs):
        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False) and person == 3

        self.word = self.present_continuous_simple(
            person=3,
            negative=negative,
            question=question,
            plural=plural
        ).to_string()

        self.if_ends_with_vowel('y')

        if person == 3 and kwargs.get('plural'):
            plural = False
        else:
            plural = kwargs.get('plural', False)

        self.word = self.past_definite(
            person=person,
            plural=plural
        ).to_string()

        return self.common_return(**kwargs)

    def past_progressive_alternative_narrative(self, **kwargs):
        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        plural = person == 3 and plural

        self.word = self.present_continuous_simple_alternative(
            person=3,
            negative=negative,
            question=question,
            plural=plural
        ).to_string()

        plural = kwargs.get('plural', False)

        if person == 3 and plural:
            plural = False

        self.if_ends_with_vowel('y')

        self.word = self.past_definite(
            person=person,
            plural=plural
        ).to_string()

        return self.common_return(**kwargs)

    def past_perfect_narrative(self, **kwargs):
        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        plural = person == 3 and plural
        self.word = self.indefinite_past(
            person=3,
            plural=plural,
            negative=negative,
            question=question
        ).to_string()

        self.if_ends_with_vowel('y')

        if person == 3 and kwargs.get('plural'):
            if self.last_letter_is_hard():
                letter_d = 't'
            else:
                letter_d = 'd'

            self.concat(f'{letter_d}{self.minor()}')
        else:
            self.word = self.past_definite(
                person=person,
                plural=kwargs.get('plural')
            ).to_string()

        return self.common_return(**kwargs)

    def doubtful_distant_past(self, **kwargs):
        """
            Öğrenilen geçmiş zamanın rivayeti
            Duymuşmuşum Duymuşmuşsun Duymuşmuş Duymuşmuşuz Duymuşmuşunuz Duymuşmuşlar
            Duymuş mumuymuşum? Duymuş mumuymuşsun? Duymuş mumuymuş? Duymuş mumuymuşuz?
            Duymuş mumuymuşsunuz Duymuşlar mıymış?
        """

        self.word = self.indefinite_past(negative=kwargs.get('negative', False)).to_string()

        if not kwargs.get('question', False):
            self.word = self.indefinite_past(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False),
                question=kwargs.get('question', False)
            ).to_string()
        else:
            if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
                self.concat(f'l{self.letter_a()}r')
                minor = self.minor()

                self.concat(f' m{minor}ym{minor}ş')
            else:
                minor = self.minor()
                self.concat(f' m{minor}y')
                self.word = self.indefinite_past(
                    person=kwargs.get('person', 3),
                    plural=kwargs.get('plural', False)
                ).to_string()

        return self.common_return(**kwargs)

    def past_in_the_future(self, **kwargs):
        self.word = self.indefinite_past(
            person=3,
            question=kwargs.get('question', False),
            negative=kwargs.get('negative', False)
        ).to_string()

        self.concat(' ol')

        self.word = self.future_simple(
            person=kwargs.get('person'),
            plural=kwargs.get('plural')
        ).to_string()

        return self.common_return(**kwargs)

    def past_conditional_narrative(self, **kwargs):
        person = kwargs.get('person', 3)
        negative = kwargs.get('negative', False)
        plural = kwargs.get('plural', False)

        if negative:
            self.concat(f'm{self.letter_a()}')

        self.concat(f's{self.letter_a()}')

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        if kwargs.get('question', False):
            self.concat(f' m{self.letter_i()}yd{self.letter_i()}')

        self.if_condition(
            person, plural,
            [1, False, 'm'],
            [2, False, 'n'],
            [1, True, 'k'],
            [2, True, f'n{self.letter_i()}z'],
        )

        return self.common_return(**kwargs)

    def past_conditional_dubitative(self, **kwargs):
        letter_a = self.letter_a()
        letter_i = self.letter_i()
        negative = kwargs.get('negative', False)
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        if negative:
            self.concat(f'm{letter_a}')

        self.concat(f's{letter_a}')

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

        self.if_ends_with_vowel('y')

        self.concat(f'm{letter_i}ş')

        self.if_condition(
            person, plural,
            [1, False, f'{letter_i}m'],
            [2, False, f's{letter_i}n'],
            [1, True, f'{letter_i}z'],
            [2, True, f's{letter_i}n{letter_i}z'],
        )

        return self.common_return(**kwargs)

    def future_simple(self, **kwargs):
        """
            Gelecek zaman
        """
        ae = self.letter_a()

        from_able = self.is_from_able()

        if kwargs.get('negative', False) and not from_able:
            self.concat(f'm{ae}')

        if self.last_letter_is_vowel():
            self.verbs_losing_vowels()
            self.concat('y')

        self.soften()

        if not kwargs.get('negative', False):
            self.harden_verb()
        
        letter_a = self.letter_a()
        letter_i = self.letter_i()
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        if kwargs.get('question', False):
            if kwargs.get('person', 3) == 3 and kwargs.get('plural', False):
                self.concat(f'{letter_a}c{letter_a}kl{letter_a}r ')
            else:
                self.concat(f'{letter_a}c{letter_a}k ')

            self.if_condition(
                person, plural,
                [1, False, f'm{letter_i}y{letter_i}m'],
                [2, False, f'm{letter_i}s{letter_i}n'],
                [3, False, f'm{letter_i}'],
                [1, True, f'm{letter_i}y{letter_i}z'],
                [2, True, f'm{letter_i}s{letter_i}n{letter_i}z'],
                [3, True, f'm{letter_i}']
            )
        elif not kwargs.get('question', False):
            self.if_condition(
                person, plural,
                [1, False, f'{letter_a}c{letter_a}ğ{letter_i}m'],
                [2, False, f'{letter_a}c{letter_a}ks{letter_i}n'],
                [3, False, f'{letter_a}c{letter_a}k'],
                [1, True, f'{letter_a}c{letter_a}ğ{letter_i}z'],
                [2, True, f'{letter_a}c{letter_a}ks{letter_i}n{letter_i}z'],
                [3, True, f'{letter_a}c{letter_a}kl{letter_a}r']
            )

        return self.common_return(**kwargs)

    def future_in_the_past(self, **kwargs):
        """
            süzecektim
        """
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        negative = kwargs.get('negative', False)

        self.future_simple(negative=negative)

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        letter_i = self.letter_i()
        
        if self.last_letter_is_hard():
            letter_d = 't'
        else:
            letter_d = 'd'

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}y')
            if self.last_letter_is_hard():
                letter_d = 't'
            else:
                letter_d = 'd'

        self.concat(f'{letter_d}')

        self.if_condition(
            person, plural,
            [1, False, f'{letter_i}m'],
            [2, False, f'{letter_i}n'],
            [3, False, f'{letter_i}'],
            [1, True, f'{letter_i}k'],
            [2, True, f'{letter_i}n{letter_i}z'],
            [3, True, f'{letter_i}']
        )

        return self.common_return(**kwargs)

    def future_dubitative(self, **kwargs):
        """
            süzecekmişim
        """
        self.word = self.future_simple(negative=kwargs.get('negative', False)).to_string()

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        letter_i = self.letter_i()

        self.concat(f'm{letter_i}ş')

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

            self.if_condition(
                person, plural,
                [1, False, 'y'],
                [2, False, 's'],
                [1, True, 'y'],
                [2, True, 's'],
            )

        self.if_condition(
            person, plural,
            [1, False, f'{letter_i}m'],
            [2, False, f'{letter_i}n'],
            [1, True, f'{letter_i}z'],
            [2, True, f'{letter_i}n{letter_i}z'],
        )

        return self.common_return(**kwargs)

    def future_conditional(self, **kwargs):
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        negative = kwargs.get('negative', False)
        
        self.future_simple(person=3, negative=negative)

        letter_a = self.letter_a()
        letter_i = self.letter_i()

        if person == 3 and plural:
            self.concat(f'l{letter_a}r')
            
        self.concat(f's{letter_a}')

        self.if_condition(
            person, plural,
            [1, False, 'm'],
            [2, False, 'n'],
            [1, True, 'k'],
            [2, True, f'n{letter_i}z'],
        )

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

        return self.common_return(**kwargs)

    def unify_verbs(self, **kwargs):
        """
            Unified verbs (Birleşik fiiler) (Not a suffix but for 'can-bil' modal verb, this is necessary)
            Ability - Yeterlilik: kızabil (bil) (English modal auxiliary verb: Can)
            Swiftness - Tezlik: koşuver (ver)
            Continuity - Süreklilik: gidedur, bakakal, alıkoy (dur, kal, gel, koy)
            Approach - Yaklaşma: (yaz) düzeyaz
        """
        self.verbs_losing_vowels()
        self.if_ends_with_vowel('y')
        self.soften()
        self.harden_verb()

        if not kwargs.get('negative', False):
            if kwargs.get('auxiliary') in ('ver', 'koy'):
                self.concat(self.minor())
            else:
                self.concat(self.letter_a())

            self.concat(kwargs.get('auxiliary'))
        if kwargs.get('negative', False):
            if kwargs.get('auxiliary') == 'bil':
                self.concat(f'{self.letter_a()}m{self.letter_a()}')
            else:
                if kwargs.get('auxiliary') in ['ver', 'koy']:
                    self.concat(self.minor())
                else:
                    self.concat(self.letter_a())

                self.concat(kwargs.get('auxiliary'))

        return self.common_return(**kwargs)

    def necessitative_mood(self, **kwargs):
        letter_a = self.letter_a()
        letter_i = self.letter_i()

        if kwargs.get('negative', False) and not self.is_from_able():
            self.concat(f'm{letter_a}')

        self.concat(f'm{letter_a}l{letter_i}')

        return self.common_return(**kwargs)

    def necessitative_mood_simple_tense(self, **kwargs):
        """
            Gereklilik kipi
            süzmeliydim
        """

        letter_i = self.letter_i()

        self.necessitative_mood()

        if kwargs.get('person', 3) == 3 and kwargs.get('plural'):
            self.concat(f'l{self.letter_a()}r')

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        self.if_condition(
            person, plural,
            [1, False, f'y{letter_i}m'],
            [2, False, f's{letter_i}n'],
            [1, True, f'y{letter_i}z'],
            [2, True, f's{letter_i}n{letter_i}z'],
        )

        return self.common_return(**kwargs)

    def necessitative_past_narrative(self, **kwargs):
        """
            Gereklilik kipi gecmis zaman
            süzmeliydim
        """

        letter_i = self.letter_i()
        negative = kwargs.get('negative', False)

        self.necessitative_mood(negative=negative)

        if kwargs.get('person', 3) == 3 and kwargs.get('plural'):
            self.concat(f'l{self.letter_a()}r')

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

        self.if_ends_with_vowel('y')

        self.concat(f'd{letter_i}')
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        self.if_condition(
            person, plural,
            [1, False, 'm'],
            [2, False, 'n'],
            [1, True, 'k'],
            [2, True, f'n{letter_i}z'],
        )

        return self.common_return(**kwargs)

    def necessitative_past_dubitative(self, **kwargs):
        """
            süzmeliymişim
        """

        letter_i = self.letter_i()
        negative = kwargs.get('negative', False)
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        self.necessitative_mood(negative=negative)

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

        self.if_ends_with_vowel('y')

        self.concat(f'm{letter_i}ş')

        self.if_condition(
            person, plural,
            [1, False, f'{letter_i}m'],
            [2, False, f's{letter_i}n'],
            [1, True, f'{letter_i}z'],
            [2, True, f's{letter_i}n{letter_i}z']
        )

        return self.common_return(**kwargs)

    def imperative_mood(self, **kwargs):
        """
            Make the verb command
            Usage: do it, break it, come!
            As different from English, imperative mood is valid also for 3rd person in Turkish
                but never for 1st person.
            For the second person, there is no suffix
        """

        ae = self.letter_a()

        from_able = self.is_from_able()

        if kwargs.get('negative', False) and not from_able:
            self.concat(f'm{ae}')

        minor = self.minor()

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        question = kwargs.get('question', False)

        if person == 2 and question:
            self.word = '-'
        elif person == 1:
            self.word = '-'
        elif person == 2 and not plural:
            if kwargs.get('formal', False):
                if self.last_letter_is_vowel():
                    self.concat('y')

                self.concat(f'{minor}n')
        elif person == 3 and not plural:
            self.concat(f's{minor}n')

            if question:
                self.concat(f' m{minor}')
        elif person == 2 and plural:
            self.verbs_losing_vowels()
            self.soften()
            self.harden_verb()
            self.if_ends_with_vowel('y')
            self.concat(f'{minor}n')

            if kwargs.get('formal', False):
                self.concat(f'{minor}z')

        elif person == 3 and plural:
            self.concat(f's{minor}n')
            self.concat(f'l{self.letter_a()}r')

            if question:
                self.concat(f' m{self.minor()}')

        return self.common_return(**kwargs)

    def conditional_mood_simple_tense(self, **kwargs):
        """
            Dilek - Şart kipi (-se, -sa)
        """
        letter_a = self.letter_a()
        letter_i = self.letter_i()
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        from_able = self.is_from_able()

        if kwargs.get('negative', False) and not from_able:
            self.concat(f'm{letter_a}')

        self.concat(f's{letter_a}')

        self.if_condition(
            person, plural,
            [1, False, 'm'],
            [2, False, 'n'],
            [1, True, 'k'],
            [2, True, f'n{letter_i}z'],
            [3, True, f'l{letter_a}r']
        )

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

        return self.common_return(**kwargs)

    def subjunctive_mood_simple_tense(self, **kwargs):
        """
            İstek kipi (geleyim, gelesin, gele, gelelim, gelesiniz, geleler)
        """
        letter_a = self.letter_a()
        letter_i = self.letter_i()
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)

        from_able = self.is_from_able()

        if kwargs.get('negative', False):
            if not from_able:
                self.concat(f'm{letter_a}')

            self.concat(f'y{letter_a}')
        else:
            self.verbs_losing_vowels()

            self.harden_verb()

            self.if_ends_with_vowel('y')

            self.soften()

            self.concat(letter_a)

        self.if_condition(
            person, plural,
            [1, False, f'y{letter_i}m'],
            [2, False, f's{letter_i}n'],
            [1, True, f'l{letter_i}m'],
            [2, True, f's{letter_i}n{letter_i}z'],
            [3, True, f'l{letter_a}r']
        )

        if kwargs.get('question', False):
            self.concat(f' m{letter_i}')

        return self.common_return(**kwargs)

    def past_definite_narrative(self, **kwargs):
        """
            Bilinen geçmiş zamanın hikayesi
            yaptıydım, yaptıydın, yaptıydı, yaptıydık, yaptıydınız, yaptıydılar
            yaptı mıydım, yaptı mıydın, yaptı mıydı, yaptı mıydık, yaptı mıydınız, yaptılar mıydı
        """

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)

        if self.is_from_passive():
            negative = False

        self.word = self.past_definite(
            person=3,
            plural=plural,
            negative=negative,
        ).to_string()

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        if question:
            self.concat(f' m{self.minor()}')

        self.if_ends_with_vowel('y')

        if person == 3 and plural:
            plural = False

        self.word = self.past_definite(
            person=person,
            plural=plural
        ).to_string()

        return self.common_return(**kwargs)

    def indefinite_past_reportative(self, **kwargs):
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        question = kwargs.get('question', False)
        negative = kwargs.get('negative', False)

        if negative:
            self.concat(f'm{self.letter_a()}y{self.letter_a()}')

            if person == 3 and plural:
                self.concat(f'l{self.letter_a()}r')
                plural = False
        else:
            self.soften()
            self.harden_verb()
            self.if_ends_with_vowel('y')
            self.concat(self.letter_a())

            if person == 3 and plural:
                self.concat(f'l{self.letter_a()}r')
                plural = False
            else:
                self.concat('y')

        if question:
            self.indefinite_past(
                person=3
            )

            self.if_condition(
                person, plural,
                [1, False, f' m{self.letter_i()}y{self.letter_i()}m'],
                [2, False, f' m{self.letter_i()}s{self.letter_i()}n'],
                [3, False, f' m{self.letter_i()}'],
                [1, True, f' m{self.letter_i()}y{self.letter_i()}z'],
                [2, True, f' m{self.letter_i()}s{self.letter_i()}n{self.letter_i()}z'],
            )
        else:
            self.indefinite_past(
                person=person,
                plural=plural
            )

        return self.common_return(**kwargs)

    def definite_past_reportative(self, **kwargs):
        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        question = kwargs.get('question', False)
        negative = kwargs.get('negative', False)

        if negative:
            self.concat(f'm{self.letter_a()}y{self.letter_a()}')

            if person == 3 and plural:
                self.concat(f'l{self.letter_a()}r')
                plural = False
            elif not question:
                self.concat('y')

            if question:
                self.concat(f' m{self.minor()}y')
        else:
            self.soften()
            self.harden_verb()
            self.if_ends_with_vowel('y')
            self.concat(self.letter_a())

            if person == 3 and plural and question:
                self.concat(f'l{self.letter_a()}r')
                plural = False

            if question:
                self.concat(f' m{self.minor()}')

            self.concat('y')

        self.past_definite(
            person=person,
            plural=plural,
        )

        return self.common_return(**kwargs)


    def past_indefinite_past(self, **kwargs):
        """
            Öğrenilen geçmiş zamanın hikayesi
            Yapmışlardı (-miş -di)
            Example: It is heard by someone that somebody did something in the past
        """

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', 3)
        question = kwargs.get('question', False)
        negative = kwargs.get('negative', False)

        if person == 3 and plural and question:
            self.word = self.indefinite_past(
                negative=negative,
                question=question,
                person=3,
                plural=plural
            ).to_string()
        else:
            self.word = self.indefinite_past(
                negative=negative,
                question=question,
                person=3
            ).to_string()

        self.if_ends_with_vowel('y')

        if person == 3 and plural and question:
            self.word = self.past_definite(person=person).to_string()
        else:
            self.word = self.past_definite(
                person=person,
                plural=plural
            ).to_string()

        return self.common_return(**kwargs)

    def indefinite_past_future(self, **kwargs):
        """
            Gelecek zamanın rivayeti
            Yapacaklardı (-acak -mış)
            Example: It is heard by someone that somebody will do something in the past
        """

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        question = kwargs.get('question', False)
        negative = kwargs.get('negative', False)

        if self.is_from_passive():
            negative = False

        self.word = self.future_simple(
            negative=negative,
            person=3,
        ).to_string()

        if person == 3 and plural:
            self.concat(f'l{self.letter_a()}r')

        if question:
            self.concat(f' m{self.minor()}')

        self.if_ends_with_vowel(f'y')
        self.concat(f'm{self.letter_i()}ş')

        i = self.letter_i()

        self.if_condition(
            person, plural,
            [1, False, f'{i}m'],
            [2, False, f's{i}n'],
            [1, True, f'{i}z'],
            [2, True, f's{i}n{i}z']
        )

        return self.common_return(**kwargs)

    def past_future(self, **kwargs):
        """
            Gelecek zamanın hikayesi
                Yapacaklardı (-acak -tı)
                Example: Somebody will do something in the past
        """

        person = kwargs.get('person', 3)
        plural = kwargs.get('plural', False)
        question = kwargs.get('question', False)

        if person == 3 and plural and question:
            self.word = self.future_simple(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False),
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()
        else:
            self.word = self.future_simple(
                negative=kwargs.get('negative', False),
                question=kwargs.get('question', False)
            ).to_string()

        if person == 3 and plural and question:
            self.concat('y')
            self.word = self.past_definite(person=kwargs.get('person', 3)).to_string()
        else:
            if kwargs.get('question', False):
                self.concat('y')

            self.word = self.past_definite(
                person=kwargs.get('person', 3),
                plural=kwargs.get('plural', False)
            ).to_string()

        return self.common_return(**kwargs)

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
        self.harden_verb()

        lower_word = self.lower()

        minor = self.minor()

        if lower_word.endswith('l'):
            self.concat(self.minor())
            self.concat('n')
        else:
            if self.last_letter_is_vowel():
                self.concat('n')

        self.concat(f'{minor}l')

        return self.common_return(**kwargs)
    
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
        self.if_ends_with_vowel('y')

        self.concat(f'ken')

        return self.common_return(**kwargs)
    
    def adverb_continuity(self, **kwargs):
        """
            Git -> Gide gide etc. (-e)

            Use this method without conjuncting
        """
        ae = self.letter_a()

        from_able = self.is_from_able()

        if kwargs.get('negative', False):
            if not from_able:
                self.concat(f'm{ae}')

            self.concat('y')
        else:
            self.harden_verb()

            self.if_ends_with_vowel('y')

        self.concat(ae)

        self.word = f'{self.word} {self.word}'

        return self.common_return(**kwargs)

    def adverb_repeatedly(self, **kwargs):
        """
            Git -> Gide gide etc. (-e)

            Use this method without conjuncting
        """
        ae = self.letter_a()

        self.word = self.past_definite(
            negative=kwargs.get('negative', False),
            person=1,
            plural=True
        ).to_string()

        self.concat(f'ç{ae}')

        return self.common_return(**kwargs)

    def adverb_after_action(self, **kwargs):
        """
            Gidince etc. (-nca)

            Generates adverb-verb for "after"

            Use this method without any conjuncting
        """

        ae = self.letter_a()
        letter_i = self.letter_i()
        minor = self.minor()
        from_able = self.is_from_able()

        self.harden_verb()

        if kwargs.get('negative', False):
            if not from_able:
                self.concat(f'm{ae}')
            
            self.concat(f'y{letter_i}')
        elif self.last_letter_is_vowel():
            self.concat(f'y{minor}')
        else:
            self.concat(f'{minor}')

        self.concat(f'nc{ae}')

        return self.common_return(**kwargs)

    def adverb_after_action_alternative(self, **kwargs):
        """
            Gidip etc. (-p)

            Generates adverb-verb for "after"

            Use this method without any conjuncting
        """

        ae = self.letter_a()
        minor = self.minor()

        from_able = self.is_from_able()

        if kwargs.get('negative', False):
            if not from_able:
                self.concat(f'm{ae}')

            self.concat('y')
        elif self.last_letter_is_vowel():
            self.concat('y')
        else:
            self.harden_verb()

        self.concat(f'{minor}p')

        return self.common_return(**kwargs)

    def adverb_without_action(self, **kwargs):
        """
            Gitmeden etc. (-madan)

            Generates adverb-verb for "without action"

            Use this method without any conjuncting
        """

        ae = self.letter_a()

        from_able = self.is_from_able()

        if not from_able:
            self.concat(f'm{ae}')

        self.concat(f'd{ae}n')

        return self.common_return(**kwargs)

    def adverb_without_action_alternative(self, **kwargs):
        """
            Gitmeksizin etc. (-meksizin)

            Generates adverb-verb for "without action"

            Use this method without any conjuncting
        """

        letter_i = self.letter_i()
        self.word = self.infinitive().to_string()
        self.concat(f's{letter_i}z{letter_i}n')

        return self.common_return(**kwargs)

    def adverb_by_action(self, **kwargs):
        """
            Giderek etc. (-erek)

            Generates adverb-verb for "by action"

            Use this method without any conjuncting
        """

        ae = self.letter_a()

        from_able = self.is_from_able()

        if kwargs.get('negative', False):
            if not from_able:
                self.concat(f'm{ae}')
        else:
            self.harden_verb()
            
        self.if_ends_with_vowel('y')

        self.concat(f'{ae}r{ae}k')

        return self.common_return(**kwargs)
    
    def adverb_since_action(self, **kwargs):
        """
            Gideli etc. (-eli)

            Generates adverb-verb for "since action"

            Use this method without any conjuncting
        """

        ae = self.letter_a()
        letter_i = self.letter_i()

        from_able = self.is_from_able()

        if kwargs.get('negative', False):
            if not from_able:
                self.concat(f'm{ae}')
        else:
            self.harden_verb()

        self.if_ends_with_vowel('y')

        self.concat(f'{ae}l{letter_i}')

        return self.common_return(**kwargs)

    def simple_tense_past_definite(self, **kwargs):
        """
            yapardim
        """

        person = kwargs.get('person', 3)
        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)

        plural = person == 3 and kwargs.get('plural')

        self.simple_tense(
            person=3,
            negative=negative,
            plural=plural,
            question=question
        )

        if plural:
            plural = False
        else:
            plural = kwargs.get('plural', False)

        self.if_ends_with_vowel('y')

        self.past_definite(
            person=person,
            plural=plural,
        )

        return self.common_return(**kwargs)

    def simple_tense_indefinite_past(self, **kwargs):
        """
            yaparmisim
        """

        person = kwargs.get('person', 3)
        negative = kwargs.get('negative', False)
        question = kwargs.get('question', False)

        plural = person == 3 and kwargs.get('plural')

        self.simple_tense(
            person=3,
            negative=negative,
            plural=plural,
            question=question
        )

        if plural:
            plural = False
        else:
            plural = kwargs.get('plural', False)

        self.if_ends_with_vowel('y')

        self.indefinite_past(
            person=person,
            plural=plural,
        )

        return self.common_return(**kwargs)
