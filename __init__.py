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
from . import tree_doc

# shortcut programme #
curPage = sp.window.curPage

def get_shortkey(action):
    """get_shortkey(action) -> shorkey, str"""
    
    # shortkeys
    shortkey ={
        'next_head': ['CTRL+R', None],
        'previous_head':['CTRL+SHIFT+R', None],
        'next_head1': ['CTRL+&', None],
        'previous_head1': ['CTRL+SHIFT+&', None],
        'next_head2': ['CTRL+é', None],
        'previous_head2': ['CTRL+SHIFT+é', None],
        'next_head3': ['CTRL+"', None],
        'previous_head3': ['CTRL+SHIFT+"', None],
        'next_head4': ["CTRL+'", None],
        'previous_head4': ["CTRL+SHIFT+'", None],
        'next_head5': ['CTRL+(', None],
        'previous_head5': ['CTRL+SHIFT+(', None],
        'next_link': ['CTRL+k', None],
        'previous_link': ['CTRL+SHIFT+k', None],
        'open_extended_tree': ['CTRL+à', None]
    } # end shortkey dico
    
    value = shortkey[action]
    # test if user set personal key for this action
    if value[1]:
        # User shortkey found
        key = value[1]
    else:
        # Default shortkey used
        key = value[0]
    # end if
    return key
# end def

def load_markpad(page):
    """Load MarkPad module"""
    
    log.h2('Load Markpad with %s language' % page.mul.name)
    # Compile regex
    page.mul.compile_regex()
    # Create goto functions
    page.mul.generate_goto_functions()
    # Creating MarkUp menu
    log('Create MarkPad menu')
    menu_markup = win.menus.add(label = "MarkPad", action = None, index = -2, submenu = True, name = 'markpad', specific = True)
    # creat sub menu and global submenus and items
    log('creat sub menu and global submenus and items')
    submenus, items = creat_submenu(menu_markup, page.mul.goto)
    # Accelerator
    log('creat accelerators')
    accelerator_active = creat_accelerator(page.mul)
    return menu_markup, submenus, items
# end def

def creat_submenu(menu_markup, goto):
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
        label = msg('Next head'), action = lambda: goto.next_head(HEAD), accelerator = get_shortkey('next_head'), name = "next_head")
    # Previous head
    items['previous_head'] = submenus['goto'].add(
        label = msg('Previous head'), action = lambda:goto.previous_head(HEAD), accelerator = get_shortkey('previous_head'), name = "previous_head")
    # next head 1
    items['next_head1'] = submenus['goto'].add(
        label = msg('Next level 1 heading'), action = lambda: goto.next_head(HEAD1), accelerator = get_shortkey('next_head1'), name = "next_head1")
    # Previous head 1
    items['previous_head1'] = submenus['goto'].add(
        label = msg('Previous level 1 heading'), action = lambda:goto.previous_head(HEAD1), accelerator = get_shortkey('previous_head1'), name = "previous_head1")
    # next link
    items['next_link'] = submenus['goto'].add(
        label = msg('Next link'), action = lambda: goto.next_link(LINK), accelerator = get_shortkey('next_link'), name = "next_link")
    # Previous link
    items['previous_link'] = submenus['goto'].add(
        label = msg('Previous link'), action = lambda:goto.previous_link(LINK), accelerator = get_shortkey('previous_link'), name = "previous_link")
    return submenus, items
# end def

def creat_accelerator(mul):
    """ Create accelerators from shorkey dico and return accelerator_active"""
    
    goto = mul.goto
    accelerator_active = {}
    
    # Tree
    accelerator_active['open_extended_tree'] = win.addAccelerator(
            get_shortkey('open_extended_tree'), tree_doc.TreeDoc(page.mul), True)

    # Goto
    # Next level 2 heading.
    accelerator_active['next_head2'] = win.addAccelerator(
        get_shortkey('next_head2'), lambda:goto.next_head(HEAD2), True)
    # Previous level 2 heading.
    accelerator_active['previous_head2'] = win.addAccelerator(
        get_shortkey('previous_head2'), lambda:goto.previous_head(HEAD2), True)
    # Next level 3 heading.
    accelerator_active['next_head3'] = win.addAccelerator(
        get_shortkey('next_head3'), lambda:goto.next_head(HEAD3), True)
    # Previous level 3 heading.
    accelerator_active['previous_head3'] = win.addAccelerator(
        get_shortkey('previous_head3'), lambda:goto.previous_head(HEAD3), True)
    # Next level 4 heading.
    accelerator_active['next_head4'] = win.addAccelerator(
        get_shortkey('next_head4'), lambda:goto.next_head(HEAD4), True)
    # Previous level 4 heading.
    accelerator_active['previous_head4'] = win.addAccelerator(
        get_shortkey('previous_head4'), lambda:goto.previous_head(HEAD4), True)
    # Next level 5 heading.
    accelerator_active['next_head5'] = win.addAccelerator(
        get_shortkey('next_head5'), lambda:goto.next_head(HEAD5), True)
    # Previous level 5 heading.
    accelerator_active['previous_head5'] = win.addAccelerator(
        get_shortkey('previous_head5'), lambda:goto.previous_head(HEAD5), True)
    return accelerator_active
# end def

