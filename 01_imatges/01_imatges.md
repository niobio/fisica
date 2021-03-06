
# Imatges

La llum i el seu comportament ha estat un misteri durant molt temps i encara avui, que el seu comportament està molt ben descrit per l'electrodinàmica quàntica, mostra comportaments que costen d'entendre. En aquesta unitat ens dedicarem a entendre el comportament bàsic de la llum per a la formació d'imatges. El primer en fer una descripció satisfactòria del comportament de la llum per ala formació d'imatges ha estat Isaac Newton al seu treball Opticks. Newton va entendre la llum com formada per petits corpuscles, com si estigués formada per boletes diminutes, i això li va permetre explicar el rebot de la llum sobre una superfície plana seguint el mateix comportament que les boles de billar. Aquest model s'anomena model corpuscular de la llum.

<figure>
  <img src="img/billiard-balls.svg" alt="" width="50%">
  <figcaption> <strong>La llum es reflecteix sobre una superfície plana de la mateixa manera que reboten les boles a les bandes d'una taula de billar.</strong> </figcaption>
</figure>

Aquest model ha estat molt reeixit per a explicar la formació d'imatges. Posteriorment s'han trobat comportaments de la llum que no es podien explicar amb el model corpuscular i es va proposar que la llum s'havia d'entendre com un fenomen ondulatori. Aquest model va ser proposat pel físic holandès Christian Huygens i el seu model va ser combatut pels seguidors de Newton. Finalment al segle XIX el físic anglès Thomas Young mostra “sense cap dubte” que el comportament de la llum era el d'un ona amb el seu experiment de la doble escletxa. La història no acaba aquí perquè just a començament del segle XX va ser necessari tornar a entendre la llum com a format per partícules anomenats quanta (actualment fotons) per a explicar fenòmens com la radiació de cos negre i l'efecte fotoelèctric.<sup><a href="#fn1" id="ref1">1</a></sup>

Per a l'estudi de la formació d'imatges tindrem en compte un parell de fets ben coneguts:

* La llum es propaga en línia recta en un medi homogeni <sup><a href="#fn2" id="ref2">2</a></sup>. Indicarem la seva trajectòria dibuixant raigs que indicaran el camí traçat per la llum.

* La velocitat de la llum és constant en un medi homogeni. Al buit la velocitat és $$c=3\times10^{8}\,\mathrm{m/s}$$
  i, a efectes pràctics, considerarem que la velocitat a l'aire és la mateixa.

## Llei de la reflexió

Podem destacar dos tipus de reflexió. Quan la superfície especular és plana tenim reflexió especular i l'exemple més clar és el mirall o una superfície metàl·lica polida i, fins i tot la superfície d'aigua quan està quieta. En cas de tenir una superfície rugosa la reflexió és difusa i no podem formar una imatge. La llei de la reflexió es compleix a nivell local però como l'angle d'incidència de cada raig és diferent respecte a la superfície, els raigs emergents no són pas paral·lels.

<figure>
  <img src="img/especular_difusa.svg" alt="" width="80%">
  <figcaption> <strong>Reflexió especular i difusa. La llei de la reflexió es verifica localment en ambdues superfícies però només a la imatge de l'esquerra tots els raigs tenen el mateix angle d'incidència i de reflexió.</strong> </figcaption>
</figure>

La llei de la reflexió sobre superfícies planes estableix que l'angle de reflexió és igual a l'angle d'incidència. Si anomenem $$\alpha_{i}$$ l'angle dels raigs d'incidència i $$\alpha_{r}$$ l'angle format pels raigs reflectits, tenim que la llei de la reflexió s'escriu:

$$\alpha_{r}=\alpha_{i}$$

Els angles d'incidència i reflexió es mesuren respecte de la línia perpendicular a la superfície de reflexió anomenada recta normal, com es veu a la figura següent.

<figure>
  <img src="img/llei_reflex.svg" alt="" width="60%">
  <figcaption> <strong> Llei de la reflexió. L'angle de reflexió és igual a l'angle d'incidència. Mesurem els alngles respecte de la recta normal.</strong> </figcaption>
</figure>

## Refracció de la llum

Com ja ho hem dit, la llum es propaga en un medi homogeni a una velocitat constant, però quan la llum passa d'un medi a un altre la seva velocitat de propagació canvia i això pot produir un canvi en la direcció de propagació de la llum. Aquest canvi en la direcció de propagació de la llum l'anomenen refracció de la llum. A la Figura [fig:refrac] es pot veure un raig de llum que incideix des d'una medi 1 amb un angle $$\alpha_{1}$$ respecte a la normal de la superfície de separació dels dos medis. Quan travessa la superfície passa a propagar-se en el medi 2 amb un angle $$\alpha_{2}$$ respecte a la mateixa recta normal. També es pot veure un raig reflectit. Sempre que hi ha una superfície de separació de dos medis hi haurà llum reflectida què, com ja hem vist, segueix la llei de la reflexió $$(\alpha_{1}=\alpha_{1}^{,})$$.

<figure>
  <img src="img/llei_refrac.svg" alt="" width="60%">
  <figcaption> <strong>Refracció de la llum. La llum es propaga per un medi 1 i passa a un medi 2 amb propietats òptiques diferents, com a conseqüència, la direcció de propagació canvia. La llei que descriu aquest comportament és la llei de Snell.</strong> </figcaption>
</figure>

Els dos angles $$\alpha_{1}$$ i $$\alpha_{2}$$ estan relacionats amb la velocitat de propagació de la llum ens els dos medis, $$v_{1}$$ i $$v_{2}$$ respectivament, a través de la llei de la refracció de la llum o **llei de Snell**:

