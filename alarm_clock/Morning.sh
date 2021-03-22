#!/bin/bash
#echo "am i precious to you now";

#SHELL=/bin/bash
#31 * * * * root ./Library/WebServer/Documents/stats.sh >/dev/null 2>&1
#$(cd /Users/joey/automation/ ; sh Morning.sh)
#afplay g_morning.mp3

python location.py

IFS=$'\n' array=($(cat $1))

for i in 0
do
	wget --user-agent="Mozilla" -O index.html ${array[i]}

	if [ $i == 0 ]; then
		java -jar tagsoup-1.2.1.jar --files index.html #334489
	else
		continue
		#java -jar tagsoup-1.2.1.jar --files 334489?day=1
	fi
	
done
sleep 5s

python3 mparsar1.py index.xhtml #334489.xhtml
#python mparsar2.py 334489?day=1.xhtml

python3 morning.py


rm index.html #334489
#rm 334489?day=1
rm index.xhtml #334489.xhtml
#rm 334489?day=1.xhtml