def load_translate_file():
    """Load the lang file to translate markpad"""
    log.h1('Load translate file')
    # Load language
    for lang in(sp.locale, 'english'):
        lang_file = os.path.join(PLUGIN_PATH, lang + '.lng')
        if os.path.isfile(lang_file) :
            # Lang file found
            log('Lang file found : %s' % lang)
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
        
        log.h1('Markup Manager init')
        # Load markup language definition from language directory
        self.markup_languages = self._fetch_markup_definition(plugin_path)
        # Extract extensions capability from each markup language
        self.caps = self._extract_capabilitys(self.markup_languages)
    # end def

    def _fetch_markup_definition(self, plugin_path):
        """Create MUL file dictionary from file present into "markup language" directory"""

        log.h2('Scan markup language directory')        
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
                log.h3('%s.mul' % mul_name) 
                # Add this markup language into markup definition dictionary
                parse_result = self._parse_mul_file(mul_name, mul_path)
                # Test parsing result.
                if parse_result:
                    log('"%s" language added in markup manager' % mul_name)
                    markup_langs[mul_name] = parse_result
            # end if # mul file found
        # end for # file
        log('Scan MUL file completed')
        return markup_langs
    # end def
    
    def _parse_mul_file(self, mul_name, mul_path):
        """Parse mul file and return MarkupLanguage definition""" 
        
        log('Parsing MUL file "%s"' % mul_name)
        # Open file.
        log('Open file "%s"' % mul_path)
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
                    log('Extensions declared : ' + str(value)[1:-1])
                    mul.extension = value
                elif 'help' in key:
                    # Help page definition
                    log('Help link : ' + value)
                    mul.help = value
                else:
                    # Regex definition
                    log('%s, regex : "%s"' %(key, value))
                    # Convert item type 
                    try : 
                        key = eval(key)
                        mul[key] = value
                    except NameError :
                        win.warning('Parsing MUL file error.\nFile : "%s"\nRrror at line %d :\n%s\nItem type "%s" does not exist.\nThis item will be ignored.' %(mul_path, n_line, line, key), 'Markpad Error')
                        log('Warning at line %d : Item type %s does not exist. Item ignored' %( n_line, key))
                    # end try
                # end if
            except ValueError and SyntaxError : 
                win.warning('Parsing MUL file error.\nFile : "%s"\nSyntaxe error at line %d\n%s' %(mul_path, n_line, line), 'Markpad Error')
                log('Error at line %d : %s' %( n_line, line))
                return None
            # end try
        # end for
        log('Close MUL file')
        mul_file.close()
        return mul
    # end def
    
    def _extract_capabilitys(self, markup_languages):
        """From MarkupManager containing MUL definition, extract markpad capabilities
        @ markup_languages, dictionary containing mul dico;
        return capability, dictionary. [ext]:"markup language name"
        """
        
        log.h2('Extract Markpad capabilities')
        # Instanciate capability dictionary
        caps = {}
        # Extract extension from each language
        for mul in markup_languages.values():
            # Verify extension definition.
            if not mul.extension:
                log('Warning, no "extension" definition found in "%s" markup language' % mul.name)
                win.warning('No extension found into "%s" markup language definition. This language will be ignored.' % mul.name, 'Markpad warning')
                # next language
                continue
            # end if
            # explore each extension and add it in the capability dictionary with its language
            log('"%s" extensions :\n%s' %(mul.name, str(mul.extension)[1:-1]))
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
                log('Regex already compiled')
                return
            # end if
            # Compile regex
            for item_type, regex_raw in self.items():
                log('Compile %s' % item_type)
                self[item_type] = re.compile(regex_raw, re.MULTILINE)
            # end for
            log('Compile completed')
            self._compiled = True
        # end def
        
        def generate_goto_functions(self):
            # Verify is goto function have not already been created
            if hasattr(self, "goto"):
                log('Gotot functions alredy generated') 
            else:
                log('Creat goto function for this language')
                self.goto = goto_regex.Goto(self)
        # end def
    # end class MarkupLanguage
# end class MarkupManager

def page_opened(page):
    """Start when new page is openned.
    find file extension and load markPad if a markup language uses this extension""" 
    
    # fetch extension of this new page
    log.h1('Page "%s" opened, search kind of this document' % page.name)
    ext = os.path.splitext(page.file)[1][1:].lower()
    if not ext:
        # This page contains a new file or file without extension.
        log('Page not saved page or file without extension.')
        ext = 'noext'
    # end if
    log('File extension : %s' % ext)
    # Search language for this extension
    if ext in markup_manager.caps:
        # MUL available for this extension
        mul_name = markup_manager.caps[ext]
        log('Markup language found : "%s".' %mul_name)
        # Add MUL reference in page
        page.mul = markup_manager.markup_languages[mul_name]
        # Load module markPad
        menu_markup, submenus, items = load_markpad(page)
    else:
        log('No markup language found for this kind of document')
        log('Markpad not loaded for "%s".' % page.name)
    # end else
# end def

## main ##
# Init log systeme
log_file_path = os.path.join(PLUGIN_PATH, 'log_markpad.md')
log = tracer.Tracer(log_file_path)
log.h1('MarkPad trace')
log.print_time()

# Load lng file to translate markpad
load_translate_file()

# Init Markup Manager.
markup_manager = MarkupManager(PLUGIN_PATH)

# Add event to load module when new page is open
win.addEvent('pageOpened', page_opened)
# Load module for the initial page
page_opened(win.curPage)
