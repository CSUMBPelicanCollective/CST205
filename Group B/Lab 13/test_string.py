#Jiwanjot Sandhu
#Pelican Collective
#Lab 13
#source https://finance.yahoo.com/news/tesla-hopes-deliver-wheel-drive-193300742.html

def main():
  changer = []
  showInformation("***Memory Test***\n Let's see if yo can memorize this short excerpt from an article and remember four key words \nAt present, Tesla is making just over 2,000 Model 3 units per week. That's much better than it has been, but Musk wants production to increase to 5,000 cars per week before he's comfortable with AWD. That gives you a hint as to how well things are faring -- Tesla originally planned to hit that goal by last December.")


  while (len(changer) < 3):
    if not changer:
      edit = requestString("How many units you think tesla is making? \nEnter a number below")
      changer.append(edit)
      showInformation("At present, Tesla is making just over" + " "  + changer[0] + " " + "Model 3 units per ___. That's much better than it has been, but Musk wants production to increase to ___ cars per week before he's comfortable with AWD. That gives you a hint as to how well things are faring -- Tesla originally planned to hit that goal by last ___.")
    if (changer[0]):
      edit = requestString("Over what time period are these units being produced? \nEnter your answer below")
      changer.append(edit)
      showInformation("At present, Tesla is making just over" + " " + changer[0] + " " + "Model 3 units per " + " " + changer[1] + ". " + "That's much better than it has been, but Musk wants production to increase to ___ cars per week before he's comfortable with AWD. That gives you a hint as to how well things are faring -- Tesla originally planned to hit that goal by last ___.")
    if (changer[1]):
      edit = requestString("What number does Elon Musk wants to increase the production by per week? \nEnter that number below")
      changer.append(edit)
      showInformation("At present, Tesla is making just over" + " " + changer[0] + " " + "Model 3 units per " + " " + changer[1] + ". " + "That's much better than it has been, but Musk wants production to increase to" + " " + changer[2] + " " + "cars per week before he's comfortable with AWD. That gives you a hint as to how well things are faring -- Tesla originally planned to hit that goal by last ___.")
    if (changer[2]):
      edit = requestString("What month does he wants to achieve this goal by? \nEnter that number below")
      changer.append(edit)
      showInformation("***Original Excerpt*** \nAt present, Tesla is making just over 2,000 Model 3 units per week. That's much better than it has been, but Musk wants production to increase to 5,000 cars per week before he's comfortable with AWD. That gives you a hint as to how well things are faring -- Tesla originally planned to hit that goal by last December. \n***Your work*** \nAt present, Tesla is making just over" + " " + changer[0] + " " + "Model 3 units per " + " " + changer[1] + ". " + "That's much better than it has been, but Musk wants production to increase to" + " " + changer[2] + " " + "cars per week before he's comfortable with AWD. That gives you a hint as to how well things are faring -- Tesla originally planned to hit that goal by last" + " " + changer[3] + " " + ".")
    if (changer[3]):
      showInformation("Thank you for playing")
main ()