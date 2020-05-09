# Python eksamens projekt

#### Gruppemedlemmer: Sofie Amalie Landt, Amanda Juhl Hansen & Benjamin Kongshaug

### Problemstilling

Med dette projekt ønsker vi at kunne hente billeder ud fra Instagram med en Bot, på baggrund af et hashtag, og på baggrund af disse billeder, kunne træne et neuralt netværk til at kunne skelne mellem billeder med forskellige hashtags.

### Udfordringer

Vores udfordring ved dette projekt er at udvinde data, dette indebærer at kunne logge ind på Instagram, som en bot, uden at blive genkendt og derved blive smidt af/blokeret fra platformen. Dataen vi vil udvinde, skal i sidste ende udgøre et datasæt bestående af en række billeder med dertilhørende target. Billederne skal bearbejdes, hvor kvaliteten skal nedsættes, og gemmes i CSV filer. Herefter er billederne klar til at træne det neurale netværk med det formål at opnå en forbedret accuracy.

Kildekoden opdaterer hele tiden de billeder der vises på Instagram, og til dette skal vi finde en løsning, således at billederne bliver gemt inden de opdateres til nye billeder. Selve udviklingen af det neurale netværk, er også en udfordring, da vi har begrænset erfaring med dette emne.

Det vil altså sige at vi primært fokusere på at udvinde data og sekundært at anvende dette. Målet med vores projekt er at opnå et neuralt netværk, der er trænet så godt, at det vil kunne kende forskel på, om et givet billede skal have enten det ene eller det andet hashtag.

### Teknologier

Til at hente og konventere billeder fra instagram har vi brugt:
- selenium (ChromeDriver)
- skimage

Til at gemme og hente billeder fra CSV filer har vi brugt:
- pandas
- numpy
- csv

Til det neural network har vi brugt:
- matplotlib.pyplot
- numpy
- keras (TensorFlow)
- sklearn
- pickle 
- skImage

Til vores CLI service har vi brugt:
- argparse
- pickle

### Hvordan køres projektet

- Clone projektet fra gitHub
- Kopier config.example.py til en fil med navnet config.py
- Udfyld user i config.py med login oplysninger fra afleveringsfilen.
- Lav en mappe kaldet "images" i roden af projektet

Vores neurale netværk er baseret på de 3 hashtags "cat", "car", "pizza" og vi anbefaler at bruge de samme.

- Åben en command prompt og naviger til roden af projektet.
- Med python insta_cli.py --help kan du se alle komandoer, nedenfor kan du se den rækkefølge vi anbefaler at gøre det i.

Programmet skal som minimum bruge 2 hashtags til det neurale netværk, der er intet max af hashtags.
Vær opmærksom på at de 3 nedenstående kommandoer tager 30-40 minutter tilsammen at eksekvere. 

###### Nedenstående kommando henter 1500 billeder med hashtag cat fra instagram og gemmer dem i en csv fil
    python insta_cli.py -ha cat 1500

###### Nedenstående kommando henter 1500 billeder med hashtag car fra instagram og gemmer dem i en csv fil
    python insta_cli.py -ha car 1500  

###### Nedenstående kommando henter 1500 billeder med hashtag pizza fra instagram og gemmer dem i en csv fil
    python insta_cli.py -ha pizza 1500     
    
Nu er alle billeder downloadet og klar til det neurale netværk.

###### Nedenstående kommando bygger, træner og pickler det neurale netværk
    python insta_cli.py -has cat car pizza 
    
###### Nedenstående kommando tester det neurale netværk og giver en accuracy på data som ikke er set før
    python insta_cli.py -t                 

Nu det tid til at bruge netværket 

###### Nedenstående kommando henter og konventere billede og netværket gætter på hvilket hashtag billede passer bedst til
    python insta_cli.py -l <LINK_TO_IMAGE> 

Nedenfor er der eksempler på billeder man kan prøve at bruge men man er også velkommen til selv at finde billeder at prøve med.

- https://previews.123rf.com/images/katerinamore/katerinamore1808/katerinamore180801119/107239902-children-s-funny-pizza-in-the-form-of-a-cat-s-face-italian-cuisine-children-s-menu.jpg
- https://www.thesun.co.uk/wp-content/uploads/2018/11/cat-2.png
- https://i.pinimg.com/736x/9c/65/72/9c6572022945ed5c9578f044189fac9a.jpg
- https://i.pinimg.com/originals/4d/3b/c4/4d3bc4b4b87b309a24aa05ee5ec4863f.jpg
