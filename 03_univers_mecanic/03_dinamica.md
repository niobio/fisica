
# L'univers mecànic

Al segle XIX els científics pensaven que l'univers funcionava com un rellotge, que tot estava determinat per les condicions inicials de moviment i que, si poguéssim conèixer la posició i velocitat de cada partícula de l'univers ens seria possible conèixer de manera completa el futur. L'única limitació estava en la manca de coneixement i la potència de càlcul necessària per tan magnífica empresa. Aquesta visió de l'univers es coneix com determinisme i uns dels seus grans postulants va ser el científic francès Pierre-Simon Laplace (veure el [dimoni de Laplace](https://ca.wikipedia.org/wiki/Dimoni_de_Laplace)). No és casual que els científics tinguessin aquesta visió de l'univers, l'èxit collit per la mecànica de Newton (també coneguda ara com mecànica clàssica) en predir el moviment planetari i el moviment en general va ser incontestable. 

Ara sabem que aquesta visió no és correcta, que la mecànica quàntica, que és la teoria que descriu la realitat d'una manera més acurada, ens assegura que la realitat no és determinista, que l'atzar juga un paper important. És a nivell microscòpic on es posa de manifest d'una manera més dramàtica aquest comportament, no obstant això, a escala macroscòpica la visió mecanicista de Newton continua essent vàlida, fins al punt que les trajectòries dels planetes i dels viatges espacials es calculen utilitzant la mecànica de Newton.

En aquesta unitat ens endinsarem en l'estudi de les causes del moviment, que són les interaccions entre els cossos i els agents amb els que representem aquestes interaccions en la mecànica clàssica, que són les forces.

## Les lleis de Newton

L'any 1687 [Isaac Newton](https://ca.wikipedia.org/wiki/Isaac_Newton) publica el llibre *Philosophiae Naturalis Principia Mathematica*, el llibre més important de la història de la física. En aquest llibre enuncia tres lleis que serveixen de principis per a desenvolupar tot el que avui coneixem com mecànica clàssica. 

### Primera llei de Newton: principi d'inèrcia

**Si un cos no interactua amb cap altre el seu estat serà el repòs o, si ja s'estava movent, el moviment rectilini uniforme.**

La forma que tenim per a modelitzar les interaccions entre cossos és a través d'una magnitud anomenada **força**. El concepte de força ens resulta intuïtiu, ja que alguna vegada hem rebut alguna empenta, la qual cosa ens acaba canviant el nostre estat de moviment.

El principi d'inèrcia es pot generalitzar pel cas en que el cos interactua amb altres, però la suma de totes les forces aplicades al cos resulta nul·la. En aquest cas tenim la mateixa situació que si no hi hagués cap força aplicada. 

Un exemple on podem visualitzar aquest principi podria ser el cas d'una persona que està a sobre d'un autobús en repòs i, de sobte, l'autobús comença a moure's. Aquesta situació, que la podem observar a la figura inferior, segur que l'hem viscut alguna vegada. Si l'autobús arrenca des del repòs i sobre nosaltres no hi ha cap força aplicada que ens faci moure amb l'autobús, nosaltres ens quedarem en repòs mentre l'autobús avança, com a conseqüència ens anirem cap el fons de l'autobús i probablement acabarem caient.

<p>
<figure>
  <img src="img/inercia2.jpg" alt="" width="70%">
  <figcaption> <strong>Aplicació del principi d'inèrcia. El bus arrenca i, si no ens agafem per tenir una força que ens faci moure junt amb l'autobús, ens quedarem a la nostra posició original (repòs) i acabarem caient.</strong> </figcaption>
</figure>
</p>

Una altra situació d'aplicació resulta quan l'autobús viatja a velocitat constant i de sobte frena, en aquest cas nosaltres continuarem viatjant a velocitat constant i ens anirem cap a la part davantera de l'autobús si no ens agafem per frenar-nos, com es pot observar a la figura inferior.

<p>
<figure>
  <img src="img/inercia1.jpg" alt="" width="70%">
  <figcaption> <strong>Aplicació del principi d'inèrcia. El bus frena i, si no ens agafem per tenir una força que ens faci frenar a nosaltres també, continuarem amb velocitat constant i acabarem esclafats contra el vidre del davant de l'autobús.</strong> </figcaption>
</figure>
</p>

### Segona llei de Newton: principi fonamental de la dinàmica

La segona llei de Newton estableix una relació de causa i efecte entre les interaccions i la generació del moviment i diu que **l'acceleració que experimenta un cos és directament proporcional a la força neta aplicada**. Aquesta llei es pot escriure amb l'expressió matemàtica:

$$\vec{F}=m\vec{a}$$

on la constant de proporcionalitat entre la força i l'acceleració és la massa del cos. És important destacar que la força que apareix a la 2a llei de Newton és la força resultant de la suma de totes les forces aplicades sobre el cos, a la que anomenarem força neta.

Podem veure d'aquesta llei que una mateixa força pot produir diferents acceleracions si s'apliquen a cossos de diferents masses. Un cos molt massiu tindrà una acceleració petita, mentre que un cos amb poca massa s'accelerarà molt. Podem dir que la massa és una mesura del que costa canviar l'estat de moviment d'un cos, és a dir, de la inèrcia del cos. La massa és una propietat intrínseca del cos, es dir, només depèn del cos i no d'agents externs. 

En el Sistema Internacional d'unitats, la unitat de massa és el kilogram (kg) i és una unitat fonamental. Tenint en compte que l'acceleració es mesura en $\mathrm{m/s^{2}}$, la unitat de força ha de ser $\mathrm{kg.m/s^{2}}$. Per ser la força una magnitud prou important aquesta unitat porta el nom de newton i es designa amb la lletra N.

Per calcular la força neta aplicada sobre un cos hem de fer la suma vectorial de totes les forces aplicades.

### Tercera llei de Newton: principi d'acció i reacció

La tercera llei de Newton ens diu que sempre que un cos exerceix una força sobre un altre, aquest segon cos exerceix una força igual i de sentit contrari sobre el primer.

Amb aquest principi queda establert que totes les forces venen per parelles, per això anomenem interaccions a l'aplicació de forces sobre algun cos, perquè la força ha d'estar produïda per algun agent extern que alhora rep una força contraria, es com dir que no podem tocar sense ser tocats.

Una conseqüència important d'aquest principi és que el parell de forces corresponents a la interacció sempre estan aplicades sobre objectes diferents, es a dir, si dos objectes interactuen un objecte aplica una força sobr el segon i el segon exerceix una igual i contraria en sentit sobre el primer, aquestes **dues forces que formen un parell d'interacció sempre estan aplicades sobre cossos diferents**. A la figura inferior es poden veure dues pilotes que xoquen i es fan forces oposades com a resultat de la interacció, però ambdues forces estan aplicades a cossos diferents. A la figura inferior es poden veure dues pilotes de bàsquet que xoquen i canvien les seves trajectòries com a resultat de les forces d'interacció. Veiem com les dues forces estan aplicades sobre cossos diferents.
<p>
<figure>
  <img src="img/accio-reaccio.svg" alt="" width="50%">
  <figcaption> <strong>Principi d'acció i reacció. Quan dos cossos interactuen exerceixen forces l'un sobre l'altre i aquestes forces sempre són d'igual intensitat i sentit oposat.</strong> </figcaption>
</figure>
</p>

## La força pes
Si sostenim un objecte amb la mà sentim una força que el cos ens fa sobre la mà i que apunta cap avall, podríem dir que estem “sentint el seu pes”, però què es en realitat aquesta força? qui l'origina? A la natura hi ha només 4 forces fonamentals i qualsevol tipus d'interacció es pot entendre com a causada per alguna d'aquestes forces. Una d'aquestes forces fonamentals és la força gravitatòria. Es tracta d'una força que es produeix sempre entre cossos que tinguin una propietat de la natura anomenada massa. Tots els cossos materials tenen aquesta propietat, per tant entre ells hi haurà una força gravitatòria que sempre serà atractiva. De les forces fonamentals aquesta és la que coneixem millor encara que sigui la més feble de les quatre, això és perquè l'atracció gravitatòria que produeix la Terra sobre els cossos al nostre voltant resulta prou intensa per a que sigui notable. I això és possible per la immensa massa que té la Terra. De fet l'atracció gravitatòria es produeix entre tots els cossos amb massa però com la massa dels cossos normals es petita aquesta força no la notem. Intentarem ara veure com podem determinar el pes d'un objecte.

La força pes és la força d'atracció que produeix el planeta sobre tots els cossos. Per entendre aquesta força podem fer el llegendari experiment que va en Galileu enfilant-se a la torre de Pisa i deixant caure dos objectes de pesos diferents. En aquest experiment Galileu va demostrar que els dos cossos queien amb la mateixa acceleració, que prop de la superfície de la Terra és de $9,81\,\mathrm{m/s^{2}}$.

<p>
<figure>
  <img src="img/pisa.png" alt="" width="50%">
  <figcaption> <strong>Experiment de Galileo Galilei a la torre inclinada de Pisa. Tots els objectes cauen amb la mateixa acceleració si el fregament que l'aire fa sobre ells és el mateix.</strong> </figcaption>
</figure>
</p>
Aleshores, si tenim un cos d'1 kg de massa i el deixem caure, sabem que caurà a $9,81\,\mathrm{m/s^{2}}$, per tant, si fem servir la segona llei de Newton tenim 

$$P=mg=1\,\mathrm{kg\times9,81\,m/s^{2}=9,81\,N}$$

que el seu pes és de 9,81 N. Aquesta serà la força que exerceix la Terra sobre aquest cos. Quan jo l'agafo amb la mà per a que no caigui en realitat estaré aplicant sobre el cos una força igual al seu pes per a equilibrar les forces i que el objecte estigui en repòs. I la força que sento jo? Doncs, aquesta força serà la reacció que el cos fa sobre mi pel principi d'acció i reacció a la força que jo estic exercint. Per tant no és el pes del cos el que jo estic sentint (encara que tingui la mateixa intensitat) sinó la reacció a la força que jo hi faig.
<p>
<figure>
  <img src="img/ma_low.png" alt="" width="50%">
  <figcaption> <strong>La mà que sosté la pilota ha de fer una força F sobre la pilota. Alhora la pilota fa una força igual i de sentit contrari sobre la mà. El pes P és exercit per la Terra (atracció gravitatòria) i el seu parell d'interacció està aplicat a la Terra i apunta cap a la pilota (aquesta força no està representada a la figura).</strong> </figcaption>
</figure>
</p>

## Restriccions al moviment

Ja hem vist una força, la força pes, que no necessita el contacte per actuar, actua a distància. Hi ha altres forces que imposen restriccions al moviment, com poden ser les forces de contacte amb el terra o parets que imposen que la superfície de la paret o el terra no es pugui travessar. Aquestes forces són perpendiculars a les superfícies de contacte i per aquest motiu són conegudes com **forces normals** (normal és un sinònim de perpendicular) i moltes vegades les simbolitzem amb la lletra $\vec{N}$.

Estudiem un cas a mode d'exemple. Suposem que tenim un cos de massa $m=2\,\mathrm{kg}$ sobre una superfície plana horitzontal i sense fregament i apliquem una força $F=30\,\mathrm{N}$ formant un angle de $37^{\circ}$ amb la superfície horitzontal. Volem determinar la força de contacte que farà el terra sobre el cos i l'acceleració amb la que es mourà el cos.

Per tenir més clara fem un esquema de la situació a la figura inferior.

<p>
<figure>
  <img src="img/normal.svg" alt="" width="50%">
  <figcaption> <strong>Exemple d'aplicació de la força de contacte normal. El terra imposa una restricció al moviment. El moviment no pot travessar la superfície del terra.</strong> </figcaption>
</figure>
</p>

Per resoldre aquesta situació hem de seguir els següents passos:

<ol>
<li><strong>Adopció d'un sistema de referència</strong>
Com les forces i les acceleracions són magnituds vectorials, les hem de poder representar en l'espai o, com en aquest cas, en el pla. Per aquest motiu hem d'adoptar un marc de referència sobre el pla a través de l'elecció un parell d'eixos ortogonals $x-y$. L'elecció de las direccions dels eixos en principi és arbitrària però, depenent de la nostra elecció, la resolució es pot fer més senzilla o més complicada. Per aquest motiu convé triar la direcció de un dels eixos coincidint amb la direcció de l'acceleració del cos (si resulta que la podem saber a priori). En aquest cas hi ha el cos no pot baixar degut a la restricció del moviment que fa el terra. Per tant es pot moure en direcció horitzontal o, si la força $\vec{F}$ resulta prou elevada podria pujar. En tot cas sembla raonable triar els eixos en les direccions horitzontal i vertical.
</li>

<li><strong>Diagrama de forces o diagrama de cos lliure</strong>

El següent pas consisteix en aïllar el cos de tot el que l'envolta i representar totes les interaccions en les que intervé a través de forces aplicades sobre el cos. Aquest tipus de diagrama es coneix com diagrama de forces o de cos lliure. Podem veure a sota la representació del diagrama de forces pel cos en qüestió, on el cos ha estat reemplaçat per un punt.
<p>
<figure>
  <img src="img/diag_forces.svg" alt="" width="50%">
  <figcaption> <strong>Diagrama de forces o de cos lliure.</strong> </figcaption>
</figure>
</p>
</li>

<li><strong>Descompondre les forces en les direccions dels eixos ortogonals</strong>

Podem observar que la direcció de la força $\vec{F}$ no coincideix amb la direcció de cap dels eixos, per tant el que farem serà descompondre la força en les seves dues components ortogonals que coincideixen amb els eixos de coordenades. En aquest cas la força $\vec{F}$ queda expressada amb dos components:

$$F_{x}=F\cos(37^{\circ})$$

$$F_{y}=F\sin(37^{\circ})$$
</li>
<li><strong>Escriure les equacions de Newton</strong>

Un cop coneixem totes les interaccions que té el nostre sistema, podem escriure l'equació vectorial de la segona llei de Newton o les equacions escalars corresponents a cada coordenada del nostre espai vectorial. En aquest cas queda el sistema d'equacions:

$$F_{x}=ma_{x}F_{y}+N-mg=ma_{y}$$

Ara es tracta de resoldre el sistema d'equacions per trobar el valor de l'acceleració i la força de contacte amb el terra. Podem destacar que el sistema que tenim està format per dues equacions i que en principi tenim 3 incògnites $(a_{x},\,a_{y}\,\mathrm{i}\,N)$. Per a poder resoldre el sistema s'hauria d'aportar una altra equació. Aquí es planteja una qüestió interessant, que té a veure amb la restricció al moviment que imposa la superfície de contacte, es poden donar dues situacions:
<ul>
<li>Si el component vertical de la força $F$, es a dir, $F_{y}$ supera el valor del pes, $mg$, aleshores el cos s'eleva i deixa d'estar en contacte amb el terra, per tant, en aquest cas $N=0$. I aquesta és l'equació que ens faltava per resoldre el sistema.</li>

<li>Si el component vertical de la força $F$, no supera el valor del pes, aleshores el cos roman sempre en contacte amb el terra i, com no hi ha moviment en la direcció vertical, no hi ha acceleració vertical i s'ha de verificar que $a_{y}=0$. En aquest cas aquesta és l'equació addicional que necessitàvem.</li>
</ul>
</li>

<li><strong>Resoldre les equacions de Newton</strong>

Un cop definit el sistema d'equacions el que queda és resoldre'l i trobar les incògnites, i això és només àlgebra.
</li>

Per saber més sobre les forces de contacte podeu consultar [https://es.khanacademy.org/science/physics/forces-newtons-laws/normal-contact-force/v/normal-force-and-contact-force||aquí].

