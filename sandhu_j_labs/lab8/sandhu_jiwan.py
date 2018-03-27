#Jiwanjot Sandhu
#Pelican Collective
#LAB 8

def sound():
  filename = pickAFile()
  s = makeSound(filename)
  return (s)

#decrease volume
def decreaseVolume(s):
  for sample in getSamples(s):
    val = getSampleValue(sample)
    setSampleValue(sample, val / 2)
  play(s)

#change volume
def cVol(add_Val):
  for sample in getSamples(s):
    val = getSampleValue(sample)
    setSampleValue(sample, val * 0.01 * add_Val)
  play(s)

#max sample
def maxSample(s)
  m_val = 0;
  for sample in getSamples(s)
    m_val = max(m_val, getSample(sample))
  return m_val

#max Volume
def maxVolume(m_val):
  m_rate = 32767 / m_val
  for sample in getSamples(s)
    up = m_rate * getSample(s)
    setSample(sample, up)
  play(s)

#go to eleven
def goToEleven(s)
  for i in range(0, getLength(s)):
  all = getSampleValueAt(s, i)
  if(i > 0):
    setSampleValueAt(s, i, 32767)
  elif(i < 0):
    setSampleValueAt(s, i, -32767)
  play(s)