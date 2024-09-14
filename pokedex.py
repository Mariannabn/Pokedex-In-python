import requests
import json
import customtkinter as ctk 
from customtkinter import * 
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import messagebox

mainpoke=CTk()
mainpoke.title("Pokedex")

url="https://pokeapi.co/api/v2/"

# -------- basic info ---------------------





 
# --------- general info -------------















labelwelc = CTkLabel(master=mainpoke, text="Search for your favourite pokemon...",font=('roboto',20))
labelwelc.place(x=136,y=30)
search = CTkEntry(master=mainpoke,width=400,)
search.place(x=100,y=80)
set_appearance_mode('dark')
mainpoke.geometry('600x600')
mainpoke.resizable(height=False,width=False)

fram =CTkFrame(master=mainpoke,width=550,height=400,fg_color="#6688a9",border_width=10,border_color="#ffffff")
fram.place(x=25,y=190)





#--------------- GUI ------------------------
heightL = CTkLabel (master=fram,text="Height: ? ",fg_color="#6688a9",bg_color="#6688a9",font=("Comic Sans MS",20))
heightL.place(x=350,y=70)
varos = CTkLabel(master=fram,text="Weight: ? ",fg_color="#6688a9",bg_color="#6688a9",font=("Comic Sans MS",20))
varos.place(x=350,y=110)
tipos = CTkLabel(master=fram,text="Type: ? ",fg_color="#6688a9",bg_color="#6688a9",font=("Comic Sans MS",20))
tipos.place(x=350,y=150)
sta = CTkLabel(master=fram,text="Stats ",bg_color="#6688a9",font=("Impact",29,'underline'),text_color="#ffcb05",corner_radius=80)

sta.place(x=350,y=190)
#--------stats--------------------------------
HP = CTkLabel(master=fram,text="HP: ? ",fg_color="#6688a9",bg_color="#363b81",font=("Comic Sans MS",18,'bold'),text_color="#363b81")
HP.place(x=350,y=240)
sp = CTkLabel(master=fram,text="Speed: ? ",fg_color="#6688a9",bg_color="#363b81",font=("Comic Sans MS",18,'bold'),text_color="#363b81")
sp.place(x=350,y=265)
at = CTkLabel(master=fram,text="Attack: ? ",fg_color="#6688a9",bg_color="#363b81",font=("Comic Sans MS",18,'bold'),text_color="#363b81")
at.place(x=350,y=290)
SpecialA = CTkLabel(master=fram,text="Special Attack: ? ",fg_color="#6688a9",bg_color="#363b81",font=("Comic Sans MS",18,'bold'),text_color="#363b81")
SpecialA.place(x=350,y=315)
Special_Defense = CTkLabel(master=fram,text="Special Defense: ? ",fg_color="#6688a9",bg_color="#363b81",font=("Comic Sans MS",18,'bold'),text_color="#363b81")
Special_Defense.place(x=350,y=340)
#--------stats--------------------------------



fr2 = CTkFrame(master=fram,fg_color="#323232",height=270,width=270,border_width=10,border_color="#7f0f0f")
fr2.place(x=25,y=80)



iddd =  CTkLabel (master=fram,text="ID: # ?",fg_color="#6688a9",text_color="#000000",font=("Comfortaa",18))
iddd.place(x=25,y=50)
gen =  CTkLabel (master=fram,text="Gender: ♂ ♀ ?",fg_color="#6688a9",text_color="#000000",font=("Comfortaa",18))
gen.place(x=25,y=350)

def name ():    
    heightL.configure(text="Height: ? ")
    varos.configure(text="Weight: ? ")
    tipos.configure(text="Type: ? ")
    HP.configure(text="HP: ? ")
    sp.configure(text="Speed: ? ") 
    at.configure(text="Attack: ? ") 
    SpecialA.configure(text="Special Attack: ? ") 
    Special_Defense.configure(text="Special Defense: ? ") 
    iddd.configure(text="ID: # ? ") 
    gen.configure(text="Gender: ♂ ♀ ?")



    on=search.get()

    customurl = f"{url}/pokemon/{on}"
    response = requests.get(customurl)
    responsejson = response.json()
    isok = response.status_code
    print (isok)
    if isok == 200:
        #-----stats---------------
        height = responsejson['height']
        weight = responsejson['weight']
        abiliti= responsejson['moves']
        abil = {move['move']['name']: move['move'] for move in responsejson ['moves']}
        base_experience = responsejson['base_experience']
        stats = {stat['stat']['name']: stat['base_stat'] for stat in responsejson['stats']}
        type = {t['type']['name'] for t in responsejson['types']}

        Lt=[]
        t=""
        Lt.append(type)

        for i in Lt:
            t= f"{i}" " "
        x=""
        for letter in t:
            if letter != "{" and letter != "}" and  letter != "'":
                x+=letter
        print(t)
            
        
        hp = stats['hp']
        Speed = stats['speed']
        attack = stats['attack']
        special_att = stats['special-attack']
        special_df = stats['special-defense']
        idd = responsejson['id']
        #------stats----------------

        #---GENDER-----------

        species_url = responsejson['species']['url']
        spiceGet = requests.get(species_url)
        spiceData = spiceGet.json()
        genrate = spiceData['gender_rate']
        if genrate == 1:
            gen.configure(text="Gender: female ♀ ")
        elif genrate == 0:
            gen.configure(text="Gender: male ♂ ")
        else:
            gen.configure(text="Gender: No gender")



         





        #---GENDER-----------

        img = responsejson['sprites']['front_default']
        image_response = requests.get(img)
        image_data = Image.open(BytesIO(image_response.content))
        ctkimg = ctk.CTkImage(light_image=image_data, dark_image=image_data, size=(250, 250))

        
       
        

        label = CTkLabel(master=mainpoke,image=ctkimg,text="",fg_color=None,bg_color="transparent")
        label.place(x=60,y=280)
        
        heightL.configure(text=f"Weight: {weight/10} Kg")
        varos.configure(text=f"Height: {height/10} Μeter")

        tipos.configure(text=f"Type: {x}")
        HP.configure(text=f"HP: {hp}")
        sp.configure(text=f"Speed: {Speed}")
        at.configure(text=f"Attack: {attack}")
        SpecialA.configure(text=f"Special Attack: {special_att}")
        Special_Defense.configure(text=f"Special Defense: {special_df}")
        iddd.configure(text=f"ID: # {idd} ")




srarchb = CTkButton(master=mainpoke,fg_color="#b6a608",hover_color='#e4d00a',text='Search',command=name)
srarchb.place(x=220,y=130)
det = CTkLabel(master=mainpoke,text="Pokemon details",font=("Impact",25,),bg_color="#6688a9",text_color="#000000")
det.place(x=220,y=210)
mainpoke.mainloop()


#label.place(x=35,y=240) 