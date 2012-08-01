PyEvents
========

PyEvents is a simple, pure python event system that handles events and handlers registration as well as events dispatching.

Usage:

1) On the handler side
    - Import the event module.
    - If the event you'll be registering with has a helper module or class
      describing the events, import it too.
    - Register the handler with the desired event passing the event id along
      with a reference to the handler. The handler should accept a dictionary
      as a parameter to have access to event specific information.
    - TIP: a single handler can register with multiple events.

    Example:
    import pyevents
    from <module> import <events_descriptions>

    # the event handler
    def some_function(info):
        print info[<some_info>]

    # register a function with an event. note the
    # handler function is registered without the ()
    event.add_event_handler(<events_descriptions>.<SOME_EVENT>, some_function)

    Now, whenever the event <SOME_EVENT> gets dispatched, the handler
    some_function(info) will be called and some additional info maybe
    passed along in the info dict, depending on the event.

2) On the event side
    - Import the event module.
    - OPTIONAL: create a module or class to contain descriptions to the desired
      events and import it too. This can be just a bunch of string or int
      variables with descriptive names.
    - Register the event with the event system.
    - When the time comes, dispatch the event.

    Example:
    import events
    from <module> import <events_descriptions>

    # register all the events described in <events_descriptions>
    for evt in dir(<events_descriptions>):
        # skip __builtin__ names
        if evt[:2] != '__':
            events.add_event(evt)

    (...) later in the code, when a particular state is reached
          and you wish to dispatch an event signaling it (...)

    events.fire(<events_descriptions>.<SOME_EVENT>, {'info':'some_info'})

That's it! Simple, huh?