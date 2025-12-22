def main():
    global date
    date = input('Date: ')
    location = input('Location: ')
    type = input('What type of workout? Cardio, boxing, weights, or r(recreational)?: ')
    if type.lower() == 'weights':
        weights()
    if type.lower() == 'cardio':
        cardio()
    if type.lower() == 'boxing':
        boxing()

def save_weights(e, s, r, w):
    with open('Weights.txt', 'a') as f: 
        f.write(f'\n{date}:\nExercise: {e} | Sets: {s} | Reps: {r} | Weight: {w}\n')


#function detailing weight workout 
def weights():
    while True: 
        exercise = input('Type in exercise: ')
        sets = input('Sets: ')
        reps = input('Reps: ')
        weight = input('How heavy? ')
        cont = input('P to export to file, or q to quit: ')
        if cont.lower() == 'p':
            save_weights(exercise, sets, reps, weight)

def save_cardio(type, duration, scale):
    with open('Cardio.txt', 'a') as f: 
        f.write(f'\nExercise type: {type} | Length: {duration} | Scale: {scale}')

#function detailing cardio workout
def cardio():
    while True:
        # date = input('Date: ')
        type = input('Type in type of cardio (swim/run/sport): ')
        length = input('Duration: ')
        scale = input('Scale (1-10): ')
        cont = input('More? Press enter to cont, press p to export, or q to exit: ')
        if cont.lower() == 'q':
            break
        if cont.lower() == 'p':
            save_cardio(type, length, scale)

#function detailing boxing workout
def boxing():
    while True:

        spar = input('Sparring day? (y/n): ')

        if spar.lower() == 'y':
            input('Rounds: ')
            input('How did you feel? Type a short summary: ')
        else:
            input('How many rounds skipping? ')
            input('How many rounds shadowboxing? ')
            input('Heavy bag rounds: ')

if __name__ == "__main__":
    main()