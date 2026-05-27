def txt2bin(txt):
  bin = []
  for c in txt:
    bin.append(padzero(dec2bin(ord(c)),8))
  return "".join(bin)

def bin2invisible(bin):
  inv = []
  for b in bin:
    if b=='0':
      inv.append(' ')
    else:
      inv.append('	')
  return "".join(inv)

def txt2invisible(txt):
  return bin2invisible(txt2bin(txt))

def invisible2bin(inv):
  i = 0
  tobinary = ""
  for i in range(len(inv)):
    if(inv[i] == ' '):
      tobinary += "0"
    if(inv[i] == '	'):
      tobinary += "1"
  return tobinary
  
def bin2txt(inv):
  i = 0
  text = ""
  chunk  = []
  for i in range(0 ,len(inv) ,8):
    chunk  = inv[i:i+8]
    text += chr(bin2dec(chunk))
  return text
  

def invisible2txt(inv):
  return bin2txt(invisible2bin(inv))
