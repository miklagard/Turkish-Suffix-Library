Turkish.py
==========

### Turkish Suffix Library for Python

## Install 
    pip install turkish-suffix-library

## Using

#### Nouns
    from turkish_suffix_library import turkish

    print(turkish.make_genitive("Öykü", proper_noun=True))
    print(turkish.make_dative("Fatma", proper_noun=True))
    print(turkish.make_dative("Yasin", proper_noun=True))
    print(turkish.make_dative("ALİ", proper_noun=True))
    print(turkish.make_abblative("Ali", proper_noun=True  ))
    print(turkish.make_accusative("Kaliningrad", proper_noun=True))
    print(turkish.make_genitive("ağaç", proper_noun=False))
    print(turkish.make_cccusative("erik", proper_noun=False))
    print(turkish.make_accusative("Erik", proper_noun=True))
    print(turkish.possessive_affix("kavanoz", person=1))
    print(turkish.possessive_affix("kavanoz", person=2))
    print(turkish.possessive_affix("kavanoz", person=3))
    print(turkish.possessive_affix("halter", person=1,plural=True))
    print(turkish.possessive_affix("halter", person=2,plural=True))
    print(turkish.possessive_affix("halter", person=3, quantity=plural))
    print(turkish.possessive_affix("Kenya", person=3, quantity=plural))
        
##### Output
    
    Öykü'nün 
    Fatma'ya 
    Yasin'e 
    ALİ'YE 
    Ali'den 
    Kaliningrad'ı
    ağacın
    eriği
    Erik'i
    kavanozum
    kavanozun
    kavanozu
    halterimiz
    halteriniz
    halterleri
    Kenyaları 

### Verbs
    Parameters: person (1, 2, 3), negative (boolean), question (boolean), plural (boolean)

    turkish.make_infinitive('git')
    > gitmek 
    
    turkish.make_infinitive('git', negative=True)
    > gitmemek

    turkish.make_future('al', person=2, plural=True)  # Second person plural
    > alacaksınız

    turkish.make_present_simple('al', person=1)  # First person single
    > alırım
    
    turkish.make_past('al', person=3, plural=True)
    > aldılar
    
    turkish.make_command('al', person=3, plural=True)
    > alsınlar
    
    turkish.make_present_continuous('ver', person=1)
    > veriyorum
    
    turkish.make_present_continuous_alternative('ver', person=1)
    > vermekteyim
    
    turkish.make_must('ver', person=2)
    > vermelisin
    
    turkish.make_wish_condition('anlat', person=3)
    > anlatsa
    
    turkish.make_wish('sakla', person=3, plural=True)
    > saklayalar
    
    turkish.make_past_perfect('anla', person=3, question=True)
    > anlamış mı
    
    turkish.make_past_past_perfect('sat', person=2, negative=True)
    > satmamıştın
    
    turkish.make_past_perfect_past_perfect('kork', person=3)
    > korkmuşmuş
    
    turkish.make_past_perfect_future('oyna', person=2, negative=True)
    > oynamayacakmışsın
    
    turkish.make_past_future('oyna', person=2, negative=True, question=True)
    > oynamayacak mıydın
    
    turkish.make_past_past('oyna', person=2, negative=True)
    > oynamadıydın
    
    turkish.make_past_condition('gül', person=2)
    > güldüysen

## Turkish Grammar
 * Turkish is a highly agglutinative language, i.e., Turkish words have many grammatical suffixes or endings that determine meaning. Turkish vowels undergo vowel harmony. When a suffix is attached to a stem, the vowel in the suffix agrees in frontness or backness and in roundedness with the last vowel in the stem. Turkish has no gender.

 * Turkish Language is a language with strict rules with only couple of exceptions which makes it very easy for simulating by coding.

 * [More Info](http://en.wikipedia.org/wiki/Turkish_grammar)

## Other Languages 
      C# Version
      https://github.com/yasinkuyu/Turkish.cs
      
      PHP Version
      https://github.com/yasinkuyu/Turkish.php
      
      JavaScript Version
      https://github.com/yasinkuyu/Turkish.js


## Special thanks for C#, PHP and JavaScript versions
      Yasin Kuyu
      https://github.com/yasinkuyu/