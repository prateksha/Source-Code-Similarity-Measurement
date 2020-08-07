#Anagram Challenge

word = input()

vowels = "AIEOU"


#player1 score
player1score = 0
for i in range(0,len(word)):
	if word[i] not in vowels:
		player1score += len(word) - i


#player2 score
player2score = 0
for i in range(0,len(word)):
	if word[i] in vowels:
		player2score += len(word) - i

if player1score > player2score:
	print("Stuart",player1score)
elif player2score > player1score:
	print("Kevin", player2score)
else:
	print("Draw")




