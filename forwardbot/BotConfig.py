from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "9239475")
    API_HASH = environ.get("API_HASH", "45bca1de511c5133d0d83e0f7f456bee")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6922036916:AAHod6WEiUf70eq6ytG2P1uRrk6__uQ-xHU")
    STRING_SESSION = environ.get("STRING_SESSION", "")
    SUDO_USERS = environ.get("SUDO_USERS", "5796251936")
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
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@KingVJ01**
    """
