#coding=utf-8
import sys, paramiko


# 基于paramiko SSH驱动
class Sshapi:
    def __init__(self, host='', port=22, user='root', passwd='', log='paramiko.log'):
        try:
            # 私钥地址，免登录
            pkey='C:\\Users\\hp\\.ssh\\id_rsa'
            key=paramiko.RSAKey.from_private_key_file(pkey)
        
            paramiko.util.log_to_file(log)

            self.ssh = paramiko.SSHClient()
            # self.ssh.load_system_host_keys()
            # 不记录目标机摘要信息
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 密钥方式
            self.ssh.connect(hostname=host, username=user, port=port, pkey=key)
            # 密码方式
            #self.ssh.connect(hostname=host, port=port, username=user, password=passwd)
        except Exception, e:
            print str(e)

    def __del__(self):
        self.ssh.close()


    def run(self, command=[]):

        result = []

        # 遍历命令列表，取出返回信息
        for m in command:
            stdin, stdout, stderr = self.ssh.exec_command(m)

            result.append(stdout.read())

        return result

