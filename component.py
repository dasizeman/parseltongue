#!/usr/bin/python
from abc import ABCMeta

'''
The Abstract Base Class for a component.  The only requirement for a component
is that it has a string representation.

Author: Dave Sizer <dasizer@gmail.com>
'''

class Component:
  __metaclass__ = ABCMeta

  @abstractmethod
  def __str__(self):
    # Abstract
    pass
