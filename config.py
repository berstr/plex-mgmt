import logging
import os

# env variables
SYNOLOGY_FILESTATION_SERVICE=None
PLEX_REST_SERVICE = None
AUDIO_FILE_EXTENSIONS = ['mp3','m4a']
VIDEO_FILE_EXTENSIONS = ['mp4']
SYNOLOGY_MUSIC_INBOX = "/music/inbox"

LOGGER = None


# ==========================
# Init of variables
# ==========================


# PLEX_REST_SERVICE is the hostname (IP address) and port number where the plex-rest service runs
# Example: 192.168.178.99
PLEX_REST_SERVICE=os.environ.get("PLEX_REST_SERVICE")
if (PLEX_REST_SERVICE == None):
    PLEX_REST_SERVICE='localhost:37082'

# SYNOLOGY_FILESTATION_SERVICE is the hostname (IP address) and port number where the synology-filestation service runs
# Example: 192.168.178.99
SYNOLOGY_FILESTATION_SERVICE=os.environ.get("SYNOLOGY_FILESTATION_SERVICE")
if (SYNOLOGY_FILESTATION_SERVICE == None):
    SYNOLOGY_FILESTATION_SERVICE='192.168.178.80:37081'


# env=os.environ.get("PLEX_REST_PORT")
# if (env != None):
#    PLEX_REST_PORT=env

def init():
    init_logger()

def init_logger():
    global LOGGER
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(console_handler)

    LOGGER = logger
