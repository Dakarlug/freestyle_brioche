# -*- coding: utf-8 -*-
import Queue, thread, datetime, time

class BriocheDoree:
  __name__ = "MerMoz Dakar"
   
  def __init__(self , args=None):	
    self.members  = []
    # Allons nous avoir 50 pizzas , Joeri :), Alioune :) ......
    # Ok , Puis que il y'a des discussions sur la mailing liste sur
    # combien de pizzas , il y'aura , qui va payer , est ce que cela
    # sera gratuit pour les filles ect , moi je met ici un
    # hook_pizzas , faites en ce que vous voulez mais que personne
    # ne touche plus a mon code 
    # self.pizzas        = 50

    

    # les pizzas waiters
    self.pizza_waiters =Queue.Queue()

    # les speakers
    self.speakers =Queue.Queue()

    # les learners list not queue
    self.learners =[]

  def add_member(self, member):
     # ajouter un membre
     self.members.append(member)
     
  def del_member(self, member):
    #  Un membre doit pouvoir quitter la brioche doree a tout instant 
    # avant que sa femme ne vienne la chercher :)
    self.members.remove(member)

  def pizza_parts_hook(self):
    # A implementer par les polemiqueurs 
    raise NotImplemented 

  def entry(self):
    # entree de la brioche doree les membres sont
    # accuelli ici  a MerMoz :)

    # starting theard before starting entry

    self.event_starting()
    # 
    
    while True:
      raw = raw_input ("Accueil Brioche doree :\n\
         Pesentateur : Nom, Presentation \n\
         Learners :Nom,1    : \n\
         Pizzas Waiters :Nom , 0:\n\
        ")
      if raw =="stop":
        # stop
        # evitez d'arreter l'event sans que les pizzas ne soient
        # distribués sinion , les pizza_waiters vont tous saccager
        # stop apres que les pizzas soit distibues.
        
        self.start_event = False
        break
      
      m = Member(raw)
      print m
      # Add to member list
      self.members.append(m)
      
      # lorsque un membre ne fait rien d'autre  que attendre les pizzas
      # met le dans la pile  pizza_waiters

      if m.presentation == "0":
        self.pizza_waiters.put(m)

       # lorque un gas vient pour suivre les prensentations  des speakers:
      if m.presentation == "1":
        self.learners.append(m)

      else:
        self.speakers.put(m) 
      # lorsque un membre prose une presentation , le mettre dans la
      # pile des speakers

  def event_starting(self):
    # Joeri a dit que l'evenment commence a 19  heures 30 le dimanche donc
    # pas  avant :
    thread.start_new_thread(self.starting_event , ())
    
  def starting_event(self):
    while self.start_event:
      
      try:
        #print "starting events"
        # PIZZA WAITER
        try:
          # get nowait
          a_pizza_waiter = self.pizza_waiters.get(False)
        except Queue.Empty:
           a_pizza_waiter =None
          

        # un pizza waiter ne fait rien d'autre que bouffer :)
        # il s'en tape des presentations , Lien Rag  :)

        # Il faut tester si il est l'heure de donner des pizzas , a 20 h 30 ? c'est bon 
        # et lui donner sa part :)  : 

        # part  = Nombre  de Pizzas disponibles / (speakers + learners + pizza_waiters_queue)


        # la distrubtion des Pizzas commence a cette heure
        if datetime.datetime.now()> datetime.datetime(2013, 10, 11, 11, 06):
            # Fix de ElWan :)
            if len(self.members):
              self.pizzas  = self.pizza_parts_hook()
              part   = self.pizzas / len(self.members)

            # Moins il y'aura de personnes presentes a la brioche plus il y'aura de
            # parts de Pizzas , Huuuuum :) . c'est le souhait des pizzas waiters
            # Hein Lien :)
            if a_pizza_waiter:
              a_pizza_waiter.gains.append("%s part de Pizzas" % part )
                
        # SPEAKERS

        # un speaker vient donner une presention , alors il faut extraire le contenu 
        # de la presentation et le donner a un LEARNER
        try:
          # get nowait
          speaker= self.speakers.get(False)
        except Queue.Empty:
           speaker =None

        if speaker:
          presentation = speaker.presentation
          for learner in self.learners:
            if presentation not in learner.gains:
              learner.gains.append(presentation)

              
      except:
        import traceback
        print traceback.format_exc()
        
      time.sleep(2)
    # event stopped , est sans doute 20 heures passes
    #print "stopped event"

      


  def  stop_event(self):
    # Lorque a 20 heures , on doit finaliser l'evenement avant que Madame Dia 
    # se pointe a la Brioche doree pour me tirer les oreils
    #if datetime.datetime.now()> datetime.datetime(2013, 10, 10, 18, 10):
    self.start_event = False 

  def start_event(self):
    # Demarrage  hostilites (Presentions, manageurs de Pizzas , les apprenants)
    self.start_event  =True

  def reporting(self):
    # au sortir de cet evenement qu'est ce que un membre
    # a gagne , juste des Pizzas ? , a t'il benefie de l'expertis d'Elwan
    # sur PyUnicode , De Joerie avec Jekyll?
    
    for m in self.members:
      print m
      print m.gains

  
"""
Les membres de DakarLug qui viendront a la brioche doree le Dimanche 
13  Novembre a 19 heures 30 
.
1 .  Si presentation n'est pas vide , la personne propose de faire une presentation

Exemple : Waly Ndiaye fait une presentation sur PyUnicode dont son attribut 
presentation  = "PyUnicode"

2 . Si un membre est venu pour suivre une presentation alors son attribut 
leaner = True  

3. Si la personne est venu juste pour bouffer nos pizzas alors presentation = ""
et learner  = ""

"""
class Member:
  def __init__(self, raw):

    # raw.split()
    args  = raw.split(",")
    print args
    if len(args)!=2:
       raise ValueError("Erreur saisie ")
    # speaker or learner :
    if args[1].strip() == "1":
      # learner:
      self.presentation = "1"
    elif args[1].strip() == "0":
      # pizzas waiters
      self.presentation = "0"
    else:
      self.presentation = args[1]
    self.name = args[0]

    # Qu'est ce que tu as gagne ,  a lissue de l'evenement
    # Brioche doree
    self.gains =[]
    
  def what_gain(self):
    """
     ce que le membre qui est venu a la brioche dorée a gagne au sortir 
    de  cet evenement 
    """
    print "%s a  appris a la fin de cette presentation" 
    for gain in gains:
      print gain

  def __str__(self):
    return "<Mamber presentation =%s  , name =%s , >"%(
      self.presentation, self.name)



