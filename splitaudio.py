from pydub import AudioSegment

audio = 'OHP Practice Interview.wav'
seconds = 20

def split_into_parts(audio, seconds):
    fullAudio = AudioSegment.from_file(audio)
    
    # Durations
    
    totalDuration = fullAudio.duration_seconds
    print(totalDuration)
    roundedDuration = (totalDuration + (seconds - 1)) // seconds * seconds
    print(roundedDuration)

    # Get number of parts needed
    numParts = int(roundedDuration / seconds)
    print(numParts)

    i = 0

    while i < numParts:
        
        # Find starting and stopping points

        firstVal = i * seconds
        lastVal = (i+1) * seconds

        # Convert to miliseconds

        firstVal = firstVal * 1000
        lastVal = lastVal * 1000

        # Split out the part

        newAudio = AudioSegment.from_wav(audio)
        newAudio = newAudio[firstVal:lastVal]
        filename = "part" + str(i+1) + ".wav"
        newAudio.export(filename, format="wav") #Exports to a wav file in the current path.

        print("part" + str(i+1))
        i =  i + 1


split_into_parts(audio, seconds)