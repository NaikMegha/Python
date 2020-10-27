class Accident(Exception):
    def __init__(self,message):
        self.message = message

    def handle(self):
        print(f"Exception occured ,{self.message}")


try:
    print("Try block")
    raise Accident("Take a look")
    10/0

except Accident as e:
      e.handle()

finally:
    print("This is finally block")
