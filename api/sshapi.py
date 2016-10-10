#coding=utf-8
import sys, paramiko

class Sshapi:
    def __init__(self, host='', port=22, user='root', passwd='', log='paramiko.log'):
        try:
            pkey='C:\\Users\\hp\\.ssh\\id_rsa'
            key=paramiko.RSAKey.from_private_key_file(pkey)
        
            paramiko.util.log_to_file(log)

            self.ssh = paramiko.SSHClient()
            # self.ssh.load_system_host_keys()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=host, username=user, port=port, pkey=key)
            #self.ssh.connect(hostname=host, port=port, username=user, password=passwd)
        except Exception, e:
            print str(e)

    def __del__(self):
        self.ssh.close()


    def run(self, command=[]):

        result = []

        for m in command:
            stdin, stdout, stderr = self.ssh.exec_command(m)

            result.append(stdout.read())

        return result

