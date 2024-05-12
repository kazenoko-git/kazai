import customtkinter, ai
class models():
    def __init__(self):
        pass

    def sozomi(username, mod):
        model = "Sozomi"
        def ask():
            ans = AI.ask(prompt=entry_prompt.get())
            print(ans)
            textbox.insert("end", f"{ans}")
        app1 = customtkinter.CTk()
        app1.title("KazAI - Sozomi")
        app1.geometry("800x200")
        AI = ai.AI(username=username, model=mod)
        frame1 = customtkinter.CTkFrame(app1, width=800, height=600)
        frame1.pack(fill=customtkinter.BOTH, expand=True)
        textbox = customtkinter.CTkTextbox(frame1, width=700, corner_radius=5, height=100)
        entry_prompt = customtkinter.CTkEntry(frame1, placeholder_text="Say Something.", height=40,
                                                width=400,
                                                corner_radius=15,
                                                placeholder_text_color="gray",
                                                fg_color="#192e2d",
                                                font=("Arial", 20, "bold"))
        button = customtkinter.CTkButton(frame1, text="Ask", command=lambda: ask(), font=("Arial", 15, "bold"))
        entry_prompt.pack(pady=10)
        button.pack(pady=10)
        textbox.pack(pady=15)
        app1.mainloop()

    def kazenoko(username, mod):
        model = "Kazenoko"
        def ask():
            ans = AI.ask(prompt=entry_prompt.get())
            print(ans)
            textbox.insert("end", f"{ans}")
        app1 = customtkinter.CTk()
        app1.title("KazAI - Kazenoko (DEFAULT)")
        app1.geometry("800x200")
        AI = ai.AI(username=username, model=mod)
        frame1 = customtkinter.CTkFrame(app1, width=800, height=600)
        frame1.pack(fill=customtkinter.BOTH, expand=True)
        textbox = customtkinter.CTkTextbox(frame1, width=700, corner_radius=5, height=100)
        entry_prompt = customtkinter.CTkEntry(frame1, placeholder_text="Say Something.", height=40,
                                                width=400,
                                                corner_radius=15,
                                                placeholder_text_color="gray",
                                                fg_color="#192e2d",
                                                font=("Arial", 20, "bold"))
        button = customtkinter.CTkButton(frame1, text="Ask", command=lambda: ask(), font=("Arial", 15, "bold"))
        entry_prompt.pack(pady=10)
        button.pack(pady=10)
        textbox.pack(pady=15)
        app1.mainloop()

    def afash(username, mod):
        model = "Afash"
        def ask():
            ans = AI.ask(prompt=entry_prompt.get())
            print(ans)
            textbox.insert("end", f"{ans}")
        app1 = customtkinter.CTk()
        app1.title("KazAI - Afash V2")
        app1.configure()
        app1.geometry("800x200")
        AI = ai.AI(username=username, model=mod)
        frame1 = customtkinter.CTkFrame(app1, width=800, height=600)
        frame1.pack(fill=customtkinter.BOTH, expand=True)
        textbox = customtkinter.CTkTextbox(frame1, width=700, corner_radius=5, height=100)
        entry_prompt = customtkinter.CTkEntry(frame1, placeholder_text="Say Something.", height=40,
                                                width=400,
                                                corner_radius=15,
                                                placeholder_text_color="gray",
                                                fg_color="#192e2d",
                                                font=("Arial", 20, "bold"))
        button = customtkinter.CTkButton(frame1, text="Ask", command=lambda: ask(), font=("Arial", 15, "bold"))
        entry_prompt.pack(pady=10)
        button.pack(pady=10)
        textbox.pack(pady=15)
        app1.mainloop()