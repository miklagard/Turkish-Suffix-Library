from turkish_suffix_library.turkish import Turkish
import sqlite3
from turkish_suffix_library.sample_verbs_list import VERBS

TENSES = [
    'imperative_mood',
    'present_continuous_simple',
    'simple_tense',
    'past_definite',
    'past_progressive_dubitative',
    'past_progressive_alternative_dubitative',
    'indefinite_past',
    'past_progressive_narrative',
    'past_progressive_alternative_narrative',
    'past_perfect_narrative',
    'doubtful_distant_past',
    'past_in_the_future',
    'past_conditional_narrative',
    'past_conditional_dubitative',
    'future_simple',
    'future_in_the_past',
    'future_dubitative',
    'future_conditional',
    'necessitative_mood_simple_tense',
    'necessitative_past_narrative',
    'necessitative_past_dubitative',
    'conditional_mood_simple_tense',
    'subjunctive_mood_simple_tense',
    'past_definite_narrative',
    'past_indefinite_past',
    'indefinite_past_future',
    'past_future'
]


class VerbsTest:
    def __init__(self):
        self.tense = None
        self.verb = None

        self.conn = sqlite3.connect('database.db')
        self.conn.execute('delete from verbs')

    def execute(self, **kwargs):
        generated = eval("Turkish('%s').%s(**%s)" % (self.verb, self.tense, kwargs))

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
            print(self.verb)
            self.tense = 'infinitive'
            self.execute()
            self.execute(negative=True)

            for tense in TENSES:
                self.tense = tense
                self.execute(person=1)
                self.execute(person=2)
                self.execute(person=3)
                self.execute(person=1, plural=True)
                self.execute(person=2, plural=True)
                self.execute(person=3, plural=True)

                self.execute(negative=True, person=1)
                self.execute(negative=True, person=2)
                self.execute(negative=True, person=3)
                self.execute(negative=True, person=1, plural=True)
                self.execute(negative=True, person=2, plural=True)
                self.execute(negative=True, person=3, plural=True)

                self.execute(negative=True, question=True, person=1)
                self.execute(negative=True, question=True, person=2)
                self.execute(negative=True, question=True, person=3)
                self.execute(negative=True, question=True, person=1, plural=True)
                self.execute(negative=True, question=True, person=2, plural=True)
                self.execute(negative=True, question=True, person=3, plural=True)

        self.conn.commit()

        self.conn.close()


test = VerbsTest()
test.proc()
