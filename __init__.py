# coding:utf-8

import os
import sys
import re

import sixpad as sp
from sixpad import msg
from sixpad import window as win

# Plugin path
PLUGIN_PATH = sp.appdir + '\\plugins\\markpad\\'
sys.path.append(PLUGIN_PATH)

import goto_regex
import regex
from item import *

# shortkeys
shortkey ={
'next_head': ['CTRL+R', None],
'next_head1': ['CTRL+1', None],
'previous_head':['CTRL+SHIFT+R', None],
'previous_head1': ['CTRL+SHIFT+1', None]
} # end shortkey dico

# shortcut programme #
page = sp.window.curPage

def get_accelerator(action):
    return shortkey[action][0]
# end def

def load_module(markup_type):
    """Load MarkPad module"""
    # Load lng file to translate markpad
    load_translate_file()
    # Compile regex
    # fetch regex for markup language
    regex_raw = regex.get_regex(markup_type)
    regex_compiled = regex.compile_regex(regex_raw)
    # instantiates goto with regex compiled
    goto = goto_regex.Goto(sp, regex_compiled)
    
    # Creating MarkUp menu
    menu_markup = win.menus.add(label = "MarkUp", action = None, index = -2, submenu = True, name = 'markup', specific = True)
    # creat sub menu and global submenus and items
    submenus, items = creat_submenu(menu_markup)
    # Accelerator
    #accelerator_active = creatAccelerator(shortkey, win)
    return goto, menu_markup, submenus, items
# end def

def creat_submenu(menu_markup):
    """Creat sub menu and item for MarkPad modul
    arg : menu_markup, 6pad menu typ
    ret
    urn submenus dico, items dico"""
    
    submenus = {}
    items = {}
    
    # Sub Menu
    # Goto
    submenus['goto'] = menu_markup.add(
    label = msg('Goto'), submenu = True, action = None, name = 'goto')
    # items in Goto sub menu
    # next head
    items['next_head'] = submenus['goto'].add(
    label = msg('Next head'), action = lambda:goto.next_item(HEAD), accelerator = get_accelerator('next_head'), name = "next_head")
# Previous head
    items['previous_head'] = submenus['goto'].add(
    label = msg('Previous head'), action = lambda:goto.previous_item(HEAD), accelerator = get_accelerator('previous_head'), name = "previous_head")
    
    return submenus, items
# end def

def creat_accelerator(shortkey, win):
     """ Create accelerators from shorkey dico and return accelerator_active"""

     accelerator_active = {}
     for action, value in shortkey.items():
         # test if user set personal key for this action
         if value[1]:
             # User shortkey found
             key = value[1]
         else:
             # Default shortkey used
             key = value[0]
         # end i
         accelerator_active[action] = win.addAccelerator(key, eval(action), True)
     # end fo
     return accelerator_active
# end de
 

def load_translate_file():
    """Load the lang file to translate markpad"""
    # Load language
    for lang in(sp.locale, 'english'):
        lang_file = os.path.join(PLUGIN_PATH, lang + '.lng')
        if os.path.isfile(lang_file) :
            # Lang file found
            sp.loadTranslation(lang_file)
    # end for
# end def

class MARKUP_LANGUAGE(dict):

    def __init__(self, plugin_path):
        """Load markdown language definition"""
        # Load markup language definition from language directory
        self.markup_langs = self._fetch_markup_definition(plugin_path)
    # end def
    
    def _fetch_markup_definition(self, plugin_path):
        """Create MUL file dictionary from file present into "markup language" directory"""
        
        # Instanciate mul dictionary
        markup_langs = {}
        # List mul file
        lang_path = os.path.join(plugin_path, 'markup language')
        list_file = os.listdir(lang_path)
        
        # Search mul file into language directory
        for file_name in list_file:
            if '.mul' in file_name[-4:]:
                # mul file found.
                # fetch language name
                lang_name = file_name[:-4]
                mul_path = os.path.join(lang_path, file_name)
                # Add this markup language into markup definition dictionary
                markup_langs[lang_name] = self._parse_mul_file(mul_path)
                
            # end if mul file found
        # end for file
        return markup_langs
    # end def
    
    def _parse_mul_file(self, mul_path):
        """Parse mul file and return dictionary language definition""" 
        # Open file.
        mul_file = open(mul_path, encoding='utf8')
                        # parse file
        # Instanciate markup_lang dictionary
        markup_lang = {}
        # Parse file line by line
        n_line = 0
        for line in mul_file:
            n_line +=1
            # Test if this line is a comment or empty.
            if line[0] in ['#', '\n', '\r']:
                # next line
                continue
            # end if
            # remove line ending, dos or unix
            line.rstrip('\n\r')
            # extract key and value
            try :
                key, value = line.split('=')
                # extension information or regex definition?
                if 'extension' in line :
                    key = 'extension'
                    value = eval(value)
                else:
                    # Regex definition
                    value = eval(value)
                    key = eval(key)
            except ValueError : 
                print('Error during MarkPad load Markup language definition\nFile : %s\nSyntaxe error at line %d\n%s' %(mul_path, n_line, line))
                return -1
            # end except
            markup_lang[key] = value
        # end for
        mul_file.close()
        return markup_lang
    # end def
# end class

## main ##
# dev
m = MARKUP_LANGUAGE(PLUGIN_PATH)
# Load MarkPad module if it didn't already""" 
# Test if the menu MarkUp is not already created 
if True : #OR sp.window.menus["markup"] == None :
    goto, menu_markup, submenus, items = load_module("markdown")
    print('MarkPad load')
else:
    print('Menu already created')
# end if