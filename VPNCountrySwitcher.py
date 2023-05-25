import time

from selenium import webdriver
from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN


def switchRegionVPN():
    initialize_VPN(save=1, area_input=['random countries europe 10'])
    for i in range(3):
        rotate_VPN()
        time.sleep(10)

    terminate_VPN()
