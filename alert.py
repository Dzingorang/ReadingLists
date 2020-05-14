# Module to read all data from product list. This is first version. When other modules will be ready this module need to be updated
# do it could be imported by other modules.

from gtts import gTTS
from playsound import playsound
import google_home_integration

def read_list(product_list, language = 'en'):
    mp3_file_name = 'text_to_be_read.mp3'
    test_text = ''

    if len(product_list) == 0:
        test_text = 'There is no product with close expiration date!'
    else:
        for row in product_list:
            days_to_expire_text = ''
            if int(row[1]) > 1:
                days_to_expire_text = '{} days. '.format(row[1])
            else:
                days_to_expire_text = '{} day. '.format(row[1])

            test_text += '{} will expire in {}'.format(row[0], days_to_expire_text)

    tts = gTTS(test_text, lang = language)
    tts.save(mp3_file_name)

    playsound(mp3_file_name, True)
    # Below code will be used by raspberry pi
    # google_home_integration.read_on_google_home_mini(test_text)

def read_text(text):
    mp3_file_name = 'text_to_be_read.mp3'
    tts = gTTS(text, lang = 'en')
    tts.save(mp3_file_name)
    playsound(mp3_file_name, True)
    # Below code will be used by raspberry pi
    # google_home_integration.read_on_google_home_mini(text)