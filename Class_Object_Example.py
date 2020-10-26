class Human:
    def __init__(self, name, gender, occupation):
        self.name = name
        self.gender = gender
        self.occupation = occupation

    def Speak(self):
        print(f'{self.name} is speaking')


if __name__ == "__main__":
    human = Human('Megha Naik', 'Female', 'SE')
    human.Speak()