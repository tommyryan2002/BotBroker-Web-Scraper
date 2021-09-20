import getpass
import keyboard
import time
import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
print(" ____        _     _______    _               __  ___  __ ")
print("|  _ \      | |   |__   __|  | |             /_ |/ _ \/_ |")
print("| |_) | ___ | |_     | | __ _| | _____ _ __   | | | | || |")
print("|  _ < / _ \| __|    | |/ _` | |/ / _ \ '__|  | | | | || |")
print("| |_) | (_) | |_     | | (_| |   <  __/ |     | | |_| || |")
print("|____/ \___/ \__|    |_|\__,_|_|\_\___|_|     |_|\___/ |_|")
print('')
print("This Program will send the user an email alert when a Tohru bot goes on sale")
print("To exit the program after inputing your information, press and hold ESC")
#asks for a users information
timeDelay = float(input("How often should the price be checked (seconds)?: "))
senderMail = input("Please enter the email you wish to send alerts from?: ")
senderPass = getpass.getpass(prompt = "Enter the above email's password?: ")
recieverMail = input("Please enter the email you wish to recieve price alerts to?: ")
priceBelow = float(input("Enter the maximum price you wish to recieve alerts about (no $)?: "))
emailCounter = 0
loopCounter = 0
#calls the anti-bot-detection library
import undetected_chromedriver as uc

#loads and minimizes target site on chrome
driver = uc.Chrome()
driver.get('https://botbroker.io/products/tohruaio?__cf_chl_jschl_tk__=a5bfa68b27a59cf97202099c24d0a0933bf73714-1602993446-0-AQ_g6QaQxyN-dPT3-aNGNX7HgGIn0ndfutQJ3jmltvtS-ss_oZM6dlsau2ofc0WXAGUwh1uXV4LR4EKQtRHnhkZZdwTGFKF-TtDGMXTxhyWHsRid1rVqAIqVQYzVWu1CoHeuIQsPnt-UkXXYfugu7KbuokW2qeJrGkSp-qU4Z1HYdHqL3VyQHLzeLOSZmztPmN67S--NXlZi5G2N1bXh05y3ITKNH394QTo__rX-F1r4Bs9uiniPpdqxOiZkjbFc2jeVsq2Uc0j8oYWHAHPvZ8fUBgE48qeEo5YzSIIvfqgW')
driver.minimize_window()
print("Cheking for low price")
print("press and hold ESC to exit the program")
#loops until escape is pressed
while True:
    x = 0
    if keyboard.is_pressed("esc"):
        print("Bot Taker has been exited!")
        driver.quit()
        break
    else:
        #waits until full page has loaded
        while x < 1:
            try:
                #searches for raw text where lowest price is stored
                lpRaw = driver.find_element_by_xpath("//span[@class='price']").text
                #converts raw text into readable float
                lpRaw2 = lpRaw.strip('$')
                lowestPrice = float(lpRaw2.strip(" Buy now @ best renewal value"))
                if lowestPrice < priceBelow and emailCounter < 1:
                    #begin email process
                    msg = MIMEMultipart()
                    message = ("TOHRU CURRENT LOWEST PRICE: $" + str(lowestPrice))
                    print(message)
                    msg['From'] = senderMail
                    msg['To'] = recieverMail
                    msg['Subject'] = "TOHRU PRICE ALERT"

                    msg.attach(MIMEText(message, 'plain'))
                    server = smtplib.SMTP('smtp.gmail.com: 587')
                    server.starttls()
                    server.login(msg['From'], senderPass)
                    server.sendmail(msg['From'], msg['To'], msg.as_string())
                    server.quit()
                   
                    emailCounter += 1
                    print (emailCounter)
                    x += 1
                else:
                    #breaks loop and refreshes page after (timeDelay)
                    print(lowestPrice, "looped", loopCounter, "times")
                    time.sleep(timeDelay)
                    driver.refresh()
                    loopCounter += 1
                    x += 1
                    
            except:
               pass

    
    

      
