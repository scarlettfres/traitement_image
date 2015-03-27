from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "10.0.204.200", 9559)
tts.say("Hello")

