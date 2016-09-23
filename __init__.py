# coding:utf-8

import os
import sys
import re

import sixpad as sp
from sixpad import msg
from sixpad import window as win

from . import goto_regex
from .item import *
from . import tracer

# shortkeys
shortkey ={
'next_head': ['CTRL+R', None],
'next_head1': ['CTRL+1', None],
'previous_head':['CTRL+SHIFT+R', None],
'previous_head1': ['CTRL+SHIFT+1', None]
} # end shortkey dico

# shortcut programme #
curPage= sp.window.curPage

def get_accelerator(action):
    return shortkey[action][0]
# end def

def load_markpad(mul):
    """Load MarkPad module"""
    
    # Creating MarkUp menu
    menu_markup = win.menus.add(label = "MarkUp", action = None, index = -2, submenu = True, name = 'markup', specific = True)
    # creat sub menu and global submenus and items
    submenus, items = creat_submenu(menu_markup)
    # Accelerator
    #accelerator_active = creatAccelerator(shortkey, win)
    return menu_markup, submenus, items
# end def

def creat_submenu(menu_markup):
    """Creat sub menu and item for MarkPad modul
    arg : menu_markup, 6pad menu typ
    return submenus dico, items dico"""
    
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
        # end if
        # end i
        accelerator_active[action] = win.addAccelerator(key, eval(action), True)
    # end for
    # end fo
    return accelerator_active
# end def

def load_translate_file():
    """Load the lang file to translate markpad"""
    # Load language
    for lang in(sp.locale, 'english'):
        lang_file = os.path.join(PLUGIN_PATH, lang + '.lng')
        if os.path.isfile(lang_file) :
            # Lang file found
            sp.loadTranslation(lang_file)
        # end if
    # end for
# end def

class MarkupManager():
    """Manage markup language
    @ plugin_path : Module path to scan MUL file into markup language directory
    * Scan MUL File
    * Exctract capabilities into caps dictionary
    * Generate MUL instance from extension"""
    
    def __init__(self, plugin_path):
        """Load markdown language definition"""
        # Load markup language definition from language directory
        self.markup_languages = self._fetch_markup_definition(plugin_path)
        # Extract extensions capability from each markup language
        self.caps = self._extract_capabilitys(self.markup_languages)
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
                mul_name = file_name[:-4]
                mul_path = os.path.join(lang_path, file_name)
                # Add this markup language into markup definition dictionary
                markup_langs[mul_name] = self._parse_mul_file(mul_name, mul_path)
            # end if # mul file found
        # end for # file
        return markup_langs
    # end def
    
    def _parse_mul_file(self, mul_name, mul_path):
        """Parse mul file and return MarkupLanguage definition""" 
        # Open file.
        mul_file = open(mul_path, encoding='utf8')
        # Instanciate MarkupLanguage class
        mul = MarkupManager.MarkupLanguage(mul_name, mul_path)
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
                value = eval(value)
                # find key type, extension, help or regex
                if 'extension' in key:
                    # Value is a list of extension compatible
                    mul.extension = value
                elif 'help' in key:
                    mul.help = value
                else:
                    # Regex definition
                    # Convert item type 
                    key = eval(key)
                    mul[key] = value
                # end if
            except ValueError : 
                print('Error during MarkPad load Markup language definition\nFile : %s\nSyntaxe error at line %d\n%s' %(mul_path, n_line, line))
                return -1
            # end try
            # end except
            
        # end for
        mul_file.close()
        return mul
    # end def
    
    def _extract_capabilitys(self, markup_languages):
        """From markup languages dico, return capability dictionary
        
        @ markup_languages, dictionary containing mul dico;
        return capability, dictionary. [ext]:"markup language name"
        """
        
        # Instanciate capability dictionary
        caps = {}
        # Extract extension from each language
        for mul in markup_languages.values():
            # Test Verify extension definition.
            if not mul.extension:
                print('Warning, no "extension" definition found in "%s" markup language' % mul.name)
                # next language
                continue
            # end if
            # explore each extension and add it in the capability dictionary with its language
            for ext in mul.extension:
                caps[ext] = mul.name
            # end for # , ext
        # end for # , mul
        return caps
    # end def
    
    class MarkupLanguage(dict):
        def __init__(self, name, path):
            self.name = name
            self.path = path
            self.help = None
            self.extension = None
            self._compiled = False
        # end def
        
        def compile_regex(self):
            if self._compiled:
                # Regex already compiled
                return
            # end if
            # Compile regex
            for item_type, regex_raw in self.items():
                mul[item_type] = re.compile(regex_raw, re.MULTILINE)
            # end for
            self._compiled = True
        # end def
        
        def create_goto_fonction(self):
            self.goto = goto_regex.Goto(sp, self)
        # end def
    # end class MarkupLanguage
# end class MarkupManager

def page_opened(page):
    # fetch extension of this new page
    ext = os.path.splitext(page.file)[1][1:].lower()
    if not ext:
        ext = 'noext'
    # Search language for this extension
    if ext in markup_manager.caps.key:
        # MUL available for this extension
        mul_name = mul.caps[ext]
        # Load MarkupLanguage 
        page.mul = markup_manager.markup_languages[mul_name]
        page.mul.goto, menu_markup, submenus, items = load_module("markdown")
# end def

## main ##
# Init log systeme
log_file_path = os.path.join(PLUGIN_PATH, 'log_markpad.md')
log = tracer.Tracer(log_file_path)
log.h1('MarkPad log')
log.print_time()

# Load lng file to translate markpad
load_translate_file()

# Init Markup Manager.
# Scan MUL files to find languages and extract compatible extension list.
markup_m = MarkupManager(PLUGIN_PATH)

win.addEvent('pageOpened', page_opened)

#menu_markup, submenus, items = load_markpad("markdown")
print("fin du main")
