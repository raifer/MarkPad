# -*- coding:utf-8 -*-

"""Functions definition to go to item thanks regex compiled"""

import sixpad as sp

from .item import *

class Goto():
    def __init__(self, mul):

        self.regex_compiled = mul
    # end def
    
    def next_head(self, header_level):
        """next_head(int header_level) --> bool match result
        Go to the next header item in
        return true if item found or false if not
        """
        
        # Get current line.
        # note: the  first line of the document is 0.
        line = sp.window.curPage.curLine
        # Skip curent line.
        line += 1
        # test each line
        while line < sp.window.curPage.lineCount:
            # Fetch text on this line.
            line_text = sp.window.curPage.line(line)
            try :
                # test this line with regex
                m_result = self.regex_compiled[header_level].search(line_text)
                if m_result :
                    # regex found item, go to this line
                    sp.window.curPage.curLine = line
                    
                    # Make and Say the result
                    # Fetch header's level.
                    if header_level == HEAD:
                        # Fetch the header level. 
                        say_level = str(self.get_header_level(line_text)) + ', '
                    else:
                        say_level = ''
                    # end else
                    # Test if regex containing parenthesis to say only the text.
                    if m_result.lastindex:
                        text = m_result.group(1)
                    else:
                         text = line_text
                     # end else
                    say_text = say_level + text
                    sp.say(say_text, True)
                    return True
                # end if
            except KeyError:
                # The regex for this header level is not define for this language.
                sp.window.warning('The regex for this header level is not defined in this language, you can append regex item in associated MUL file. Header index : %d' % header_level)
                return False
            # End except 
            # Goto to the next line
            line += 1
        # end whil
        # Item not found, making bip and return False
        sp.window.messageBeep(0)
        return False
    # end def
    
    def previous_head(self, header_level):
        """previous_head(int header_level) --> bool match result
        Go to the previous header item in
        return true if item found or false if not
        """
        
        # Get current line.
        # note: the  first line of the document is 0.
        line = sp.window.curPage.curLine
        # Skip curent line.
        line -= 1
        # test each line
        while line >= 0:
            # Fetch text on this line.
            line_text = sp.window.curPage.line(line)
            try :
                # test this line with regex
                m_result = self.regex_compiled[header_level].search(line_text)
                if m_result :
                    # regex found item, go to this line
                    sp.window.curPage.curLine = line
                    
                    # Make and Say the result
                    # Fetch header's level.
                    if header_level == HEAD:
                        # Fetch the header level. 
                        say_level = str(self.get_header_level(line_text)) + ', '
                    else:
                        say_level = ''
                    # end else
                    # Test if regex containing parenthesis to say only the text.
                    if m_result.lastindex:
                        text = m_result.group(1)
                    else:
                         text = line_text
                     # end else
                    say_text = say_level + text
                    sp.say(say_text, True)
                    return True
                # end if
            except KeyError:
                # The regex for this header level is not define for this language.
                sp.window.warning('The regex for this header level is not defined in this language, you can append regex item in associated MUL file. Header index : %d' % header_level)
                return False
            # End except 
            # Goto to the next line
            line -= 1
        # end whil
        # Item not found, making bip and return False
        sp.window.messageBeep(0)
        return False
    # end def

    def next_link(self, item_type):
        """Go to the mext link 
        item_type: in
        return true if item found or false if not
        """
        
        # Get current line, note that line number start from 0. 
        line = sp.window.curPage.curLine
        # Start search at the position of the cursor.
        cur_column = sp.window.curPage.curColumn + 1
        
        while line < sp.window.curPage.lineCount:
            # Get line offset.
            line_offset = sp.window.curPage.lineStartOffset(line)
            # Fetch text of this line
            line_text = sp.window.curPage.line(line)
            try:
                # test this line with regex.
                m_result = self.regex_compiled[item_type].search(line_text, pos = cur_column)
            except KeyError:
                # The regex is not define for this language.
                sp.window.warning('This item is not defined to this language, you can append regex item in associated MUL file. Item index : %d' % item_type)
                return False
            # End except                 
            
            if m_result:
                # Get the position of the result
                match_pos = m_result.start()
                # Jump to this position
                sp.window.curPage.position = match_pos + line_offset
                # say this match result
                sp.say(m_result.group(0), True)
                return True
            # end if
            
            # For the next loop
            line += 1
            cur_column = 0
        # end while
        
        # Item not found, making bip and return False
        sp.window.messageBeep(0)
        return False
    # end def
    
    def previous_link(self, item_type):
        """Go to the previous link 
        item_type: in
        return true if item found or false if not
        """
        
        # Get current line, note that line number start from 0. 
        line = sp.window.curPage.curLine
        # Start search at the position of the cursor.
        #Get column position 
        cur_column = sp.window.curPage.curColumn
        
        while line >= 0:
            # Get line offset.
            line_offset = sp.window.curPage.lineStartOffset(line)
            # Fetch text of this line
            line_text = sp.window.curPage.line(line)
            try:
                # test this line with regex.
                iter_result = self.regex_compiled[item_type].finditer(line_text, pos = 0, endpos = cur_column)
            except KeyError:
                # The regex is not define for this language.
                sp.window.warning('This item is not defined to this language, you can append regex item in associated MUL file. Item index : %d' % item_type)
                return False
            # End except                 
            
            m_result = None
            # Keep last result.
            for m_result in iter_result:
                pass
            
            if m_result:
                # Get the position of the result
                match_pos = m_result.start()
                # Jump to this position
                sp.window.curPage.position = match_pos + line_offset
                # say this match result
                sp.say(m_result.group(0), True)
                return True
            # end if
            
            # For the next loop
            line -= 1
            # Move search cursor at the end of this line.
            cur_column = sp.window.curPage.lineLength(line)
        # end while
        
        # Item not found, making bip and return False
        sp.window.messageBeep(0)
        return False
    # end def
    
    def get_header_level(self, line_text):
        """get_header_level(line_text) --> int level of header or False 
        Return the level of the header passed in line_text. 
        Return False if the text does not contain header."""
        
        # For each level 1 to 5, test line_text with regex
        for level in range(1, 6) :
             if self.regex_compiled[level].search(line_text):
                 return level
         # end for
         # Header's level not found
        return False
     # end def
# end class