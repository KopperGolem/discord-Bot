from random import choice, randint

greetings = ['Hallo', 'Hi', 'Was geht', 'Guten tag','Moin',]





def get_response(user_input: str) -> str:
        lowered: str = user_input.lower()

        if user_input == 'Hallo':
                return 'Hallo :)'
        else:
            return choice(['Ich Verstehe nicht',
                           'Kannst du das wiederholen?',
                           'Ich Verstehe nur Hallo :('])

def get_response2(user_input: str) -> str:
       lowered: str = user_input.lower()
       if user_input in greetings:
              return choice(greetings)


       