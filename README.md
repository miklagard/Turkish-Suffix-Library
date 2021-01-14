Turkish.py
==========

### Turkish Suffix Library for Python

## Install 
    pip install turkish-suffix-library

## Using

#### Nouns
    from turkish_suffix_library.turkish import Turkish

    print(Turkish('araba').dative())
    print(Turkish('sebep').ablative())
    print(Turkish('sebep').accusative())
    print(Turkish('ecdat').accusative())
   
    print(Turkish('çanta').plural().possessive(person=1).ablative().to_json())
    print(Turkish('aparat').possessive(person=2))
    print(Turkish('batak').possessive(person=3))
   
    print(Turkish('idrak').possessive(person=1, plural=True))
    print(Turkish('ok').possessive(person=2, plural=True))
    print(Turkish('çanta').possessive(person=3, plural=True))
   
    print(f'{Turkish("Elif").genitive(proper_noun=True)} {Turkish("Öküz").possessive(person=3)}.')
   
    print(Turkish('dört').ordinal())
    print(Turkish('yedi').distributive())
    Turkish('kedi').instrumental()

        
##### Output
    arabaya
    sebepten
    sebebi
    ecdadı
    {
         'result': 'çantalarımdan', 
         'stem': 'çanta', 
         'history': [
            {'action': 'plural', 'current': 'çantalar', 'kwargs': {}}, 
            {'action': 'possessive', 'current': 'çantalarım', 'kwargs': {'person': 1}}, 
            {'action': 'ablative', 'current': 'çantalarımdan', 'kwargs': {}}
         ]
    }
    aparatın
    batağı
    idrakımız
    okunuz
    çantaları
    Elif'in Öküzü.
    dördüncü
    yedişer
    kediyle


## Turkish Grammar
 * Turkish is a highly agglutinative language, i.e., Turkish words have many 
   grammatical suffixes or endings that determine meaning. Turkish vowels 
   undergo vowel harmony. When a suffix is attached to a stem, the vowel in 
   the suffix agrees in frontness or backness and in roundedness with the last 
   vowel in the stem. Turkish has no gender.

 * Turkish Language is a language with strict rules with an only couple of 
   exceptions which makes it very easy for simulating by coding.

 * [More Info](http://en.wikipedia.org/wiki/Turkish_grammar)

## User Interface

The most of the methods are not supported yet, under development

* Source code: https://github.com/miklagard/tr

* Demo: https://trstem.com

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