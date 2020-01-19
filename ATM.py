
#!/usr/bin/env python


from jinja2 import Environment,FileSystemLoader
from openpyxl import load_workbook
import getpass
from netmiko import ConnectHandler



if __name__ == "__main__":
    while True:
        file = raw_input("Please enter the Excel file name : ")
        un = raw_input("Please enter your Username : ")
        pwd = getpass.getpass("Please enter your Password :")
        wb = load_workbook(filename=file, read_only=True)
        ws = wb['Sheet1']
        for item in ws.rows:
            mlist = [cell.value for cell in item]
            env = Environment(loader=FileSystemLoader('.'))
            tunnel_temp = env.get_template("ATM.j2")
            conf_temp= tunnel_temp.render(ip=mlist[1])
            with open('config.txt', 'w') as fp:
                fp.writelines(conf_temp)
            #device = ConnectHandler(device_type='cisco_ios', ip=mlist[0], username=un, password=pwd)
            #conf = device.send_config_from_file('config.txt')
        raw_input("Press Enter to exit")
        break
