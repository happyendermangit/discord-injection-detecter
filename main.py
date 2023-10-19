import customtkinter
import os


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk() 
app.geometry("800x400")
app.title('Discord injection checker')

def getuser():
    return os.getenv("USERPROFILE").split("\\")[2]

def check():
    try:
        discord_location = os.getenv('localappdata') + "/discord/"

        codes = [
            "module.exports = require('./core.asar');",
            f'require("C:\\\\Users\\\\{getuser()}\\\\AppData\\\\Roaming\\\\BetterDiscord\\\\data\\\\betterdiscord.asar");\nmodule.exports = require("./core.asar");'
        ]

        app_folder = discord_location + "/" + os.listdir(discord_location)[0] + "/modules"
        for folder in os.listdir(app_folder):
            if folder.startswith('discord_desktop_core-'):
                with open(app_folder + "/" + folder + "/discord_desktop_core" + "/index.js", 'r', encoding="utf-8") as f:
                    code = f.read()
                    if code in codes:
                        result_label.configure(text="Your discord Stable client is safe! You don't need to worry", text_color="green")
                    else:
                        result_label.configure(text="INJECTED CLIENT!!!! REINSTALL AND CHANGE PASSWORD", text_color="red")
    except:
        result_label.configure(text="You don't have discord stable installed!", text_color="red")

def checkCanary():
    try:
        discord_location = os.getenv('localappdata') + "/DiscordCanary/"

        codes = [
            "module.exports = require('./core.asar');",
            f'require("C:\\\\Users\\\\{getuser()}\\\\AppData\\\\Roaming\\\\BetterDiscord\\\\data\\\\betterdiscord.asar");\nmodule.exports = require("./core.asar");'
        ]

        app_folder = discord_location + "/" + os.listdir(discord_location)[0] + "/modules"
        for folder in os.listdir(app_folder):
            if folder.startswith('discord_desktop_core-'):
                with open(app_folder + "/" + folder + "/discord_desktop_core" + "/index.js", 'r', encoding="utf-8") as f:
                    code = f.read()
                    if code in codes:
                        result_label.configure(text="Your discord Canary client is safe! You don't need to worry", text_color="green")
                    else:
                        result_label.configure(text="INJECTED CLIENT!!!! REINSTALL AND CHANGE PASSWORD", text_color="red")
    except:
        result_label.configure(text="You don't have discord canary installed!", text_color="red")

def checkPTB():
    try:
        discord_location = os.getenv('localappdata') + "/DiscordPTB/"

        codes = [
            "module.exports = require('./core.asar');",
            f'require("C:\\\\Users\\\\{getuser()}\\\\AppData\\\\Roaming\\\\BetterDiscord\\\\data\\\\betterdiscord.asar");\nmodule.exports = require("./core.asar");'
        ]

        app_folder = discord_location + "/" + os.listdir(discord_location)[0] + "/modules"
        for folder in os.listdir(app_folder):
            if folder.startswith('discord_desktop_core-'):
                with open(app_folder + "/" + folder + "/discord_desktop_core" + "/index.js", 'r', encoding="utf-8") as f:
                    code = f.read()
                    if code in codes:
                        result_label.configure(text="Your discord PTB client is safe! You don't need to worry", text_color="green")
                    else:
                        result_label.configure(text="INJECTED CLIENT!!!! REINSTALL AND CHANGE PASSWORD", text_color="red")
    except:
        result_label.configure(text="You don't have discord PTB installed!", text_color="red")



result_label = customtkinter.CTkLabel(master=app, text="", font=("Sans serif", 30))
result_label.pack(pady=30)

button = customtkinter.CTkButton(master=app, text="Check if injected (Discord stable version)", command=check, font=("Sans serif", 14))
button.pack(pady=20)

button = customtkinter.CTkButton(master=app, text="Check if injected (Discord canary)", command=checkCanary, font=("Sans serif", 14))
button.pack(pady=20)

button = customtkinter.CTkButton(master=app, text="Check if injected (Discord PTB)", command=checkPTB, font=("Sans serif", 14))
button.pack(pady=20)


app.mainloop()

