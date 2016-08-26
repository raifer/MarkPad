# coding:utf-8

import os
import sys
import re

import sixpad as sp

# Constant
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
textFR={
'goto': 'Déplacement',
'nextHead': 'Allé au titre suivant'
} # end dico

# shortkeys
shortkey={
'Goto.nextHead': ['CTRL+H', None],
'Goto.nextHead1': ['CTRL+1', None]
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

class Goto(object):
    """Functions to go to item"""

    def nexItem(itemType):
        """Go to the next item
        itemType: int
        return true if item found or false if not.
        """
        
        # Get current line
        line = sp.window.curPage.curLine
        # test each line
        while line < page.lineCount():
            line += 1
            # test this line with regex
            if regexCompiled[itemType].match(page.line(line)):
                # regex found item, go to this line
                page.curLine = line
                # say this line heading 
                sayText(getLineHeading(page.curLine), True)
                return True
            # end if
        # end while
        # Item not found, bip and return False
        sp.window.messageBeep(0)
        return False
    # end def
# end class

def loadMarkPad():
    """Load MakPad module if it didn't already""" 
    # Test if the menu MarkUp is not already created 
    if sp.window.menus["markUp"] == None:
        # Load MarkPad module
        # Compile regex
        regexCompiled = compileRegex(regex)
        # Creating MarkUp menu 
        menuMarkUp = sp.window.menus.add(label = "MarkUp", action = None, index = -3, submenu = True, name = 'markUp')
        # sub menu
        creatSubMenu()
        # Accelerator
        AcceleratorActive = creatAccelerator()
    # end if
# end def

def creatSubMenu(menuMarkUp):
    # template
    #menu = menuMarkUp.add(label = "", submenu = True, action = None, name = "")
    
    # Goto
    menuGoto = menuMarkUp.add(
    label = text['menuGoto'], submenu = True, action = None, name = 'goto')
    # Goto sub menu
    # nextHead
    menuNextHead = menuMarkUp.add(
    label = text['nextHead'], submenu = False, function = Goto.nextItem(HEAD), name = "nextHead")

        # test
    menuTest = menuMarkUp.add(label = "Lancer le test", submenu = False, action = test, name = "test")
# end def

def creatAccelerator(shortkey):
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
         AcceleratorActive[action] = sp.window.addAccelerator(key, eval(action), True)
     # end for
     return AcceleratorActive
# end def
 
def compileRegex(regex):
     # creating dico for compiled regex
     regexCompiled = {}
     for item, regexText in regex.items():
         regexCompiled[item] = re.compile(regexText, re.MULTILINE)
     # end for
     return regexCompiled
# end def


if __name__ == "__main__":
    # Store accelerators into dictionary
    global AcceleratorActive
    # Dictionary to store compiled regex
    global regexCompiled
    # Store markup menu into dictionary
    global menuMarkUp
    
    loadMarkPad()
    sp.say("fin du script", True)
else:
    print("not main")