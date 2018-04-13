file = open("C:\\Users\\rocky.moreno\\Documents\\GitHub\\CST205\\moreno_r_labs\\lab16\\superweb.html", "wt")

def addText():
  return "<h1><b>Hell<br>llo</h1>"


def makePage():
  #replace the directory in the line below with the path to your file
  file.write("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 
  Transition//EN" "http://www.w3.org/TR/html4/loose.dtd">
  
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  
  <body>
  
  <h1>MY PYTHON PAGE!!!</h1>
  """
  
  + addText() +
  
  """
  </body>
  </html>""")
  
makePage()

file.close()