# Alarm-Clock
## Created June 30th 2020
## This application will run on any mac os machine (mac os high sierra 10.13.6 or higher) ONLY


### Languages used

python

bash (shell scripting)


### To Use:

* Open a terminal shell and navigate to the desired directory 
* Run `git clone https://github.com/gamblinflanagan/Alarm-Clock.git`


### To run: 

* Open a terminal shell type `crontab-e`
* Press i then write out the following commands
* `30 8 * * * $(cd /Path_to_file/alarm_clock/sound_files ; sh play.sh)`
* `30 8 * * * $(cd /Path_to_file/alarm_clock ; sh Morning.sh source.txt)`
* This will run the files when your mac clock strikes 8:30AM every day of every week of every month of every year
* Press esc then :wq then enter to save

* To check if the crontab commands saved enter the command `crontab-l`

* More information on crontab here https://crontab.guru


### Link To Survey

https://forms.gle/y7dKuC9MQc3BTmv79
