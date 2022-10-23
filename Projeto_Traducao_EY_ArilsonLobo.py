import speech_recognition as sr
from googletrans import Translator
from playsound import playsound
from IPython.display import Audio
from gtts import gTTS
import pyglet
import time


def ouvir_microfone():    
    
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()
    
    #usando o microfone
    with sr.Microphone() as source:
        
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)        
        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")        
        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)
        
    try:        
    
        #frase = microfone.recognize_google(audio,language='pt-BR') 
        frase = microfone.recognize_google(audio,language='en-NG')   
        # en-GB en-TZ en-ZA en-SG en-PH en-NG
        print("Você disse: " + frase)        
    
    except sr.UnknownValueError:
        print("Não entendi") 
    except sr.RequestError:
        print(" There is some problem with Google Speech Recognition") 
        
    
    translator = Translator()

    # configurando a entrada e a saída
    translated_ita = translator.translate(frase, src='en', dest='pt')

    # texto traduzido
    translated_ita.text

    # informando a linguagem
    tts = gTTS(translated_ita.text,lang='pt')

    language = "pt"
    gtts_object = gTTS(text = translated_ita.text, 
                    lang = language,
                    slow = False)

    gtts_object.save("fala.wav")

    # ouvindo a tradução
    sound = pyglet.media.load("fala.wav" , streaming=False)
    sound.play()
    time.sleep(sound.duration)   
                                
    return frase

# executando
ouvir_microfone()