$$\frac{\sin(\alpha_{1})}{v_{1}}=\frac{\sin(\alpha_{2})}{v_{2}}$$

Podem deduir de la llei que si la llum passa a un segon medi on es propaga a una velocitat més petita, $$(v_{2}<v_{1})$$, l'angle de sortida serà més petit que l'angle d'entrada $$(\alpha_{2}<\alpha_{1})$$. El mateix raonament és valid en cas contrari, si la velocitat del segon medi és més gran, també ho serà l'angle de sortida. Pots dir quin dels dos casos mostra la figura anterior? 

## Índex de refracció

A la llei de Snell apareixen les velocitats de propagació de la llum. Per a no tenir que treballar amb valors de velocitats tan grans (recordem que la velocitat de la llum al buit és $$c=3\times10^{8}\mathrm{m/s})$$ el que es fa és multiplicar ambdós membres de l'equació $$\eqref{eq:snell}$$ per la velocitat de la llum al buit, $$c$$, per a obtenir

$$
\begin{equation}\label{eq:snell}
\frac{c}{v_{1}}\sin(\alpha_{1})=\frac{c}{v_{2}}\sin(\alpha_{2})
\end{equation}
$$


Definirem índex de refracció, $$n$$, d'un medi on la velocitat de propagació és $$v$$ al quocient

$$n=\frac{c}{v}$$

Podem observar que l'índex de refracció és una magnitud adimensional (no porta unitats) i, donat que la velocitat de propagació de la llum en qualsevol medi és sempre inferior a la velocitat de la llum al buit, l'índex de refracció sempre és un nombre superior a 1. Amb aquesta definició podem reescriure la llei de Snell de la següent manera:

$$n_{1}\sin(\alpha_{1})=n_{2}\sin(\alpha_{2})$$

on $$n_{1}$$ i $$n_{2}$$ són, respectivament, els índex de refracció dels medis 1 i 2.

A la taula següent es pot observar el llistat dels índex de refracció d'alguns materials.


|Material   |Índex de refracció|
|-----------|------------------|
|Buit       |1                 |
|Aire       |1,000293          |
|Aigua      |1,333             |
|Etanol     |1,36              |
|Vidre comú |1,46              |
|Vidre crown|1,52              |
|Vidre flint|1,62              |
|Diamant    |2,42              |

## Reflexió total interna

Ja hem vist que quan la llum travessa una superfície de separació entre dos medis transparents de diferent índex de refracció es produeix un canvi en la direcció de la llum al passar d'un medi a l'altre. 

<figure>
  <img src="img/angle_limit.svg" alt="" width="100%">
  <figcaption> <strong>Reflexió total interna. Quan la llum passa de l'aigua a l'aire, l'angle refractat, $$\alpha_{2}^{,}$$, resulta més gran que l'angle d'incidència, $$\alpha_{1}$$. Si augmentem l'angle $$\alpha_{1}$$ arribarà a un valor per al qual l'angle de refracció és rasant $$(\alpha_{2}^{,}=90^{\circ})$$. Aquest angle d'incidència es diu angle límit, $$\alpha_{L}$$, i a partir d'aquest valor no hi ha raig refractat i només tenim llum reflectida.</strong></figcaption>
</figure>

Aquest fenomen es diu refracció i hem vist que quan la llum passa d'un medi a un altre d'índex de refracció més alt, la llum transmesa surt amb un angle més petit respecte a la normal. Si tenim el cas invers on la llum passa d'un medi d'índex més alt cap a un d'índex més baix, com és el cas de passar d'aigua a l'aire o de vidre a l'aire, la relació d'angles s'inverteix, en aquest cas tenim que $$\alpha_{2}^{,}>\alpha_{1}$$ (veure figura anterior).

Si continuem augmentant l'angle d'incidència trobarem que hi arribarà el moment que per a un angle $$\alpha_{1}<90^{\circ}$$, tindrem un angle de refracció $$\alpha_{2}^{,}=90^{\circ}$$. A aquest angle l'anomenen angle límit $$(\alpha_{L})$$ i, a partir d'aquest angle, només hi haurà llum reflectida. Aquest fenomen es coneix com a reflexió total interna i és el que utilitzen les fibres òptiques per a transmetre informació en forma de polsos lumínics al llarg de grans distàncies sense tenir pèrdues d'energia.

<figure>
  <img src="img/fibra_optica.svg" alt="" width="40%">
  <figcaption><strong>Les fibres òptiques utilitzen el fenomen de reflexió total per a transmetre informació sense pèrdues.</strong></figcaption>
</figure>

L'angle límit per a la separació de dos medis d'índex de refracció $$n_{1}>n_{2}$$, el podem trobar utilitzant la llei de Snell on imposarem la condició $$\alpha_{2}^{,}=90^{\circ}$$:

$$n_{1}\sin(\alpha_{L})=n_{2}\sin(90^{\circ})$$

i, com $$\sin(90^{\circ})=1$$, obtenim:

$$
\begin{equation}\label{eq:angle_limit}
\sin(\alpha_{L})=\frac{n_{2}}{n_{1}}
\end{equation}
$$

La relació $$\eqref{eq:angle_limit}$$ és la condició d'angle límit. A partir d'aquest valor d'angle d'incidència tindrem reflexió total. De la relació [eq:angle_limit] podem veure que la condició només es satisfà si el quocient $$n_{2}/n_{1}<1$$, ja que la funció sinus és una funció que sempre és menor a 1. En cas contrari, si el medi 2 tingués un índex de refracció major que el medi 1, no trobaríem solució.

