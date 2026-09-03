# Vacuum Agent Function
def vacuum_agent(location, status):

    # Clean the room if it is dirty
    if status == "Dirty":
        return "Suck"

    # Move right from A
    elif location == "A":
        return "Move Right"

    # Move left from B
    elif location == "B":
        return "Move Left"


# Display heading
print("========== Vacuum Cleaner World ==========")

# Take current location
location = input("Enter Current Location (A/B): ").upper()

# Take room status
status = input("Enter Room Status (Clean/Dirty): ").capitalize()

# Get agent action
action = vacuum_agent(location, status)

# Display result
print("Action Performed :", action)