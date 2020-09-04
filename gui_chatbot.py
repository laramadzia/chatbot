import tkinter as tk
import integracjaWitAI
import tupla
import json


with open("messages.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)


def send_wit():
    msg = txt_entrybox.get("1.0", 'end-1c').strip()  # Gets text from the textbox
    txt_entrybox.delete("0.0", tk.END)  # Deletes users text

    txt_chatbox.config(state=tk.NORMAL, wrap=tk.WORD)
    txt_chatbox.tag_configure("bold")
    txt_chatbox.insert(tk.END, "Ty: ", "bold", msg + '\n\n')

    if msg == '':
        txt_chatbox.insert(tk.END, "Chatbot: ", "bold", data["empty"] + '\n\n')
    elif msg != '':
        res = integracjaWitAI.wit_response(msg)
        if res == 'zgoda':
            handle_response()
        elif res == 'sprzeciw':
            txt_chatbox.insert(tk.END, "Chatbot: ", "bold", data["help"] + '\n\n')
        else:
            txt_chatbox.insert(tk.END, "Chatbot: ", "bold", switch_response(res) + '\n\n')

    txt_chatbox.config(state=tk.DISABLED)
    txt_chatbox.yview(tk.END)


def switch_response(res):
    types = {
        'kredyt_hipoteczny': "Produkt dla ciebie to kredyt hipoteczny. Chcesz wnioskować?",
        'kredyt_gotowkowy': "Produkt dla ciebie to kredyt gotowkowy. Chcesz wnioskować?",
    }
    return types.get(res, data["dontUnderstand"])


def handle_response():
    txt_chatbox.insert(tk.END, "Chatbot: ", "bold", tupla.daneKlienta[0] + '\n\n')
    btn_send['command'] = send_data


pytanie = 1


def send_data():
    global pytanie
    msg = txt_entrybox.get("1.0", 'end-1c').strip()  # Gets text from the textbox
    txt_entrybox.delete("0.0", tk.END)  # Deletes users text

    txt_chatbox.config(state=tk.NORMAL, wrap=tk.WORD)
    txt_chatbox.tag_configure("bold")
    txt_chatbox.insert(tk.END, "Ty: ", "bold", msg + '\n\n')

    txt_chatbox.insert(tk.END, "Chatbot: ", "bold", tupla.daneKlienta[pytanie] + '\n\n')
    pytanie += 1


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
txt_chatbox.insert(tk.END, *data['welcome'])
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

# Enter button triggers sendWit ----- NOT WORK
root.bind('<Return>', lambda x: send_wit)

# Place and size all components on the screen
scrollbar.place(x=380, y=6, height=385)
txt_chatbox.place(x=6, y=6, height=386, width=375)
txt_entrybox.place(x=128, y=401, height=90, width=263)
btn_send.place(x=6, y=401, height=90)

root.mainloop()
