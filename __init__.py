# coding:utf-8


import os
import sys
import re

import sixpad as sp
from sixpad import msg
from sixpad import window as win

# Constant
# Plugin path

PLUGINPATH= sp.appdir + '\\plugins\\markpad\\'

## itemType
HEAD = 0
HEAD1 = 1
HEAD2 = 2
HEAD3 = 3
HEAD4 = 4
HEAD5 = 5
HEAD6 = 6
HEAD7 = 7
HEAD8 = 8
HEAD9 = 9
LIST = 10
LIST1 = 11
LIST2 = 12
LIST3 = 13
LIST4 = 14

# text IHM
for lang in(sp.locale, 'english'):
    langFile = os.path.join(PLUGINPATH, lang + '.lng')
    if os.path.isfile(langFile) :
        print("Lang file found : %s" % langFile)
        sp.loadTranslation(langFile)

textFR={
'goto': 'Déplacement',
'nextHead': 'Allé au titre suivant'
} # end dico

# shortkeys
shortkey ={
'nextHead': ['CTRL+H', None],
'nextHead1': ['CTRL+1', None]
} # end shortkey dico

# shortcut programme #
page = sp.window.curPage

# Regex definition #
# devra être viré
regex = {
    HEAD:'^#+ '
    #"regClsPython": "^[ \t]*class[^\\w\
    #"regFuncPython": "^[ \t]*def[^\\w\\d_].*?:.*",
    #"regClsAndFuncPython": "^[ \t]*((?:class|def)[^\\w\\d_].*?:.*$)"
} # end regex dico

def test():
    sp.say("test ok", True)
    return
# end def

def getAccelerator(action):
    return shortkey[action][0]
# end def

class Goto(object):
    """Functions to go to item"""

def nextItem(itemType):
    """Go to the next item
    itemType: int
    return true if item found or false if not.
    """
    
    # Get current line
    line = sp.window.curPage.curLine
    # test each line
    while line < page.lineCount:
        lineText = page.line(line)
        line += 1
        # test this line with regex
        if regexCompiled[itemType].match(lineText):
            # regex found item, go to this line
            page.curLine = line
            # say this line heading 
            sp.say(page.curLineText, True)
            return True
        # end if
    # end while
    # Item not found, bip and return False
    sp.window.messageBeep(0)
    return False
# end def
# end class

def loadModule(markUpType):
    """Load MarkPad module"""
    # Compile regex
    # fetch regex for markUp language
    regex=getRegex(markUpType)
    regexCompiled = compileRegex(regex)
    # Creating MarkUp menu 
    menuMarkUp = win.menus.add(label = "MarkUp", action = None, index = -2, submenu = True, name = 'markUp')
    # creat sub menu and global subMenus and items
    subMenus, items = creatSubMenu(menuMarkUp)
    # Accelerator
    #AcceleratorActive = creatAccelerator(shortkey, win)
    return regexCompiled, menuMarkUp, subMenus, items

def creatSubMenu(menuMarkUp):
    """Creat sub menu and item for MarkPad module
    arg : menuMatkUp, 6pad menu type
    return subMenus dico, items dico"""
    
    subMenus = {}
    items = {}
    
    # Sub Menu
    # Goto
    subMenus['goto'] = menuMarkUp.add(
    label = msg('Goto'), submenu = True, action = None, name = 'goto')
    # items in Goto sub menu
    # nextHead
    items['nextHead'] = subMenus['goto'].add(
    label = msg('Next head'), action = lambda:nextItem(HEAD), accelerator = getAccelerator('nextHead'), name = "nextHead")

        # test
    subMenus['test'] = menuMarkUp.add(label = "Lancer le test", submenu = False, action = test, name = "test")
    
    return subMenus, items
# end def

def creatAccelerator(shortkey, win):
     """ Create accelerators from shorkey dico and return AcceleratorActive"""

     AcceleratorActive = {}
     for action, value in shortkey.items():
         # test if user set personal key for this action
         if value[1]:
             # User shortkey found
             key = value[1]
         else:
             # Default shortkey used
             key = value[0]
         # end if
         AcceleratorActive[action] = win.addAccelerator(key, eval(action), True)
     # end for
     return AcceleratorActive
# end def
 
def getRegex(markUpType):
    return regex

def compileRegex(regex):
     # creating dico for compiled regex
     regexCompiled = {}
     for item, regexText in regex.items():
         regexCompiled[item] = re.compile(regexText, re.MULTILINE)
     # end for
     return regexCompiled
# end def

## main ##
# Load MarkPad module if it didn't already""" 
# Test if the menu MarkUp is not already created 
if True :#OR sp.window.menus["markUp"] == None :
    regexCompiled, menuMarkUp, subMenus, items = loadModule("markdown")
    print('MarkPad load')
    # end if
else:
    print("Menu already created")