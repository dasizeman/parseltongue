#!/usr/bin/python

import logging

"""
This is the main ParselTongue Parser class.  It handles storing the current page
state as well as the class responsible for managing page transitions.

Author: Dave Sizer <dasizer@gmail.com>
"""

class Parser:
    current_state       # The PageState that the parser currently thinks its in

    base_state          # The place where the parser starts, and where it will
                        # return to if something goes wrong

    transition_manager  # The TransitionManager that defines how to transitions
                        # occur on this site

    page_states         # The dictionary of page states that this parser knows
                        # How to handle

    logger              # The logger for this parser

    '''
    Initialize a new Parser.

    Arguments:
    transition_manager - The TransitionManager to be used with this parser.

    base_state - The PageState this parser will begin on.  The parser will
    begin by calling the transition logic to this state.  Transition to this
    state SHOULD NOT fail, except for some server-side problems. In other words,
    this transition should be just a GET, and not require certain page elements
    to be present
    '''
    def __init__(self,project_path, base_state):
        self.load_components(project_path)
        self.base_state = base_state
        self.change_state(base_state)
        self.logger = logging.getLogger('parser')
        self.logger.setLevel(logging.DEBUG)

    '''
    Change from the current state to a new one.  Will handle the transition
    between states based on the transition manager

    Arguments:
    to_state - The state to transition to.

    from_state - The state to assumed before the transition.  In every case
    except at the beginning of parsing, this will be current_state (unless you
    want to call this manually for some reason).  At the beginning, it will be
    None
    '''
    def change_state(self,to_state, from_state=None):
        #TODO: Resolve the named state to an actual PageState object here, and
        # pass it into the transtion manager.
        if self.transition_manager.transition_to(to_state, from_state):
            self.current_state = to_state
        else:
            self.current_state = self.transition_manager.handle_unknown_state()
            if not self.current_state:
                self.logger.warning('The transition manger encountered an' +
                'unhandled state, returning to base state.')
                self.transition_manager.transition_to(base_state)
                self.current_state = base_state

    self.current_state.parse();

    def load_elements(self, project_path):
        # TODO: Use refection to load the transition manager and states, and put
        # everything in the python path
        for item in os.lsdir(project_path):
            print item

    '''
    Return the component dictionary of the current state
    '''
    def get_components(self):
        return self.current_state.get_components()

            



