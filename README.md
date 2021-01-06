# BotbBoker-Web-Scraper
A terminal based python script that will alert a user when the price of a shoe bot drops below a certain price.
# Required Files
This script makes use of ultrafunkamsterdam's Undetected Chrome Driver to bypass Cloud Flare on botbroker.io
https://github.com/ultrafunkamsterdam/undetected-chromedriver
# How it Works
This script will initially ask for a user's sending email and password, the recieving email, the price at which they wish to be notified, and how often they wish to check the price.
The program will open up a new chrome window, navigate to the desired products page (for this project I used tohruAIO as the desired product), find the price in the html, and minimize the window
It will continually refresh the page until it detects that the price has dropped below the target value. It will send an email to the user. 
For this to work the sending email must have the gmail security setting "Less secure app access" turned on.
To exit the program hold ESC until you get the message "Bot Taker has been exited!"

To be used effectively, the user should run this script for the entire time that they have their computer turned on.
