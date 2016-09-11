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

# Constant
# text IHM
for lang in(sp.locale, 'english'):
    langFile = os.path.join(PLUGIN_PATH, lang + '.lng')
    if os.path.isfile(langFile) :
        print("Lang file found : %s" % langFile)
        sp.loadTranslation(langFile)
    # end if
# end for

# shortkeys
shortkey ={
'next_head': ['CTRL+R', None],
'next_head1': ['CTRL+1', None]
} # end shortkey dico

# shortcut programme #
page = sp.window.curPage

def test():
    sp.say("test ok", True)
    return
# end def

def get_accelerator(action):
    return shortkey[action][0]
# end def

def load_module(markup_type):
    """Load MarkPad module"""
    # Compile regex
    # fetch regex for markup language
    regex_raw = regex.get_regex(markup_type)
    regex_compiled = regex.compile_regex(regex_raw)
    
    # instantiates goto with regex compiled
    goto = goto_regex.Goto(sp, regex_compiled)
    # Creating MarkUp menu 
    
    menu_markup = win.menus.add(label = "MarkUp", action = None, index = -2, submenu = True, name = 'markup')
    # creat sub menu and global submenus and items
    submenus, items = creat_submenu(menu_markup)
    # Accelerator
    #accelerator_active = creatAccelerator(shortkey, win)
    return goto, menu_markup, submenus, items
# end def

def creat_submenu(menu_markup):
    """Creat sub menu and item for MarkPad module
    arg : menu_markup, 6pad menu type
    return submenus dico, items dico"""
    
    submenus = {}
    items = {}
    
    # Sub Menu
    # Goto
    submenus['goto'] = menu_markup.add(
    label = msg('Goto'), submenu = True, action = None, name = 'goto')
    # items in Goto sub menu
    # next_head
    items['next_head'] = submenus['goto'].add(
    label = msg('Next head'), action = lambda:goto.next_item(HEAD), accelerator = get_accelerator('next_head'), name = "next_head")

        # test
    submenus['test'] = menu_markup.add(label = "Lancer le test", submenu = False, action = test, name = "test")
    
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
         # end if
         accelerator_active[action] = win.addAccelerator(key, eval(action), True)
     # end for
     return accelerator_active
# end def
 


## main ##
# Load MarkPad module if it didn't already""" 
# Test if the menu MarkUp is not already created 
if True : #OR sp.window.menus["markup"] == None :
    goto, menu_markup, submenus, items = load_module("markdown")
    print('MarkPad load')
else:
    print("Menu already created")
# end if