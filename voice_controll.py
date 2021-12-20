import speech_recognition as sr
import pyautogui
import webbrowser

r = sr.Recognizer()
webbrowser.open("https://quizlet.com/599658947/learn")

while True:
    audio = 0
    text = 0

    with sr.Microphone() as f:
        r.adjust_for_ambient_noise(f)
        print("Listening...")
        audio = r.listen(f)
    try:
        text = r.recognize_google(audio, language="ja-JP")
    except Exception:
        print("Error")
        continue
    print(text)

    if text == "1":
        pyautogui.press("1")
    if text == "2":
        pyautogui.press("2")
    if text == "3":
        pyautogui.press("3")
    if text == "4":
        pyautogui.press("4")