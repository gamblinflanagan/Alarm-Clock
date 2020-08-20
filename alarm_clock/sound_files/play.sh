

rand=$[RANDOM%6+1]
#rand=0
#echo $rand

if [ $rand == 1 ]; then
	afplay gMorning_lost.mp3
elif [ $rand == 2 ]; then
	afplay gMorning_swan.mp3
elif [ $rand == 3 ]; then
	afplay gMorning_dances_harp1.mp3
elif [ $rand == 4 ]; then
	afplay gMorning_dances_harp2.mp3
elif [ $rand == 5 ]; then
	afplay gMorning_flowers.mp3
elif [ $rand == 6 ]; then
	afplay gMorning_maria.mp3
fi



#default case for testing
if [ $rand == 0 ]; then
	afplay gMorning_maria.mp3
fi
	
	
#SONGS RECORDED

#(unique to prototype) i was lost without you
#The swan
#Dances for Harp and Orchestra, L. 103: 1. Danse sacrée
#Dances for Harp and Orchestra, L. 103: 2. Danse profane
#Tchaikovsky - Waltz of the Flowers

#SONGS TO RECORD 
#EDWARD ELGAR: Chanson de Matin

#ave maria charles gounod
#the blue danube johann strauss Eugene Ormandy
#Canon and Gigue in D major
#greensleeves music for baby
#Symphony No 6 Ludiwig van Beethoven
#The four Seasons