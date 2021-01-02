from turkish_suffix_library.turkish import Turkish
import sqlite3
from turkish_suffix_library.sample_verbs_list import VERBS


class VerbsTest:
    def __init__(self):
        self.tense = None
        self.verb = None

        self.conn = sqlite3.connect('database.db')
        self.conn.execute('delete from verbs')

    def execute(self, cmd, **kwargs):
        generated = eval("Turkish('%s').%s(**%s)" % (self.verb, cmd, kwargs))

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
            self.execute('infinitive')
            self.execute('infinitive', negative=True)

            # self.tense = 'Birleşik fiil'
            # exec ('unify_verbs', 'auxiliary='bil', negative=False)
            # exec ('unify_verbs', 'auxiliary='bil', negative=True)

            self.tense = 'Emir kipi'
            self.execute('command', person=2)
            self.execute('command', person=3)
            self.execute('command', question=True, person=3)
            self.execute('command', person=2, plural=True)
            self.execute('command', person=2, plural=True, formal=True)
            self.execute('command', person=3, plural=True)
            self.execute('command', question=True, person=3, plural=True)

            self.execute('command', negative=True, person=2)
            self.execute('command', negative=True, person=3)
            self.execute('command', negative=True, question=True, person=3)
            self.execute('command', negative=True, person=2)
            self.execute('command', negative=True, person=2, plural=True, formal=True)
            self.execute('command', negative=True, person=3, plural=True)
            self.execute('command', negative=True, question=True, person=3, plural=True)

            self.tense = 'Şimdiki zaman'
            self.execute('present_continuous', person=1)
            self.execute('present_continuous', person=2)
            self.execute('present_continuous', person=3)
            self.execute('present_continuous', person=1, plural=True)
            self.execute('present_continuous', person=2, plural=True)
            self.execute('present_continuous', person=3, plural=True)

            self.execute('present_continuous', negative=True, person=1)
            self.execute('present_continuous', negative=True, person=2)
            self.execute('present_continuous', negative=True, person=3)
            self.execute('present_continuous', negative=True, person=1, plural=True)
            self.execute('present_continuous', negative=True, person=2, plural=True)
            self.execute('present_continuous', negative=True, person=3, plural=True)

            self.execute('present_continuous', negative=True, question=True, person=1)
            self.execute('present_continuous', negative=True, question=True, person=2)
            self.execute('present_continuous', negative=True, question=True, person=3)
            self.execute('present_continuous', negative=True, question=True, person=1, plural=True)
            self.execute('present_continuous', negative=True, question=True, person=2, plural=True)
            self.execute('present_continuous', negative=True, question=True, person=3, plural=True)

            self.tense = 'Şimdiki zaman 2'
            self.execute('present_continuous_alternative', person=1)
            self.execute('present_continuous_alternative', person=2)
            self.execute('present_continuous_alternative', person=3)
            self.execute('present_continuous_alternative', person=1, plural=True)
            self.execute('present_continuous_alternative', person=2, plural=True)
            self.execute('present_continuous_alternative', person=3, plural=True)

            self.execute('present_continuous_alternative', negative=True, person=1)
            self.execute('present_continuous_alternative', negative=True, person=2)
            self.execute('present_continuous_alternative', negative=True, person=3)
            self.execute('present_continuous_alternative', negative=True, person=1, plural=True)
            self.execute('present_continuous_alternative', negative=True, person=2, plural=True)
            self.execute('present_continuous_alternative', negative=True, person=3, plural=True)

            self.execute('present_continuous_alternative', negative=True, question=True, person=1)
            self.execute('present_continuous_alternative', negative=True, question=True, person=2)
            self.execute('present_continuous_alternative', negative=True, question=True, person=3)
            self.execute('present_continuous_alternative',
                         negative=True, question=True, person=1, plural=True)
            self.execute('present_continuous_alternative',
                         negative=True, question=True, person=2, plural=True)
            self.execute('present_continuous_alternative',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Gelecek zaman'
            self.execute('future', person=1)
            self.execute('future', person=2)
            self.execute('future', person=3)
            self.execute('future', person=1, plural=True)
            self.execute('future', person=2, plural=True)
            self.execute('future', person=3, plural=True)

            self.execute('future', negative=True, person=1)
            self.execute('future', negative=True, person=2)
            self.execute('future', negative=True, person=3)
            self.execute('future', negative=True, person=1, plural=True)
            self.execute('future', negative=True, person=2, plural=True)
            self.execute('future', negative=True, person=3, plural=True)

            self.execute('future', negative=True, question=True, person=1)
            self.execute('future', negative=True, question=True, person=2)
            self.execute('future', negative=True, question=True, person=3)
            self.execute('future', negative=True, question=True, person=1, plural=True)
            self.execute('future', negative=True, question=True, person=2, plural=True)
            self.execute('future', negative=True, question=True, person=3, plural=True)

            self.tense = 'Geniş zaman'
            self.execute('present_simple', person=1)
            self.execute('present_simple', person=2)
            self.execute('present_simple', person=3)
            self.execute('present_simple', person=1, plural=True)
            self.execute('present_simple', person=2, plural=True)
            self.execute('present_simple', person=3, plural=True)

            self.execute('present_simple', question=True, person=1)
            self.execute('present_simple', question=True, person=2)
            self.execute('present_simple', question=True, person=3)
            self.execute('present_simple', question=True, person=1, plural=True)
            self.execute('present_simple', question=True, person=2, plural=True)
            self.execute('present_simple', question=True, person=3, plural=True)

            self.execute('present_simple', negative=True, question=True, person=1)
            self.execute('present_simple', negative=True, question=True, person=2)
            self.execute('present_simple', negative=True, question=True, person=3)
            self.execute('present_simple',
                         negative=True, question=True, person=1, plural=True)
            self.execute('present_simple',
                         negative=True, question=True, person=2, plural=True)
            self.execute('present_simple',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Geçmiş zaman'
            self.execute('past', person=1)
            self.execute('past', person=2)
            self.execute('past', person=3)
            self.execute('past', person=1, plural=True)
            self.execute('past', person=2, plural=True)
            self.execute('past', person=3, plural=True)

            self.execute('past', negative=True, person=1)
            self.execute('past', negative=True, person=2)
            self.execute('past', negative=True, person=3)
            self.execute('past', negative=True, person=1, plural=True)
            self.execute('past', negative=True, person=2, plural=True)
            self.execute('past', negative=True, person=3, plural=True)

            self.execute('past', negative=True, question=True, person=1)
            self.execute('past', negative=True, question=True, person=2)
            self.execute('past', negative=True, question=True, person=3)
            self.execute('past', negative=True, question=True, person=1, plural=True)
            self.execute('past', negative=True, question=True, person=2, plural=True)
            self.execute('past', negative=True, question=True, person=3, plural=True)

            self.tense = 'Gereklilik kipi'
            self.execute('must', person=1)
            self.execute('must', person=2)
            self.execute('must', person=3)
            self.execute('must', person=1, plural=True)
            self.execute('must', person=2, plural=True)
            self.execute('must', person=3, plural=True)

            self.execute('must', negative=True, person=1)
            self.execute('must', negative=True, person=2)
            self.execute('must', negative=True, person=3)
            self.execute('must', negative=True, person=1, plural=True)
            self.execute('must', negative=True, person=2, plural=True)
            self.execute('must', negative=True, person=3, plural=True)

            self.execute('must', negative=True, question=True, person=1)
            self.execute('must', negative=True, question=True, person=2)
            self.execute('must', negative=True, question=True, person=3)
            self.execute('must', negative=True, question=True, person=1, plural=True)
            self.execute('must', negative=True, question=True, person=2, plural=True)
            self.execute('must', negative=True, question=True, person=3, plural=True)

            self.tense = 'Dilek-Şart kipi'
            self.execute('wish_condition', person=1)
            self.execute('wish_condition', person=2)
            self.execute('wish_condition', person=3)
            self.execute('wish_condition', person=1, plural=True)
            self.execute('wish_condition', person=2, plural=True)
            self.execute('wish_condition', person=3, plural=True)

            self.execute('wish_condition', question=True, person=1)
            self.execute('wish_condition', question=True, person=2)
            self.execute('wish_condition', question=True, person=3)
            self.execute('wish_condition', question=True, person=1, plural=True)
            self.execute('wish_condition', question=True, person=2, plural=True)
            self.execute('wish_condition', question=True, person=3, plural=True)

            self.execute('wish_condition', negative=True, question=True, person=1)
            self.execute('wish_condition', negative=True, question=True, person=2)
            self.execute('wish_condition', negative=True, question=True, person=3)
            self.execute('wish_condition',
                         negative=True, question=True, person=1, plural=True)
            self.execute('wish_condition',
                         negative=True, question=True, person=2, plural=True)
            self.execute('wish_condition',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'İstek kipi'
            self.execute('wish', person=1)
            self.execute('wish', person=2)
            self.execute('wish', person=3)
            self.execute('wish', person=1, plural=True)
            self.execute('wish', person=2, plural=True)
            self.execute('wish', person=3, plural=True)

            self.execute('wish', negative=True, person=1)
            self.execute('wish', negative=True, person=2)
            self.execute('wish', negative=True, person=3)
            self.execute('wish', negative=True, person=1, plural=True)
            self.execute('wish', negative=True, person=2, plural=True)
            self.execute('wish', negative=True, person=3, plural=True)

            self.execute('wish', negative=True, question=True, person=1)
            self.execute('wish', negative=True, question=True, person=2)
            self.execute('wish', negative=True, question=True, person=3)
            self.execute('wish', negative=True, question=True, person=1, plural=True)
            self.execute('wish', negative=True, question=True, person=2, plural=True)
            self.execute('wish', negative=True, question=True, person=3, plural=True)

            self.tense = 'Öğrenilen geçmiş zaman'
            self.execute('learned_past', person=1)
            self.execute('learned_past', person=2)
            self.execute('learned_past', person=3)
            self.execute('learned_past', person=1, plural=True)
            self.execute('learned_past', person=2, plural=True)
            self.execute('learned_past', person=3, plural=True)

            self.execute('learned_past', negative=True, person=1)
            self.execute('learned_past', negative=True, person=2)
            self.execute('learned_past', negative=True, person=3)
            self.execute('learned_past', negative=True, person=1, plural=True)
            self.execute('learned_past', negative=True, person=2, plural=True)
            self.execute('learned_past', negative=True, person=3, plural=True)

            self.execute('learned_past', negative=True, question=True, person=1)
            self.execute('learned_past', negative=True, question=True, person=2)
            self.execute('learned_past', negative=True, question=True, person=3)
            self.execute('learned_past',
                         negative=True, question=True, person=1, plural=True)
            self.execute('learned_past',
                         negative=True, question=True, person=2, plural=True)
            self.execute('learned_past',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Öğrenilen geçmiş zamanın hikayesi'
            self.execute('past_learned_past', person=1)
            self.execute('past_learned_past', person=2)
            self.execute('past_learned_past', person=3)
            self.execute('past_learned_past', person=1, plural=True)
            self.execute('past_learned_past', person=2, plural=True)
            self.execute('past_learned_past', person=3, plural=True)

            self.execute('past_learned_past', negative=True, person=1)
            self.execute('past_learned_past', negative=True, person=2)
            self.execute('past_learned_past', negative=True, person=3)
            self.execute('past_learned_past', negative=True, person=1, plural=True)
            self.execute('past_learned_past', negative=True, person=2, plural=True)
            self.execute('past_learned_past', negative=True, person=3, plural=True)

            self.execute('past_learned_past', negative=True, question=True, person=1)
            self.execute('past_learned_past', negative=True, question=True, person=2)
            self.execute('past_learned_past', negative=True, question=True, person=3)
            self.execute('past_learned_past',
                         negative=True, question=True, person=1, plural=True)
            self.execute('past_learned_past',
                         negative=True, question=True, person=2, plural=True)
            self.execute('past_learned_past',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Öğrenilen geçmiş zamanın rivayeti'
            self.execute('learned_past_learned_past', person=1)
            self.execute('learned_past_learned_past', person=2)
            self.execute('learned_past_learned_past', person=3)
            self.execute('learned_past_learned_past', person=1, plural=True)
            self.execute('learned_past_learned_past', person=2, plural=True)
            self.execute('learned_past_learned_past', person=3, plural=True)

            self.execute('learned_past_learned_past', negative=True, person=1)
            self.execute('learned_past_learned_past', negative=True, person=2)
            self.execute('learned_past_learned_past', negative=True, person=3)
            self.execute('learned_past_learned_past', negative=True, person=1, plural=True)
            self.execute('learned_past_learned_past', negative=True, person=2, plural=True)
            self.execute('learned_past_learned_past', negative=True, person=3, plural=True)

            self.execute('learned_past_learned_past', negative=True, question=True, person=1)
            self.execute('learned_past_learned_past', negative=True, question=True, person=2)
            self.execute('learned_past_learned_past', negative=True, question=True, person=3)
            self.execute('learned_past_learned_past',
                         negative=True, question=True, person=1, plural=True)
            self.execute('learned_past_learned_past',
                         negative=True, question=True, person=2, plural=True)
            self.execute('learned_past_learned_past',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Gelecek zamanın rivayeti'
            self.execute('learned_past_future', person=1)
            self.execute('learned_past_future', person=2)
            self.execute('learned_past_future', person=3)
            self.execute('learned_past_future', person=1, plural=True)
            self.execute('learned_past_future', person=2, plural=True)
            self.execute('learned_past_future', person=3, plural=True)

            self.execute('learned_past_future', negative=True, person=1)
            self.execute('learned_past_future', negative=True, person=2)
            self.execute('learned_past_future', negative=True, person=3)
            self.execute('learned_past_future', negative=True, person=1, plural=True)
            self.execute('learned_past_future', negative=True, person=2, plural=True)
            self.execute('learned_past_future', negative=True, person=3, plural=True)

            self.execute('learned_past_future', negative=True, question=True, person=1)
            self.execute('learned_past_future', negative=True, question=True, person=2)
            self.execute('learned_past_future', negative=True, question=True, person=3)
            self.execute('learned_past_future',
                         negative=True, question=True, person=1, plural=True)
            self.execute('learned_past_future',
                         negative=True, question=True, person=2, plural=True)
            self.execute('learned_past_future',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Gelecek zamanın hikayesi'
            self.execute('past_future', person=1)
            self.execute('past_future', person=2)
            self.execute('past_future', person=3)
            self.execute('past_future', person=1, plural=True)
            self.execute('past_future', person=2, plural=True)
            self.execute('past_future', person=3, plural=True)

            self.execute('past_future', negative=True, person=1)
            self.execute('past_future', negative=True, person=2)
            self.execute('past_future', negative=True, person=3)
            self.execute('past_future', negative=True, person=1, plural=True)
            self.execute('past_future', negative=True, person=2, plural=True)
            self.execute('past_future', negative=True, person=3, plural=True)

            self.execute('past_future', negative=True, question=True, person=1)
            self.execute('past_future', negative=True, question=True, person=2)
            self.execute('past_future', negative=True, question=True, person=3)
            self.execute('past_future',
                         negative=True, question=True, person=1, plural=True)
            self.execute('past_future',
                         negative=True, question=True, person=2, plural=True)
            self.execute('past_future',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Geçmiş zamanın hikayesi'
            self.execute('past_past', person=1)
            self.execute('past_past', person=2)
            self.execute('past_past', person=3)
            self.execute('past_past', person=1, plural=True)
            self.execute('past_past', person=2, plural=True)
            self.execute('past_past', person=3, plural=True)

            self.execute('past_past', negative=True, person=1)
            self.execute('past_past', negative=True, person=2)
            self.execute('past_past', negative=True, person=3)
            self.execute('past_past', negative=True, person=1, plural=True)
            self.execute('past_past', negative=True, person=2, plural=True)
            self.execute('past_past', negative=True, person=3, plural=True)

            self.execute('past_past', negative=True, question=True, person=1)
            self.execute('past_past', negative=True, question=True, person=2)
            self.execute('past_past', negative=True, question=True, person=3)
            self.execute('past_past',
                         negative=True, question=True, person=1, plural=True)
            self.execute('past_past',
                         negative=True, question=True, person=2, plural=True)
            self.execute('past_past',
                         negative=True, question=True, person=3, plural=True)

            self.tense = 'Bilinen geçmiş zamanın şartı'
            self.execute('past_condition', person=1)
            self.execute('past_condition', person=2)
            self.execute('past_condition', person=3)
            self.execute('past_condition', person=1, plural=True)
            self.execute('past_condition', person=2, plural=True)
            self.execute('past_condition', person=3, plural=True)

            self.execute('past_condition', negative=True, person=1)
            self.execute('past_condition', negative=True, person=2)
            self.execute('past_condition', negative=True, person=3)
            self.execute('past_condition', negative=True, person=1, plural=True)
            self.execute('past_condition', negative=True, person=2, plural=True)
            self.execute('past_condition', negative=True, person=3, plural=True)

            self.execute('past_condition', negative=True, question=True, person=1)
            self.execute('past_condition', negative=True, question=True, person=2)
            self.execute('past_condition', negative=True, question=True, person=3)
            self.execute('past_condition',
                         negative=True, question=True, person=1, plural=True)
            self.execute('past_condition',
                         negative=True, question=True, person=2, plural=True)
            self.execute('past_condition',
                         negative=True, question=True, person=3, plural=True)

        self.conn.commit()

        self.conn.close()


test = VerbsTest()
test.proc()
