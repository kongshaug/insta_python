# insta_python

Gruppemedlemmer: Sofie Amalie Landt, Amanda Juhl Hansen & Benjamin Kongshaug

Python eksamens projekt


Valg af teknologier (biblioteker)
Til dette projekt forventer vi at bruge:

Selenium
Pandas
Keras
Time
Regular Expressions
tqdm
Tensorflow
Mathplotlib.pyplot
pymysql og sqlalchemy





### Problemstillingen

Med dette projekt ønsker vi at kunne hente billeder ud fra Instagram med en Bot, på baggrund af et hashtag, og på baggrund af disse billeder, kunne træne et neuralt netværk til at kunne skelne mellem billeder med forskellige hashtags.

### Udfordringer

Vores udfordring ved dette projekt er at udvinde data, dette indebærer at kunne logge ind på Instagram, som en bot, uden at blive genkendt og derved blive smidt af/blokeret fra platformen. Dataen vi vil udvinde, skal i sidste ende udgøre et datasæt bestående af en række billeder med dertilhørende target. Billederne skal bearbejdes, hvor kvaliteten skal nedsættes, og gemmes i CSV filer. Herefter er billederne klar til at træne det neurale netværk med det formål at opnå en forbedret accuracy.

Kildekoden opdaterer hele tiden de billeder der vises på Instagram, og til dette skal vi finde en løsning, således at billederne bliver gemt inden de opdateres til nye billeder. Selve udviklingen af det neurale netværk, er også en udfordring, da vi har begrænset erfaring med dette emne.

Det vil altså sige at vi primært fokusere på at udvinde data og sekundært at anvende dette. Målet med vores projekt er at opnå et neuralt netværk, der er trænet så godt, at det vil kunne kende forskel på, om et givet billede skal have enten det ene eller det andet hashtag.

## Teknologier

Til at hente og konventere billeder fra instagram har vi brugt:

selenium (ChromeDriver)
skimage

Til at gemme og hente billeder fra CSV filer har vi brugt:

pandas
numpy
csv

Til det neural network har vi brugt:

matplotlib.pyplot
numpy
keras (TensorFlow)
SkLearn
Pickle 
skImage

Til vores CLI service har vi brugt:

Argparse
Pickle




Hvordan køres projektet
