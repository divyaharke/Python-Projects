from datetime import *
from email import message
import time
import schedule
import psutil
import os
from sys import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Mail_Sender(dir,toaddr):
    fromaddr = "divya.29.harke@gmail.com"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "Mail sending using automation"

    body = """Hi 
    I am Divya Harke. I am attaching log file with email. 
	Please check it."""
                    
                     

    msg.attach(MIMEText(body,'plain'))

    attach = open(dir,'rb')

    p = MIMEBase('application','octet-stream')
    p.set_payload((attach).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % dir)                 
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("divya.29.harke@gmail.com","fnswxfczgjrszdcd")
    text = msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()

def create_log(dir,listprocess):
    file_name = "Divya's%s.log"%(time.time()) 
    Complete_Name = os.path.join(dir,file_name)
    fd = open(Complete_Name,"w")
    des = "-" * 80
    fd.write(des+"\n")
    fd.write("Marvellous Infosystem Process Logger : " + time.ctime() + "\n")
    fd.write(des+"\n")
    for elem in listprocess:
        fd.write(str(elem)+"\n")
    fd.close    
    Mail_Sender(Complete_Name,argv[2])    


def Process_Monitor_log(dir):
    listprocess = list()
    
    if not os.path.exists(dir):
        os.mkdir(dir)
    else:
        pass    

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['memory'] = proc.memory_info().vms / (1024*1024)
            listprocess.append(pinfo)
        except Exception:
            pass    
    
    create_log(dir,listprocess)
       


def main():
    print("----- Log File Sending through Mail -----")
    print("Application name : " +argv[0])
   

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (len(argv)==2):
        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("usage : ApplicationName Directory_name Sender_MailID")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : This Script is used to send the mail attach with log file")
            exit()

    if (len(argv)==3):
        try:
            #Process_Monitor_log()
            schedule.every(1).minute.do(Process_Monitor_log,argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)
        except ValueError:
            print("Value Error")

        except Exception as e: 
            print("Error : ",e)

if __name__ == "__main__":
    main()               