Parseltongue - A State-Based Python Web Parsing Engine

Goals - Develop a highly extensible, robust, and scalable framework for parsing
and interacting with websites.

Paradigms - Hopefully Python does/can play nice with inheritance and/or
abstract classes (turns out it does as of 2.7.9, with ABCMeta functionality!
Will have to see how this works)

I will outline the classes I have thought of so far as well as how I forsee
them interacting: 
-Parser 
-PageState 
-TransitionManager 
-Component
-BasicActionHelper

The Parser will store the current page state.  A PageState will contain methods
for parsing a certain type of page, as well as store information about the
current page, specifically a map of named Components.  A Component will have
some sort of structure for storing information about page elements.  A
TransitionManager will hold logic regarding how to deal with transitions between
PageStates (a transition could be passed as a pair of PageStates). A
well-developed TransitionManager will likely check the PageState to make sure
that the components required for the transition have actually been found.  The
Parser will have a transition_to() method, which when called will invoke the
TransitionManager's handling logic and pass it the current PageState.  

Hopefully I will be able to take advantage of virtual/abstract methods/classes
here, as most of the classes will be implemented on a site-specific basis.  A
PageState's parsing in order to populate the component dictionary will be
abstract.  Components themselves will be abstract, as it will probably be useful
to implement custom methods of storing component data.  The TransitionManager
will be abstract, but will need to implement perform_transition(), which will
handle the transition for any pair of states.  

Finally, the BasicActionHelper, like its name suggests, is just a helper class
for performing basic interactions with a webserver such as HTTP GET and POST.
If this framework gets off the ground and there is a demand and/or personal need
for it, I will write other functionality modules as well.

I can probably set up the framework so that it can dynamically import parser
elements given that they are in a predefined directory structure.  Like so:
parseltongue_project/
  --manager/
  --states/
  --components/
  --helpers/
Where each directory contains the python files for the elements

In the far of future, it would be nice to develop a type of scripting language
for use with Parseltongue, which would allow automatic, dynamic website
scrapings and data collection.  But let's focus on actually building the core
framework first.

I will be making an example project using the framework, which I hope will also
be a nice example of how I see it actually being used.  Stay tuned.
