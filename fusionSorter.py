#import numpy as np
import pandas as pd
#import warnings
#import tkinter as tk
import PySimpleGUI as sg

df = pd.read_csv('fusionDex.csv')
filters = ["Head", "Body", "Either", "TypeOne", "TypeTwo", "MAX BASE STAT TOTAL", "MIN BASE STAT TOTAL", "MAX HP", "MIN HP", "MAX ATTACK", "MIN ATTACK", "MAX DEFENSE", "MIN DEFENSE", "MAX SPECIAL ATTACK", "MIN SPECIAL ATTACK", "MAX SPECIAL DEFENSE", "MIN SPECIAL DEFENSE", "MAX SPEED", "MIN SPEED", "ABILITY", "MIN WEIGHT", "MAX WEIGHT"]
reset = filters
sorting = ["INFORMAL DEX", "ASCENDING"]
def gui():
    layout1 = [[sg.Text("Do you want to select FILTERS, SORT the results, or VIEW the results? You'll be able to return here by pressing the RETURN button on any other page.")], [sg.Button("FILTERS")], [sg.Button("SORT")], [sg.Button("VIEW")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))

    while True:
        event, values = window.read()
        if event == "FILTERS":
            window.close()
            filtered()
        if event == "SORT":
            window.close()
            sort()
        if event == "VIEW":
            window.close()
            view()
        if event == sg.WIN_CLOSED:
            break
