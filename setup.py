import os

class installer:
    def __init__(self):
        self.libs()
        self.move_to_bin()

    def libs(self):
        os.system('sudo apt install python3-kivy')
        os.system('pip3 install -r requirements.txt')
        os.system('sudo pip3 install -r requirements.txt')

    def move_to_bin(self):
        with open('Kivymd-Viewer','r') as file:
            file = file.read()

        with open('/usr/bin/Kivymd-Viewer','w') as bin:
            bin.write(file)

        # permission XXX
        os.system('chmod 777 /usr/bin/Kivymd-Viewer')

if __name__=='__main__':
    install = installer()
