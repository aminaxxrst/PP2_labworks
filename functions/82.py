#send() method allows you to send a value to the generator
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen)
gen.send("Hello") #Received: Hello
gen.send("World") #Received: World