def filtered():
    layout1 = [[sg.Text("What do you want to view filters for? SPECIES, TYPING, STATS, ABILITIES, or WEIGHT? You can restore all filters to their default by pressing RESET.")], [sg.Button("SPECIES")], [sg.Button("TYPING")], [sg.Button("STATS")], [sg.Button("ABILITIES")], [sg.Button("WEIGHT")], [sg.Button("RESET")], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    global filters
    global reset
    while True:
        event, values = window.read()
        if event == "SPECIES":
            window.close()
            pkmnFilter()
        if event == "TYPING":
            window.close()
            typeFilter()
        if event == "STATS":
            window.close()
            statFilter()
        if event == "ABILITIES":
            window.close()
            abilityFilter()
        if event == "WEIGHT":
            window.close()
            weightFilter()
        if event == "RESET":
            window.close()
            filters = reset
            gui()
        if event == "RETURN":
            window.close()
            gui()
        if event == sg.WIN_CLOSED:
            break
def pkmnFilter():
    layout1 = [[sg.Text("Do you want to set the HEAD Pokemon or set the BODY Pokemon? Or do you want to set a Pokemon that can be EITHER head or body?")], [sg.Button("HEAD")], [sg.Button("BODY")], [sg.Button("EITHER")], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    
    while True:
        event, values = window.read()
        if event == "HEAD":
            window.close()
            setHead()
        if event == "BODY":
            window.close()
            setBody()
        if event == "EITHER":
            window.close()
            setEither()
        if event == "RETURN":
            window.close()
            gui()
        if event == sg.WIN_CLOSED:
            break
def setHead():
    global filters
    layout1 = [[sg.Text("What Pokemon should be locked in as the head?")], [sg.InputText()], [sg.Button('SUBMIT')], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    
    while True:
        event, values = window.read()
        if event == 'SUBMIT':
            filters[0] = values[0]
            window.close()
            setHead()
        if event == "RETURN":
            window.close()
            gui()
        if event == sg.WIN_CLOSED:
            break
def setBody():
    global filters
    layout1 = [[sg.Text("What Pokemon should be locked in as the body?")], [sg.InputText()], [sg.Button('SUBMIT')], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    
    while True:
        event, values = window.read()
        if event == 'SUBMIT':
            filters[1] = values[0]
            window.close()
            setBody()
        if event == "RETURN":
            window.close()
            gui()
        if event == sg.WIN_CLOSED:
            break
def setEither():
    global filters
    layout1 = [[sg.Text("What Pokemon do you want to view fusions of? This will erase any filters set for the head or body.")], [sg.InputText()], [sg.Button('SUBMIT')], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    
    while True:
        event, values = window.read()
        if event == 'SUBMIT':
            filters[2] = values[0]
            filters[1] = "Body"
            filters[0] = "Head"
            window.close()
            setEither()
        if event == "RETURN":
            window.close()
            gui()
        if event == sg.WIN_CLOSED:
            break
def typeFilter():
    #Normal, Fire, Fighting, Water, Flying, Grass, Poison, Electric, Ground, Psychic, Rock, Ice, Bug, Dragon, Ghost, Dark, Steel, or Fairy
    layout1 = [[sg.Text("What type do you want the Pokemon in the results to be?")], [sg.Button("NORMAL")], [sg.Button("FIRE")], [sg.Button("FIGHTING")], [sg.Button("WATER")], [sg.Button("FLYING")], [sg.Button("GRASS")], [sg.Button("POISON")], [sg.Button("ELECTRIC")], [sg.Button("GROUND")], [sg.Button("PSYCHIC")], [sg.Button("ROCK")], [sg.Button("ICE")], [sg.Button("BUG")], [sg.Button("DRAGON")], [sg.Button("GHOST")], [sg.Button("DARK")], [sg.Button("STEEL")], [sg.Button("FAIRY")], [sg.Button("SET BOTH TYPES")], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    global filters
    while True:
        event, values = window.read()
        if event in ["NORMAL", "FIRE", "FIGHTING", "WATER", "FLYING", "GRASS", "POISON", "ELECTRIC", "GROUND", "PSYCHIC", "ROCK", "ICE", "BUG", "DRAGON", "GHOST", "DARK", "STEEL", "FAIRY"]:
            filters[3] = event
            window.close()
            typeFilter()
        if event == "SET BOTH TYPES":
            window.close()
            typeTwoFilter()
        if event == "RETURN":
            window.close()
            gui()
        if event == sg.WIN_CLOSED:
            break
def typeTwoFilter():
    #Normal, Fire, Fighting, Water, Flying, Grass, Poison, Electric, Ground, Psychic, Rock, Ice, Bug, Dragon, Ghost, Dark, Steel, or Fairy
    layout1 = [[sg.Text("What type do you want the Pokemon in the results to be?")], [sg.Button("NORMAL")], [sg.Button("FIRE")], [sg.Button("FIGHTING")], [sg.Button("WATER")], [sg.Button("FLYING")], [sg.Button("GRASS")], [sg.Button("POISON")], [sg.Button("ELECTRIC")], [sg.Button("GROUND")], [sg.Button("PSYCHIC")], [sg.Button("ROCK")], [sg.Button("ICE")], [sg.Button("BUG")], [sg.Button("DRAGON")], [sg.Button("GHOST")], [sg.Button("DARK")], [sg.Button("STEEL")], [sg.Button("FAIRY")], [sg.Button("SET ONE TYPE")], [sg.Button("SET OTHER TYPE")], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    global filters
    while True:
        event, values = window.read()
        if event in ["NORMAL", "FIRE", "FIGHTING", "WATER", "FLYING", "GRASS", "POISON", "ELECTRIC", "GROUND", "PSYCHIC", "ROCK", "ICE", "BUG", "DRAGON", "GHOST", "DARK", "STEEL", "FAIRY"]:
            filters[4] = event
            window.close()
            typeTwoFilter()
        if event == "SET ONE TYPE":
            filters[4] = "TypeTwo"
            window.close()
            typeFilter()
        if event == "SET OTHER TYPE":
            window.close()
            typeFilter()
        if event == "RETURN":
            window.close()
            gui()
        if event == sg.WIN_CLOSED:
            break
def statFilter():
    layout1 = [[sg.Text("Type in a value below then click the desired button. The value typed in will either be the maximum or minimum of a stat. The buttons indicate which it will be.")], [sg.InputText()], [sg.Button('MAX BASE STAT TOTAL')], [sg.Button('MIN BASE STAT TOTAL')], [sg.Button('MAX HP')], [sg.Button('MIN HP')], [sg.Button('MAX ATTACK')], [sg.Button('MIN ATTACK')], [sg.Button('MAX DEFENSE')], [sg.Button('MIN DEFENSE')], [sg.Button('MAX SPECIAL ATTACK')], [sg.Button('MIN SPECIAL ATTACK')], [sg.Button('MAX SPECIAL DEFENSE')], [sg.Button('MIN SPECIAL DEFENSE')], [sg.Button('MAX SPEED')], [sg.Button('MIN SPEED')], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    global filters
    while True:
        event, values = window.read()
        if event == "MAX BASE STAT TOTAL":
            filters[5] = values[0]
            window.close()
            statFilter()
        elif event == "MIN BASE STAT TOTAL":
            filters[6] = values[0]
            window.close()
            statFilter()
        elif event == "MAX HP":
            filters[7] = values[0]
            window.close()
            statFilter()
        elif event == "MIN HP":
            filters[8] = values[0]
            window.close()
            statFilter()
        elif event == "MAX ATTACK":
            filters[9] = values[0]
            window.close()
            statFilter()
        elif event == "MIN ATTACK":
            filters[10] = values[0]
            window.close()
            statFilter()
        elif event == "MAX DEFENSE":
            filters[11] = values[0]
            window.close()
            statFilter()
        elif event == "MIN DEFENSE":
            filters[12] = values[0]
            window.close()
            statFilter()
        elif event == "MAX SPECIAL ATTACK":
            filters[13] = values[0]
            window.close()
            statFilter()
        elif event == "MIN SPECIAL ATTACK":
            filters[14] = values[0]
            window.close()
            statFilter()
        elif event == "MAX SPECIAL DEFENSE":
            filters[15] = values[0]
            window.close()
            statFilter()
        elif event == "MIN SPECIAL DEFENSE":
            filters[16] = values[0]
            window.close()
            statFilter()
        elif event == "MAX SPEED":
            filters[17] = values[0]
            window.close()
            statFilter()
        elif event == "MIN SPEED":
            filters[18] = values[0]
            window.close()
            statFilter()
        elif event == "RETURN":
            window.close()
            gui()
        elif event == sg.WIN_CLOSED:
            break
def abilityFilter():
    global filters
    layout1 = [[sg.Text("All Pokemon shown in the results should have what ability?")], [sg.InputText()], [sg.Button('SUBMIT')], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    
    while True:
        event, values = window.read()
        if event == 'SUBMIT':
            filters[19] = values[0]
            window.close()
            abilityFilter()
        elif event == "RETURN":
            window.close()
            gui()
        elif event == sg.WIN_CLOSED:
            break
def weightFilter():
    global filters
    layout1 = [[sg.Text("WARNING: WEIGHT INFORMATION MAY BE WRONG!")], [sg.Text("Type in a value below then click the MAX WEIGHT button to set it as the maximum weight or the MIN WEIGHT button to set it as the minimum weight.")], [sg.InputText()], [sg.Button('MAX WEIGHT')], [sg.Button('MIN WEIGHT')], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    
    while True:
        event, values = window.read()
        if event == 'MAX WEIGHT':
            filters[20] = values[0]
            window.close()
            weightFilter()
        elif event == 'MIN WEIGHT':
            filters[21] = values[0]
            window.close()
            weightFilter()
        elif event == "RETURN":
            window.close()
            gui()
        elif event == sg.WIN_CLOSED:
            break
def sort():
    layout1 = [[sg.Text("What should the results be ordered by, and in what order?")], 
               [sg.Button("INFORMAL DEX")], [sg.Button("ALPHABETICAL BY HEAD POKEMON NAME")], [sg.Button("ALPHABETICAL BY BODY POKEMON NAME")], [sg.Button("BY BASE STAT TOTAL")], [sg.Button("BY HP")], [sg.Button("BY ATTACK")], [sg.Button("BY DEFENSE")], [sg.Button("BY SPECIAL ATTACK")], [sg.Button("BY SPECIAL DEFENSE")], [sg.Button("BY SPEED")], [sg.Button("BY WEIGHT")], [sg.Button("ASCENDING")], [sg.Button("DESCENDING")], [sg.Button("RETURN")]]
    window = sg.Window(title="Pokemon Fusion Dex Search Engine", layout = layout1, margins=(500, 250))
    #Informal dex number, alphabetical by head, alphabetical by body, stats, weight
    global sorting
    while True:
        event, values = window.read()
        if event == "INFORMAL DEX":
            sorting[0] = event
            window.close()
            sort()
        elif event == "ALPHABETICAL BY HEAD POKEMON NAME":
            sorting[0] = event 
            window.close()
            sort()
        elif event == "ALPHABETICAL BY BODY POKEMON NAME":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY BASE STAT TOTAL":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY HP":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY ATTACK":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY DEFENSE":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY SPECIAL ATTACK":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY SPECIAL DEFENSE":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY SPEED":
            sorting[0] = event
            window.close()
            sort()
        elif event == "BY WEIGHT":
            sorting[0] = event
            window.close()
            sort()
        elif event == "ASCENDING":
            sorting[1] = "ASCENDING"
            window.close()
            sort()
        elif event == "DESCENDING":
            sorting[1] = "DESCENDING"
            window.close()
            sort()
        elif event == "RETURN":
            window.close()
            gui()
        elif event == sg.WIN_CLOSED:
            break
def view():
    #filters = ("Head", "Body", "Either", "TypeOne", "TypeTwo", "MAX BASE STAT TOTAL", "MIN BASE STAT TOTAL", "MAX HP", "MIN HP", "MAX ATTACK", "MIN ATTACK", "MAX DEFENSE", "MIN DEFENSE", "MAX SPECIAL ATTACK", "MIN SPECIAL ATTACK", "MAX SPECIAL DEFENSE", "MIN SPECIAL DEFENSE", "MAX SPEED", "MIN SPEED", "ABILITY", "MIN WEIGHT", "MAX WEIGHT")
    global df
    #Filters
    if filters[0] != "Head":
        if filters[0] in df['nameHead'].values:
            df = df[df['nameHead'] == filters[0]]
    if filters[1] != "Body":
        if filters[1] in df['nameBody'].values:
            df = df[df['nameBody'] == filters[1]]
    if filters[2] != "Either":
        if (filters[2] in df['nameBody'].values) or (filters[2] in df['nameHead'].values):
            df = df[(df['nameBody'] == filters[2]) | (df['nameHead'] == filters[2])]
    if filters[3] != "TypeOne":
        if filters[3] in df['type1'].values:
            df = df[df['type1'] == filters[3]]
    if filters[4] != "TypeTwo":
        if filters[4] in df['type2'].values:
            df = df[df['type2'] == filters[4]]
    if filters[5] != "MAX BASE STAT TOTAL":
        df = df[df['base_total'] <= int(filters[5])]
    if filters[6] != "MIN BASE STAT TOTAL":
        df = df[df['base_total'] >= int(filters[6])]
    if filters[7] != "MAX HP":
        df = df[df['hp'] <= int(filters[7])]
    if filters[8] != "MIN HP":
        df = df[df['hp'] >= int(filters[8])]
    if filters[9] != "MAX ATTACK":
        df = df[df['attack'] <= int(filters[9])]
    if filters[10] != "MIN ATTACK":
        df = df[df['attack'] >= int(filters[10])]
    if filters[11] != "MAX DEFENSE":
        df = df[df['defense'] <= int(filters[11])]
    if filters[12] != "MIN DEFENSE":
        df = df[df['defense'] >= int(filters[12])]
    if filters[13] != "MAX SPECIAL ATTACK":
        df = df[df['sp_attack'] <= int(filters[13])]
    if filters[14] != "MIN SPECIAL ATTACK":
        df = df[df['sp_attack'] >= int(filters[14])]
    if filters[15] != "MAX SPECIAL DEFENSE":
        df = df[df['sp_defense'] <= int(filters[15])]
    if filters[16] != "MIN SPECIAL DEFENSE":
        df = df[df['sp_defense'] >= int(filters[16])]
    if filters[17] != "MAX SPEED":
        df = df[df['speed'] <= int(filters[17])]
    if filters[18] != "MIN SPEED":
        df = df[df['speed'] >= int(filters[18])]
    if filters[20] != "MIN WEIGHT":
        df = df[df['weight_kg'] >= int(filters[20])]
    if filters[21] != "MAX WEIGHT":
        df = df[df['weight_kg'] >= int(filters[21])]
        
    df = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])
    
    #Sorting
    if sorting[0] == "INFORMAL DEX":
        if sorting[1] == "DESCENDING":
            df = df.iloc[::-1]
    elif sorting[0] == "ALPHABETICAL BY HEAD POKEMON NAME":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='nameHead')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='nameHead')
            df = df.iloc[::-1]
    elif sorting[0] == "ALPHABETICAL BY BODY POKEMON NAME":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='nameBody')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='nameBody')
            df = df.iloc[::-1]
    elif sorting[0] == "BY BASE STAT TOTAL":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='base_total')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='base_total')
            df = df.iloc[::-1]
    elif sorting[0] == "BY HP":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='hp')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='hp')
            df = df.iloc[::-1]
    elif sorting[0] == "BY ATTACK":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='attack')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='attack')
            df = df.iloc[::-1]
    elif sorting[0] == "BY DEFENSE":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='defense')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='defense')
            df = df.iloc[::-1]
    elif sorting[0] == "BY SPECIAL ATTACK":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='sp_attack')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='sp_attack')
            df = df.iloc[::-1]
    elif sorting[0] == "BY SPECIAL DEFENSE":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='sp_defense')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='sp_defense')
            df = df.iloc[::-1]
    elif sorting[0] == "BY SPEED":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='speed')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='speed')
            df = df.iloc[::-1]
    elif sorting[0] == "BY WEIGHT":
        if sorting[1] == "ASCENDING":
            df = df.sort_values(by='weight_kg')
        elif sorting[1] == "DESCENDING":
            df = df.sort_values(by='weight_kg')
            df = df.iloc[::-1]
    
    # Create the window layout
    headings = list(df.columns)
    values = df.values.tolist()
    layout = [[sg.Table(values=values, headings=headings)]]
    
    # Create the window and display it
    window = sg.Window("Pokemon Fusion Dex Search Engine", layout)
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    
    
gui()