## Miralls esfèrics

Els miralls esfèrics són superfícies reflectants de forma esfèrica que, per les seves característiques que estudiarem a continuació, es fan servir en diverses aplicacions, com ser els miralls que hi ha en les cantonades on hi ha entrecreuaments de carrers amb poca visibilitat, miralls retrovisors dels cotxes, telescopis reflectors, etc.

<figure>
  <img src="img/mirall_concau_focus.svg" alt="" width="80%">
  <figcaption><strong>El punt F correspon al focus del mirall còncau i és per un passen tots els raigs que venen paral·lels a l'eix òptic. L'eix òptic divideix el mirall en dues parts iguals i passa pel punt O anomenat vèrtes del mirall.</strong> </figcaption>
</figure>


La llei de reflexió és una llei local, es a dir es verifica punt a punt i també és vàlida per a miralls esfèrics però, com la superfície del mirall no és plana, un feix de raigs paral·les no incideixen tots amb el mateix angle sobre cada punt de la superfície del mirall i, per tant, els raigs reflectits no sortiran tots paral·lels com en el cas d'un mirall pla, sinó que passaran tots pel mateix punt. Aquest punt l'anomenarem **punt focal** o **focus** del mirall.<sup><a href="#fn3" id="ref3">3</a></sup>. A la figura anterior  podem observar com un feix de raigs paral·lels incideix sobre un mirall esfèric còncau i en reflectir-se passen tots pel focus.

El focus, F, és una característica del mirall i està relacionat amb el **centre de curvatura**, C, del mirall. La distància entre el centre de curvatura C i qualsevol punt del mirall val sempre el mateix i s'anomena **radi de curvatura**, R, del mirall. La distància entre el vèrtex, O, i el punt focal s'anomena distància focal, f, del mirall. La distància focal i el radi del mirall estan relacionats a través de l'expressió

$$f=\frac{R}{2}$$

S'acostuma anomenar els miralls còncaus com **miralls convergents**, ja que fan que un feix de raigs paral·lels tinguin tendència a convergir en un punt.

### Formació d'imatges en miralls còncaus

Per a estudiar la formació d'imatges utilitzarem un mètode gràfic basat en l'estudi del camí seguit pels raigs de llum. Hi ha alguns raigs pels quals nosaltres sabrem la seva trajectòria i que anomenarem **raigs principals**. A partir de la marxa d'aquests raigs podrem saber quina és la posició i mida de la imatge.

Introduirem el mètode per a un mirall còncau amb l'objecte a una distància del mirall més gran que el radi de curvatura, R, del mirall. Per a indicar l'objecte farem servir una fletxa amb la seva cua sobre l'eix òptic i la seva punta a una altura igual a la de l'objecte. Tractarem de trobar la posició i la mida de la imatge i, per fer això, només necessitem trobar la imatge de la punta de la fletxa. Per a trobar la imatge farem servir els raigs principals que es podem veure a la figura següent.

<figure>
  <img src="img/mirall_concau_1.svg" alt="" width="80%">
  <figcaption><strong>Marxa de raigs per a un objecte ubicat a una distància més gran que el radi de curvatura del mirall còncau.</strong> </figcaption>
</figure>

La regla per a la construcció de la marxa de raig amb els raigs principals són<sup><a href="#fn4" id="ref4">4</a></sup>:

1. El raig que va paral·lel a l'eix òptic es reflecteix passant pel focus del mirall (raig blau). Això ho sabem de la definició de focus.

2. El raig que passa pel focus es reflecteix sortint paral·lel a l'eix òptic (raig verd). També és per la definició de focus i per la reversibilitat del camí òptic.

3. El raig que passa pel centre de curvatura es reflecteix tornant pel mateix camí (raig vermell), ja que incideix sobre la superfície del mirall en direcció normal (perpendicular a la superfície).

4. El raig que incideix en el vèrtex del mirall es reflecteix amb el mateix angle respecte de l'eix òptic (raig magenta), de manera que l'eix òptic és la bisectriu entre els raigs incident i reflectit.

5. La imatge es forma on es troben els raigs reflectits<sup><a href="#fn5" id="ref5">5</a></sup>. Si posem una pantalla en aquell lloc veurem que es forma sobre ella la imatge, per aquest motiu diem que la imatge és **real**, també veiem que la imatge està **invertida** i que té una mida **menor**.

6. Per a determinar la distància entre el mirall i la imatge hem de mesurar amb un regle i fer servir el factor d'escala utilitzat, el mateix per a determinar l'altura de la imatge. No és necessari fer servir la mateixa escala per a la direcció horitzontal i vertical.

Veurem ara, seguint la mateixa metodologia constructiva com és la imatge quan l'objecte es troba entre el centre de curvatura i el focus. A la figura inferior es pot veure la marxa de raigs. Podem observar que els raigs convergeixen en un punt per a formar la imatge, per aquest motiu la imatge és real. També veiem que és invertida i major.

<figure>
  <img src="img/mirall_concau_2.svg" alt="" width="80%">
  <figcaption><strong>Formació de la imatge quan l'objecte es troba a una distància entre la focal i el radi del mirall. Les seves característiques són: Real, invertida i major.</strong> </figcaption>
</figure>

