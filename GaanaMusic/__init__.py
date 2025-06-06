from GaanaMusic.core.bot import Gaana
from GaanaMusic.core.dir import dirr
from GaanaMusic.core.git import git
from GaanaMusic.core.userbot import Userbot
from GaanaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Gaana()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
