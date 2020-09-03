# Selenium-Automation
Automate your whatsapp and instagram using selenium in python.
1).You can download chromedriver from https://chromedriver.chromium.org/downloads.
2).Don't forget to give path of your chromedriver executable file in the automation code.
   Change path in the line ---> driver = webdriver.Chrome(r"PATH")
3).In whatsapp_automation it asks you to :-
    i).   Enter name to whom you want to send message 
    ii).  number of times to send same message
    iii). Enter your message 
   This code automatically opens whatsapp in chromedriver. All you need to do is scan the QR code in browser.It automatically sends n messages to your contact which you will          enter. It also gets logout by itself.
4).Ensure that your give exact contact name as it is in your whatsapp.
5).In insta_automation it asks you to :-
    i).   Enter email id or username  :
    ii).  enter password  :
   This code automatically opens instagram in chromedriver by itself.It automatically gets login to instagram and scrape all followers and following list and gets logout              immediately .After it gives followers and following count and prints a list of members who are not following you back.
6).Ensure you also have good internet connectivity.
