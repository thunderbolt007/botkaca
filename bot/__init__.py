# GOAL:
# load config

import os
from bot.config import Config

CONFIG = Config({
    'ROOT' : os.getcwd(),
    'WORKDIR' : 'sessions',
    'LOG_FILE' : 'log.txt',
    'MAX_LOG_SIZE' : 10 * 1024 * 1024,
    'API_HASH' : 5fbc91808465973dcd79340baa8ee3e0,
    'API_ID' : 2403946,
    'BOT_TOKEN' : 1604374441:AAEAsAZgA0UCPDR-2xI7T59MLVkyzCjeAE8,
    'BOT_PASSWORD' : None,
    'CHAT_ID' : '-1001468848929',
    'EDIT_SLEEP' : 3,
    'UPLOAD_MAX_SIZE' : 2000 * 1024 * 1024,
    'UPLOAD_AS_DOC' : 0,
    'UPLOAD_AS_ZIP' : 0,
    'ARIA2_DIR' : 'downloads',
    'TORRENT_TRACKER' : '',
    'BAR_SIZE' : 10,
    'THUMBNAIL_NAME' : 'default_thumbnail.jpg',
    'LOCAL' : 'en'
})

# GOAL:
# prepare workdir

workdir = os.path.join(CONFIG.ROOT, CONFIG.WORKDIR)
if not os.path.isdir(workdir):
    os.mkdir(workdir)
del workdir

# GOAL:
# logging any important sign

logfile = os.path.join(CONFIG.ROOT, CONFIG.WORKDIR, CONFIG.LOG_FILE)

if os.path.exists(logfile):
    with open(logfile, "r+") as f_d:
        f_d.truncate(0)

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            logfile,
            maxBytes=CONFIG.MAX_LOG_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# GOAL:
# Log configuration

LOGGER.info(dict(CONFIG))

del logfile

# GOAL:
# Localization

LOCAL = __import__(name = 'bot.locals.' + CONFIG.LOCAL, fromlist = ['LOCAL']).LOCAL

# GOAL:
# load Command format

COMMAND = Config({
    'START' : 'start',
    'PASSWORD' : 'pass',
    'HELP' : 'help@kratosleechbot',
    'LEECH' : 'leech@kratosleechbot',
    'CANCEL_LEECH' : 'cancel@kratosleechbot',
    'LEECH_LIST' : 'list@kratosleechbot',
    'UPLOAD_AS_DOC' : 'upload_as_doc@kratosleechbot',
    'UPLOAD_AS_ZIP' : 'upload_as_zip@kratosleechbot',
    'SET_THUMBNAIL' : 'set_thumbnail@kratosleechbot',
    'RESET_THUMBNAIL' : 'reset_thumbnail@kratosleechbot',
    'SET_TRACKER' : 'set_tracker@kratosleechbot'
}, 'COMMAND_')

# GOAL:
# set status

STATUS = type('obj', (object,), {
    'ARIA2_API' : None,
    'UPLOAD_AS_DOC' : bool(int(CONFIG.UPLOAD_AS_DOC)),
    'UPLOAD_AS_ZIP' : bool(int(CONFIG.UPLOAD_AS_ZIP)),
    'DEFAULT_TRACKER' : CONFIG.TORRENT_TRACKER.split(','),
    'CHAT_ID' : CONFIG.CHAT_ID.split(',')
})
