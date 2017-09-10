
# Les ones i el so
Els fenòmens ondulatoris s’han demostrat com una forma fonamental del comportament de la natura. Abans es creia que la natura estava constituïda per matèria i que els fenòmens ondulatoris eren una de les possibles manifestacions de la matèria. Actualment sabem que la natura està constituïda per ones i que la matèria és una de les seves manifestacions. Podem dir que els fenòmens ondulatoris constitueixen una característica fonamental de la natura.

#### Continguts

* [Fenòmens periòdics i oscil·lacions](#1)
    * [Període i freqüència](#1.1)
* [Moviment harmònic simple (MHS)](#2)
    * [L'Equació del moviment harmònic simple](#2.1)
    * [Velocitat i acceleració](#2.2)
    * [Oscil·lació d'una molla](#2.3)


## Fenòmens periòdics i oscil·lacions <a class="anchor" id="1"></a>

Els fenòmens periòdics són aquells que es repeteixen en el temps, sempre de la mateixa manera. El moviment de la Terra al voltant del Sol o el de la Lluna al voltant de la Terra són exemples de moviments periòdics.<sup><a href="#fn1" id="ref1">1</a></sup>

Aquests tipus de moviments són molt abundants a la natura. Gràcies als fenòmens periòdics podem mesurar el temps.

Hi ha fenòmens periòdics que es poden propagar en l'espai als que anomenem ones periòdiques. Els nostres sentits més utilitzats, la vista i la oïda, estan adaptats per a detectar aquests tipus de fenòmens periòdics, la llum i el so.

Les ones no només transmeten informació sinó també energia, gairebé tota la energia que fem servir prové, directa o indirectament, del Sol en forma d'ones.

<figure>
  <img src="img/jovian-moons.png" alt="" width="70%">
  <figcaption> En la seqüència es pot observar el moviment dels satèl·lits jovians al voltant de planeta. </figcaption>
</figure>


### Període i freqüència <a class="anchor" id="1.1"></a>

En els moviments periòdics hi ha magnituds que varien amb els temps, tot i això arriba un moment en que aquestes magnituds tornen a prendre el valor inicial i, a partir d'aquell moment, repeteixen els mateixos valors. Diem aleshores que s'ha completat un cicle.

En els moviments periòdics s'anomena període, T, al temps que dura un cicle. Si mesurem el temps $\Delta t$ que tarda un sistema en fer $n$ cicles podem obtenir el valor del període com

$$T=\frac{\Delta t}{n}$$
 
Una magnitud relacionada amb el període és la freqüència, $\nu$, que correspon al nombre de cicles que es fan per unitat de temps i es mesura en $\mathrm{s^{-1}}$ o hertz (Hz): 

$$\nu=\frac{n}{\Delta t}$$

i que està relacionada amb el període a través de la relació

$$
\begin{equation}\label{eq:freq}
\nu=\frac{1}{T}
\end{equation}
$$

## Moviment harmònic simple (MHS) <a class="anchor" id="2"></a>

Entre els moviments oscil·latoris el més senzill de descriure matemàticament és el moviment harmònic simple. El físic i matemàtic francès [Jean Baptiste Fourier](http://ca.wikipedia.org/wiki/Jean_Baptiste_Joseph_Fourier) va demostrar que qualsevol moviment oscil·latori es pot descompondre en una suma de moviments harmònics simples, això fa que el seu estudi sigui fonamental per a la comprensió de qualsevol moviment oscil·latori.

Definim el MHS com la projecció d'un moviment circular uniforme sobre la recta continguda en el pla de la seva trajectòria. En la Figura [fig:mhs_def] podem veure las posicions que adopta un mòbil amb MHS per a diferents instants de temps. Si tenim en compte que cada punt està separat del següent per un interval de temps sempre igual ens podem adonar que el MHS té velocitat més gran en la part central que en els extrems.


<figure>
  <img src="img/mvhs_def.svg" width="70%">
  <figcaption> En la figura es poden veure posicions successives (A0, A1, A2, ...) d'un mòbil amb moviment circular a intervals iguals de temps . La seva projecció sobre la recta (B0, B1, B2, ...) descriu un MHS. La freqüència angular del MHS coincideix amb la velocitat angular, $\omega$, del moviment circular. </figcaption>
</figure>

### L'Equació del moviment harmònic simple <a class="anchor" id="2.1"></a>

Si tenim en compte la definició de MHS com la projecció d'un moviment circular uniforme podem deduir l'equació de moviment del MHS. Considerem un moviment circular de radi A amb velocitat angular $\omega$, l'angle girat durant un temps $t$ serà $\varphi=\omega t$ i la projecció sobre la recta serà 


$$\begin{equation}\label{eq:mhs}
x=A\sin(\varphi)=A\sin(\omega t)
\end{equation}$$



Direm que $\varphi$ és la fase del MHS i, com veiem, és una funció del temps. El moviment està limitat a moure's dintre del rang [-A, A]. La posició del mòbil es coneix com elongació i anomenarem amplitud de l'oscil·lació a la quantitat A, 
que correspon a l'elongació màxima. La freqüència angular, $\omega$, del MHS coincideix amb la velocitat angular del MCU generatriu. De l'equació $\ref{eq:mhs}$ veiem que l'elongació corresponent a l'instant inicial $(t=0)$ és igual a zero i això pot ser diferent si el moviment comença des d'una altra posició. Per aquest motiu no podem considerar l'equació $\ref{eq:mhs}$ com a una equació general per a descriure un MHS. Per a poder tenir una descripció general del MHS hem de donar a l'equació la llibertat de prende qualsevol valor inicial entre -A i A. Això ho podem aconseguir afegint una constant de fase o fase inicial, $\varphi_{0}$, a la fase $\varphi$ de l'equació $\ref{eq:mhs}$. D'aquesta manera ens queda:

$$\begin{equation}
x=A\sin(\omega t+\varphi_{0})\label{eq:eq_mov_mhs}
\end{equation}$$

on $A$, $\omega$ i $\varphi_{0}$ són paràmetres constants. Un cop determinats aquests paràmetres el MHS queda completament determinat. 

El moviment es torna a repetir quan ha passat un temps $T$ al que anomenem període de manera que s'ha de complir que $\omega T=2\pi$ expressió que relaciona el període amb la freqüència angular. Tenim, doncs

$$T=\frac{2\pi}{\omega}$$

Utilitzant la relació $\ref{eq:freq}$ també podem escriure 

$$\omega=2\pi\nu$$

### Velocitat i acceleració <a class="anchor" id="2.2"></a>

Un cop tenim l'equació de moviment $\ref{eq:eq_mov_mhs}$ que ens dóna la posició del mòbil com a funció del temps, podem deduir l'equació de la velocitat perquè sabem que la derivada de la posició ens dóna la velocitat. Si prenem la derivada de l'equació $\ref{eq:eq_mov_mhs}$ obtenim

$$v=\frac{dx}{dt}=A\omega\cos(\omega t+\varphi_{0})$$
 

Veiem que la velocitat també varia periòdicament amb el temps i prenent com a valor màxim

$$\begin{equation}\label{eq:vmax}
v_{\mathrm{max}}=A\omega
\end{equation}$$  

Si ara prenem la derivada de la velocitat obtindrem l'acceleració com a funció del temps

$$\begin{equation}\label{eq:acceleracio}
a=\frac{dv}{dt}=-A\omega^{2}\sin(\omega t+\varphi_{0})
\end{equation}$$  

En aquest cas obtenim que l'acceleració es comporta de manera contraria a l'elongació, quan l'elongació pren el seu valor màxim positiu, l'acceleració pren el valor màxim però negatiu. L'acceleració pren el seu valor màxim

$$a_{\mathrm{max}}=A\omega^{2}$$

quan $\sin(\omega t+\varphi_{0})=-1$.

### Oscil·lació d'una molla <a class="anchor" id="2.2"></a>

Si comparem l'equació $\ref{eq:acceleracio}$ amb l'equació $\ref{eq:eq_mov_mhs}$ veiem que l'acceleració està relacionada amb l'elongació a través de l'expressió <sup><a href="#fn2" id="ref2">2</a></sup>

$$\begin{equation}\label{eq:a_vs_x}
a=-\omega^{2}x
\end{equation}$$  

Si multipliquem l'acceleració per la massa del cos que es mou seguint un MHS i apliquem la segona llei de Newton obtenim la força que actua sobre la massa

$$\begin{equation}\label{eq:hooke}
F=ma=-m\omega^{2}x
\end{equation}$$  
 
Veiem de l'expressió $\ref{eq:hooke}$ que la força és proporcional a l'elongació. Però nosaltres ja coneixem un sistema per al qual la força resulta proporcional a l'elongació, es tracta de la molla, que segueix la llei de Hooke:

$$\begin{equation}\label{eq:hooke2}
F=-kx
\end{equation}$$  

on $k$ és la constant elàstica. Veiem que si apartem una molla de la seva posició d'equilibri i la deixem anar, aquesta descriurà un MHS. Si igualem l'equació $\ref{eq:hooke}$ amb l'equació $\ref{eq:hooke2}$ obtenim que 

$$\begin{equation}\label{eq:mw2}
k=m\omega^{2}
\end{equation}$$  

que relaciona els valors de la constant elàstica de la molla i la massa unida a ella amb la freqüència angular amb la que oscil·larà la molla. Reagrupant els factors podem obtenir la freqüència angular d'oscil·lació

$$
\begin{equation}\label{eq:freq_molla}\omega=\sqrt{\frac{k}{m}}\end{equation}
$$ 

<figure>
  <img src="img/molla.png" width="70%">
  <figcaption> Oscil·lació d'una molla. La força resulta proporcional a l'elongació i intenta restaurar l'equilibri. El moviment resultant és un MHS, la freqüència angular del qual està relacionada amb la constant elàstica, $k$, de la molla i de la massa, $m$, unida a ella a través de l'equació $\ref{eq:freq_molla}$.</figcaption>
</figure>

### El pèndol senzill <a class="anchor" id="2.3"></a>

Anomenarem pèndol senzill a una cos petit (que considerarem puntual) que penja d'un fil inextensible i de massa menyspreable. Si enganxem l'extrem lliure del fil del sostre i el deixem penjar amb la massa en l'altre extrem, el fil tindrà una posició vertical. Si apartem el fil una mica d'aquesta posició vertical i el deixem lliure començarà a moure's fent un moviment oscil·latori. Demostrarem aquí que, sota determinades condicions, aquest moviment serà un MHS.

El pèndol de la figura [fig:Pendol-senzill] té una longitud L
 . Per a veure quin tipus de moviment tindrà el pèndol mirarem a quines forces està sotmès. Les úniques interaccions a les que està sotmès són el pes de la massa m
  i la tensió del fil. Si descomponem la força pes en les direcció radial i tangencial veiem que la força que produeix el moviment és la component tangencial (la component radial del pes i la tensió del fil es resten, donat coma resultat la força centrípeta que produeix la curvatura de la trajectòria). Per tant, la força motriu serà:F=ma_{t}=-mg\sin(\varphi)
 on g
  correspon al mòdul de l'acceleració de la gravetat. El signe negatiu apareix per a indicar que la força té el signe contrari a l'angle, que és positiu en el sentit contrari al de les manetes del rellotge.

Per tant, l'acceleració seràa_{t}=-g\sin(\varphi)
 
 

 

#### Notes

<sup id="fn1">1.Els moviments periòdics ens permeten mesurar el temps. El temps que tarda la Terra en fer una volta al voltant del Sol ens permet definir l'any, el temps que tarda la Lluna en envoltar la Terra ens permet definir el mes i el temps que tarda la Terra en donar un gir sobre si mateixa permet definir el dia. <a href="#ref1" title="Tornar al text.">↩</a></sup>

<sup id="fn2">2. A vegades es fa servir l'equació $\ref{eq:a_vs_x}$ com a definició de MHS i, a partir d'ella es dedueix l'equació de moviment $\ref{eq:eq_mov_mhs}$. Qualsevol de les dues aproximacions són equivalents com ja hem demostrat.
<a href="#ref2" title="Tornar al text.">↩</a></sup>

