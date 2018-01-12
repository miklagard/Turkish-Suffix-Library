Turkish.py
==========

### Turkish Suffix Library for Python

## Install 

## Using
    
    tr = turkish()

    print tr.makeGenitive("Öykü", { proper_noun : true } )
    print tr.makeDative("Fatma", { proper_noun : true } )
    print tr.makeDative("Yasin", { proper_noun : true } )
    print tr.makeDative("ALİ", { proper_noun : true } )
    print tr.makeAblative("Ali", { proper_noun : true } )
    print tr.makeAccusative("Kaliningrad", { proper_noun : true } )
    print tr.makeGenitive("ağaç", { proper_noun : false } )
    print tr.makeAccusative("erik", { proper_noun : false } )
    print tr.makeAccusative("Erik", { proper_noun : true } )
    print tr.possessiveAffix("kavanoz", { person : "1", quantity : "singular" } )
    print tr.possessiveAffix("kavanoz", {  person : "2", quantity : "singular"} )
    print tr.possessiveAffix("kavanoz", {  person : "3", quantity : "singular"} )
    print tr.possessiveAffix("halter", {  person : "1", quantity : "plural"} )
    print tr.possessiveAffix("halter", {  person : "2", quantity : "plural"} )
    print tr.possessiveAffix("halter", {  person : "3", quantity : "plural"} )
    print tr.possessiveAffix("Kenya", {  person : "3", quantity : "plural"} )
        
# Output
    
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