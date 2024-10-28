import random
password_dictionary = {
'0':'ly', 
'1':'!J', 
'2':'Px', 
'3':'@A', 
'4':'&g', 
'5':'#z', 
'6':'?x', 
'7':'lZ', 
'8':'y5',
'9':'Fn',
'a':'$2',
'A':'%1',
'b':'2A',
'B':'1x',
'c':'3T',
'C':'6s',
'd':'!2',
'D':'6z',
'e':'Ax',
'E':'2!',
'f':'4g',
'F':'3g',
'g':'ax',
'G':'1@',
'h':'H1',
'H':'p!',
'i':'i2',
'I':'i3',
'j':'4$',
'J':'R1',
'k':'R2',
'K':'z#',
'l':'<1',
'L':'>$',
'm':'F3',
'M':'Ce',
'n':'zQ',
'N':'3p',
'o':'tr',
'O':'xs',
'p':'<t',
'P':'>r',
'q':'yz',
'Q':'E3',
'r':'f4',
'R':'%1',
's':'$3',
'S':'#0',
't':'iB',
'T':'4!',
'u':'.o',
'U':'v3',
'v':'z.',
'V':'k#',
'x':'1X',
'X':'qP',
'w':'3#',
'W':'>i',
'y':'b4',
'Y':'n7',
'z':'m4',
'Z':'s2'
}
#this basic program generates a password
def crypto(password):
  count = 0
  new_pass = []
  pass_len = len(password)
  while count < pass_len:
    new_pass.append(password_dictionary[password[count]])
    count+=1
  return "".join(new_pass)
  
type_pass = input("What kind of password you want:\n 1- Random 15 or more digits pwd \n 2- Create basic pwd based on input \n")
match type_pass:
  case "1":
    pass_int = str(random.getrandbits(28))
    print(crypto(pass_int))
  case "2":
    inp_pass = input('Enter a password (only numbers and letters):\n')
    print(crypto(inp_pass))