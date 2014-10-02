#!/usr/bin/env python2
#
#  tts.py - converts text to speech, can be used as a module in some of your experiment, just import it and call say(text_string);
#
#  Copyright (c) 2014 Shubham Chaudhary <me@shubhamchaudhary.in>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys,re,urllib
import os,os.path

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse

def google_translate(text):
    if not text:
        text = "speak to me Shubham Chaudhary"
    tts_text = text.replace(" ","+")
    tts_url = "http://translate.google.com/translate_tts?tl=en&q="+tts_text
    get_command = 'wget ' + tts_url + '-O test.mp3';
    if os.system(get_command):
        os.system("aplay test.mp3")

def pyttsx_tts(text):
    import pyttsx;
    engine = pyttsx.init();
    if not text:
        # text = "speak to me Shubham Chaudhary"
        print 'No text passed to speech engine';
        return;
    engine.say(text);
#     voices = engine.getProperty('voices')
#     pyttsx.voice.Voice.gender('female');
#     for voice in voices:
#        engine.setProperty('voice', voice.id)
#        engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()
    engine.runAndWait();

def espeak_engine(text):
    from espeak import espeak
    from datetime import datetime

    t = datetime.now().strftime('%k %M')
    espeak.synth('You\'re listening to Lukes radio station. The time is %s'%t)
    return;

def say(text):
    return pyttsx_tts(text);
    return espeak_engine(text);

def print_usage():
#     print('Usage: ',sys.argv[0],' [filename <Default: .login.txt>] || [password] || [username password]');
    print 'Usage: ',sys.argv[0],' [filename <Default: .login.txt>] || [password] || [username password]' ;

def print_help():
#     print('--------- Help ---------');
    print '--------- Help ---------' ;
    print_usage();

def main(argv):
    # Parse command line arguments
    argc = len(argv);
    text=''
    if argc == 2:
        if argv[1] == '-h' or argv[1] == '--help':
            print_help();
            return;
        elif argv[1] == '-i' or argv[1] == '--input':
            text = raw_input('Enter text you want me to speak: ');
#     else:
#         print_usage();

    # Check input
    if not text:
        print('So you want me to say something to you, so sweet. Finally I get a chance to speak :)');

    # Show some details to user

    try:
        say(text);
    except:
        raise;
    return 0

if __name__ == '__main__':
    try:
        main(sys.argv);
    except KeyboardInterrupt:
        print('\nClosing garacefully :)',sys.exc_info()[1]);
    ### TODO: Handle other errors
    except:
        print('Unexpected Error:',sys.exc_info()[0],'\nDetails:',sys.exc_info()[1]);
#         raise;
