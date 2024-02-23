# GWSW Persleidingen

<style>
  .symbolSmall{width:20px;height:20px;margin-right:1em;vertical-align:middle}
  .symbol{width:30px;height:30px;margin-right:1em;vertical-align:middle}
</style>

De module GWSW-Persleidingen is ontwikkeld door Johan Post (Partners4UrbanWater) en Wouter van Riel (Infralytics), in samenwerking met de werkgroep GWSW-Persleidingen, bestaande uit:
- Frans Hamers, Waterschap Aa en Maas
- Theo Heimensen, Waterschap Vallei en Veluwe
- Werner Jousma, Acquaint
- Roland Markus, Xylem
- Demas Poldervaart, Gemeente Rotterdam
- Thomas Staverman, Waternet
- Michiel Tukker, Deltares
- Sjaak Verkerk, Antea Group
- Paul van Wetten, Hoogheemraadschap van Rijnland

Vanuit Stichting RIONED is Eric Oosterom de verantwoordelijk projectmanager. Vragen over de module en de totstandkoming en vaststelling ervan kunt u stellen via gwsw@rioned.org. 


# Inleiding
<!---Context, GWSW-project -->
Een groot deel van de persleidingen in Nederland is aangelegd in de jaren 70 en 80 toen RWZI's op grote schaal werden gebouwd. Deze leidingen hebben jaren gefunctioneerd zonder veel problemen, waardoor beheeractiviteiten beperkt waren tot voornamelijk reparaties na een incident. Nu veel persleidingen hun theoretische levensduur naderen of reeds gepasseerd zijn, is behoefte aan inzicht in de actuele leidingconditie en een schatting van de resterende levensduur. Data spelen hierin een steeds prominentere rol, enerzijds omdat op basis van leidinggegevens kan worden gedifferentieerd welke leidingen risicovol zijn en aandacht behoeven, anderzijds omdat metingen en inspecties nieuwe gegevens genereren die ook vastgelegd en uitgewisseld worden. Naast constructieve aspecten worden voor hydraulische berekeningen over de afvoercapaciteit of drukextremen ook gegevens uitgewisseld.

