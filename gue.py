import shutil
columns = shutil.get_terminal_size().columns
		


print("GUESS A WORD".center(columns))
word=[]
g_word=[]*100
c=0


n=input("enter a word for guessing".center(columns))
word[:0]=n
print(word)

print("GOOD LUCK".center(columns))
word_complition="_"*len(word)
	

tries=len(word)-1
while tries>=0:
	print("\n\nyou will have %s chances left"%tries)
	print("\n\n",word_complition.center(columns))
	gw=input("guess the character :".center(columns))
	if gw in word:
		if len(gw)==1:
			if gw in g_word:
				print("you already guessed this letter".center(columns))
				g_word.append(gw)
			else:
				c+=1
				print("\n")
				print("good you guessed corectly".center(columns))
				g_word.append(gw)
				word_as_list=list(word_complition)
				indices=[i for i, letter in enumerate(word) if letter==gw]
				for index in indices:
					word_as_list[index]=gw
				word_complition="".join(word_as_list)
				
	else:	
		
		print("you have guessed wrong latter".center(columns))
	tries=tries-1

if c>=len(word)-1:
	print("\n\n")
	print("congraz you won the game".center(columns))
else:
	print("\n\n")
	print("sorry you failed the game".center(columns))
		









	
