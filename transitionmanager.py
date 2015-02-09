#!/usr/bin/python
from abc import ABCMeta

'''
The Abstract Base Class for a TransitionManager

Author: Dave Sizer <dasizer@gmail.com>
'''

class TransitionManager:
    __metaclass__ = ABCMeta
    
    '''
    Handles the transitions from from_state to to_state.  If from_state is None,
    this is most likely the beginning of parsing, or we are transitioning to the
    base state for some other reason. 
    
    TRANSITIONS TO THE BASE STATE (I.E WHEN THERE IS NO FROM_STATE) SHOULD NOT FAIL.
    
    Arguments:
    to_state - The state the parser is transitioning to
    from_state - The state the parser is currently in. If from_state is None,
    assume a transition to the base state.

    Return - True if the transition was successful, false otherwise
    '''
    @abstractmethod
    def transition_to(self,to_state, from_state=None):
        # Abstract
        pass
    '''
    Called by the parser if a transition was unsucessful because of an unknown
    current state.  Should try to deduce the state based on elements in the page
    and return this.  This is for when transition_to fails because it assumes a
    certain from_state that is somehow incorrect.

    Arguments:
    from_state - The current page state that transition_to failed to handle

    Return - The determined page state; None if this cannot be determined. 
    '''
    @abstractmethod
    def handle_unknown_state(self,from_state):
        # Abstract
        pass
