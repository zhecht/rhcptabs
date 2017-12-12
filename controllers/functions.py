import os

all_songs = {

  "redhotchilipeppers": ["True Men Don't Kill Coyotes", "Baby Appeal", "Buckle Down", "Get Up and Jump", "Why Don't You Love Me", "Green Heaven", "Mommy, Where's Daddy?", "Out in L.A.", "Police Helicopter", "You Always Sing the Same", "Grand Pappy Du Plenty","B-Sides","What It Is"],
  "freakystyley": ["Jungle Man", "Hollywood (Africa)", "American Ghost Dance", "If You Want Me to Stay", "Nevermind", "Freaky Styley", "Blackeyed Blonde", "The Brothers Cup", "Battleship", "Lovin' and Touchin'", "Catholic School Girls Rule", "Sex Rap", "Thirty Dirty Birds", "Yertle the Turtle","B-Sides","Bone","Millionaires Against Hunger", "Prince of Sadness", "Set It Straight"],
  "theupliftmofopartyplan": ["Fight Like a Brave", "Funky Crime", "Me and My Friends", "Backwoods", "Skinny Sweaty Man", "Behind the Sun", "Subterranean Homesick Blues", "Party on Your Pussy", "No Chump Love Sucker", "Walkin' on Down the Road", "Love Trilogy", "Organic Anti-Beat Box Band", "B-Sides", "Blues For Meister"],
  "mothersmilk": ["Good Time Boys", "Higher Ground", "Subway to Venus", "Magic Johnson", "Nobody Weird Like Me", "Knock Me Down", "Taste the Pain", "Stone Cold Bush", "Fire", "Pretty Little Ditty", "Punk Rock Classic", "Sexy Mexican Maid", "Johnny, Kick a Hole in the Sky", "B-Sides", "Salute to Kareem", "Show Me Your Soul", "Song That Made Us What We Are Today"],
  "bloodsugarsexmagik": ["The Power of Equality", "If You Have to Ask", "Breaking the Girl", "Funky Monks", "Suck My Kiss", "I Could Have Lied", "Mellowship Slinky in B Major", "The Righteous & the Wicked", "Give It Away", "Blood Sugar Sex Magik", "Under the Bridge", "Naked in the Rain", "Apache Rose Peacock", "The Greeting Song", "My Lovely Man", "Sir Psycho Sexy", "They're Red Hot", "B-Sides", "Castles Made of Sand", "Fela's Cock", "Little Miss Lover", "Search & Destroy", "Sikamikanico", "Soul to Squeeze"],
  "onehotminute": ["Warped", "Aeroplane", "Deep Kick", "My Friends", "Coffee Shop", "Pea", "One Big Mob", "Walkabout", "Tearjerker", "One Hot Minute", "Falling into Grace", "Shallow Be Thy Game", "Transcending", "B-Sides", "Bob", "I Found Out", "I've Been Down", "Let's Make Evil", "Melancholy Mechanics", "Strech"],
  "californication": ["Around the World", "Parallel Universe", "Scar Tissue", "Otherside", "Get on Top", "Californication", "Easily", "Porcelain", "Emit Remmus", "I Like Dirt", "This Velvet Glove", "Savior", "Purple Stain", "Right on Time", "Road Trippin'", "B-Sides", "Bunker Hill", "Fat Dance", "Gong Li", "How Strong", "Instrumental #1", "Instrumental #2", "Over Funk", "Quixoticelixer", "Teatro Jam"],
  "bytheway": ["By the Way", "Universally Speaking", "This Is the Place", "Dosed", "Don't Forget Me", "The Zephyr Song", "Can't Stop", "I Could Die for You", "Midnight", "Throw Away Your Television", "Cabron", "Tear", "On Mercury", "Minor Thing", "Warm Tape", "Venice Queen", "B-Sides", "Bicycle Song", "Body Of Water", "Eskimo", "Havana Affair", "Out Of Range", "Rivers Of Avalon", "Runaway", "Slowly Deeply", "Someone", "Teenager In Love", "Time"],
  "stadiumarcadium": ["Dani California", "Snow ((Hey Oh))", "Charlie", "Stadium Arcadium", "Hump de Bump", "She's Only 18", "Slow Cheetah", "Torture Me", "Strip My Mind", "Especially in Michigan", "Warlocks", "C'mon Girl", "Wet Sand", "Hey", "Desecration Smile", "Tell Me Baby", "Hard to Concentrate", "21st Century", "She Looks to Me", "Readymade", "If", "Make You Feel Better", "Animal Bar", "So Much I", "Storm in a Teacup", "We Believe", "Turn It Again", "Death of a Martian","B-Sides","Million Miles of Water", "Whatever We Want", "Lately", "A Certain Someone", "Mercy Mercy", "Funny Face", "I'll Be Your Domino", "Joe", "Save this Lady"],
  "imwithyou": ["Monarchy of Roses", "Factory of Faith", "Brendan's Death Song", "Ethiopia", "Annie Wants a Baby", "Look Around", "The Adventures of Rain Dance Maggie", "Did I Let You Know", "Goodbye Hooray", "Happiness Loves Company", "Police Station", "Even You Brutus?", "Meet Me at the Corner", "Dance, Dance, Dance"],
  "imbesideyou": ["Strange Man", "Long Progression", "Magpies on Fire", "Victorian Machinery", "Never is a Long Time", "Love of Your Life", "The Sunset Sleeps", "Hometown Gypsy", "Pink as Floyd", "Your Eyes Girl", "In Love Dying", "Catch My Death", "How It Ends", "Brave from Afar", "This Is the Kitt", "Hanalei", "Open/Close"],
  "thegetaway": ["The Getaway", "Dark Necessities", "We Turn Red", "The Longest Wave", "Goodbye Angels", "Sick Love", "Go Robot", "Feasting on the Flowers", "Detroit", "The Ticonderoga", "Encore", "The Hunter", "Dreams of a Samurai"]
}

