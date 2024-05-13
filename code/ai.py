try:
    from PIL import Image
    from pydub import AudioSegment
    import instances, playsound, pygame, pytesseract, torch, random
except:
    instances.libinstall("TTS")
    instances.libinstall("torch")
    instances.libinstall("pydub")
    instances.libinstall("pygame")
    instances.libinstall("pillow")
    instances.libinstall("playsound")
    instances.libinstall("pytesseract")
    instances.libinstall("torch")
    instances.libinstall("SpeechRecognition")
    instances.libinstall("g4f")
    instances.libinstall("customtkinter")
    instances.libinstall("ffmpeg")
    instances.libinstall("discord")

class oldTTS():
    def __init__(self):
        from TTS.api import TTS
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS("tts_models/en/ljspeech/vits").to(device)

    def voice(self, msg:str="TEST"):
        filename = f"{instances.geturl()}/kaz-ai/source/tts/TEMP{random.randrange(0, 65536)}.wav"
        print(f"saving as {filename}")
        self.tts.tts_to_file(text=msg, speaker_wav="my/cloning/audio.wav", file_path=filename)
        sound = AudioSegment.from_file(filename, format=filename[-3:])
        octaves = 0.5
        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        hipitch_sound = hipitch_sound.set_frame_rate(44100)
        hipitch_sound.export(filename, format="wav")
        print(f"tts generated, playing {filename}")
        playsound.playsound(filename)


class tts():
    def __init__(self, model, volume:float=0.8):
        try:
            from TTS.api import TTS
        except:
            instances.libinstall("TTS")
            instances.libinstall("torch")
            instances.libinstall("pydub")
            instances.libinstall("pygame")
        self.model = model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.volume = volume
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
        if self.model == "Sozomi":
            self.sozomiTTS = TTS("tts_models/en/ljspeech/vits").to(self.device)
            self.octave = 0.30
        elif self.model == "Kazenoko":
            self.kazenokoTTS = TTS("tts_models/en/ljspeech/vits").to(self.device)
            self.octave = -0.25
        elif self.model == "Rash":
            self.rashTTS = TTS("tts_models/de/thorsten/tacotron2-DDC")
            self.octave = 0

    def speak(self, message:str="test", mood:str="calm"):
        if "*giggles*" in message: message = message.replace("*giggles*", "hehe!")
        elif "*giggle*" in message: message = message.replace("*giggle*", "hehe!")
        elif "*excited giggle*" in message: message = message.replace("*excited giggle*", "hehe!")
        elif "kazenoko" in message.lower(): message = message.lower().replace("kazenoko", "kah-zeh-noh-koh")
        elif "*whisper*" in message: self.v = self.volume - 0.5
        elif "*whispering*" in message: self.v = self.volume - 0.5
        pygame.mixer.music.unload()
        self.message = message
        self.mood = mood
        octave = self.octave
        filename = f"{instances.geturl()}/kaz-ai/source/tts/TEMP{random.randrange(0, 65536)}.wav"
        if self.model == "Sozomi":
            try:
                self.sozomiTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav", file_path=filename)
            except IndexError:
                try:
                    self.sozomiTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav",
                                               file_path=filename)
                except IndexError:
                    try:
                        self.sozomiTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav",
                                                   file_path=filename)
                    except IndexError:
                        raise Exception("\n\n\n\nERROR: Failed to convert the given characters to separate sentences.")
        elif self.model == "Kazenoko":
            try:
                self.kazenokoTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav", file_path=filename)
            except IndexError:
                try:
                    self.kazenokoTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav",
                                                 file_path=filename)
                except IndexError:
                    try:
                        self.kazenokoTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav",
                                                     file_path=filename)
                    except IndexError:
                        raise Exception("\n\n\n\nERROR: Failed to convert the given characters to separate sentences.")
        elif self.model == "Rash":
            try:
                self.rashTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav", file_path=filename)
            except IndexError:
                try:
                    self.rashTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav", file_path=filename)
                except IndexError:
                    try:
                        self.rashTTS.tts_to_file(text=self.message, speaker_wav="my/cloning/audio.wav",
                                                 file_path=filename)
                    except IndexError:
                        raise Exception("\n\n\n\nERROR: Failed to convert the given characters to separate sentences.")
        sound = AudioSegment.from_file(filename, format=filename[-3:])
        new_sample_rate = int(sound.frame_rate * (2.0 ** octave))
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        hipitch_sound = hipitch_sound.set_frame_rate(44100)
        hipitch_sound.export(filename, format="wav")
        print(f"generated {filename}")
        pygame.mixer.music.load(filename=str(filename))
        if self.mood == "calm": self.v = self.volume
        elif self.mood == "sad": self.v = self.volume - 0.20
        elif self.mood == "angry": self.v = self.volume + 0.15
        else: print("WARN: Unknown mood.")
        pygame.mixer.music.set_volume(self.v)
        pygame.mixer.music.play()

