import tkinter as tk
import integration_wit
import json


with open("messages.json", "r", encoding="utf-8") as json_file:
    messages = json.load(json_file)

with open("loan_application", "r", encoding="utf-8") as json_file2:
    credit_qst = json.load(json_file2)


def user_msg():
    msg = txt_entrybox.get("1.0", 'end-1c').strip()  # Gets text from the textbox
    txt_entrybox.delete("0.0", tk.END)  # Deletes users text

    txt_chatbox.config(state=tk.NORMAL, wrap=tk.WORD)
    txt_chatbox.tag_configure("bold")
    txt_chatbox.insert(tk.END, *messages["you"], msg + '\n')
    txt_chatbox.see(tk.END)
    return msg


def chatbot_msg(text, additional=''):
    txt_chatbox.insert(tk.END, *messages[text], additional)
    txt_chatbox.see(tk.END)


def send_wit():
    msg = user_msg()
    if msg == '':
        chatbot_msg("empty_msg")
    elif msg != '':
        res = integration_wit.wit_response(msg)
        if res == 'agreement':
            handle_response()
        elif res == "resistance":
            chatbot_msg("help")
        else:
            chatbot_msg(res)


question = 0


def handle_response():
    btn_send['command'] = send_data
    chatbot_msg("chatbot", credit_qst[question])


def connect_wit():
    btn_send['command'] = send_wit


def send_data():
    global question
    msg = user_msg()

    if question == 0 and msg == "tak":
        chatbot_msg("regular_client")
        connect_wit()
    elif question == credit_qst.index(credit_qst[-1]):
        check_form(msg)
    else:
        question += 1
        chatbot_msg("chatbot", credit_qst[question])


def check_form(msg):
    if msg == "tak":
        chatbot_msg("thanks")
    else:
        chatbot_msg("help")
    connect_wit()


#####################################################

root = tk.Tk()

# Window parameters
root.iconbitmap(r'technology_bot.ico')
root.title("Chatbot - wirtualny doradca kredytowy")
root.geometry("400x500")
root.resizable(width=tk.FALSE, height=tk.FALSE)

# Create chat window and first message
txt_chatbox = tk.Text(root, bd=0, bg="white", font=("Verdana", 12))
txt_chatbox.tag_configure("bold", font=("Verdana", 12, "bold"))
txt_chatbox.insert(tk.END, *messages["welcome"])
txt_chatbox.config(state=tk.DISABLED, wrap=tk.WORD)

# Bind scrollbar to chat window
scrollbar = tk.Scrollbar(root, command=txt_chatbox.yview)
txt_chatbox['yscrollcommand'] = scrollbar.set

# Create Button to send message
btn_send = tk.Button(root, font=("Verdana", 12, 'bold'), text="Wyślij", width=10, height=5,
                  bd=0, bg="#fbdb44", activebackground="#f0d058", fg='#000000',
                  anchor=tk.CENTER, cursor="hand2",
                  command=send_wit)


# Create the box to enter message
txt_entrybox = tk.Text(root, bd=0, bg="white", font=("Verdana", 12))
txt_entrybox.config(wrap=tk.WORD)
txt_entrybox.pack()

# Place and size all components on the screen
scrollbar.place(x=380, y=6, height=385)
txt_chatbox.place(x=6, y=6, height=386, width=375)
txt_entrybox.place(x=128, y=401, height=90, width=263)
btn_send.place(x=6, y=401, height=90)

root.mainloop()
