# -*- coding: utf-8 -*-
import freestyle_brioche

class BriocheDoreeYouPayYourPart(freestyle_brioche.BriocheDoree):
  """
  Implementation de ta propre logique pizza_hook() , que plus personne
  ne touche a ma classe de Base freestyle_brioche.py 
  """
  def pizza_parts_hook(self):
      # Que chacun paye sa part de Pizzas , filles ou  garcons , je
      # m'en fous
      # une part de pizzas par personne sachant que 5 part dans une Pizza
      # cela fait self.members / 5 . et que chacun paye sa part :)
      if len(self.members)>5:
          return len(self.members)

      # J'ai bien peur que avec les discussions unitules sur filles
      # et garcons , developpeurs ou pas qu'on se trouve avec mois
      # de  cinq personnes et dans ce cas , une pizza suffira de
      # cinq part 
      return 5
    

if __name__ =="__main__":
  
   # accueil brioche doree 
   m = BriocheDoreeYouPayYourPart()
   m.start_event = True
   m.entry()

   # au sortir de cet evenement qu'est ce que un membre
   # a gagne , juste des Pizzas ? , a t'il benefie de l'expertis d'Elwan
   # sur PyUnicode , De Joerie avec Jekyll?
   m.reporting()
   
