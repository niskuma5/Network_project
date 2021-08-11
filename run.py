import os
import urllib3
import json
import requests
from netmiko import ConnectHandler
import re
import sys
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
from python_webex.v1.Bot import Bot
from python_webex.v1.Card import Card
from pprint import pprint
from flask import Flask, request
from python_webex import webhook
import re


from datetime import datetime

# Assigning the required parameter like bot_email,teams_token,bot_url,bot_app_name

bot_email = "samplebot52@webex.bot"
teams_token = "NjVkZjE0ZjYtMmZkYi00OWFjLThjOTUtZmZhMWY2MzI3YTk4OGI5ZmIyZjctYjdm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
bot_url = "https://f739dace3690.in.ngrok.io"
bot_app_name = "sample-bot"





# Managed Device Details - Used for netmiko connection
device_address = "sbx-nxos-mgmt.cisco.com"
device_type = "cisco_ios"
device_port = 8181
device_username = "admin"
device_password = "Admin_1234!"


# Just return spark message immediately

def ret_message(incoming_msg):
    m = Response()
    u = 'https://sayingimages.com/wp-content/uploads/'
    u = u + 'aaaaaalll-righty-then-alrighty-meme.jpg'
    m.files = u
    return m


# Return any Random jokes Using an Api

def chuck_joke(message):
    url = 'http://api.icndb.com/jokes/random'
    response = requests.get(url)
    print(response)
    joke = json.loads(response.read())["value"]["joke"]
    return joke



# This function is used to greet the sender

def greeting(incoming_msg):
    sender = bot.teams.people.get(incoming_msg.personId)
    response = Response()
    response.markdown = "Hello {}, I'm a friendly network chatbot.  ".format(
        sender.firstName
    )
    response.markdown += "My name is @netbot. "

    response.markdown += "\n\nSee what I can do by asking for **/help**. \n **Note This is a group room and you have to call me specifically with `@%s` for me to respond**"
    return response


def get_interface_details(
    device_address, device_type, device_port, device_username, device_password
):
    """Retrieve the Interface Configuration
    """
    # Create a CLI command template
    show_interface_config_temp = "do show running-config interface", "do show version","do show ip route","do show system uptime","do show ip arp"

    # Open CLI connection to device
    with ConnectHandler(
        ip=device_address,
        username=device_username,
        password=device_password,
        port=device_port,
        device_type=device_type,
    ) as ch:

        # Create desired CLI command and send to device
        command = show_interface_config_temp
        interface = ch.send_config_set(command)
        # output =ch.send_command("show ip int brief")
        

        # Return the info
        return interface


def netmiko_interface_details(incoming_msg):
    """Retrieve the interface details from the configuration
       using netmiko example
    """

  
    response = Response()

    hold_tight(incoming_msg,"device health")

    # Use the netmiko function to get the interface deatil, by passing the required parameter
    interface = get_interface_details(
        device_address,
        device_type,
        device_port,
        device_username,
        device_password,

    )
    if interface:

    # Create and Return the message
        response.markdown = """ {} """.format(interface)
        return response
    else:
        response.markdown = "Nothing to Display"


def get_version_details(
    device_address, device_type, device_port, device_username, device_password
):
    """Retrieve the Interface Configuration
    """
    # Create a CLI command template
    show_interface_config_temp = "show running-config interface", "show version"

    # Open CLI connection to device
    with ConnectHandler(
        ip=device_address,
        username=device_username,
        password=device_password,
        port=device_port,
        device_type=device_type,
    ) as ch:

        # Create desired CLI command and send to device
        command = "do show system uptime"
        interface = ch.send_config_set(command)
        # output = ch.send_command(command)
       

        # Return the info
        return interface


def netmiko_version_details(incoming_msg):
    """Retrieve the interface details from the configuration
       using netmiko example
    """
   

    response = Response()
    hold_tight(incoming_msg,'system uptime')

    # Use the netmiko function
    interface = get_version_details(
        device_address,
        device_type,
        device_port,
        device_username,
        device_password,

    )


    # Create and Return the message
    response.markdown = """ {} """.format(interface)
    return response


def get_ip_details(
    device_address, device_type, device_port, device_username, device_password
):
    """Retrieve the Interface Configuration
    """
    # Create a CLI command template
    

    # Open CLI connection to device
    with ConnectHandler(
        ip=device_address,
        username=device_username,
        password=device_password,
        port=device_port,
        device_type=device_type,
    ) as ch:

        # Create desired CLI command and send to device
        command = "do show ip interface brief"
        interface = ch.send_config_set(command)
        # output = ch.send_command('show ip int brief')
       

        # Return the info
        return interface


