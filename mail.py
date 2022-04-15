import imapclient
import pprint as p
import pyzmail

#Connecting to gmail server
imapObj = imapclient.IMAPClient('imap.gmail.com',ssl=True)
#logging into gmail account
imapObj.login('alexandervalencia1994@gmail.com','C4n4d42309')

#print list of folder
# p.pprint(imapObj.list_folders())

#select folder containing all emails
imapObj.select_folder('[Gmail]/All Mail', readonly=False)
#search for undesirable emails with serch method
UIDs=imapObj.search(['OR','OR','OR','OR','OR','OR','FROM','linkedin', 'FROM', \
    'wordpress', 'FROM', 'sncf', 'FROM', 'admiral','FROM','skillshare','FROM','no-reply','FROM', 'platzi'])

#print ids presenting each mail
print(UIDs)

"""     # ─── SHOW MESSAGES AND SUBJECTS ─────────────────────────────────────────────────
for i in UIDs:
    #extract all iformation into special format
    rawMessages = imapObj.fetch([i], ['BODY[]'])
    msg = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])

    #print email content
    # msg.html_part.get_payload().decode(msg.html_part.charset)

    #print subject
    print(msg.get_subject()) """
print(imapObj.delete_messages(UIDs))
imapObj.expunge()
imapObj.logout()

"""  # ─── DELETE MESSAGES FROM FORLDER BIN AND SPAM ──────────────────────────────────
folders = ["[Gmail]/Spam", "[Gmail]/Bin"]
for i in folders:
    imapObj.select_folder(i, readonly=False)
    UIDs = imapObj.search(['ALL'])
    imapObj.delete_messages(UIDs)
    imapObj.expunge() """
