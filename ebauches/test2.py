from naoqi import ALProxy
motion = ALProxy("ALMotion","10.0.204.200", 9559)
motion.setStiffnesses("Body", 1.0)
