from pafy import new

link = input(Enter ur link  )
audio = new(link)
stream = audio.audiostreams
stream[1].download()






'''
test = new('httpswww.youtube.comwatchv=8nBFqZppIF0')

stream = test.streams
for i in stream
    print(i)
stream[0].download()
'''
''''
link = input(Enter ur link  )
video = new(link)
stream = video.streams
stream[1].download()
'''