#python program to find match through songs
#get user input
username1=input('what is your name?: ')
song1=input('which song do you like?: ')
username2=input('what is your name?: ')
song2=input('which song do you like?: ')
username3=input('what is your name?: ')
song3=input('which song do you like?: ')
username4=input('what is your name?: ')
song4=input('which song do you like?: ')
username5=input('what is your name?: ')
song5=input('which song do you like?: ')
#comparing songs
if song1==song2:
    print('congratulations!',(username1), 'and',(username2),'are a match')
if song2==song3:
    print('congratulations!',(username2),'and',(username3),'are a match')
if song3==song4:
    print('congratulations!',(username3),'and',(username4),'are a match')
if song4==song5:
    print('congratulations!',(username4),'and',(username5),'are a match')
if song1==song3:
    print('congratulations!',(username1), 'and',(username3),'are a match')
if song1==song4:
    print('congratulations!',(username1), 'and',(username4),'are a match')
if song1==song5:
    print('congratulations!',(username1), 'and',(username5),'are a match')
if song2==song4:
    print('congratulations!',(username2), 'and',(username4),'are a match')
if song2==song5:
    print('congratulations!',(username2), 'and',(username5),'are a match')
if song3==song5:
    print('congratulations!',(username3), 'and',(username5),'are a match')




    
    
#---------------------------------------------------------------------------------------------------------------------




data = {}
match = {}

def getuser_songs(user, data):
    songs = []
    print("Please give 5 songs name")
    for i in range(5):
        s = input(str(i+1) + ")")
        songs.append(s)
    data[user] = songs
    print(data)

def compare(data, user, match):
    songs = []
    compare_s = []
    for i in data['bisesh']:
        songs.append(i)
    if user != 'bisesh':
        for i in data[user]:
            compare_s.append(i)
    for j in songs:
        for k in compare_s:
            if j == k:
                match[user] = 'bisesh'
    
    print(match)
# qu = int(input("Comparison between how may users ?"))
# if qu >= 2:
for i in range(2):
    print("Please give your name")
    name = input("Name : ")
    getuser_songs(name, data)

for i in data:
    compare(data, i, match)


    
