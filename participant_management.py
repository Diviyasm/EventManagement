class Participant:
    def __init__(self, participant_id, name, email, phone_number):
        self.participant_id = participant_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

class EventManagementSystem:
    def __init__(self):
        self.participants = {}

    def add_participant(self, participant):
        self.participants[participant.participant_id] = participant
        print(f"Participant '{participant.name}' added successfully.")

    def update_participant(self, participant_id, **kwargs):
        if participant_id in self.participants:
            for key, value in kwargs.items():
                if hasattr(self.participants[participant_id], key):
                    setattr(self.participants[participant_id], key, value)
            print(f"Participant ID '{participant_id}' updated successfully.")
        else:
            print(f"Participant ID '{participant_id}' not found.")

    def delete_participant(self, participant_id):
        if participant_id in self.participants:
            del self.participants[participant_id]
            print(f"Participant ID '{participant_id}' deleted successfully.")
        else:
            print(f"Participant ID '{participant_id}' not found.")
