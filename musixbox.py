def read_strip(filename):
  musicdic = {}
  with open(filename,"r") as myfile:
    for l in myfile:
      fileline = l.split()
      key = fileline[0]
      value = []
      for x in fileline[1:]:
        value.append(int(x))
        #key,value = fileline[0],fileline[1:] tuple defines dic key and value
      musicdic[key] = value
  #print(musicdic)
  return musicdic

def play_music(score):
  chordlist = [] 
  keys = list(score.keys())
  values = list(score.values())
  for i in range(len(values[0])):
      chord = []
      for j in range(len(keys)):
        if values[j][i] == 1:
          chord.append(keys[j])
      chordlist.append(chord)
  return chordlist
  
  
    