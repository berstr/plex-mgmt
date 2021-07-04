import requests
import re
import config

from modules.classes import SynologyFile

def is_video_file(file):
    if file.ext in  config.VIDEO_FILE_EXTENSIONS:
        return True
    else:
        return False

def is_audio_file(file):
    if file.ext in  config.AUDIO_FILE_EXTENSIONS:
        return True
    else:
        return False

def parse_filename(file):
    result = None
    pattern = '^(.*) \- (.*) \((.*)\)$'
    m = re.match(pattern(file.name))
    if (m != None) and (m.group() == file.name) and (len(m.groups()) == 3):
        result = {'artist':m.group(1),'title':m.group(2),'year':m.group(3)}
    return result

# checks if the list of files have a video file that corresponds to the audio song file
# audio_file:   SynologyFile
# files:        [] SynologyFile
def search_video_file(audio_file, video_files):
    result = None
    for video_file in video_files:
        if is_video_file(video_file):
            if audio_file.name == video_file.name:
                result = video_file
                break
    return result

def filter_audio_files(files):
    result = []
    for file in files:
        if is_audio_file(file):
            result.append(file)
    return result

def filter_video_files(files):
    result = []
    for file in files:
        if is_video_file(file):
            result.append(file)
    return result



def list_files(path):
    result = []
    PARAMS = {
        "path": path
    }
    URL = 'http://' + config.SYNOLOGY_FILESTATION_SERVICE + '/folder/list'
    r = requests.get(url=URL, params=PARAMS)
    # print(r.status_code)
    #print(r.json())
    files = r.json()['synology']['data']['files']
    for file in files:
        if file['isdir'] == False:
            result.append(SynologyFile.SynologyFile(file['path']))
    return result
   


def file_info(path):
    PARAMS = {
        "path": path
    }
    URL = 'http://' + config.SYNOLOGY_FILESTATION_SERVICE + '/file/info'
    r = requests.get(url=URL, params=PARAMS)
    # print(r.status_code)
    # print(r.json())
    return r.json()['synology']['data']['files'][0]