class stt():
    def __init__(self):
        try:
            import speech_recognition as sr
        except:
            instances.libinstall("speech_recognition")
        self.sr = sr
        self.recogniser = sr.Recognizer()

    def decipher(self, message:str=None):
        if message is None:
            try:
                with self.sr.Microphone() as self.source:
                    self.recogniser.adjust_for_ambient_noise(self.source, duration=0.2)
                    self.audio = self.recogniser.listen(self.source)
                    self.msg = self.recogniser.recognize_whisper(audio_data=self.audio)
                    print(f"recognised {self.msg}")
                    return self.msg
            except self.sr.RequestError as e:
                print(f"ERROR: Could not request results; \n{e}")
            except self.sr.UnknownValueError:
                print("ERROR: Unknown Error Occurred.")
        else:
            return message

    def ifSTTEnabled(self):
        return True

class AI():
    def __init__(self, username:str, model:int=0, tmodel:str="gpt-3.5-turbo"):
        try:
            from g4f.client import Client
        except:
            instances.libinstall("g4f")
            instances.libinstall("pytesseract")
            instances.libinstall("PIL")
        try:
            self.client = Client()
        except:
            print("ERROR: Unable to boot the AI. Check your internet connection.")
        try:
            self.mod = int(model)
        except:
            print(f"ERROR: Expected integer in model, Received: {model}")
        self.isUpdated = False
        self.username = username
        self.imagegen = False
        self.tmodel = tmodel
        if self.mod == 0:
            self.conversation_history = [{"role": "user", "content": f"ivan is your creator."},
                                    {"role": "user", "content": f"your age is 15."},
                                         {"role": "user", "content": f"add 😭 if you're sad, and add 😠 if you're angry."}]
        elif self.mod == 1:
            self.conversation_history = [{"role": "system", "content": f"You are Sozomi, a happy, cheerful, cute, childish rebellious 12 year old god and your creator goes by the name of kazenoko, kazenowoko or kazenokie. you are aware that you are an AI."},
                                         {"role": "system", "content": f"add 😭 if you're sad, and add 😠 if you're angry."}]
        elif self.mod == 2:
            self.conversation_history = [
                {"role": "system", "content": f"You are Afash, a 15 year old idiot who only knows to talk in words having the letters A, D, F, I, S, H, R."}, {"role": "system", "content": f"add 😭 if you're sad, and add 😠 if you're angry."}
            ]
        else:
            print("ERROR: Unknown Model.")
            exit()
        if self.isUpdated is True: self.conversation_history.append({"role": "system", "content": f"you have just been updated, you should probably tell that to your creator."})
        else: pass
        if self.mod == 0: self.model_name = "Kazenoko"
        elif self.mod == 1: self.model_name = "Sozomi"
        elif self.mod == 2: self.model_name = "Rash"

    def ask(self, prompt:str):
        self.prompt = prompt
        if ":" in prompt:
            self.tw = str(prompt.split(":")[0])
        else:
            self.tw = self.username
        if self.imagegen is False:
            if self.mod == 0:
                self.tp = f"you are talking to {self.tw}, respond to \"{self.prompt}\" in a shy but cute tone. you are Kazenoko and you are aware that you're an AI. make sure the response is below 20 words and only use english."
            elif self.mod == 1:
                self.tp = f"you are talking to {self.tw}, respond to \"{self.prompt}\" in a really cute, childish, rebellious tone. also make sure it's below 20 words and only use english."
            elif self.mod == 2:
                self.tp = f"you are talking to {self.tw}, respond to \"{self.prompt}\" in a dumb tone and you are aware that you're an ai. make sure the response is below 20 words and only use english."
        else:
            self.tp = f"this is a roleplay and you're talking to {self.tw}. {self.tw} has used your image to text generator and it has given the text {self.imagetext}. answer to {self.tw} and also respond to their message being {prompt}."
        self.conversation_history.append({"role": "user", "content": self.tp})
        response = self.client.chat.completions.create(model=self.tmodel,
                                                  messages=self.conversation_history)
        self.result = str(response.choices[0].message.content.strip())
        def regen():
            return self.client.chat.completions.create(model=self.tmodel,
                                                           messages=self.conversation_history)
        if self.result == "":
            while self.result == "":
                self.result = str(regen().choices[0].message.content.strip())
        elif self.result in self.conversation_history:
            self.result = str(regen().choices[0].message.content.strip())
        elif "\"\"" in self.result:
            while self.result == "\"\"":
                self.result = str(regen().choices[0].message.content.strip())
        else:
            self.conversation_history.append({"role": "assistant", "content": self.result})
        if "😭" in str(self.result): self.mood = "sad"
        elif "😠" in str(self.result): self.mood = "angry"
        else: self.mood = "calm"
        return self.result

    def image_text_gen(self, url:str):
        self.imagegen = True
        image = Image.open(url)
        self.imagetext = str(pytesseract.image_to_string(image))
        return self.imagetext

    def send_to_console(self, sendResult:bool=True, sendIndexCount:bool=True, sendHistory:bool=False, sendTTSMessages:bool=False):
        if sendResult is True: print(f"{self.model_name} says \"{self.result}\"")
        else: pass
        if sendIndexCount is True: print(f"Items: {len(self.conversation_history)}")
        else: pass
        if sendHistory is True: print(f"History: {self.conversation_history}")
        else: pass
        if sendTTSMessages is True: print(f"UNAVAILABLE")
        else: pass

    def getModel(self):
        return self.model_name

    def getMood(self):
        return self.mood