Het GegevensWoordenboek Stedelijk Water ([GWSW](https://data.gwsw.nl/)) is een open standaard ontwikkeld en beheerd door de Stichting RIONED, namens de sector. De beoogde meerwaarde van ‘allemaal dezelfde taal spreken’ is verbetering van de kwaliteit van gegevens en de uitwisseling ervan. Gangbare stedelijk  water objecten en structuren zijn reeds beschreven in het deelmodel GWSW basis. Daarnaast zijn verschillende andere deelmodellen ontwikkeld of in ontwikkeling die toegespitst zijn op specifieke toepassingen. Gezien de recente ontwikkelingen op het gebied van persleidingen, sinds ca. 2018 verenigd in de 'Werkgroep Persleidingen' onder leiding van Stichting RIONED en Stowa, heeft Stichting RIONED besloten nu ook een deelmodel Persleidingen te definiëren. 

# Beoogde toepassing
Voor het beheer van persleidingen worden data steeds relevanter. Het GWSW is gericht op het verbeteren van de datakwaliteit, -uitwisseling en -benutting. Bij de ontwikkeling van GWSW-Persleidingen zijn de volgende toepassingen als uitgangspunt gebruikt:
## Reactief beheer
Bij een leidingbreuk is het zaak maatregelen te nemen om de afvoer van afvalwater te herstellen en de gevolgen voor de omgeving te beperken. Hierbij zijn verschillende informatiebronnen ondersteunend. Uit het persleidingenoverzicht volgt welke achterliggende gemalen afgeschakeld moeten worden en welke afsluiters bediend. Nog voor een schep de grond in is gegaan kan op basis van het materiaal en diameter al worden bepaald welk type reparatie van welke grootte nodig is.
## Risicoinventarisatie
Een risicoinventarisatie is een veelgebruikt middel voor vervangingsbesluitvorming of het prioriteren van inspecties en leidingconditiemetingen. Om risico's te duiden worden gegevens over de kans op een faalgebeurtenis en de mogelijke gevolgen geïnventariseerd. Voor de kans-kant zijn leidingeigenschappen zoals jaar van aanleg, materiaal en historische faalgebeurtenissen relevant. De bruikbaarheid van geregistreerde historische faalgebeurtenissen hangt nauw samen met het detailniveau waarop deze geregistreerd zijn. Zo is het van belang te differentiëren tussen incidenten met een externe oorzaak, zoals graafschade, die niet veroorzaakt wordt door een verslechterde constructieve toestand en ook bij nieuwe leidingen kan optreden. De gevolg-kant kent twee aspecten, namelijk de kwetsbaarheid van de omgeving (nabijgelegen waterkeringen, andere leidingen, etc.) en het achterliggende gebied dat bij een afvoeronderbreking niet meer kan afvoeren. 
## Voorkomen graafschade
Om graafschade te voorkomen wordt informatie over de leidingligging verstrekt aan de partij die voornemens is grondroerwerzkaamheden uit te voeren. In de praktijk blijkt soms dat de kwaliteit van deze liggingsgegevens matig is, waardoor de leidingligging in het veld enkele tot soms tientallen meters afwijkt van de ligging volgens het beheersysteem. Daarnaast is de ligging soms bekend vanuit verschillende gegevensbronnen waarbij alleen de laatste ontsluitbaar is. De kwaliteit en actualiteit van deze gegevens kan worden geduid door deze van een datum en wijze van inwinning (b.v. schatting, ontwerptekening, inmeting, etc.) te voorzien. 
## Toetsen hydraulisch functioneren
Software wordt gebruikt om de hydraulische afvoercapaciteit van persleiding modelmatig te toetsen. Naast inzicht in de te verwachten afvoerdebieten kan hiermee ook getoetst worden of luchtophoping te verwachten is en wat de maximale en minimale optredende drukken zijn. Het laatste is ook van belang bij het bepalen van de minimaal benodigde buissterkte. Het GWSW kan de uitwisseling met dergelijke software verbeteren.
## Bepalen actuele leidingconditie en schatten restlevensduur
Bij inspecties en leidingconditiemetingen worden data over leidingkenmerken zoals de wanddikte, hoekverdraaiing of ligging gegenereerd. Wanneer uit een toetsing aan de maatstaven volgt dat de leiding niet voldoet, dient deze vervangen te worden. Voor een dergelijke toetsing dienen dus zowel de metingen als de maatstaven vastgelegd te zijn. 

Veel beheerders gebruiken conditiemetingen ook om de restlevensduur te schatten, waarbij metingen worden vergeleken met de aanlegsituatie en de opgetreden degradatie wordt geprojecteerd op de toekomst. Dergelijke restlevensduurschattingen zijn alleen mogelijk wanneer oude gegevens niet overschreven worden maar gezamenlijk worden vastgelegd.

<!---Applicaties (extern en/of op GWSW Server) Gegevensbehoefte-->

# Inrichting van het deelmodel

Belangrijkste GWSW-aanpassingen  
Modelleerprincipes

## Gegevens op verschillende detailniveaus
Waar persleidinggegevens eerder alleen nog op persleidng- of leidingsegmentniveau (zie ook Figuur 1) werden vastgelegd, worden met de komst van nieuwe inspectietechnieken ook steeds meer gegevens op buisniveau geregistreerd. GWSW persleidingen kan met gegevens op alle detailniveaus in Figuur 1 omgaan, door steeds de onderlinge relaties te beschrijven: dus een buisdeel is onderdeel van een leidingsegement, wat weer onderdeel is van een persleiding, etc. Hierdoor zijn gegevens uit verschillende bronnen goed te combineren.  

<img src="media/Buis_SysteemNiveau.png" style="width:80%;height:80%" />

*Figuur 1 - Verschillende niveaus waarop gegevens over persleidingen worden vastgelegd*  

## Leiding volgen over de gehele levensduur
Bij het berekenen van de restlevensduur van een leiding is het niet alleen van belang de huidige conditie te weten, maar ook te schatten hoe snel degradatieprocessen zoals zetting of aantasting gaan. Deze snelheid kan vervolgens geprojecteerd worden om te schatten binnen hoeveel jaar de leiding 'op' is. Binnen GWSW persleidingen kunnen meerdere metingen van een leidingkenmerk naast elkaar staan, zonder dat de nieuwste meetwaarde de vorige overschrijft. 

| **Diepteligging   (z-coördinaat)** | **Wijze van inwinning** | **Datum van inwinning** |
|------------------------------------|-------------------------|-------------------------|
| 11.73 m NAP                        | Revisie                 | 01-01-1971              |
| 11.68 m NAP                        | GPS Landmeting          | 12-07-1996              |
| 11.66 m NAP                        | Inspectie               | 06-08-2022              |

# Realisatie

Deelnemers  
Taakverdeling, rol werkgroep, projectleider, RIONED  
Fasering in de tijd

# Handleiding, toepassen

Help bij  
* opbouw datasets
* gebruik apps
