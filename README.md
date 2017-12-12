# rhcptabs

1) First download all the files

2) Controllers --> Holds the python scripts
   Views --> All the htmls. Base has the html for every page and is called at the top of main.html and album.html
   static --> Holds all the pics/ js/ css/ tabs/ files

3) In functions.py, you need to change the variable url to your local path. Just setting url="" would work for local development. It's at the bottom of the functions.py in def get_tab_names()

## Running the site

1) `python3 app.py` If you get an error, you probably don't have flask downloaded. Run `pip3 install flask`

2) This will run the site on localhost:3000. Visit this in your browser to develop