all_urls = {
  "live": {"url": "live.jpg", "name": "All Live Shows"},
  "redhotchilipeppers": {"url": "redhotchilipeppers.jpg", "name": "Red Hot Chili Peppers" },
  "freakystyley": {"url": "freakystyley.jpg", "name":  "Freaky Styley"},
  "theupliftmofopartyplan": {"url": "upliftmofo.jpg", "name": "The Uplift Mofo Party Plan" },
  "mothersmilk": {"url": "mothersmilk.jpg", "name": "Mother's Milk" },
  "bloodsugarsexmagik": {"url": "bssm.jpg", "name": "Blood Sugar Sex Magik"  },
  "onehotminute": {"url": "onehotminute.jpg", "name": "One Hot Minute"  },
  "californication": {"url": "californication.jpg", "name": "Californication" },
  "bytheway":{ "url": "btw.jpg", "name": "By The Way" },
  "stadiumarcadium": {"url": "sa.jpg", "name": "Stadium Arcadium" },
  "imwithyou": {"url": "iwy.jpg", "name": "I'm With You" },
  "imbesideyou": {"url": "imbesideyou.jpg", "name": "I'm Beside You" },
  "thegetaway": {"url": "getaway.jpg", "name": "The Getaway" }
}

live_concerts = [
  {"id": "hyde_park","where": "Hyde Park", "when":"2004", "songs": ["Brandy", "By The Way", "Don't Forget Me", "I Feel Love", "Leverage of Space", "Right on Time", "Rolling Sly Stone"]},
  {"id": "slane_castle", "where": "Slane Castle", "when":"2003", "songs": ["Californication", "Can't Stop", "Don't Forget Me" ,"Give It Away", "Parallel Universe", "Under The Bridge", "The Zephyr Song"]},
  {"id": "la_cigale", "where": "La Cigale", "when":"2006", "songs": ["Don't Forget Me", "Soul to Squeeze"]},
  {"id":"off_the_map", "where": "Off The Map", "when":"2001", "songs": ["Easily", "Under The Bridge"]},
  {"id": "reading", "where": "Reading", "when":"2006", "songs": ["Don't Forget Me"]},
  {"id": "montreal", "where": "Montreal", "when":"2006","songs": ["Don't Forget Me"]},
]


def get_songs(album_name):
  if album_name == "live":
    return live_concerts,all_urls['live']
  return all_songs[album_name],all_urls[album_name]

def get_tab_names(path,album_name,num):
  try:
    url = "/home/zhecht/rhcptabs/"
    if path == "live":
      return os.listdir(url+'static/tabs/live/%s/%d' % (album_name,num))
    return os.listdir(url+'static/tabs/%s/%d' % (album_name,num))
  except:
    return []
  


