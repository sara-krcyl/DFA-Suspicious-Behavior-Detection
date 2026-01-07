import random

# DFA States
NORMAL = "Normal"
IDLE = "Idle"
HIGH_ACTIVITY = "HighActivity"
VIOLATION = "ViolationDetected"

# Accepting states
ACCEPTING_STATES = {VIOLATION}

# Event set
EVENTS = [
    "KeyPress",
    "MouseMove",
    "IdleTimeout",
    "BurstTyping",
    "WindowChange"
]

# Transition table
TRANSITIONS = {
    (NORMAL, "KeyPress"): NORMAL,
    (NORMAL, "MouseMove"): NORMAL,
    (NORMAL, "IdleTimeout"): IDLE,
    (NORMAL, "BurstTyping"): HIGH_ACTIVITY,
    (NORMAL, "WindowChange"): VIOLATION,

    (IDLE, "IdleTimeout"): IDLE,
    (IDLE, "WindowChange"): VIOLATION,
    (IDLE, "KeyPress"): NORMAL,
    (IDLE, "MouseMove"): NORMAL,
    (IDLE, "BurstTyping"): HIGH_ACTIVITY,

    (HIGH_ACTIVITY, "WindowChange"): VIOLATION,
    (HIGH_ACTIVITY, "MouseMove"): NORMAL,
    (HIGH_ACTIVITY, "IdleTimeout"): IDLE,
    (HIGH_ACTIVITY, "BurstTyping"): HIGH_ACTIVITY,
    (HIGH_ACTIVITY, "KeyPress"): NORMAL,

    # Absorbing state
    (VIOLATION, "KeyPress"): VIOLATION,
    (VIOLATION, "MouseMove"): VIOLATION,
    (VIOLATION, "IdleTimeout"): VIOLATION,
    (VIOLATION, "BurstTyping"): VIOLATION,
    (VIOLATION, "WindowChange"): VIOLATION,
}


def run_random_simulation():
    current_state = NORMAL
    input_sequence = []
    state_path = [current_state]

    print("\n--- New Random DFA Simulation ---")
    print(f"Start State: {current_state}")

    while current_state not in ACCEPTING_STATES:
        event = random.choice(EVENTS)
        input_sequence.append(event)

        current_state = TRANSITIONS[(current_state, event)]
        state_path.append(current_state)

    # Simulation finished (ACCEPT reached)
    print("\nSimulation finished!")
    print("\nGenerated Input Sequence:")
    print(" ".join(input_sequence))

    print("\nState Path:")
    print(" -> ".join(state_path))

    print("\nFINAL RESULT: ACCEPTED (Suspicious behavior detected)")


def main():
    print("=== Suspicious Behavior Detection DFA Simulator ===")

    while True:
        run_random_simulation()

        choice = input("\nRun another random example? (y/n): ").strip().lower()
        if choice != "y":
            print("\nExiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
