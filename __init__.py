# coding:utf-8

import os
import sys
import re

import sixpad as sp

# Shortcut programme #
page = sp.window.curPage

# Regex definition #
regexp = {
    "regClsPython": "^[ \t]*class[^\\w\
    "regFuncPython": "^[ \t]*def[^\\w\\d_].*?:.*",
    "regClsAndFuncPython": "^[ \t]*((?:class|def)[^\\w\\d_].*?:.*$)"}

def test():
    sp.say("test ok", True)
    #print("Fonction teste lancée")
    return

def nexItem(itemType):
    regexCompiled = re.compile(regexp[itemType], re.MULTILINE)
    line = sp.window.curPage.curLine

    while line < page.lineCou        line += 1
        if regHead.match(page.line(line)):
            page.curLine = line
            sayText(getLineHeading(page.curLine), True)
            return True
    # end while
    sp.window.messageBeep(0)
    return False

# Teste si le menu MarkUp n'est pas déjà crée
if sp.window.menus["markUp"] == None:
    # Création du menu MarkUp
    menuMarkUp = sp.window.menus.add(label = "MarkUp", action = None, index = - 3, submenu = True, name = "markUp")
    menuTest = menuMarkUp.add(label = "Lancer le test", submenu = False, action = test, name = "test")

# test raccourci
idAcceleratorTest = sp.window.addAccelerator("CTRL+T", test, True)
 
 
sp.say("fin du script", True)