import customtkinter, models, time

mod = 2048
username = ""
model = "DEFAULT"
i = -1

def gui1():
    def add_account():
        global username, model, i
        username = entry_username.get()
        model = entry_model.get()
        textbox.configure(text=f"Booting {model} now.")
        i = 0
        app1.update()
        app1.after(5000, app1.quit())
        time.sleep(0.1)
        modchecker()


    app1 = customtkinter.CTk()
    app1.title("KazAI")
    app1.geometry("800x250")
    textbox = customtkinter.CTkLabel(app1, text="Type your username.\n", font=("Arial", 20, "bold"))
    frame1 = customtkinter.CTkFrame(app1, width=800, height=600)
    frame1.pack(fill=customtkinter.BOTH, expand=True)
    entry_username = customtkinter.CTkEntry(frame1, placeholder_text="Username",height=40,
                                            width=400,
                                            corner_radius=15,
                                            placeholder_text_color="gray",
                                            fg_color="#192e2d",
                                            font=("Arial", 20, "bold"))
    entry_model = customtkinter.CTkEntry(frame1, placeholder_text="Model",
                                                height=40,
                                                width=400,
                                                corner_radius=15,
                                                placeholder_text_color="gray",
                                                fg_color="#192e2d",
                                                font=("Arial", 20, "bold"))
    button = customtkinter.CTkButton(frame1, text="Enter", command=add_account,font=("Arial", 15, "bold"))
    entry_username.pack(pady=10)
    entry_model.pack(pady=10)
    button.pack(pady=10)
    textbox.pack(pady=15)
    app1.mainloop()

def modchecker():
    global mod, username
    if model == "":
        mod = 0
    elif model.lower() == "sozomi":
        mod = 1
    elif model.lower() == "kazenoko":
        mod = 0
    elif model.lower() == "kazenowoko":
        mod = 0
    elif model.lower() == "default":
        mod = 0
    else:
        exit()
    sozomi.gui2(username, mod)
    quit(0)


gui1()
