import os
import color
import imaplib
import time



os.system('clear')
os.system('figlet -f small "GHS JULIAN"|lolcat\n')

# taking input from user


email = input(color.BOLD+color.YELLOW+color.BOLD+"\n   [+] Enter Your Email :  "+color.LIGHT_CYAN)
password = input(color.BOLD+color.YELLOW+color.BOLD+"\n   [+] Enter Your Password :  "+color.LIGHT_CYAN)


imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(email, password)
imap.select("INBOX")
status, message_id_list = imap.search(None, 'ALL')
messages = message_id_list[0].split()
os.system('figlet -f small "   Deleting..."|lolcat\n')
time.sleep(0.3)
count = 1
for mail in messages:
    imap.store(mail, "+FLAGS", "\\Deleted")
    print("   "+color.BOLD+color.GREEN+color.BOLD+str(count)+color.RED+color.BOLD+" ==>> Selected For Deleting \n")
    count += 1

imap.expunge()
imap.close()
imap.logout()
os.system('clear')
os.system('figlet -f small "   Deleted"|lolcat\n')
