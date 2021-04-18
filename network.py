import wifi
import pandas as pd
import os
import sys

def check_root():
    if not os.geteuid()==0:
        sys.exit('This script must be run as root')

def get_pssw():
    return input('password: ')

def get_interface():
    interface=input('interface name: ')
    return interface

def get_argv():
    try:
        if(sys.argv[1]=='--help' or sys.argv[1]=='-h'): return 0
        if(sys.argv[1]=='--new' or sys.argv[1] == '-n'): return 1
        elif(sys.argv[1]=='--connect' or sys.argv[1]== '-c'): return 2
        else: return -1
    except IOError:
        sys.exit('argument required')

def helper():
    print('syntax: command arg')
    print('arg: ')
    print('\t --connect, -c : enable network interface and connect')
    print('\t --new, -n : scan for nerby wifi networks and connect to it (wifi network interface with: ip link)')

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

def new_network(interface, config_file):
    networks=wifi.Cell.all(interface)
    net=build_table(networks)

    print(pd.DataFrame (net, columns = ['ssid', 'MAC_address', 'signal', 'quality', 'channel', 'mode']))
    selected_network=input('select network [0, 1, 2, ...]: ')
    try:
        print(net['ssid'][int(selected_network)])
        os.system('wpa_passphrase "'+ str(net['ssid'][int(selected_network)]) +'" '+ str(get_pssw()) +' >> '+config_file)
        connect_network(interface)
    except IOError:
        print('select valid network')

def connect_network(interface, config_file):
    os.system('dhcpcd')
    os.system('wpa_supplicant -B -i '+ interface +' -c'+config_file)

def check_config_file(interface):
    config_file='/etc/wpa_supplicant/wpa_supplicant-'+str(interface)+'.conf'
    if (not os.path.exists(config_file)): os.mknod(config_file, mode=0o0644)
    return config_file

def setup():
    interface=get_interface()
    config_file=check_config_file(interface)
    return interface, config_file

def main():
    check_root()
    arg=get_argv()
    if(get_argv()==0): helper()
    else:
        if(get_argv()==1):
            interface, config_file=setup()
            new_network(interface, config_file)
        elif(get_argv()==2):
            interface, config_file=setup()
            connect_network(interface, config_file)
        else: sys.exit('invalid argument')

if __name__=='__main__':
    main()
