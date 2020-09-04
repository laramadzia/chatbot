from tkinter import *
import integracjaWitAI
import tupla


def send_wit():
    msg = EntryBox.get("1.0", 'end-1c').strip()  # Gets text from the textbox
    EntryBox.delete("0.0", END)  # Deletes users text

    ChatBox.config(state=NORMAL, wrap=WORD)
    ChatBox.tag_configure("bold")
    ChatBox.insert(END, "Ty: ", "bold", msg + '\n\n')

    if msg == '':
        ChatBox.insert(END, "Chatbot: ", "bold", "Nie potrafię odpowiedzieć na pustą wiadomość." + '\n\n')
    elif msg != '':
        res = integracjaWitAI.wit_response(msg)
        if res == 'zgoda':
            handle_response(res)
        elif res == 'sprzeciw':
            ChatBox.insert(END, "Chatbot: ", "bold", "Rozumiem, zatem w czym mogę Ci dzisiaj pomóc?" + '\n\n')
        else:
            ChatBox.insert(END, "Chatbot: ", "bold", switch_response(res) + '\n\n')

    ChatBox.config(state=DISABLED)
    ChatBox.yview(END)


def switch_response(res):
    types = {
        'kredyt_hipoteczny': "Produkt dla ciebie to kredyt hipoteczny. Chcesz wnioskować?",
        'kredyt_gotowkowy': "Produkt dla ciebie to kredyt gotowkowy. Chcesz wnioskować?",
    }
    return types.get(res, "Nie rozumiem. Zadaj pytanie inaczej.")


def handle_response(res):
    if res == 'zgoda':
        ChatBox.insert(END, "Chatbot: ", "bold", tupla.daneKlienta[0] + '\n\n')
        SendButton['command'] = send_data


pytanie = 0


def send_data():
    msg = EntryBox.get("1.0", 'end-1c').strip()  # Gets text from the textbox
    EntryBox.delete("0.0", END)  # Deletes users text

    ChatBox.config(state=NORMAL, wrap=WORD)
    ChatBox.tag_configure("bold")
    ChatBox.insert(END, "Ty: ", "bold", msg + '\n\n')

    for pytanie in tupla.daneKlienta:
        ChatBox.insert(END, "Chatbot: ", "bold", pytanie[1] + '\n\n')


#####################################################

root = Tk()

# Window parameters
root.iconbitmap(r'technology_bot.ico')
root.title("Chatbot - wirtualny doradca kredytowy")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

# Create chat window and first message
ChatBox = Text(root, bd=0, bg="white", font=("Verdana", 12))
ChatBox.tag_configure("bold", font=("Verdana", 12, "bold"))
ChatBox.insert(END,
               "Chatbot: ", "bold",
               "Witaj! Jestem wirtualnym doradcą. Pomogę Ci w wyborze produktu kredytowego i zawnioskowaniu o niego."
               + '\n'
               + "Na co chcesz przeznaczyć dodatkowe środki?"
               + '\n\n')
ChatBox.config(state=DISABLED, wrap=WORD)

# Bind scrollbar to chat window
scrollbar = Scrollbar(root, command=ChatBox.yview)
ChatBox['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(root, font=("Verdana", 12, 'bold'), text="Wyślij", width=10, height=5,
                    bd=0, bg="#fbdb44", activebackground="#f0d058", fg='#000000',
                    anchor=CENTER, cursor="hand2",
                    command=send_wit)


# Create the box to enter message
EntryBox = Text(root, bd=0, bg="white", font=("Verdana", 12))
EntryBox.config(wrap=WORD)
EntryBox.pack()

# Enter button triggers sendWit ----- NOT WORK
root.bind('<Return>', lambda x: send_wit)

# Place and size all components on the screen
scrollbar.place(x=380, y=6, height=385)
ChatBox.place(x=6, y=6, height=386, width=375)
EntryBox.place(x=128, y=401, height=90, width=263)
SendButton.place(x=6, y=401, height=90)

root.mainloop()
