freestyle_brioche
=================

freestyle_brioche



freestyle_brioche_doree.py by Alioune Dia 10-10-2013 16:50 in Python 2.6

Une brioche doree , en plus d'accueillir des gens , qui vont proposer des 
prensentations , qui vont commencer exactement a 19 heures ,  et j'imagine 
 que a  20  heures ont va manger des Pizzas et parler de sujets extras , alors 
comment doit on ecrire tout  ca en Python ?
En plus de la class BriocheDoree qui va acceillir , distribtions Pizzas ,
et .....
Les membres de DakarLug qui viendront a la brioche doree le Dimanche 
13  Novembre a 19 heures 30 
.
1 .  Si presentation n'est pas vide , la personne propose de faire une
presentation
Exemple : Waly Ndiaye fait une presentation sur PyUnicode dont son attribut 
presentation  = "PyUnicode"
2 . Si un membre est venu pour suivre une presentation alors son attribut
presentation  =""
leaner = 1  
3. Si la personne est venu juste pour bouffer nos pizzas alors
presentation = "" et learner  = 0


L'exection de ca :
__________________

['alioune', '0']
['Lien', '1']
['Pat', '1']
['Elwan', 'PyUnicode']


L'exection donnera:
___________________

<Mamber presentation =0  , name =alioune , >
gain = []
<Mamber presentation =1  , name =Lien , >
gain = ["'PyUnicode'"]
<Mamber presentation =1  , name =Pat , >
gain =["'PyUnicode'"]
<Mamber presentation ='PyUnicode'  , name =Elwan , >
[]

On conclut que Alioune qui ete juste venu pour manger de Pizzas
aura comme gains = [] :) , Lien Rag et Patt qui sont venu suivre
la presention [PyUnicode] de Elwan ont des gains de gain =["'PyUnicode'"]


Tellement fier de mon freestyle_brioche.py que je viens de la
mettre sut git 