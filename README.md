Give Webex users access to outside services right from their Webex spaces. Bots help users automate tasks, bring external content into the discussion, and gain efficiencies.
This is just a simple Network help project used to connect with any network vendor devices and fetch the required detail from the server. Through Webex Teams, With the help of a bot, we can inquire about any network device operational status, .i.e. network interface status, arp table, and can make configuration changes to network devices.

Steps to run this code:-

1. Python must be installed in your system.
2. Download the code from the source.
3. Download the Ngrok file from google. (
https://ngrok.com/)
4. You must have an account on Webex teams.
5. Open this link
https://developer.webex.com/docs/bots and Create one Webex Bot and copy the Bot token,bot_email,bot_name and save it somewhere this detail will be used at later point of time.
6. you must have network device detail(exp. router, switch or firewall) to which you want to connect and fetch the required detail, for example, device_host,device_address,device_port,device_type
7. open folder named BOT_PROJECT inside source folder using Command-line interface.
8. Create the virtual environment using the command "python -m venv env" and then Activate the same virtual environment using the command, env\Scripts\Activate
9. Open the folder webexbot and Install all the dependencies using the command pip install -r requirements.txt
10. Now, open the ngrok folder in a separate command-line interface.
11. Once you are inside the ngrok folder, run this command "ngrok http --region=XX 5000"
12. After running the above command, you will get two publically accessible URLs,
Copy the one that has "HTTPS" as a prefix.
13. Now, open the run.py file and paste the above copied URL at line where "bot_url" name is mentioned.
14. Open run.py file again and paste the bot_email,bot_name,bot_token at top of the file.
15. In the same run.py file paste the device detail also device_address,device_port,device_username,device_password,device_type.
16. Now run the python file using "python run.py" in the terminal.
17. Now open Webex teams and search your bot and start with /help command, you will get further assistance from bot.