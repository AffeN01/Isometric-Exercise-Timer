import time
import sys

PRESETS = {
    1: (20, 1, 1),
    2: (10, 5, 1.25),
    3: (25, 2, 1),
    4: (10, 10, 2),
    5: (50, 1, 1),
    6: (25, 3, 1),
}

def tense_and_relax(reps, tense_time, relax_time):
    print("Starting tense and relax exercise...")
    total_phases = reps * 2  # Tensing and relaxing phases
    for rep in range(1, reps + 1):
        print(f"\nRepetition {rep}/{reps}: Tense!")
        execute_phase(tense_time, total_phases, "green")
        print(f"\nRepetition {rep}/{reps}: Relax!")
        execute_phase(relax_time, total_phases, "red")

def execute_phase(total_time, total_phases, color):
    start_time = time.time()
    end_time = start_time + total_time
    while time.time() <= end_time:
        elapsed_time = time.time() - start_time
        phase_percentage = (elapsed_time / total_time) * 100
        draw_progress_bar(total_time, elapsed_time, phase_percentage, color)
        time.sleep(0.05)  # Adjust the sleep time as needed for smooth updating
    print("\nPhase complete!")

def draw_progress_bar(total_time, elapsed_time, percentage, color):
    bar_length = 50
    progress = int((elapsed_time / total_time) * bar_length)
    if color == "green":
        bar = '\033[92m' + '#' * progress + '\033[0m' + '-' * (bar_length - progress)
    elif color == "red":
        bar = '\033[91m' + '#' * progress + '\033[0m' + '-' * (bar_length - progress)
    sys.stdout.write("\r[%s] %.1f%%" % (bar, percentage))
    sys.stdout.flush()

def get_user_input():
    print("Welcome!")
    while True:
        try:
            print("Choose an option:")
            print("1. Select a preset")
            print("2. Set custom settings")
            option = int(input("Enter your choice: "))
            if option not in [1, 2]:
                raise ValueError
            return option
        except ValueError:
            print("Invalid option. Please enter 1 or 2.")

def display_presets():
    print("\nPresets:")
    for key, value in PRESETS.items():
        print(f"Preset {key}: {value[0]} repetition(s), {value[1]} second(s) tense, {value[2]} second(s) relaxed")

if __name__ == "__main__":
    selected_settings = None  # Initialize selected settings variable
    while True:
        option = get_user_input()
        if option == 1:
            while True:
                try:
                    display_presets()
                    preset_choice = int(input(f"Enter the preset number (1-{len(PRESETS)}): "))
                    reps, tense_time, relax_time = PRESETS[preset_choice]
                    tense_and_relax(reps, tense_time, relax_time)

                    choice = int(input("Do you want to:\n1. Start another set\n2. Return to the start menu\n3. Quit program\nEnter your choice: "))
                    if choice == 1:
                        continue  # Start another set
                    elif choice == 2:
                        break  # Return to the start menu
                    elif choice == 3:
                        sys.exit()  # Quit the program
                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")
                except KeyError:
                    print(f"Invalid preset number. Please enter a number between 1 and {len(PRESETS)}.")
        elif option == 2:
            while True:
                try:
                    if selected_settings is None:
                        reps = int(input("Enter amount of repetitions: "))
                        tense_time = float(input("Enter seconds to tense: "))
                        relax_time = float(input("Enter seconds to relax: "))
                    else:
                        reps, tense_time, relax_time = selected_settings

                    tense_and_relax(reps, tense_time, relax_time)

                    choice = int(input("Do you want to:\n1. Start another set\n2. Return to the start menu\n3. Quit program\nEnter your choice: "))
                    if choice == 1:
                        selected_settings = (reps, tense_time, relax_time)  # Store selected settings
                        continue  # Start another set
                    elif choice == 2:
                        selected_settings = None  # Reset selected settings
                        break  # Return to the start menu
                    elif choice == 3:
                        sys.exit()  # Quit the program
                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif option == 3:
            sys.exit()  # Quit the program
