##Wordle##
import random
new_board = []
for i in range(6):
    new_board.append(["-","-","-","-","-","-"])
## Printing out the board and choosing a random word from the word bank ##
def print_board():
  board = []
  for i in range(6):
    board.append(["-","-","-","-","-","-"])
  for i in range(6):
    print((" ").join(board[i]))
def random_word():
  random_num = random.randint(0,499)
  word = word_bank(random_num)
  return word
def word_bank(random_num):
  word_bank = ["abroad","accept","access","across","acting","action","active","actual","advice","advise","affect","afford","afraid","agency","agenda","almost","always","amount","animal","annual","answer","anyone","anyway","appeal","appear","around","arrive","artist","aspect","assess","assist","assume","attack","attend","august","author","avenue","backed","barely","battle","beauty","became","become","before","behalf","behind","belief","belong","berlin","better","beyond","bishop","border","bottle","bottom","bought","branch","breath","bridge","bright","broken","budget","burden","bureau","button","camera","cancer","cannot","carbon","career","castle","casual","caught","center","centre","chance","change","charge","choice","choose","chosen","church","circle","client","closed","closer","coffee","column","combat","coming","common","comply","copper","corner","costly","county","couple","course","covers","create","credit","crisis","custom","damage","danger","dealer","debate","decade","decide","defeat","defend","define","degree","demand","depend","deputy","desert","design","desire","detail","detect","device","differ","dinner","direct","doctor","dollar","domain","double","driven","driver","during","easily","eating","editor","effect","effort","eighth","either","eleven","emerge","empire","employ","enable","ending","energy","engage","engine","enough","ensure","entire","entity","equity","escape","estate","ethnic","exceed","except","excess","expand","expect","expert","export","extend","extent","fabric","facing","factor","failed","fairly","fallen","family","famous","father","fellow","female","figure","filing","finger","finish","fiscal","flight","flying","follow","forced","forest","forget","formal","format","former","foster","fought","fourth","French","friend","future","garden","gather","gender","german","global","golden","ground","growth","guilty","handed","handle","happen","hardly","headed","health","height","hidden","holder","honest","impact","import","income","indeed","injury","inside","intend","intent","invest","island","itself","jersey","joseph","junior","killed","labour","latest","latter","launch","lawyer","leader","league","leaves","legacy","length","lesson","letter","lights","likely","linked","liquid","listen","little","living","losing","lucent","luxury","mainly","making","manage","manner","manual","margin","marine","marked","market","martin","master","matter","mature","medium","member","memory","mental","merely","merger","method","middle","miller","mining","minute","mirror","mobile","modern","modest","module","moment","morris","mostly","mother","motion","moving","murder","museum","mutual","myself","narrow","nation","native","nature","nearby","nearly","nights","nobody","normal","notice","notion","number","object","obtain","office","offset","online","option","orange","origin","output","oxford","packed","palace","parent","partly","patent","people","period","permit","person","phrase","picked","planet","player","please","plenty","pocket","police","policy","prefer","pretty","prince","prison","profit","proper","proven","public","pursue","raised","random","rarely","rather","rating","reader","really","reason","recall","recent","record","reduce","reform","regard","regime","region","relate","relief","remain","remote","remove","repair","repeat","replay","report","rescue","resort","result","retail","retain","return","reveal","review","reward","riding","rising","robust","ruling","safety","salary","sample","saving","saying","scheme","school","screen","search","season","second","secret","sector","secure","seeing","select","seller","senior","series","server","settle","severe","should","signal","signed","silent","silver","simple","simply","single","sister","slight","smooth","social","solely","sought","source","soviet","speech","spirit","spoken","spread","spring","square","stable","status","steady","stolen","strain","stream","street","stress","strict","strike","string","strong","struck","studio","submit","sudden","suffer","summer","summit","supply","surely","survey","switch","symbol","system","taking","talent","target","taught","tenant","tender","tennis","thanks","theory","thirty","though","threat","thrown","ticket","timely","timing","tissue","toward","travel","treaty","trying","twelve","twenty","unable","unique","united","unless","unlike","update","useful","valley","varied","vendor","versus","victim","vision","visual","volume","walker","wealth","weekly","weight","wholly","window","winner","winter","within","wonder","worker","wright","writer","yellow"]
  return(word_bank[random_num])

## Creating the new board for the player. They get to see where their correct letter lands at. ##

def new_board(correct_letters,turn):
  
  board.append(correct_letters)
def guess_check(guess,answer):
  correct_letters = []
  correct_letters_length = []
  turn = 0
  while True:
    if guess == answer:
      return True
    else:
      correct_letters = []
      correct_letters_length = []
      for i in range(6):
        if guess[i] == answer[i]:
          correct_letters.append(guess[i])
          correct_letters_length.append(guess[i])
        if guess[i] != answer[i]:
          correct_letters.append("-")
      turn += 1
      new_board(correct_letters,turn)
      print("You got "+str(len(correct_letters_length))+" letters right!")
      print()
      print("They were: ")
      print(correct_letters)
      guess = input("Type another guess (Make sure there are only 6 characters): ")
      while True:
        if len(guess) != 6:
          print("Sorry, that guess wasn't valid,")
          guess = input("Type a guess (Make sure there are only 6 characters): ")
        if len(guess) == 6:
          break
print("Welcome to Wordle!")
print("Guess the six letter word!")
print()
print_board()
answer = random_word()
guess = input("Type a guess (Make sure there are only 6 characters): ")
if len(guess) > 6 or len(guess) < 6:
  print("Sorry, that guess wasn't valid,")
  guess = input("Type a guess (Make sure there are only 6 characters): ")
print(answer)
win = guess_check(guess,answer)
if win == True:
  print("You win! You got the word: " + answer)
if win == False:
  print("You lose :( Your word was " + answer)