from melvis.voice_input import listen
from melvis.voice_output import speak
from melvis.commands import handle_command
from melvis.brain import ask_melvis

def main():
    speak("Melvis is online and ready to assist.")

    while True:
        user_input = listen()

        if not user_input:
            continue

        print(f"You: {user_input}")

        if user_input.lower() in ["stop melvis", "exit", "quit"]:
            speak("Goodbye Elvis.")
            break

        command_response = handle_command(user_input)

        if command_response:
            speak(command_response)
        else:
            ai_response = ask_melvis(user_input)
            speak(ai_response)

if __name__ == "__main__":
    main()