def netmiko_ip_details(incoming_msg):
    """Retrieve the interface details from the configuration
       using netmiko example
    """
    # device = bot.extract_message("/health-check", incoming_msg.text).strip()
    # device1 = bot.extract_message("device=",device).strip()
    

    response = Response()
    
    hold_tight(incoming_msg,"show ip interface brief")

    # Use the netmiko function
    interface = get_ip_details(
        device_address,
        device_type,
        device_port,
        device_username,
        device_password,

    )

    # Create and Return the message
    response.html = """ {} """.format(interface)
    return response




bot_local = Bot(auth_token="NjVkZjE0ZjYtMmZkYi00OWFjLThjOTUtZmZhMWY2MzI3YTk4OGI5ZmIyZjctYjdm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f")

def hold_tight(incoming_msg,argument):
    
   
    
    sender = bot.teams.people.get(incoming_msg.personId)
    print(sender)
    return bot_local.send_message(room_id="Y2lzY29zcGFyazovL3VzL1JPT00vMGVjYWIzMzAtYTUxYS0xMWViLWFmNGYtZjk2NDExMTQ0MGVh", text='Hold tight,' + " " + sender.firstName + ', I’m getting the facts of'+ " " + argument + " " +'for you. ####################################################################')
   


def get_ip_arp_details(device_address, device_type, device_port, device_username, device_password):
    cat2960 = {
       'device_type': device_type,
       'host': device_address,
       'username': device_username,
      'password': device_password,
      'port':device_port
     
      
       
    }
   
    
    
    command = "do show ip arp"
    net_connect = ConnectHandler(**cat2960) 
    # net_connect.enable()
    output = net_connect.send_config_set(command) 
   
    print(output) 

    
    return output
    


def netmiko_ip_arp_details(incoming_msg):
    """Retrieve the interface details from the configuration
       using netmiko example
    """


    # device = bot.extract_message("/health-check", incoming_msg.text).strip()
    # device1 = bot.extract_message("device=",device).strip()

    response = Response()
    # Use the netmiko function
    hold_tight(incoming_msg,"show arp")
    interface = get_ip_arp_details(
       device_address,
        device_type,
        device_port,
        device_username,
        device_password,

    )
    

    
    if len(interface)>0:


    # Create and Return the message

        print(interface)
        
        response.markdown = """ {} """.format(interface)
        return response

    else:
        response.markdown = "Nothing to Display"








def get_resources_details(device_address, device_type, device_port, device_username, device_password):
    cat2960 = {
       'device_type': device_type,
       'host': device_address,
       'username': device_username,
      'password': device_password,
      'port':device_port
     
      
       
    }
   
    
    
    command = "do show system resource"
    net_connect = ConnectHandler(**cat2960) 
    # net_connect.enable()
    output = net_connect.send_config_set(command) 
   
    print(output) 

    
    return output
    


def netmiko_resources_details(incoming_msg):
    """Retrieve the interface details from the configuration
       using netmiko example
    """
  


    response = Response()

    # Use the netmiko function
    hold_tight(incoming_msg,"system resources")
    interface = get_resources_details(
       device_address,
        device_type,
        device_port,
        device_username,
        device_password,

    )


    # Create and Return the message
    print(interface)
    response.html = """ {} """.format(interface)
    return response





# Create a new bot Object
bot = TeamsBot(
bot_app_name,
teams_bot_token=teams_token,
teams_bot_url=bot_url,
teams_bot_email=bot_email,
debug=True,
)






# Add Bot commands

bot.add_command('/Hello', 'help for do something', greeting)
bot.add_command('/demo', 'sampel that allows spark message to be returned',
                ret_message)
bot.add_command('/chuck', 'Get a random Chuck Norris Joke', chuck_joke)




bot.add_command('/health-check', 'To check the health of devices', netmiko_interface_details)
bot.add_command("/show-Uptime", 'Show uptime of devices', netmiko_version_details)
bot.add_command("/show-ip",'show IP interface brief', netmiko_ip_details)
bot.add_command("/show-arp", 'Show arp detail', netmiko_ip_arp_details)
bot.add_command("/show-resource", 'Show resources detail', netmiko_resources_details)

















if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)