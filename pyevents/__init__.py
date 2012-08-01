"""
MIT LICENSE
Copyright (C) 2012 Mauricio Galdieri

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

#
# Module variables
#
_events = {}
_events_list = set()
_handlers_list = set()

#
# Utility class
#
class EventError(Exception):
    """
    Class representing an event error.
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#
# Handler specific methods
#
def add_event_handler(event_type, handler):
    """
    Adds a handler to the handlers list that will be called whenever
    the events to which this handler is registered get dispatched
    """
    if not _events.has_key(event_type):
        raise EventError("Event %s does not exists."%event_type)
    else:
        _events[event_type].add(handler)
        _handlers_list.add(handler)

def remove_event_handler(event_type, handler):
    """
    Removes a handler from the handlers list of a specific event,
    so it won't be called when this event gets dispatched
    """
    try:
        _events[event_type].remove(handler)
    except KeyError:
        raise EventError("Handler %s is not present in this event's handlers list"%handler)

def clear_event_handler(handler):
    """
    Removes a handler from the list of handlers of all
    the available events, so it won't be called anymore.
    """
    if handler not in _handlers_list:
        raise EventError("Handler %s not registered with any event."%handler)
    else:
        _handlers_list.remove(handler)
        for event in _events:
            _events[event].discard(handler)

#
# Event specific methods
#
def add_event(event):
    """
    Adds an event to the events list. All handlers registered
    with this event will be called when this event is dispatched
    """
    _events[event] = set()
    _events_list.add(event)

def remove_event(event):
    """
    Removes an event from the events list. This effectively removes
    all the handles registered with this event and it won't be available
    for dispatching anymore.
    """
    if event not in _events_list:
        raise EventError("Event %s not registered."%event)
    else:
        _events_list.remove(event)
        del _events[event]

def clear_events():
    """
    Removes all the registered events and its corresponding handlers.
    This effectively resets the events system.
    """
    _events_list.clear()
    _handlers_list.clear()
    _events.clear()

def fire(event, info={}):
    """
    Calls all the handlers registered with this event and passes them
    a dictionary containing any information relevant to the event.
    """
    for handler in _events[event]:
        handler(info)