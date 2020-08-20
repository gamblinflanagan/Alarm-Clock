Created June 30th 2020
This application will run on any mac os machine (mac os high sierra 10.13.6 or higher)

to run the it open a terminal shell type crontab-e
press i then write out the following commands


30 8 * * * $(cd /Path_to_file/alarm_clock/sound_files ; sh play.sh)
30 8 * * * $(cd /Path_to_file/alarm_clock ; sh Morning.sh source.txt)

this will run the files at 8:30am every day of every week of every month of every year

press esc then :wq then enter to save

to check if the crontab commands saved enter the command crontab-l

more information on crontab here
https://crontab.guru