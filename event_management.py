class Event:
    def __init__(self, event_id, event_name, event_date, location, max_participants):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.max_participants = max_participants

class EventManagementSystem:
    def __init__(self):
        self.events = {}

    def add_event(self, event):
        self.events[event.event_id] = event
        print(f"Event '{event.event_name}' added successfully.")

    def update_event(self, event_id, **kwargs):
        if event_id in self.events:
            for key, value in kwargs.items():
                if hasattr(self.events[event_id], key):
                    setattr(self.events[event_id], key, value)
            print(f"Event ID '{event_id}' updated successfully.")
        else:
            print(f"Event ID '{event_id}' not found.")

    def delete_event(self, event_id):
        if event_id in self.events:
            del self.events[event_id]
            print(f"Event ID '{event_id}' deleted successfully.")
        else:
            print(f"Event ID '{event_id}' not found.")
