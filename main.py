import tkinter as tk
import json
from chatbot_app import ChatbotApp


def main():
    root = tk.Tk()

    # Open json files
    with open("messages.json", "r", encoding="utf-8") as json_file:
        messages = json.load(json_file)
    with open("loan_application.json", "r", encoding="utf-8") as json_file2:
        credit_qst = json.load(json_file2)["questions"]

    # Window parameters
    root.iconbitmap(r'technology_bot.ico')
    root.title("Chatbot - wirtualny doradca kredytowy")
    root.geometry("400x500")
    root.resizable(width=tk.FALSE, height=tk.FALSE)
    app = ChatbotApp(root, messages, credit_qst)
    root.mainloop()


if __name__ == '__main__':
    main()