Si l'objecte es troba a una distància menor que la distància focal trobem que els raigs reflectits no convergeixen enlloc, sinó que, al contrari divergeixen al sortir del mirall. Per aquest motiu no podem trobar la imatge posant una pantalla perquè hi ha una posició on es pugui formar. Però com és que veiem la imatge si no es forma enlloc? En realitat nosaltres veiem la imatge perquè els nostres ulls formen una imatge real sobre la retina dels nostres ulls que juga el paper de pantalla. Això és possible perquè l'ull forma un sistema convergent que acaba tancant els raigs fins que convergeixen sobre la retina (estudiarem l'ull humà amb cert detall més endavant). I on veurem la imatge? Doncs, la veurem com si vingués de una posició que es troba darrere del mirall, com si estigués en la posició on convergeixen els raig reflectits si els prolonguem cap enrere. Direm en aquest cas que la imatge és virtual, dreta i major.

<figure>
  <img src="img/mirall_concau_3.svg" alt="" width="90%">
  <figcaption>Marxa de raigs quan l'objecte es troba a una distància és menor a la distància focal. La imatge és <strong>virtual</strong>, <strong>dreta</strong> i <strong>major</strong>.  </figcaption>
</figure>

### Formació d'imatges en miralls convexos

En el cas dels miralls convexos, els raigs que hi arriben paral·lels a a l'eix òptic no convergeixen sinó al contrari, divergeixen i, per aquest motiu, aquests miralls també es coneixem com **miralls divergents**. El focus d'aquests miralls es troba on semblen provenir els raigs paral·lels un cop s'han reflectit al mirall, com es pot observar a la figura inferior.

<figure>
  <img src="img/focus_mirall_convex.svg" alt="" width="90%">
  <figcaption><strong>Definició de focus per a un mirall convex. El focus és el punt d'on semblen procedir un feix de raigs paral·lels després de reflectir-s'hi.</strong></figcaption>
</figure>

Quant a la formació de la imatge d'un objecte veurem que sempre té les mateixes característiques. A la figura següent es poden veure els raigs principals provinents de l'extrem d'un objecte ubicat a una distància més gran que la distància focal. El raig que va paral·lel a l'eix òptic surt reflectit en una direcció, la prolongació de la qual passa pel focus (raig blau). El raig que va en direcció del focus (raig verd), es reflecteix paral·lel a l'eix òptic. El raig que va en direcció del radi de curvatura (raig vermell), surt reflectit en la mateixa direcció, ja que incideix perpendicular a la superfície del mirall. Per últim el raig que incideix en el vèrtex, O, del mirall surt amb el mateix angle respecte a l'eix òptic, ja que l'eix òptic és normal a la superfície en aquell punt. La imatge es forma en el punt on convergeixen la prolongació dels raigs reflectits, darrere el mirall, on la llum no hi arriba. Direm que la imatge és virtual per aquest motiu. També observem que la imatge està dreta i té una mira menor a la del objecte.

<figure>
  <img src="img/mirall_convex_1.svg" alt="" width="90%">
  <figcaption><strong>Mirall convex. Marxa de raigs per a un objecte ubicat a una distància més gran que la distància focal. La imatge formada és virtual, dreta i més petita que l'objecte.</strong></figcaption>
</figure>

El cas on l'objecte es troba a una distància més petita a la distància focal és molt semblant i la marxa de raigs es construeix de la mateixa manera. Podem observar que la imatge té les mateixes característiques (virtual, dreta i menor), però que a mesura que l'objecte s'apropa al mirall la imatge es va fent més gran (Figura següent). 

<figure>
  <img src="img/mirall_convex_2.svg" alt="" width="90%">
  <figcaption><strong>Mirall convex. Marxa de raigs per a un objecte ubicat a una distància més petita que la distància focal. La imatge formada és virtual, dreta i més petita que l'objecte.</strong></figcaption>
</figure>



## Augment lateral

L'augment lateral, $$m$$, és la relació que hi ha entre la grandària de la imatge, $$y'$$, i la de l'objecte, $$y$$,

$$
\begin{equation}\label{eq:augment}
m=\frac{y'}{y}
\end{equation}
$$

El valor de $$y'$$ serà positiu quan la imatge estigui dreta i negatiu quan la imatge estigui invertida. Per altra banda si la imatge és més gran que l'objecte tindrem que $$\lvert y'\rvert > y$$, i quan la imatge sigui més petita que l'objecte tindrem que $$\lvert y' \rvert <y$$.

## Les matemàtiques dels miralls

Fins ara havíem fet servir la construcció gràfica per a trobar la posició on es formarà la imatge i la seva mida. Ara veurem que també es poden obtenir d'una manera analítica fent servir la següent fórmula:

$$
\begin{equation}\label{eq:formula_miralls}
\frac{1}{s}+\frac{1}{s'}=\frac{1}{f}
\end{equation}
$$

on $$s$$ és la distància objecte, $$s'$$ és la distància imatge i $$f$$ és la distància focal. D'aquesta manera, si coneixem la posició de l'objecte i la distància focal del mirall, podem trobar la posició de la imatge. La diferència entre miralls còncaus i convexos radica en el signe de la distància focal, mentre que pel mirall còncau la distància focal és positiva, pels miralls convexos la distància focal resulta negativa. De fet, tot el que estigui ubicat a la dreta del mirall tindrà posició negativa, així, si obtenim un valor de $$s'$$ negatiu sabrem que la imatge estarà ubicada a la dreta del mirall on la llum no hi arriba i que la imatge és virtual.

Si observem la figura de sota, observem que els dos triangles que queden definits són semblants, ja que els angles d'incidència i reflexió són congruents $$(\theta=\theta')$$ degut a la llei de a reflexió i a que l'eix òptic és normal a la superfície en el punt O.

<figure>
  <img src="img/mirall_triang.svg" alt="" width="90%">
  <figcaption>Degut a que l'angle de reflexió és igual a l'angle d'incidència, tenim que els dos triangles són semblants i, per tant, podem deduir que $$y/s=y'/s'$$.</figcaption>
</figure>

Degut a que els triangles són semblants tenim que es compleix les següent relació:

$$\frac{y}{s}=-\frac{y'}{s'}$$

on el signe negatiu apareix degut a que $$y'$$ resulta negativa per estar la imatge invertida i la resta de quantitats són positives. Per a poder igualar ambdós costats de l'equació, hem de posar el signe negatiu al membra de la dreta. Aquesta relació ens porta a una altra manera de calcular l'augment lateral si reconsiderem l'expressió $$\eqref{eq:augment}$$:

$$
\begin{equation}\label{eq:augment2}
m=\frac{y'}{y}=-\frac{s'}{s}
\end{equation}
$$

Les equacions $$\eqref{eq:formula_miralls}$$ i $$\eqref{eq:augment2}$$ ens permeten obtenir de manera analítica la posició i altura de la imatge a partir de la posició i altura de l'objecte per a un mirall de distància focal coneguda. D'aquesta manera hem obtingut un mètode alternatiu al mètode gràfic per a obtenir la imatge donada per un mirall. <sup><a href="#fn6" id="ref6">6</a></sup>


## Lents

Les lents són sistemes òptics formades per dues superfícies, una de les quals al menys ha de ser corba. Les dues superfícies refracten els raig de llum que hi incideixen, de manera que la trajectòria dels raigs canvia i formen una imatge que depèn del tipus de lent i de la posició relativa de l'objecte respecte de la lent. Per a estudiar el camí que segueix la llum en travessar les superfícies de la lent s'ha de fer servir la llei de Snell.

A la figura següent es pot veure diferents tipus de lents. Les lents que són més gruixudes al centre són del tipus convergent i les que són més primes a la part central són lents divergents.

<figure>
  <img src="img/lents.svg" alt="" width="100%">
  <figcaption><strong>Diferents tipus de lents. Les lents de la primera fila s'anomenen lents convergent i la fila de sota s'anomenen lents divergents.</strong></figcaption>
</figure>

### Focus d'una lent convergent

De manera anàloga a com hem definit el focus d'un mirall, definirem el focus d'una lent, amb la diferència que en les lents la llum travessa les seves superfícies. En el cas d'una lent convergent, els raigs que hi arriben paral·lels a l'eix òptic, després de travessar la lent, convergeixen tots en un punt al que anomenarem focus principal o focus imatge de la lent (Figura següent). En la pràctica podem trobar el focus posant la lent als raigs del Sol i cercant amb un paper el punt on tots el raigs convergeixen, això és possible perquè els raigs del Sol ens hi arriben paral·lels degut a la gran distància que tenim del Sol.

<figure>
  <img src="img/lent_convergent_focus_i.svg" alt="" width="90%">
  <figcaption>Definició de focus imatge per a una lent convergent.</figcaption>
</figure>

De la mateixa manera, definirem focus objecte al punt per al qual si posem una font puntual emissora de llum en aquella posició, els raigs que sortirien de la lent anirien paral·lels a l'eix òptic.

<figure>
  <img src="img/lent_convergent_focus_o.svg" alt="" width="90%">
  <figcaption>Definició de focus objecte per a una lent convergent.</figcaption>
</figure>

### Potència d'una lent

La distància que hi ha entre el centre de la lent i el focus s'anomena distància focal de la lent. Podem dir que quant més petita és la distància focal més potent és la lent, ja que té un poder refractiu major al desviar més la trajectòria dels raigs. Definirem com a potència d'una lent a la inversa de la seva distància focal, $$f$$, mesurada en metres,

$$P=\frac{1}{f}$$
 

Calculada d'aquesta manera la potència té unitats de **diòptries** (D)<sup><a href="#fn7" id="ref7">7</a></sup>. D'aquesta manera, una lent que té una distància focal de 50 cm (0,5 m) tindrà una potència $$P=1/0,5=2\mathrm{D}$$. 

### Formació d'imatges per una lent convergent

Per a trobar la imatge formada per una lent convergent farem servir també els raigs principals. Els raigs principals són tres:

* El **raig paral·lel** a l'eix òptic es desvia passant pel focus imatge F' (raig blau a la figura inferior).

* El **raig central**, el que passa pel centre O de la lent (raig magenta a la figura, no es desvia (en realitat pateix una desviació mínima quan es tracta de lents primes degut a la refracció en les dues cares de la lent). 

* El **raig focal**, que passa pel focus objecte F (raig verd la figura, es desvia sortint paral·lel a l'eix òptic.

La imatge es forma en el punt on es creuen els tres raigs principals. 

Les característiques de la imatge dependrà no només del tipus de lent que fem servir, sinó que també dependrà de la ubicació de l'objecte respecte del centre de la lent O.

Per a començar estudiarem el cas d'un objecte ubicat a una distància més gran que el doble de la distància focal, podem veure la formació de la imatge a la figura inferior. En aquest cas la imatge resulta real<sup><a href="#fn8" id="ref8">8</a></sup>, invertida i menor que l'objecte. També podem veure que la imatge es forma a un distància més propera a la lent que la distància de l'objecte.

La reversibilitat del camí òptic fa que si posem l'objecte en la posició on es troba la imatge, veurem que la imatge passa a formar-se en la posició on abans estava l'objecte. Així doncs, podem deduir que si l'objecte es troba a una distància més gran que la distància focal però més petita que dues vegades la distància focal, la imatge també serà real, invertida però, en aquest cas, serà més gran que l'objecte.

<figure>
  <img src="img/lent_convergent_1.svg" alt="" width="90%">
  <figcaption>Marxa de raigs per a un objecte a una distància més gran que dues vegades la distància focal. Les característiques de la imatge són: real, invertida i més petita que l'objecte.</figcaption>
</figure>

Per a confirmar el que acabem de deduir a partir de la reversibilitat del camí òptic, traçarem la marxa de raigs ubicant l'objecte a una distància propera al focus encara que més gran. El resultat es pot veure a la figura inferior.

<figure>
  <img src="img/lent_convergent_2.svg" alt="" width="90%">
  <figcaption>Marxa de raigs per a un objecte a una distància entre una i dues distàncies focals de la lent. Les característiques de la imatge són: real, invertida i més gran que l'objecte.</figcaption>
</figure>

Un cas diferent el tenim quan l'objecte es troba a una distància més petita que la focal respecte de la lent. Podem veure a la figura inferior la marxa dels raigs principals. En aquest cas els raigs refractats surten divergint de la lent, raó per la qual no es poden trobar per a formar una imatge. La imatge la podem trobar a partir de la prolongació enrere dels raigs refractats. El punt on convergeixen els raigs és el punt on es formarà una imatge virtual, ja que la llum no hi arriba allí però, si posem l'ull a la part dreta de la lent veurem la imatge formada en aquella posició degut a que el nostre cervell està condicionat a pensar que la llum es propaga en línia recta i això ens porta a la posició de la imatge.<sup><a href="#fn9" id="ref9">9</a></sup>

<figure>
  <img src="img/lent_convergent_3.svg" alt="" width="90%">
  <figcaption>Marxa de raigs per a un objecte a una distància més petita que la focal. Les característiques de la imatge són: virtual, dreta i més gran que l'objecte. Aquest és el cas d'una lupa.</figcaption>
</figure>

### Focus d'una lent divergent

Les lents divergents tenen el comportament contrari a les lents convergents. En aquest cas els raigs que entren a la lent paral·lels surten d'ella obrint-se de tal manera que si prolonguem els raigs refractats enrere trobem que tots ells es troben un un punt al que anomenarem focus imatge F' com es veu a la figura inferior. 
  
<figure>
  <img src="img/lent_divergent_focus_i.svg" alt="" width="90%">
  <figcaption>Focus principal o focus imatge d'una lent divergent.</figcaption>
</figure>

Si tenim en compte la reversibilitat del camí òptic i invertim el cas anterior podem definir el focus objecte. es tracta del punt on hauríem de dirigir un feix de llum per tal de que, quan surtin de la lent ho fessin paral·lels a l'eix òptic, com es veu a la figura següent.

<figure>
  <img src="img/lent_divergent_focus_o.svg" alt="" width="90%">
  <figcaption>Focus objecte d'una lent divergent.</figcaption>
</figure>

### Formació d'imatges per una lent divergent

Per a estudiar la formació d'imatges per una lent divergent hem de tenir en compte que els focus imatge i objecte estan intercanviats. Estudiarem primer la formació de la imatge per a un objecte a una distància de la lent més gran que la distància focal (Figura inferior). Traçarem els raigs principals seguint els criteris ja establers:

1. El raig paral·lel a l'eix òptic (blau), es desvia obrint-se i la seva prolongació enrere ha de passar pel focus imatge F'.

2. El raig que passa pel centre O de la lent (magenta) no té desviació.

3. El raig que parteix en direcció al focus objecte (verd), surt paral·lel a l'eix òptic.

4. La imatge es troba en el entrecreuament de les prolongacions enrere dels raigs que han travessat les lents. La imatge que es forma és virtual, dreta i menor com es veu a la figura següent.

<figure>
  <img src="img/lent_divergent_1.svg" alt="" width="90%">
  <figcaption>Marxa de raigs per a un objecte a una distància més gran que la focal. Les característiques de la imatge són: virtual, dreta i més petita que l'objecte.</figcaption>
</figure>

Quan l'objecte es troba a una distància més petita que la focal, com és el cas de la figura inferior, la imatge que es forma té les mateixes característiques que en el cas anterior amb la diferència que, quant més a prop de la lent estigui l'objecte, més gran es veurà la imatge. La construcció de la marxa de raigs és anàloga al cas anterior. 

<figure>
  <img src="img/lent_divergent_2.svg" alt="" width="90%">
  <figcaption>Marxa de raigs per a un objecte a una distància més petita que la focal. Les característiques de la imatge no canvien, continua sent virtual, dreta i més petita que l'objecte.</figcaption>
</figure>

### Les equacions de les lents

Per a les lents tenim que són vàlides les equacions que hem trobat pels miralls, per tant, pel que fa a les posicions tenim <sup><a href="#fn10" id="ref10">10</a></sup>:

$$\frac{1}{s}+\frac{1}{s'}=\frac{1}{f}$$
 

Per l'augment lateral:

$$m=\frac{y'}{y}=-\frac{s'}{s}$$
 

Resulta important detenir-se en la convenció de signes necessària per a que les relacions anteriors siguin vàlides. Definirem com **espai objecte** l'espai que es troba a l'esquerra de la lent i **espai imatge** l'espai que es troba a la dreta de la lent. Tot el que pertany a l'objecte (posició $$s$$ i distància focal objecte $$f$$) serà positiva si està dintre de l'espai objecte i negativa en cas que estigui a l'espai imatge. De manera anàloga, tot el que pertany a la imatge (posició $$s'$$ i distància focal imatge $$f'$$) serà positiva quan es està dintre de l'espai imatge i negativa en cas contrari. En canvi, pel que fa a l'eix vertical, tot el que estigui per sobre de l'eix òptic el considerarem positiu i si està per dessota el considerarem negatiu. 

Amb la convenció adoptada les lents convergents tenen distància focal positiva (també són conegudes com a lents positives) i les lents divergents tenen distància focal negativa (lents negatives). També passa que les imatges reals tenen una posició positiva i les virtuals tenen una posició negativa. Les imatges que estan dretes tindran una altura positiva i les que estan invertides tindran una altura negativa.

## La visió i l'ull

L'ull és un dels aparells més meravellosos que es poden trobar a la natura, han estat necessaris milers de milions d'anys d'evolució per a que la natura hagi pogut arribar a un grau de sofisticació tal. Aquí ens interessarem per l'ull com a instrument òptic i deixarem de banda altres aspectes de la visió com ser els biològics o psicològics. Com a instrument òptic podem dir que l'ull és un sistema convergent que acaba formant una imatge real sobre una pantalla que tenim al fons de l'ull anomenada **retina**. La imatge que es forma a la retina és una imatge invertida, però es el nostre cervell qui s'encarrega de que la veiéssim de manera dreta. 

Per arribar a la retina la llum ha de travessar una sèrie de medis refringents que s'encarreguen de desviar els raigs de llum i formar la imatge sobre la retina. Les diferents parts de l'ull humà es poden observar a la figura inferior. El major desviament es produeix quan la llum passa de l'aire a la còrnia, ja que aquí és on tenim el canvi més brusc de índex de refracció. Després la llum travessa l'humor aquós, passa per la pupil·la (furat rodejat per l'iris i que canvia de diàmetre segons la necessitat de l'ull de rebre més o menys llum). Els següent que fa la llum és travessar el cristal·lí, una lent que controlada pels músculs ciliars i que pot canviar el seu gruix i, amb això, la seva distància focal. El cristal·lí és l'encarregat d'enfocar “acomodant” l'ull per veure els objectes que es troben a diferents distàncies. 

<figure>
  <img src="img/ull.svg" alt="" width="100%">
  <figcaption>Ull humà. La llum travessa diferents capes transparents abans d'arribar a formar una imatge real sobre la retina. </figcaption>
</figure>

A continuació la llum travessa l'humor vitri que, com l'humor aquós, és un líquid transparent encarregat de mantenir el globus ocular “inflat” i que transporta els nutrients i les deixalles de les cel·les de les parts transparents de l'ull El fet de que els medis refractius de l'ull hagin de ser transparents impedeix que tinguin capil·lars sanguins per a proveir els nutrients a les cel·les, la qual cosa fa que tingui una forma alternativa de fer arribar els aliments i de desfer-se de les deixalles de les cel·les d'aquests medis.. La imatge, finalment, es forma a la retina on la llum és captada unes cel·les sensibles a la llum anomenades bastons i cons. Els cons són sensibles als colors i n'hi ha de tres tipus, uns especialitzats en el color blau, altres en el vermell i altres en el verd. Es troben fonamentalment en una regió d'aproximadament 1\,\mathrm{mm^{2}}
  anomenada fòvea ubicada on està l'eix òptic de l'ull (allà on va a parar la imatge quan fixem la mirada) i és la regió d'alta resolució de l'ull on podem apreciar detalls fins de la imatge. Més enllà de la fòvea s'ubiquen els cons que no poden percebre els colors i són les que es fan servir amb poca llum (visió nocturna) i ens donen la visió perifèrica. Podem veure a la figura una gràfica amb la densitat de bastons i cons de la retina. 
  
<figure>
  <img src="img/densitat_receptors.svg" alt="" width="70%">
  <figcaption>Densitat de receptors de la retina. Els cons s'ubiquen fonamentalment a la fòvea i són els responsables de la visió allà on enfoquem la mirada i de la visió dels colors. Els bastons no poden distingir els colors i són responsables de la visió nocturna i perifèrica. </figcaption>
</figure>

Al punt cec no hi ha bastons ni cons i és que allí és d'on surt el nervi òptic portant tota la informació de les cel·les sensores cap al cervell.

### Defectes de la visió

No sempre l'ull produeix una bona imatge sobre la retina i moltes vegades hem de recórrer a l'oftalmòleg per tal de corregir alguns defectes o poder veure bé. Un dels problemes més usuals de la visió és la miopia (Figura següent), que es produeix quan som incapaços de enfocar objectes llunyans. En aquest cas, la imatge es forma abans de la retina. La correcció d'aquest defecte s'aconsegueix amb una lent divergent, de manera que fa disminuir la potència del sistema refractiu de l'ull obrint els raigs per a que acabin formant la imatge a la retina.

<figure>
  <img src="img/ull_miop.svg" alt="" width="70%">
  <figcaption>Miopia. (a) La imatge d'objectes llunyans es forma abans de la retina. (b) La correcció es fa amb lents divergents que obren els raigs. </figcaption>
</figure>

Una altre problema comú és el contrari a la miopia anomenat hipermetropia, en aquest cas la imatge d'objectes propers no es forma a la retina, sinó que es forma darrera la retina i la manera de corregir aquest problema és amb lents convergents que augmentes la potència refractiva de l'ull fent que els raigs es tanquin més com es veu a la figura inferior.

<figure>
  <img src="img/ull_hiper.svg" alt="" width="70%">
  <figcaption>Hipermetropia. (a) La imatge d'objectes propers es forma després de la retina. (b) La correcció es fa amb lents convergents que tanquen els raigs. </figcaption>
</figure>

Un tercer defecte molt comú de la visió és l'astigmatisme, aquest defecte es deu a que l'ull no té una simetria axial i desvia els raigs de llum més en una direcció que en altra, per tant quan enfoquem en un eix no podem veure en focus en un altre. La manera de corregir aquest defecte és amb lents cilíndriques o esferotòriques quan hi ha també miopia o hipermetropia associada. Una altra manera de corregir aquests defectes és amb cirurgia refractiva, que consisteix en la utilització de làser per a produir una modificació de la curvatura de la còrnia.

<figure>
  <img src="img/cercle_astigmatic.png" alt="" width="70%">
  <figcaption>Cercle astigmàtic. Quan tenim astigmatisme es resulta impossible enfocar totes les ratlles del cercle alhora.</figcaption>
</figure>

Hi ha defectes de la visió que esdevenen amb l'edat, com ser la presbícia, també coneguda com a vista cansada, i que apareix després dels 40-45 anys d'edat. Aquest problema, del que gairebé ningú pot escapar, consisteix en un enduriment del cristal·lí que ja no pot acomodar-se per fixar la vista a diferents distància i necessita ajuda de lents per a veure de prop. Una altra malaltia del cristal·lí són les cataractes, que consisteix en la opacitat del cristal·lí que no deixa passar la llum per a formar la imatge sobre la retina. Aquesta malaltia és més comú en gent gran. Per a corregir-la és necessari la cirurgia on es reemplaça el cristal·lí per una lent intraocular de distància focal fixa.

El glaucoma és una altra malaltia de l'ull que es produeix al nervi òptic que es produeix, generalment, degut a una pressió intraocular és massa alta. El glaucoma sense tractar pot conduir a un dany irreversible del disc òptic de la retina amb una conseqüent pèrdua de camp de visió, la qual cosa pot convertir-se en una ceguera parcial o total.

#### Notes
<sup id="fn1">1. Aquests fenòmens els estudiarem al segon curs de Física. <a href="#ref1" title="Tornar al text.">↩</a></sup>

<sup id="fn2">2. Anomenem medi homogeni a un medi que té les mateixes propietats físiques en tots els seus punts. Per exemple, l'aigua a temperatura ambient és un medi homogeni, mentre que l'aigua bullint no ho és, ja que hi ha bombolles que tenen propietats físiques diferents a les de l'aigua líquida.<a href="#ref2" title="Tornar al text.">↩</a></sup>

<sup id="fn3">3. En realitat, per a que hi hagi un punt focal ben definit la superfície del mirall ha de ser parabòlica. Fer miralls parabòlics és molt més complicat que fer miralls esfèrics, per això s'utilitzen miralls esfèrics. Els errors que es cometen per utilitzar superfícies esfèriques son petits si els raigs viatgen en direccions que no s'aparten massa de l'eix òptic (raigs paraxials). Nosaltres sempre treballarem fent servir l'aproximació paraxial.<a href="#ref3" title="Tornar al text.">↩</a></sup>

<sup id="fn4">4.Per a la construcció de la imatge estudiarem el comportament de raigs que surten de la punta de la fletxa. Si l'objecte no emet llum, la llum serà la que reflecteix a partir d'una il·luminació externa. Els objectes reflecteixen llum en totes direccions, de tots aquests raig estudiarem el camí dels que ens interessen.<a href="#ref4" title="Tornar al text.">↩</a></sup>

<sup id="fn5">5. Observeu que encara que el mirall és esfèric, tracem una línia recta i fem reflectir els raigs sobre aquesta recta, això ho fem per a què la construcció pugui sortir bé quan fem servir l'aproximació paraxial (raigs propers a l'eix òptic).<a href="#ref5" title="Tornar al text.">↩</a></sup>

<sup id="fn6">6. La relació [eq:augment2] que ha estat deduïda utilitzant un mirall còncau també és vàlida per a miralls convexos i la seva deducció és anàloga a la que hem fet aquí.<a href="#ref6" title="Tornar al text.">↩</a></sup>

<sup id="fn7">7. És important no oblidar que per calcular la potència en diòptries és obligatori que la distància focal estigui expressada en metres.<a href="#ref7" title="Tornar al text.">↩</a></sup>

<sup id="fn8">8. Recordem que per a formar una imatge real és necessari que els raigs es tornin a trobar en un punt, ja que són portadors de la informació d'un punt de l'objecte. Si posem una pantalla en la posició on es forma la imatge podrem observar la imatge projectada sobre ella.<a href="#ref8" title="Tornar al text.">↩</a></sup>

<sup id="fn9">9. Nosaltres podem veure les imatges virtuals perquè el nostres ulls acaben formant una imatge real sobre la retina. Els raigs que ingresen al nostre ull com raigs divergents acaben convergint a la nostra retina degut a a que l'ull és un sistema òptic convergent. <a href="#ref9" title="Tornar al text.">↩</a></sup>

<sup id="fn10">10. La deducció de les relacions següents es pot fer de manera anàloga a la que vam fer servir pels miralls, tot es basa en les relacions de triangles semblants, en aquest cas es fa servir el raig que passa pel centre de la lent per a trobar els angles congruents.<a href="#ref10" title="Tornar al text.">↩</a></sup>
