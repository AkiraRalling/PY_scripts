import pyautogui as pgui
import time

class Config():

    @staticmethod
    def notepad():
        pgui.hotkey('winleft', 'd')
        pgui.rightClick(943, 27)
        pgui.click(958, 176)

    @staticmethod
    def openvpn():
        pgui.click(1152, 745)
        pgui.rightClick(1190, 663)
        pgui.click(1034, 424)
        time.sleep(1)
        pgui.typewrite(["enter"])
        time.sleep(3)

    @staticmethod
    def chrome():
        pgui.hotkey('winleft')
        pgui.typewrite('chrome\n', 0.1)
        time.sleep(1)
        pgui.click(1215, 50)
        time.sleep(1)
        pgui.click(1034, 159)
        pgui.hotkey('winleft', 'd')
        time.sleep(1)

    @staticmethod
    def cisco():
        pgui.hotkey('winleft')
        pgui.typewrite('cisco\n', 0.1)
        time.sleep(1)
        pgui.typewrite(["enter"], 0.2)
        time.sleep(1)
        pgui.press('tab')
        time.sleep(1)
        pgui.press('enter')
        pgui.typewrite('&KOfqC&5%k%`q$wIN.rx', 0.1)
        pgui.press('tab')
        pgui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pgui.press('tab')
        pgui.press('enter')

    @staticmethod
    def authenticator():
        pgui.hotkey('winleft')
        pgui.typewrite('chrome\n', 0.1)
        time.sleep(1)
        pgui.click(339, 49)
        pgui.typewrite("10.203.130.10:8080", 0.1)
        pgui.press('enter')
        time.sleep(0.5)
        pgui.typewrite("a.salimgareev", 0.1)
        pgui.press('tab')
        pgui.typewrite('frod1234')
        pgui.press('enter')


class StartScript(Config):

    @staticmethod
    def choose_script():
        flag = True
        while flag:
            numb = input("Choose number (For exit prees 'Enter') :\n\t 1 - only notepad\n\t 2 - openvpn\n\t 3 -"
                         " chrome\n\t 4 - cisco\n\t 5 - authenticator.\n")

            if numb == '1':
                Config.notepad()
            elif numb == '2':
                Config.openvpn()
            elif numb == '3':
                Config.chrome()
            elif numb == '4':
                Config.cisco()
            elif numb == '5':
                Config.authenticator()

            if numb == '':
                break


start_ = StartScript()
start_.choose_script()
