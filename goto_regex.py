# -*- coding:utf-8 -*-

"""Functions definition to go to item thanks regex compiled"""

import sixpad as sp

from .item import *

class Goto():
    def __init__(self, mul):

        self.regex_compiled = mul
    # end def
    
    def next_item(self, item_type):
        """Go to the next item_type in
        return true if item found or false if not
        """
        
        # Get current line, note that  first line is 0
        line = sp.window.curPage.curLine
        # First test with next lin
        line += 1
        # test each line
        while line < sp.window.curPage.lineCount:
            # Fetch text on this line.
            line_text = sp.window.curPage.line(line)
            try :
                # test this line with regex
                if self.regex_compiled[item_type].match(line_text):
                    # regex found item, go to this line
                    sp.window.curPage.curLine = line
                    # say this line heading 
                    sp.say(line_text, True)
                    return True
                # end if
            except KeyError:
                # The regex is not define for this language.
                sp.window.warning('This item is not defined to this language, you can append regex item in associated MUL file. Item index : %d' %item_type)
                return False
            # End except 
                                                
                                
            # increment lines counter 
            line += 1
        # end whil
        # Item not found, make a bip and return False
        sp.window.messageBeep(0)
        return False
    # end def
    
    def previous_item(self, item_type):
        """Go to the previous ite
        item_type: in
        return true if item found or false if not
        """
        
        # Get current line, note that line number start from 0. 
        line = sp.window.curPage.curLine
        # First test on the previous lin
        line -= 1
        
        # test each line
        while line >= 0:
            # Fetch text of this line
            line_text = sp.window.curPage.line(line)
            try :
                # test this line with regex
                if self.regex_compiled[item_type].match(line_text):
                    # regex found item, go to this line
                    sp.window.curPage.curLine = line
                
                    # say this line heading 
                    sp.say(line_text, True)
                    return True
                # end if
            except KeyError:
                # The regex is not define for this language.
                sp.window.warning('This item is not defined to this language, you can append regex item in associated MUL file. Item index : %d' %item_type)
                return False
            # End except 
                                                
            
            # Decrement line number to test previous lin
            line -= 1
        # end whil
        # Item not found, making bip and return False
        sp.window.messageBeep(0)
        return False
    # end def
# end class