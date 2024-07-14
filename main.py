from event_management import Event, EventManagementSystem
from participant_management import Participant
from registration_management import Registration
import datetime

def main():
    system = EventManagementSystem()

    while True:
        try:
            print("\nEvent Management System")
            print("1. Add Event")
            print("2. Update Event")
            print("3. Delete Event")
            print("4. Add Participant")
            print("5. Update Participant")
            print("6. Delete Participant")
            print("7. Add Registration")
            print("8. Update Registration")
            print("9. Cancel Registration")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                event_id = int(input("Enter event ID: "))
                event_name = input("Enter event name: ")
                event_date = input("Enter event date (YYYY-MM-DD): ")
                location = input("Enter event location: ")
                max_participants = int(input("Enter maximum participants: "))
                event = Event(event_id, event_name, event_date, location, max_participants)
                system.add_event(event)

            elif choice == "2":
                event_id = int(input("Enter event ID to update: "))
                kwargs = {}
                if input("Update event name? (y/n): ") == "y":
                    kwargs['event_name'] = input("Enter new event name: ")
                if input("Update event date? (y/n): ") == "y":
                    kwargs['event_date'] = input("Enter new event date (YYYY-MM-DD): ")
                if input("Update event location? (y/n): ") == "y":
                    kwargs['location'] = input("Enter new event location: ")
                if input("Update max participants? (y/n): ") == "y":
                    kwargs['max_participants'] = int(input("Enter new max participants: "))
                system.update_event(event_id, **kwargs)

            elif choice == "3":
                event_id = int(input("Enter event ID to delete: "))
                system.delete_event(event_id)

            elif choice == "4":
                participant_id = int(input("Enter participant ID: "))
                name = input("Enter participant name: ")
                email = input("Enter participant email: ")
                phone_number = input("Enter participant phone number: ")
                participant = Participant(participant_id, name, email, phone_number)
                system.add_participant(participant)

            elif choice == "5":
                participant_id = int(input("Enter participant ID to update: "))
                kwargs = {}
                if input("Update name? (y/n): ") == "y":
                    kwargs['name'] = input("Enter new name: ")
                if input("Update email? (y/n): ") == "y":
                    kwargs['email'] = input("Enter new email: ")
                if input("Update phone number? (y/n): ") == "y":
                    kwargs['phone_number'] = input("Enter new phone number: ")
                system.update_participant(participant_id, **kwargs)

            elif choice == "6":
                participant_id = int(input("Enter participant ID to delete: "))
                system.delete_participant(participant_id)

            elif choice == "7":
                registration_id = int(input("Enter registration ID: "))
                event_id = int(input("Enter event ID: "))
                participant_id = int(input("Enter participant ID: "))
                registration_date = input("Enter registration date (YYYY-MM-DD): ")
                registration = Registration(registration_id, event_id, participant_id, registration_date)
                system.add_registration(registration)

            elif choice == "8":
                registration_id = int(input("Enter registration ID to update: "))
                kwargs = {}
                if input("Update event ID? (y/n): ") == "y":
                    kwargs['event_id'] = int(input("Enter new event ID: "))
                if input("Update participant ID? (y/n): ") == "y":
                    kwargs['participant_id'] = int(input("Enter new participant ID: "))
                if input("Update registration date? (y/n): ") == "y":
                    kwargs['registration_date'] = input("Enter new registration date (YYYY-MM-DD): ")
                system.update_registration(registration_id, **kwargs)

            elif choice == "9":
                registration_id = int(input("Enter registration ID to cancel: "))
                system.cancel_registration(registration_id)

            elif choice == "10":
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Input error: {e}. Please enter valid data.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
