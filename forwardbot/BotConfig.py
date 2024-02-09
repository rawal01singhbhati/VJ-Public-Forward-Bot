from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "16494736")
    API_HASH = environ.get("API_HASH", "2cb7fa5859e2de684e3e10d9c049621a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6449542986:AAGfy0dRTR_hPXak9AorRZIeEIehwgvLOv0")
    STRING_SESSION = environ.get("STRING_SESSION", "")
    SUDO_USERS = environ.get("SUDO_USERS", "5071104456")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **श्री राम भक्त**
    """
