import requests
import json
import os
import re

import config
#from modules import synology
#from modules.classes import PlexSong as plex
from modules.menu import inbox

config.init()

inbox.menu()
