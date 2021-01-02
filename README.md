Turkish.py
==========

### Turkish Suffix Library for Python

## Install 
    pip install turkish-suffix-library

## Using

#### Nouns
    from turkish_suffix_library.turkish import Turkish

    print(Turkish('Öykü').genitive(proper_noun=True).to_string())
    print(Turkish('Cem').dative(proper_noun=True).to_string())
    print(Turkish('Nil').dative(proper_noun=True).to_string())
    print(Turkish('ALİ').dative(proper_noun=True).to_string())
    print(Turkish('Taylan').ablative(proper_noun=True).to_string())
    print(Turkish('Amasya').accusative(proper_noun=True).to_string())
    print(Turkish('ağaç').genitive(proper_noun=False).to_string())
    print(Turkish('erik').accusative(proper_noun=False).to_string())
    print(Turkish('Erik').accusative(proper_noun=True).to_string())
    print(Turkish('kavanoz').possessive_affix(person=1).to_string())
    print(Turkish('kavanoz').possessive_affix(person=2).to_string())
    print(Turkish('kavanoz').possessive_affix(person=3).to_string())
    print(Turkish('halter').possessive_affix(person=1, plural=True).to_string())
    print(Turkish('halter').possessive_affix(person=2, plural=True).to_string())
    print(Turkish('halter').possessive_affix(person=3, plural=True).to_string())
    print(Turkish('Kenya').possessive_affix(person=3, plural=True).to_string())
        
##### Output
    
    Öykü'nün 
    Cem'e 
    Nil'e 
    ALİ'YE 
    Taylan'dan 
    Amasya'yı
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

    Turkish('git').infinitive().to_string()
    > gitmek 
    
    Turkish('git').infinitive(negative=True).to_string()
    > gitmemek

    Turkish('al').future(person=2, plural=True).to_string()  # Second person plural
    > alacaksınız

    Turkish('al').present_simple(person=1).to_string()  # First person single
    > alırım
    
    Turkish('al').past(person=3, plural=True).to_string()
    > aldılar
    
    Turkish('al').command(person=3, plural=True).to_string()
    > alsınlar
    
    Turkish('ver').present_continuous(person=1).to_string()
    > veriyorum
    
    Turkish('ver').present_continuous_alternative(person=1).to_string()
    > vermekteyim
    
    Turkish('ver').must(person=2).to_string()
    > vermelisin
    
    Turkish('anlat').wish_condition(person=3).to_string()
    > anlatsa
    
    Turkish('sakla').wish(person=3, plural=True).to_string()
    > saklayalar
    
    Turkish('anla').learned_past(person=3, question=True).to_string()
    > anlamış mı
    
    Turkish('sat').past_learned_past(person=2, negative=True).to_string()
    > satmamıştın
    
    Turkish('kork').learned_past_learned_past(person=3).to_string()
    > korkmuşmuş
    
    Turkish('oyna').learned_past_future(person=2, negative=True).to_string()
    > oynamayacakmışsın
    
    Turkish('oyna').past_future(person=2, negative=True, question=True).to_string()
    > oynamayacak mıydın
    
    Turkish('oyna').past_past(person=2, negative=True).to_string()
    > oynamadıydın
    
    Turkish('gül').past_condition(person=2).to_string()
    > güldüysen

## Turkish Grammar
 * Turkish is a highly agglutinative language, i.e., Turkish words have many 
   grammatical suffixes or endings that determine meaning. Turkish vowels 
   undergo vowel harmony. When a suffix is attached to a stem, the vowel in 
   the suffix agrees in frontness or backness and in roundedness with the last 
   vowel in the stem. Turkish has no gender.

 * Turkish Language is a language with strict rules with an only couple of 
   exceptions which makes it very easy for simulating by coding.

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