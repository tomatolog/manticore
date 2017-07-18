Quick summary of the ranking factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Table 5.1.

+------+------+------+------+
| Name | Leve | Type | Summ |
|      | l    |      | ary  |
+======+======+======+======+
| max\ | quer | int  | maxi |
| _lcs | y    |      | mum  |
|      |      |      | poss |
|      |      |      | ible |
|      |      |      | LCS  |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | for  |
|      |      |      | the  |
|      |      |      | curr |
|      |      |      | ent  |
|      |      |      | quer |
|      |      |      | y    |
+------+------+------+------+
| bm25 | docu | int  | quic |
|      | ment |      | k    |
|      |      |      | esti |
|      |      |      | mate |
|      |      |      | of   |
|      |      |      | BM25 |
|      |      |      | (1.2 |
|      |      |      | ,    |
|      |      |      | 0)   |
|      |      |      | with |
|      |      |      | out  |
|      |      |      | synt |
|      |      |      | ax   |
|      |      |      | supp |
|      |      |      | ort  |
+------+------+------+------+
| bm25 | docu | int  | prec |
| a(k1 | ment |      | ise  |
| ,    |      |      | BM25 |
| b)   |      |      | ()   |
|      |      |      | valu |
|      |      |      | e    |
|      |      |      | with |
|      |      |      | conf |
|      |      |      | igur |
|      |      |      | able |
|      |      |      | K1,  |
|      |      |      | B    |
|      |      |      | cons |
|      |      |      | tant |
|      |      |      | s    |
|      |      |      | and  |
|      |      |      | synt |
|      |      |      | ax   |
|      |      |      | supp |
|      |      |      | ort  |
+------+------+------+------+
| bm25 | docu | int  | prec |
| f(k1 | ment |      | ise  |
| ,    |      |      | BM25 |
| b,   |      |      | F()  |
| {fie |      |      | valu |
| ld=w |      |      | e    |
| eigh |      |      | with |
| t,   |      |      | extr |
| …})  |      |      | a    |
|      |      |      | conf |
|      |      |      | igur |
|      |      |      | able |
|      |      |      | fiel |
|      |      |      | d    |
|      |      |      | weig |
|      |      |      | hts  |
+------+------+------+------+
| fiel | docu | int  | bit  |
| d\_m | ment |      | mask |
| ask  |      |      | of   |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | fiel |
|      |      |      | ds   |
+------+------+------+------+
| quer | docu | int  | numb |
| y\_w | ment |      | er   |
| ord\ |      |      | of   |
| _cou |      |      | uniq |
| nt   |      |      | ue   |
|      |      |      | incl |
|      |      |      | usiv |
|      |      |      | e    |
|      |      |      | keyw |
|      |      |      | ords |
|      |      |      | in a |
|      |      |      | quer |
|      |      |      | y    |
+------+------+------+------+
| doc\ | docu | int  | numb |
| _wor | ment |      | er   |
| d\_c |      |      | of   |
| ount |      |      | uniq |
|      |      |      | ue   |
|      |      |      | keyw |
|      |      |      | ords |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | in   |
|      |      |      | the  |
|      |      |      | docu |
|      |      |      | ment |
+------+------+------+------+
| lcs  | fiel | int  | Long |
|      | d    |      | est  |
|      |      |      | Comm |
|      |      |      | on   |
|      |      |      | Subs |
|      |      |      | eque |
|      |      |      | nce  |
|      |      |      | betw |
|      |      |      | een  |
|      |      |      | quer |
|      |      |      | y    |
|      |      |      | and  |
|      |      |      | docu |
|      |      |      | ment |
|      |      |      | ,    |
|      |      |      | in   |
|      |      |      | word |
|      |      |      | s    |
+------+------+------+------+
| user | fiel | int  | user |
| \_we | d    |      | fiel |
| ight |      |      | d    |
|      |      |      | weig |
|      |      |      | ht   |
+------+------+------+------+
| hit\ | fiel | int  | tota |
| _cou | d    |      | l    |
| nt   |      |      | numb |
|      |      |      | er   |
|      |      |      | of   |
|      |      |      | keyw |
|      |      |      | ord  |
|      |      |      | occu |
|      |      |      | rren |
|      |      |      | ces  |
+------+------+------+------+
| word | fiel | int  | numb |
| \_co | d    |      | er   |
| unt  |      |      | of   |
|      |      |      | uniq |
|      |      |      | ue   |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | keyw |
|      |      |      | ords |
+------+------+------+------+
| tf\_ | fiel | floa | sum( |
| idf  | d    | t    | tf\* |
|      |      |      | idf) |
|      |      |      | over |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | keyw |
|      |      |      | ords |
|      |      |      | ==   |
|      |      |      | sum( |
|      |      |      | idf) |
|      |      |      | over |
|      |      |      | occu |
|      |      |      | rren |
|      |      |      | ces  |
+------+------+------+------+
| min\ | fiel | int  | firs |
| _hit | d    |      | t    |
| \_po |      |      | matc |
| s    |      |      | hed  |
|      |      |      | occu |
|      |      |      | rren |
|      |      |      | ce   |
|      |      |      | posi |
|      |      |      | tion |
|      |      |      | ,    |
|      |      |      | in   |
|      |      |      | word |
|      |      |      | s,   |
|      |      |      | 1-ba |
|      |      |      | sed  |
+------+------+------+------+
| min\ | fiel | int  | firs |
| _bes | d    |      | t    |
| t\_s |      |      | maxi |
| pan\ |      |      | mum  |
| _pos |      |      | LCS  |
|      |      |      | span |
|      |      |      | posi |
|      |      |      | tion |
|      |      |      | ,    |
|      |      |      | in   |
|      |      |      | word |
|      |      |      | s,   |
|      |      |      | 1-ba |
|      |      |      | sed  |
+------+------+------+------+
| exac | fiel | bool | whet |
| t\_h | d    |      | her  |
| it   |      |      | quer |
|      |      |      | y    |
|      |      |      | ==   |
|      |      |      | fiel |
|      |      |      | d    |
+------+------+------+------+
| min\ | fiel | floa | min( |
| _idf | d    | t    | idf) |
|      |      |      | over |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | keyw |
|      |      |      | ords |
+------+------+------+------+
| max\ | fiel | floa | max( |
| _idf | d    | t    | idf) |
|      |      |      | over |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | keyw |
|      |      |      | ords |
+------+------+------+------+
| sum\ | fiel | floa | sum( |
| _idf | d    | t    | idf) |
|      |      |      | over |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | keyw |
|      |      |      | ords |
+------+------+------+------+
| exac | fiel | bool | whet |
| t\_o | d    |      | her  |
| rder |      |      | all  |
|      |      |      | quer |
|      |      |      | y    |
|      |      |      | keyw |
|      |      |      | ords |
|      |      |      | were |
|      |      |      | a)   |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | and  |
|      |      |      | b)   |
|      |      |      | in   |
|      |      |      | quer |
|      |      |      | y    |
|      |      |      | orde |
|      |      |      | r    |
+------+------+------+------+
| min\ | fiel | int  | mini |
| _gap | d    |      | mum  |
| s    |      |      | numb |
|      |      |      | er   |
|      |      |      | of   |
|      |      |      | gaps |
|      |      |      | betw |
|      |      |      | een  |
|      |      |      | the  |
|      |      |      | matc |
|      |      |      | hed  |
|      |      |      | keyw |
|      |      |      | ords |
|      |      |      | over |
|      |      |      | the  |
|      |      |      | matc |
|      |      |      | hing |
|      |      |      | span |
|      |      |      | s    |
+------+------+------+------+
| lccs | fiel | int  | Long |
|      | d    |      | est  |
|      |      |      | Comm |
|      |      |      | on   |
|      |      |      | Cont |
|      |      |      | iguo |
|      |      |      | us   |
|      |      |      | Subs |
|      |      |      | eque |
|      |      |      | nce  |
|      |      |      | betw |
|      |      |      | een  |
|      |      |      | quer |
|      |      |      | y    |
|      |      |      | and  |
|      |      |      | docu |
|      |      |      | ment |
|      |      |      | ,    |
|      |      |      | in   |
|      |      |      | word |
|      |      |      | s    |
+------+------+------+------+
| wlcc | fiel | floa | Weig |
| s    | d    | t    | hted |
|      |      |      | Long |
|      |      |      | est  |
|      |      |      | Comm |
|      |      |      | on   |
|      |      |      | Cont |
|      |      |      | iguo |
|      |      |      | us   |
|      |      |      | Subs |
|      |      |      | eque |
|      |      |      | nce, |
|      |      |      | sum( |
|      |      |      | idf) |
|      |      |      | over |
|      |      |      | cont |
|      |      |      | iguo |
|      |      |      | us   |
|      |      |      | keyw |
|      |      |      | ord  |
|      |      |      | span |
|      |      |      | s    |
+------+------+------+------+
| atc  | fiel | floa | Aggr |
|      | d    | t    | egat |
|      |      |      | e    |
|      |      |      | Term |
|      |      |      | Clos |
|      |      |      | enes |
|      |      |      | s,   |
|      |      |      | log( |
|      |      |      | 1+su |
|      |      |      | m(id |
|      |      |      | f1\  |
|      |      |      | *idf |
|      |      |      | 2*\  |
|      |      |      | pow( |
|      |      |      | dist |
|      |      |      | ance |
|      |      |      | ,    |
|      |      |      | -1.7 |
|      |      |      | 5))  |
|      |      |      | over |
|      |      |      | the  |
|      |      |      | best |
|      |      |      | pair |
|      |      |      | s    |
|      |      |      | of   |
|      |      |      | keyw |
|      |      |      | ords |
+------+------+------+------+
