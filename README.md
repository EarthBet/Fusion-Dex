# Fusion-Dex
This is a Pokedex for Pokemon Infinite Fusion which lets you filter out and sort Pokemon.

fusionDex.csv contains the informal Pokedex number used by players of Pokemon Fusion (HeadDexNumber-BodyDexNumber), the head Pokemon's name, the body Pokemon's name, the typing, the base stat total, the individual stats, the abilities, and the weight of every possible Pokemon Fusion (except the few triple-fusions).

fusionSorter.py opens a GUI that allows the user to place filters on the data and change the order in which the data is displayed.
fusionSorter.py, however, is currently lesser in functionality than Fusion Sorter.ipynb. With fusionSorter.py all text inputs are case sensitive, the entirety of the results are loaded in at once, and closing the results table will close the entire program.

Fusion Sorter.ipynb has those three changes fixed and, additionally, it can be run online here: https://colab.research.google.com/github/EarthBet/Fusion-Dex/blob/main/Fusion%20Sorter.ipynb
Additionally, it doesn't use pop-up GUIs like fusionSorter.py, instead using features that _I think_ are unique to Jupyter Notebook and cannot be run on normal Python. Or, at least, not as is.

Things to note

1. While it doesn't install anything onto your computer, the server running the program needs to install two packages every time you restart your session. There is some leniency here, if you start a session soon after your previous session ended it seems it will still have everything installed. I haven't done much testing with this.

2. You need a Google account to run the program on Google Colab. I _tried_ to get this working on a number of other websites that wouldn't have that requirement, but for some reason the buttons don't work on any of them. They display, but they won't actually do anything.

3. If you don't want to use Google Colab you have three alternatives:

3a. Download it and run it using Jupyter Notebook.

3b. Download fusionSorter.py. While it doesn't have everything that Fusion Sorter.ipynb has, it has most of the features. 

3c. Wait a few days until I get it running through some other method.
