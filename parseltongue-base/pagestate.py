#!/usr/bin/python
from abc import ABCMeta

'''
The Abstract Base Class for a PageState

Author: Dave Sizer <dasizer@gmail.com>
'''

class PageState:
  __metaclass__ = ABCMeta

  
  components_         # A dictionary of components 
                      # parsed from the current page state

  @abstractproperty
  def components(self):
    return self.components_



  '''
  Parses the current page state into components
  '''
  @abstractmethod
  def parse(self):
    # Abstract
    pass
