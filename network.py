import wifi
import pandas as pd
import os
import sys

def check_root():
    if not os.geteuid()==0:
        sys.exit('This script must be run as root!')

def get_pssw():
    return input('password: ')

def build_table(networks):
    ssid=[]
    address=[]
    signal=[]
    quality=[]
    channel=[]
    mode=[]
    for network in networks:
        ssid.append(network.ssid)
        address.append(network.address)
        signal.append(network.signal)
        quality.append(network.quality)
        channel.append(network.channel)
        mode.append(network.mode)
    net={'ssid': ssid, 'MAC_address': address, 'signal': signal, 'quality': quality, 'channel': channel, 'mode': mode}
    return net

def main():
    check_root()
    interface=input('interface name: ')
    networks=wifi.Cell.all(interface)
    net=build_table(networks)

    print(pd.DataFrame (net, columns = ['ssid', 'MAC_address', 'signal', 'quality', 'channel', 'mode']))
    selected_network=input('select network [0, 1, 2, ...]: ')
    try:
        print(net['ssid'][int(selected_network)])
    except:
        print('select valid network')
    os.system('wpa_passphrase "'+ str(net['ssid'][int(selected_network)]) +'" '+ str(get_pssw()) +' >> /etc/wpa_supplicant/wpa_supplicant-wlp1s0.conf')


if __name__=='__main__':
    main()
