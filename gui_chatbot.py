import tkinter as tk
import integration_wit
import json


with open("messages.json", "r", encoding="utf-8") as json_file:
    messages = json.load(json_file)

with open("loan_application", "r", encoding="utf-8") as json_file2:
    credit_qst = json.load(json_file2)


def send_wit():
    msg = txt_entrybox.get("1.0", 'end-1c').strip()  # Gets text from the textbox
    txt_entrybox.delete("0.0", tk.END)  # Deletes users text

    txt_chatbox.config(state=tk.NORMAL, wrap=tk.WORD)
    txt_chatbox.tag_configure("bold")
    txt_chatbox.insert(tk.END, *messages["you"], msg + '\n')

    if msg == '':
        txt_chatbox.insert(tk.END, *messages["empty_msg"])
    elif msg != '':
        res = integration_wit.wit_response(msg)
        if res == 'agreement':
            handle_response()
        elif res == "resistance":
            txt_chatbox.insert(tk.END, *messages["help"])
        else:
            print(res)
            txt_chatbox.insert(tk.END, *messages[res])

    txt_chatbox.config(state=tk.DISABLED)
    txt_chatbox.yview(tk.END)


def handle_response():
    txt_chatbox.insert(tk.END, *messages["chatbot"] + credit_qst[0])
    btn_send['command'] = send_data


question = 1


def send_data():
    global question
    msg = txt_entrybox.get("1.0", 'end-1c').strip()  # Gets text from the textbox
    txt_entrybox.delete("0.0", tk.END)  # Deletes users text

    txt_chatbox.config(state=tk.NORMAL, wrap=tk.WORD)
    txt_chatbox.insert(tk.END, *messages["you"] + msg)

    txt_chatbox.insert(tk.END, credit_questions[question])
    question += 1


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
