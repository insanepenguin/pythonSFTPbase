import paramiko
import time
targz = ""
localpath = ""
pssswd = ""
usr = ""

serverAddress = ""

client = paramiko.SSHClient()

client.load_system_host_keys()

client.set_missing_host_key_policy(paramiko.WarningPolicy)

client.connect(serverAddress, port=22, username=usr, password=pssswd)

tr = paramiko.Transport((serverAddress, 22))

tr.connect(password=pssswd, username=usr)

sftp = paramiko.SFTPClient.from_transport(tr)

sftp.put(targz, "/home/epb9635/mini.tar.gz")
#tar -zxvf min_project1.tar.gz



stdin, stdout, stderr = client.exec_command("tar -zxvf mini.tar.gz")
stdin1, stdout1, stderr1 = client.exec_command("ls -a -l")
time.sleep(5)#this will ensure that all of the files have had the time to be unpacked
print(stdout1)
dirlist = sftp.listdir('.')
print(dirlist[2])
for files in dirlist:
    print(files)
    if(files.find("APM")>=0):
        print(' -> Attempting to download: "{}", and saving it {}'.format(files, localpath + files))
        print(' --> remotepath stat: {}'.format(sftp.stat(files)))
        sftp.get(files, localpath + files)
        print(files)
    else:
        print("No")
client.close()

sftp.close()

tr.close()