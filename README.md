# cfb-data

<b>Summary:</b>
Python code used to pull data related to FBS college football teams. 

<b>Vision:</b>
<p>I'm building this project on a raspberry pi (4B) with the vision 
of having the device left on permanently and using crontab jobs to 
notify me of college football events that I am interested in (such 
as forward and retrospective schedule or game results information for 
selected teams).</p>

<p>I am initially building in some customizability via a config.ini 
file (read further for more info), including the customizability of 
outgoing email server for notifications. </p>

<p>In the longer run, I would like to use this as stepping stone into
a similar project for college basketball.

<b><i>Important:</b></i>
When cloning this repo, ensure you rename config_template.ini to 
config.ini and populate the values as described in the comments 
in that file.  The code will not function without the necessary 
values.

<b>This project gratefully leverages the following other projects:</b>
<li>api.collegefootballdata.com for:
  <ul>
  <li>Ingestion of schedule data
  <li>Developer of that API can be found at www.github.com/BlueSCar
  </ul>

<li>www.sports-reference.com for:
  <ul>
  <li>Ranking data
  <li>Developer of that API can be found at: www.github.com/roclark
  </ul>

<br><br>
<b>Go Deacs!</b>
