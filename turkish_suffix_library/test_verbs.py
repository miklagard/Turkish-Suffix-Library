from turkish_suffix_library import turkish as tr
import sqlite3
from turkish_suffix_library.sample_verbs_list import VERBS


class VerbsTest:
    def __init__(self):
        self.tense = None
        self.verb = None

        self.conn = sqlite3.connect('database.db')
        self.conn.execute('delete from verbs')

    def execute(self, cmd, **kwargs):
        generated = eval("%s('%s', **%s)" % (cmd, self.verb, kwargs))

        plurality = kwargs.get("plural")
        negative = kwargs.get("negative", False)
        question = kwargs.get("question", False)

        if plurality:
            plurality = 1
        else:
            plurality = 0

        if negative:
            negative = 1
        else:
            negative = 0

        if question:
            question = 1
        else:
            question = 0

        person = kwargs.get("person", 3)

        sql = f"""
            insert into verbs(
                generated, 
                tense, 
                question, 
                person, 
                plurality, 
                negative, 
                source_verb
            ) values (
                '{generated}',
                '{self.tense}',
                '{question}',
                '{person}',
                '{plurality}',
                '{negative}',
                '{self.verb}'
            ) 
        """

        self.conn.execute(sql)

    def proc(self):
        for self.verb in VERBS:
            self.tense = 'Mastar'
            self.execute('tr.make_infinitive')
            self.execute('tr.make_infinitive', negative=True)

            # self.tense = 'Birleşik fiil'
            # exec ('tr.unify_verbs', 'auxiliary='bil', negative=False)
            # exec ('tr.unify_verbs', 'auxiliary='bil', negative=True)

            self.tense = 'Emir kipi'
            self.execute('tr.make_command', person=2)
            self.execute('tr.make_command', person=3)
            self.execute('tr.make_command', question=True, person=3)
            self.execute('tr.make_command', person=2, plural=True)
            self.execute('tr.make_command', person=2, plural=True, formal=True)
            self.execute('tr.make_command', person=3, plural=True)
            self.execute('tr.make_command', question=True, person=3, plural=True)

            self.execute('tr.make_command', negative=True, person=2)
            self.execute('tr.make_command', negative=True, person=3)
            self.execute('tr.make_command', negative=True, question=True, person=3)
            self.execute('tr.make_command', negative=True, person=2)
            self.execute('tr.make_command', negative=True, person=2, plural=True, formal=True)
            self.execute('tr.make_command', negative=True, person=3, plural=True)
            self.execute('tr.make_command', negative=True, question=True, person=3, plural=True)

            self.tense = 'Şimdiki zaman'
            self.execute('tr.make_present_continuous', person=1)
            self.execute('tr.make_present_continuous', person=2)
            self.execute('tr.make_present_continuous', person=3)
            self.execute('tr.make_present_continuous', person=1, plural=True)
            self.execute('tr.make_present_continuous', person=2, plural=True)
            self.execute('tr.make_present_continuous', person=3, plural=True)

            self.execute('tr.make_present_continuous', negative=True, person=1)
            self.execute('tr.make_present_continuous', negative=True, person=2)
            self.execute('tr.make_present_continuous', negative=True, person=3)
            self.execute('tr.make_present_continuous', negative=True, person=1, plural=True)
            self.execute('tr.make_present_continuous', negative=True, person=2, plural=True)
            self.execute('tr.make_present_continuous', negative=True, person=3, plural=True)

            self.execute('tr.make_present_continuous', negative=True, question=True, person=1)
            self.execute('tr.make_present_continuous', negative=True, question=True, person=2)
            self.execute('tr.make_present_continuous', negative=True, question=True, person=3)
            self.execute('tr.make_present_continuous', negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_present_continuous', negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_present_continuous', negative=True, question=True, person=3, plural=True)

            self.tense = 'Şimdiki zaman 2'
            self.execute('tr.make_present_continuous_alternative', person=1)
            self.execute('tr.make_present_continuous_alternative', person=2)
            self.execute('tr.make_present_continuous_alternative', person=3)
            self.execute('tr.make_present_continuous_alternative', person=1, plural=True)
            self.execute('tr.make_present_continuous_alternative', person=2, plural=True)
            self.execute('tr.make_present_continuous_alternative', person=3, plural=True)

            self.execute('tr.make_present_continuous_alternative', negative=True, person=1)
            self.execute('tr.make_present_continuous_alternative', negative=True, person=2)
            self.execute('tr.make_present_continuous_alternative', negative=True, person=3)
            self.execute('tr.make_present_continuous_alternative', negative=True, person=1, plural=True)
            self.execute('tr.make_present_continuous_alternative', negative=True, person=2, plural=True)
            self.execute('tr.make_present_continuous_alternative', negative=True, person=3, plural=True)

            self.execute('tr.make_present_continuous_alternative', negative=True, question=True, person=1)
            self.execute('tr.make_present_continuous_alternative', negative=True, question=True, person=2)
            self.execute('tr.make_present_continuous_alternative', negative=True, question=True, person=3)
            self.execute('tr.make_present_continuous_alternative',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_present_continuous_alternative',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_present_continuous_alternative',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Gelecek zaman'
            self.execute('tr.make_future', person=1)
            self.execute('tr.make_future', person=2)
            self.execute('tr.make_future', person=3)
            self.execute('tr.make_future', person=1, plural=True)
            self.execute('tr.make_future', person=2, plural=True)
            self.execute('tr.make_future', person=3, plural=True)

            self.execute('tr.make_future', negative=True, person=1)
            self.execute('tr.make_future', negative=True, person=2)
            self.execute('tr.make_future', negative=True, person=3)
            self.execute('tr.make_future', negative=True, person=1, plural=True)
            self.execute('tr.make_future', negative=True, person=2, plural=True)
            self.execute('tr.make_future', negative=True, person=3, plural=True)

            self.execute('tr.make_future', negative=True, question=True, person=1)
            self.execute('tr.make_future', negative=True, question=True, person=2)
            self.execute('tr.make_future', negative=True, question=True, person=3)
            self.execute('tr.make_future', negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_future', negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_future', negative=True, question=True, person=3, plural=True)

            self.tense = 'Geniş zaman'
            self.execute('tr.make_present_simple', person=1)
            self.execute('tr.make_present_simple', person=2)
            self.execute('tr.make_present_simple', person=3)
            self.execute('tr.make_present_simple', person=1, plural=True)
            self.execute('tr.make_present_simple', person=2, plural=True)
            self.execute('tr.make_present_simple', person=3, plural=True)

            self.execute('tr.make_present_simple', question=True, person=1)
            self.execute('tr.make_present_simple', question=True, person=2)
            self.execute('tr.make_present_simple', question=True, person=3)
            self.execute('tr.make_present_simple', question=True, person=1, plural=True)
            self.execute('tr.make_present_simple', question=True, person=2, plural=True)
            self.execute('tr.make_present_simple', question=True, person=3, plural=True)

            self.execute('tr.make_present_simple', negative=True, question=True, person=1)
            self.execute('tr.make_present_simple', negative=True, question=True, person=2)
            self.execute('tr.make_present_simple', negative=True, question=True, person=3)
            self.execute('tr.make_present_simple',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_present_simple',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_present_simple',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Geçmiş zaman'
            self.execute('tr.make_past', person=1)
            self.execute('tr.make_past', person=2)
            self.execute('tr.make_past', person=3)
            self.execute('tr.make_past', person=1, plural=True)
            self.execute('tr.make_past', person=2, plural=True)
            self.execute('tr.make_past', person=3, plural=True)

            self.execute('tr.make_past', negative=True, person=1)
            self.execute('tr.make_past', negative=True, person=2)
            self.execute('tr.make_past', negative=True, person=3)
            self.execute('tr.make_past', negative=True, person=1, plural=True)
            self.execute('tr.make_past', negative=True, person=2, plural=True)
            self.execute('tr.make_past', negative=True, person=3, plural=True)

            self.execute('tr.make_past', negative=True, question=True, person=1)
            self.execute('tr.make_past', negative=True, question=True, person=2)
            self.execute('tr.make_past', negative=True, question=True, person=3)
            self.execute('tr.make_past', negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past', negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past', negative=True, question=True, person=3, plural=True)

            self.tense = 'Gereklilik kipi'
            self.execute('tr.make_must', person=1)
            self.execute('tr.make_must', person=2)
            self.execute('tr.make_must', person=3)
            self.execute('tr.make_must', person=1, plural=True)
            self.execute('tr.make_must', person=2, plural=True)
            self.execute('tr.make_must', person=3, plural=True)

            self.execute('tr.make_must', negative=True, person=1)
            self.execute('tr.make_must', negative=True, person=2)
            self.execute('tr.make_must', negative=True, person=3)
            self.execute('tr.make_must', negative=True, person=1, plural=True)
            self.execute('tr.make_must', negative=True, person=2, plural=True)
            self.execute('tr.make_must', negative=True, person=3, plural=True)

            self.execute('tr.make_must', negative=True, question=True, person=1)
            self.execute('tr.make_must', negative=True, question=True, person=2)
            self.execute('tr.make_must', negative=True, question=True, person=3)
            self.execute('tr.make_must', negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_must', negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_must', negative=True, question=True, person=3, plural=True)

            self.tense = 'Dilek-Şart kipi'
            self.execute('tr.make_wish_condition', person=1)
            self.execute('tr.make_wish_condition', person=2)
            self.execute('tr.make_wish_condition', person=3)
            self.execute('tr.make_wish_condition', person=1, plural=True)
            self.execute('tr.make_wish_condition', person=2, plural=True)
            self.execute('tr.make_wish_condition', person=3, plural=True)

            self.execute('tr.make_wish_condition', question=True, person=1)
            self.execute('tr.make_wish_condition', question=True, person=2)
            self.execute('tr.make_wish_condition', question=True, person=3)
            self.execute('tr.make_wish_condition', question=True, person=1, plural=True)
            self.execute('tr.make_wish_condition', question=True, person=2, plural=True)
            self.execute('tr.make_wish_condition', question=True, person=3, plural=True)

            self.execute('tr.make_wish_condition', negative=True, question=True, person=1)
            self.execute('tr.make_wish_condition', negative=True, question=True, person=2)
            self.execute('tr.make_wish_condition', negative=True, question=True, person=3)
            self.execute('tr.make_wish_condition',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_wish_condition',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_wish_condition',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'İstek kipi'
            self.execute('tr.make_wish', person=1)
            self.execute('tr.make_wish', person=2)
            self.execute('tr.make_wish', person=3)
            self.execute('tr.make_wish', person=1, plural=True)
            self.execute('tr.make_wish', person=2, plural=True)
            self.execute('tr.make_wish', person=3, plural=True)

            self.execute('tr.make_wish', negative=True, person=1)
            self.execute('tr.make_wish', negative=True, person=2)
            self.execute('tr.make_wish', negative=True, person=3)
            self.execute('tr.make_wish', negative=True, person=1, plural=True)
            self.execute('tr.make_wish', negative=True, person=2, plural=True)
            self.execute('tr.make_wish', negative=True, person=3, plural=True)

            self.execute('tr.make_wish', negative=True, question=True, person=1)
            self.execute('tr.make_wish', negative=True, question=True, person=2)
            self.execute('tr.make_wish', negative=True, question=True, person=3)
            self.execute('tr.make_wish', negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_wish', negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_wish', negative=True, question=True, person=3, plural=True)

            self.tense = 'Öğrenilen geçmiş zaman'
            self.execute('tr.make_past_perfect', person=1)
            self.execute('tr.make_past_perfect', person=2)
            self.execute('tr.make_past_perfect', person=3)
            self.execute('tr.make_past_perfect', person=1, plural=True)
            self.execute('tr.make_past_perfect', person=2, plural=True)
            self.execute('tr.make_past_perfect', person=3, plural=True)

            self.execute('tr.make_past_perfect', negative=True, person=1)
            self.execute('tr.make_past_perfect', negative=True, person=2)
            self.execute('tr.make_past_perfect', negative=True, person=3)
            self.execute('tr.make_past_perfect', negative=True, person=1, plural=True)
            self.execute('tr.make_past_perfect', negative=True, person=2, plural=True)
            self.execute('tr.make_past_perfect', negative=True, person=3, plural=True)

            self.execute('tr.make_past_perfect', negative=True, question=True, person=1)
            self.execute('tr.make_past_perfect', negative=True, question=True, person=2)
            self.execute('tr.make_past_perfect', negative=True, question=True, person=3)
            self.execute('tr.make_past_perfect',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past_perfect',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past_perfect',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Öğrenilen geçmiş zamanın hikayesi'
            self.execute('tr.make_past_past_perfect', person=1)
            self.execute('tr.make_past_past_perfect', person=2)
            self.execute('tr.make_past_past_perfect', person=3)
            self.execute('tr.make_past_past_perfect', person=1, plural=True)
            self.execute('tr.make_past_past_perfect', person=2, plural=True)
            self.execute('tr.make_past_past_perfect', person=3, plural=True)

            self.execute('tr.make_past_past_perfect', negative=True, person=1)
            self.execute('tr.make_past_past_perfect', negative=True, person=2)
            self.execute('tr.make_past_past_perfect', negative=True, person=3)
            self.execute('tr.make_past_past_perfect', negative=True, person=1, plural=True)
            self.execute('tr.make_past_past_perfect', negative=True, person=2, plural=True)
            self.execute('tr.make_past_past_perfect', negative=True, person=3, plural=True)

            self.execute('tr.make_past_past_perfect', negative=True, question=True, person=1)
            self.execute('tr.make_past_past_perfect', negative=True, question=True, person=2)
            self.execute('tr.make_past_past_perfect', negative=True, question=True, person=3)
            self.execute('tr.make_past_past_perfect',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past_past_perfect',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past_past_perfect',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Öğrenilen geçmiş zamanın rivayeti'
            self.execute('tr.make_past_perfect_past_perfect', person=1)
            self.execute('tr.make_past_perfect_past_perfect', person=2)
            self.execute('tr.make_past_perfect_past_perfect', person=3)
            self.execute('tr.make_past_perfect_past_perfect', person=1, plural=True)
            self.execute('tr.make_past_perfect_past_perfect', person=2, plural=True)
            self.execute('tr.make_past_perfect_past_perfect', person=3, plural=True)

            self.execute('tr.make_past_perfect_past_perfect', negative=True, person=1)
            self.execute('tr.make_past_perfect_past_perfect', negative=True, person=2)
            self.execute('tr.make_past_perfect_past_perfect', negative=True, person=3)
            self.execute('tr.make_past_perfect_past_perfect', negative=True, person=1, plural=True)
            self.execute('tr.make_past_perfect_past_perfect', negative=True, person=2, plural=True)
            self.execute('tr.make_past_perfect_past_perfect', negative=True, person=3, plural=True)

            self.execute('tr.make_past_perfect_past_perfect', negative=True, question=True, person=1)
            self.execute('tr.make_past_perfect_past_perfect', negative=True, question=True, person=2)
            self.execute('tr.make_past_perfect_past_perfect', negative=True, question=True, person=3)
            self.execute('tr.make_past_perfect_past_perfect',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past_perfect_past_perfect',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past_perfect_past_perfect',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Gelecek zamanın rivayeti'
            self.execute('tr.make_past_perfect_future', person=1)
            self.execute('tr.make_past_perfect_future', person=2)
            self.execute('tr.make_past_perfect_future', person=3)
            self.execute('tr.make_past_perfect_future', person=1, plural=True)
            self.execute('tr.make_past_perfect_future', person=2, plural=True)
            self.execute('tr.make_past_perfect_future', person=3, plural=True)

            self.execute('tr.make_past_perfect_future', negative=True, person=1)
            self.execute('tr.make_past_perfect_future', negative=True, person=2)
            self.execute('tr.make_past_perfect_future', negative=True, person=3)
            self.execute('tr.make_past_perfect_future', negative=True, person=1, plural=True)
            self.execute('tr.make_past_perfect_future', negative=True, person=2, plural=True)
            self.execute('tr.make_past_perfect_future', negative=True, person=3, plural=True)

            self.execute('tr.make_past_perfect_future', negative=True, question=True, person=1)
            self.execute('tr.make_past_perfect_future', negative=True, question=True, person=2)
            self.execute('tr.make_past_perfect_future', negative=True, question=True, person=3)
            self.execute('tr.make_past_perfect_future',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past_perfect_future',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past_perfect_future',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Gelecek zamanın hikayesi'
            self.execute('tr.make_past_future', person=1)
            self.execute('tr.make_past_future', person=2)
            self.execute('tr.make_past_future', person=3)
            self.execute('tr.make_past_future', person=1, plural=True)
            self.execute('tr.make_past_future', person=2, plural=True)
            self.execute('tr.make_past_future', person=3, plural=True)

            self.execute('tr.make_past_future', negative=True, person=1)
            self.execute('tr.make_past_future', negative=True, person=2)
            self.execute('tr.make_past_future', negative=True, person=3)
            self.execute('tr.make_past_future', negative=True, person=1, plural=True)
            self.execute('tr.make_past_future', negative=True, person=2, plural=True)
            self.execute('tr.make_past_future', negative=True, person=3, plural=True)

            self.execute('tr.make_past_future', negative=True, question=True, person=1)
            self.execute('tr.make_past_future', negative=True, question=True, person=2)
            self.execute('tr.make_past_future', negative=True, question=True, person=3)
            self.execute('tr.make_past_future',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past_future',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past_future',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Geçmiş zamanın hikayesi'
            self.execute('tr.make_past_past', person=1)
            self.execute('tr.make_past_past', person=2)
            self.execute('tr.make_past_past', person=3)
            self.execute('tr.make_past_past', person=1, plural=True)
            self.execute('tr.make_past_past', person=2, plural=True)
            self.execute('tr.make_past_past', person=3, plural=True)

            self.execute('tr.make_past_past', negative=True, person=1)
            self.execute('tr.make_past_past', negative=True, person=2)
            self.execute('tr.make_past_past', negative=True, person=3)
            self.execute('tr.make_past_past', negative=True, person=1, plural=True)
            self.execute('tr.make_past_past', negative=True, person=2, plural=True)
            self.execute('tr.make_past_past', negative=True, person=3, plural=True)

            self.execute('tr.make_past_past', negative=True, question=True, person=1)
            self.execute('tr.make_past_past', negative=True, question=True, person=2)
            self.execute('tr.make_past_past', negative=True, question=True, person=3)
            self.execute('tr.make_past_past',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past_past',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past_past',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Bilinen geçmiş zamanın şartı'
            self.execute('tr.make_past_condition', person=1)
            self.execute('tr.make_past_condition', person=2)
            self.execute('tr.make_past_condition', person=3)
            self.execute('tr.make_past_condition', person=1, plural=True)
            self.execute('tr.make_past_condition', person=2, plural=True)
            self.execute('tr.make_past_condition', person=3, plural=True)

            self.execute('tr.make_past_condition', negative=True, person=1)
            self.execute('tr.make_past_condition', negative=True, person=2)
            self.execute('tr.make_past_condition', negative=True, person=3)
            self.execute('tr.make_past_condition', negative=True, person=1, plural=True)
            self.execute('tr.make_past_condition', negative=True, person=2, plural=True)
            self.execute('tr.make_past_condition', negative=True, person=3, plural=True)

            self.execute('tr.make_past_condition', negative=True, question=True, person=1)
            self.execute('tr.make_past_condition', negative=True, question=True, person=2)
            self.execute('tr.make_past_condition', negative=True, question=True, person=3)
            self.execute('tr.make_past_condition',
                         negative=True, question=True, person=1, plural=True)
            self.execute('tr.make_past_condition',
                         negative=True, question=True, person=2, plural=True)
            self.execute('tr.make_past_condition',
                         negative=True, question=True, person=3, plural=True)

        self.conn.commit()

        self.conn.close()


test = VerbsTest()
test.proc()
