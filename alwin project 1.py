def opspilot_ai():
    print("OpsPilot AI: Ask about an operations issue, or type 'exit'.")

    while True:
        question = input("You: ").strip().lower()

        if question == "exit":
            print("OpsPilot AI: Goodbye.")
            break
        elif "server" in question or "down" in question:
            answer = "Check server health, recent deployments, and application logs."
        elif "alert" in question:
            answer = "Review the alert details, severity, and affected services."
        elif "backup" in question:
            answer = "Check the latest backup status and verify a recent restore."
        else:
            answer = "I can help with servers, alerts, and backups. What’s the issue?"

        print(f"OpsPilot AI: {answer}")


if __name__ == "__main__":
    opspilot_ai()