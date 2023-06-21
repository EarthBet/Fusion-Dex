# Fusion-Dex
This is a Pokedex for Pokemon Infinite Fusion which lets you filter out and sort Pokemon.

fusionDex.csv contains the informal Pokedex number used by players of Pokemon Fusion (HeadDexNumber-BodyDexNumber), the head Pokemon's name, the body Pokemon's name, the typing, the base stat total, the individual stats, the abilities, and the weight of every possible Pokemon Fusion (except the few triple-fusions).

fusionSorter.py opens a GUI that allows the user to place filters on the data and change the order in which the data is displayed.
fusionSorter.py, however, is currently lesser in functionality than Fusion Sorter.ipynb. With fusionSorter.py all text inputs are case sensitive, the entirety of the results are loaded in at once, and closing the results table will close the entire program.

Fusion Sorter.ipynb has those three changes fixed and, additionally, it can be run online here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EarthBet/Fusion-Dex/main?urlpath=https%3A%2F%2Fgithub.com%2FEarthBet%2FFusion-Dex%2Fblob%2Fmain%2FFusion%2520Sorter.ipynb) 
Additionally, it doesn't use pop-up GUIs like fusionSorter.py, instead using features that _I think_ are unique to Jupyter Notebook and cannot be run on normal Python. Or, at least, not as is.
