IFS=$'\n' array=($(cat $1))

for i in 0 1
do
	wget --user-agent="Mozilla" ${array[i]}
	
	java -jar tagsoup-1.2.1.jar --files 334489
	
	java -jar tagsoup-1.2.1.jar --files 334489?day=1
done

python mparsar1.py 334489.xhtml

sleep 10s

rm 334489
rm 334489?day=1
rm 334489.xhtml
rm 334489?day=1.xhtml



#* * * * * $(cd /Users/joey/automation/ ; python mparsar1.py 334489.xhtml)