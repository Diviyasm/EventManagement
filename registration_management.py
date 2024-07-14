from collections import defaultdict

class Registration:
    def __init__(self, registration_id, event_id, participant_id, registration_date):
        self.registration_id = registration_id
        self.event_id = event_id
        self.participant_id = participant_id
        self.registration_date = registration_date

class EventManagementSystem:
    def __init__(self):
        self.registrations = defaultdict(list)

    def add_registration(self, registration):
        if registration.event_id not in self.events:
            print(f"Event ID '{registration.event_id}' not found.")
            return
        if registration.participant_id not in self.participants:
            print(f"Participant ID '{registration.participant_id}' not found.")
            return
        self.registrations[registration.event_id].append(registration)
        print(f"Registration ID '{registration.registration_id}' added successfully.")

    def update_registration(self, registration_id, **kwargs):
        found = False
        for event_registrations in self.registrations.values():
            for registration in event_registrations:
                if registration.registration_id == registration_id:
                    found = True
                    for key, value in kwargs.items():
                        if hasattr(registration, key):
                            setattr(registration, key, value)
                    print(f"Registration ID '{registration_id}' updated successfully.")
                    break
            if found:
                break
        if not found:
            print(f"Registration ID '{registration_id}' not found.")

    def cancel_registration(self, registration_id):
        found = False
        for event_id, event_registrations in self.registrations.items():
            for registration in event_registrations:
                if registration.registration_id == registration_id:
                    event_registrations.remove(registration)
                    found = True
                    print(f"Registration ID '{registration_id}' canceled successfully.")
                    break
            if found:
                break
        if not found:
            print(f"Registration ID '{registration_id}' not found.")
