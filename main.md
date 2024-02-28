<!--- Markdown viewer:https://markdownlivepreview.com/
Table generator: https://www.tablesgenerator.com/markdown_tables
  -->

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

# Nieuw in GWSW persleidingen
In dit hoofdstuk zijn de belangrijkste vernieuwingen aan het GWSW vanuit een beheerdersperspectief beschreven. In hoofdstuk 4 is per onderdeel uitgewerkt welke informatie uitgewisseld dient te worden.

## Vaste data over persleidingen
Het zwaartepunt van GWSW persleidingen ligt op de de vaste gegevens van persleidingen. Denk hierbij bijvoorbeeld aan leidingmateriaal of wanddikte, maar ook kenmerken die nodig zijn om hydraulische berekeningen uit te voeren. Appendages zoals ontluchters en afsluiters vallen ook binnen de scope. De vaste gegevens zijn reeds deels gespecificeerd in het GWSW. In deze module zijn waar nodig bestaande modelconcepten aangepast en missende concepten toegevoegd.

## Gegevens op verschillende detailniveaus
Waar persleidinggegevens eerder alleen nog op persleidng- of leidingsegmentniveau (zie ook Figuur 3.1) werden vastgelegd, worden met de komst van nieuwe inspectietechnieken ook steeds meer gegevens op buisniveau geregistreerd. GWSW persleidingen kan met gegevens op alle detailniveaus in Figuur 1 omgaan, door steeds de onderlinge relaties te beschrijven: dus een buisdeel is onderdeel van een leidingsegement, wat weer onderdeel is van een persleiding, etc. Hierdoor zijn gegevens uit verschillende bronnen goed te combineren.  

<img src="media/Buis_SysteemNiveau.png" style="width:80%;height:80%" />

*Figuur 3.1 - Verschillende niveaus waarop gegevens over persleidingen worden vastgelegd*  

## Leiding volgen over de gehele levensduur
Bij het berekenen van de restlevensduur van een leiding is het niet alleen van belang de huidige conditie te weten, maar ook te schatten hoe snel degradatieprocessen zoals zetting of aantasting gaan. Deze snelheid kan vervolgens geprojecteerd worden om te schatten binnen hoeveel jaar de leiding 'op' is. Binnen GWSW persleidingen kunnen meerdere metingen van een leidingkenmerk naast elkaar staan, zonder dat de nieuwste meetwaarde de vorige overschrijft. 

Een voorbeeld hiervan is opgenomen in Tabel 3.1, waar meerdere diepteliggingen van een persleiding in zettingsgevoelig gebied beschikbaar zijn. Het gaat hierbij om de oorspronkelijke diepte tijdens aanleg en twee metingen na 25 en 51 jaar. 

*Tabel 3.1 - Voorbeeld van een object waarvan de drie verschillende diepteliggingen zijn vastgelegd*  

| **Objectnaam** | **Diepteligging (z-coördinaat)** | **Wijze van inwinning** | **Datum van inwinning** |
|----------------|----------------------------------|-------------------------|-------------------------|
| xx_1           | 11.73 m NAP                      | Revisie                 | 01-01-1971              |
| xx_1           | 11.68 m NAP                      | GPS Landmeting          | 12-07-1996              |
| xx_1           | 11.66 m NAP                      | Inspectie               | 06-08-2022              |

## Persleidingincidenten
De STandaard voor Uniforme Incidentenregistratie Persleidingen (STUIP) van Stichting RIONED / STOWA is als onderdeel van GWSW persleidingen opgenomen. Deze standaard beschrijft welke aspecten van een persleidingincident vastgelegd moeten worden om tot een bruikbare informatiebron voor risicogestuurd beheer te komen.

# Inhoud module
Tabel 4.1 geeft een overzicht van de kenmerken die oorspronkelijk al in GWSW basis over persleidingen werden vastgelegd, zie ook [https://data.gwsw.nl/1.6/Basis/Persleiding](https://data.gwsw.nl/1.6/basis/index.html?menu_item=classes&item=../../def/1.6/Basis/Persleiding). Hierbij was bewust de keuze gemaakt om geen van de kenmerken verplicht te stellen, wat betekent dat ook wanneer van een persleiding maar weinig gegevens bekend waren het toch mogelijk was deze via het GWSW uit te wisselen. In de rest van dit hoofdstuk is per thema uitgewerkt welke concepten in GWSW persleidingen zijn toegevoegd.

*Tabel 4.1 - Persleidingkenmerken in GWSW basis*  

| **Kenmerk**             | **Waardetype**                                                                                             | **Verplicht veld** | **Toelichting**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------------------------------------------------------|
| Begindatum              | [yyyymmdd] xsd:date                                                                                        | Nee                | Datum waarop het fysieke object is geplaatst of geinstalleerd                                                    |
| Breedte leiding         | [mm] xsd:integer                                                                                                       | Nee                | De bij het materiaal gebruikelijke aanduiding van de breedte van een   leiding                                   |
| Diameter leiding        | [mm] xsd:integer                                                                                                       | Nee                | De lengte van de middellijn van de cirkel die de binnen- of de   buitenzijde van de leidingdoorsnede beschrijft. |
| Drukklasse              | [bar] xsd:decimal                                                                                                      | Nee                | De maximale druk die de buis van een bepaalde klasse kan weerstaan                                               |
| Einddatum               | [yyyymmdd] xsd:date                                                                                        | Nee                | Datum waarop het fysieke object geen onderdeel meer van het fysieke   systeem is                                 |
| Hoogte leiding          | [mm] xsd:integer                                                                                                       | Nee                | De bij het materiaal gebruikelijke aanduiding van de hoogte van een   leiding                                    |
| Leidingorientatie       | [gml] geo:gmlLiteral                                                                                       | Nee                | Geografische beschrijving van leiding in XY coordinaten, met optioneel Z   coordinaten                           |
| Lengte leiding          | [m] xsd:decimal                                                                                            | Nee                |                                                                                                                  |
| Materiaal leiding       | Asbestcement,       Beton met stalen kern,       etc.                                                      | Nee                | De bouwstof van de leiding                                                                                       |
| Revisietekening         | Tekeningnummer                                                                                             | Nee                | Een tekening die na aanleg is opgesteld en in detail de aangelegde   situatie weergeeft                          |
| Status functioneren     | Buiten gebruik,       In aanleg,       In gebruik,       In ontwerp                                        | Nee                |                                                                                                                  |
| Toegankelijk            | Alleen toegankelijk voor   apparatuur,       Niet toegankelijk,       Toegankelijk voor mens en apparatuur | Nee                | Aanduiding van de toegankelijkheid op basis van constructieve   eigenschappen                                    |
| Verbindingstype         | Flensverbinding,       Glijverbinding,       etc.                                                          | Nee                | De wijze waarop de buizen binnen een leiding zijn verbonden                                                      |
| Verhoogd   risico       |                                                                                                            | Nee                | In kader WION, er geldt een verhoogd risico bij ontgraven voor deze   leiding                                    |
| Voegmateriaal           | Rubberring,       Voegenkit,       etc.                                                                    | Nee                | Afdichtingsmateriaal van de buisverbindingen                                                                     |
| Voorzorgsmaatregel      |                                                                                                            | Nee                | In kader WION, document met bijzondere maatregelen bij ontgraven                                                 |
| Vorm leiding            | Rechthoekig,       Rond,       etc.                                                                        | Nee                | De vorm van de dwarsdoorsnede van de leiding                                                                     |
| Wanddikte               | [mm] xsd:integer xsd:integer                                                                                           | Nee                | Dikte van de wand van de constructie                                                                             |
| Wandruwheid             | [mm] xsd:integer xsd:integer                                                                                           | Nee                | K-Nikuradse   waarde profielwand                                                                                 |
| Wandruwheid binnenboven | [mm] xsd:integer xsd:integer                                                                                           | Nee                |                                                                                                                  |
| Wandruwheid binnenonder | [mm] xsd:integer xsd:integer                                                                                           | Nee                |                                                                                                                  |
| Wibon thema             | Laagspanning (thema),       Middenspanning (thema),       Riool onder druk (thema),       etc.             | Nee                |                                                                                                                  |                                                                                             |

## Algemeen
De algemeen toegevoegde concepten zijn in Tabel 4.2 opgenomen 

*Tabel 4.2 - Algemeen toegevoegde concepten GWSW persleidingen*  

| **Behoefte**                                             | **Bestaande situatie** | **Voorstel**          | **Waardetype** | **Verplicht** | **Toelichting**                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------|-----------------------:|----------------------:|----------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reparatiestukken toevoegen:   lining                     | Deelliner              | Deelliner             | nvt.           | Nee           | Deelliner als concept bestaat   reeds en heeft een oriëntatie, dus kan op kaart worden weergegeven. Concept   was echter alleen beschikbaar voor vrijverval leidingen.                                                                                                                                                        |
| Reparatiestukken toevoegen:   reparatieklem              | -                      | Reparatieklem         | nvt.           | Nee           | Reparatieklem bestond nog niet   als concept.                                                                                                                                                                                                                                                                                 |
| Reparatiestukken toevoegen:   reparatiering              | -                      | Reparatiering         | nvt.           | Nee           | Reparatiering bestond nog niet   als concept, Aquaring als synoniem toevoegen.                                                                                                                                                                                                                                                |
| Persleiding beschrijven op   buisniveau                  | Buisdeel               | Buisdeel              | nvt.           | Nee           | Buisdeel als concept bestaat   reeds, maar was nog niet voorzien van    oriëntatie en kon dus niet op kaart worden weergegeven. Ook miste het   buismateriaal nog.                                                                                                                                                            |
| Inprikkers op persleidingen   toevoegen                  | -                      | Inprikker             | nvt.           | Nee           | Het is gewenst de locatie van   (industriële) inprikkers in kaart te brengen. Perceelaansluitpunt bestaat al   en zou grotendeels gekopiërd kunnen worden. Dit concept was al voorzien van   een oriëntatie en kon dus op kaart worden weergegeven. Ook de reeds bestaande   kenmerken zoals lozingseisen zijn van toepassing |
| Verbindingsstukken (Bochtstuk,   T-stuk, etc.) toevoegen | Verbindingsstuk        | Verbindingsstuk       | nvt.           | Nee           | Verbindingsstuk als concept   bestaat reeds en heeft verschillende subtypen zoals bochtstuk en T-stuk. Deze   was nog niet beschikbaar voor persleidingen                                                                                                                                                                     |
| Missende hulpstukken toevoegen                           | Compensator            | Compensator           | nvt.           | Nee           | Compensator als concept bestaat   reeds, maar was nog geen onderdeel van een persleiding                                                                                                                                                                                                                                      |
| Missende appendages toevoegen                            | Mechanische afsluiter  | Mechanische afsluiter |                |               | Mechanische afsluiter bestaat   reeds, maar was nog geen onderdeel van een persleiding en had geen oriëntatie                                                                                                                                                                                                                 |
| Missende   waterslagvoorzieningen toevoegen              | -                      | Be-   en ontluchter   | nvt.           | Nee           | Deze waterslagvoorziening was   nog niet opgenomen in het GWSW                                                                                                                                                                                                                                                                |
|                                                          | -                      | Buffertoren           | nvt.           | Nee           | Deze waterslagvoorziening was   nog niet opgenomen in het GWSW                                                                                                                                                                                                                                                                |
| Mangat toevoegen                                         | Mangat                 | Mangat                | nvt.           | Nee           | Mangat als concept bestaat reeds   en heeft een oriëntatie, dus kan op kaart worden weergegeven. Concept was   echter alleen beschikbaar voor druk- en vacuümriolen.                                                                                                                                                          |
| Minimaal   benodigde wanddikte als maatstaf toevoegen    | -                      | Minimaal benodigde wanddikte | [mm] xsd:integer    | Nee           | Minimaal benodigde wanddikte   bestond nog niet als concept.                                                                                                                                                                                                                                                                  |

## Risico
De XXX toegevoegde concepten zijn in Tabel 4.2 opgenomen 

*Tabel 4.2 - XXX toegevoegde concepten GWSW persleidingen*  

| **Behoefte**                                                                                     | **Bestaande situatie** | **Voorstel**     | **Waardetype**   | **Verplicht** | **Toelichting**                                                                                         |
|--------------------------------------------------------------------------------------------------|------------------------|------------------|------------------|---------------|---------------------------------------------------------------------------------------------------------|
| Toevoegen   debiet persleiding tijdens dwa / hwa. Benodigde gegevens in geval van   calamiteiten | -                      | Afvoerdebiet dwa | [m3/h] xsd:float | Nee           | Kenmerk bestond nog niet                                                                                |
|                                                                                                  | -                      | Afvoerdebiet hwa | [m3/h] xsd:float | Nee           | Kenmerk bestond nog niet                                                                                |
| Toevoegen   of een leiding is voorzien van een beschermende coating                              | Coating                | Coating          | nvt.             | Nee           | Concept Coating bestond al, maar   was nog geen kenmerk van een buisdeel, leidingsegment of persleiding |
| Toevoegen   geschatte restlevensduur                                                             | Restlevensduur         | Restlevensduur   | [yyyy] xsd:gYear | Nee           | Concept restlevensduur bestond   al, maar was nog geen kenmerk van een buisdeel of leidingsegment en niet   voorzien van wijze en datum van inwinning |

## Persleidinginspecties
De XXX toegevoegde concepten zijn in Tabel 4.3 opgenomen

*Tabel 4.3 - XXX toegevoegde concepten GWSW persleidingen*  

| **Behoefte**                                              | **Bestaande situatie** | **Voorstel**                | **Waardetype**      | **Verplicht** | **Toelichting**                                                                                                                           |
|-----------------------------------------------------------|------------------------|-----------------------------|---------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Toevoegen wanddikte buis                                  | Wanddikte              | Wanddikte                   |                     | Nee           | Wanddikte als concept bestaat   reeds, maar maakte nog geen onderscheid tussen gemeten en oorspronkelijke   wanddikte bij aanleg.         |
|                                                           | -                      |    Bij aanleg               | [mm] xsd:decimal    | Nee           | Oorspronkelijke wanddikte bij aanleg                                                                                                      |
|                                                           | -                      |    Minimaal gemeten         | [mm] xsd:decimal    | Nee           | Minimaal gemeten wanddikte buisdeel                                                                                                       |
|                                                           | -                      |    Gemiddeld gemeten        | [mm] xsd:decimal    | Nee           | Gemiddeld gemeten wanddikte buisdeel                                                                                                      |
|                                                           | -                      |    Maximaal gemeten         | [mm] xsd:decimal    | Nee           | Maximaal gemeten wanddikte buisdeel                                                                                                       |
| Toevoegen   Voegwijdte verbinding                         | -                      | Voegwijdte verbinding       | [mm] xsd:decimal    | Nee           | Voegwijdte verbinding bestond   nog niet als concept                                                                                      |
| Toevoegen Hoekverdraaiing verbinding                      | -                      | Hoekverdraaiing horizontaal | [grd] xsd:decimal    | Nee           | Hoekverdraaiing als concept   bestaat reeds, maar hierbij werd geen onderscheid gemaakt tussen horizontale   en verticale hoekverdraaiing |
|                                                           | -                      | Hoekverdraaiing verticaal   | [grd] xsd:decimal    | Nee           | Hoekverdraaiing als concept   bestaat reeds, maar hierbij werd geen onderscheid gemaakt tussen horizontale   en verticale hoekverdraaiing |
| Toevoegen aantal draadbreuk voorgespannen   betonbuisdeel | -                      | Aantal draadbreuken         | [pcs] xsd:integer | Nee           | draadbreuken in voorgespannen betonbuizen bestaat nog niet als concept                                                                    |
| Lekkage                                                   | -                      | Lekkage                     | nvt.                | Nee           | Lekkage bestond nog niet als concept                                                                                                      |
| Gasophoping                                               | -                      | Gasophoping                 | nvt.                | Nee           | Gasophoping bestond nog niet als concept                                                                                                  |
| Vervuiling                                                | -                      | Vervuiling                  | nvt.                | Nee           | Vervuiling bestond nog niet als concept                                                                                                   |
| Ovaliteit                                                 | -                      | Ovaliteit                   | [%] xsd:integer     | Nee           | Vervorming van een ronde leiding bestond nog niet als concept                                                                             |


## Hydraulica
De XXX toegevoegde concepten zijn in Tabel 4.4 opgenomen

| **Behoefte**                              | **Bestaande situatie** | **Voorstel**              | **Waardetype**  | **Verplicht** | **Toelichting**                                                                                                                                                |
|-------------------------------------------|------------------------|---------------------------|-----------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Toevoegen   verschillende leidingdrukken  | Drukklasse             | Druk:                     |                 | Nee           | Drukklasse als concept bestaat   reeds, maar maakte nog geen onderscheid tussen de drukklasse van een buis, de   ontwerpdruk van de leiding en gemeten drukken |
|                                           |                        |    Nominale druk (DN)     | [bar] xsd:float | Nee           |                                                                                                                                                                |
|                                           |                        |    Ontwerpdruk            | [bar] xsd:float | Nee           |                                                                                                                                                                |
|                                           |                        |    Opleveringsdruktest    | [bar] xsd:float | Nee           |                                                                                                                                                                |
|                                           |                        |    Testdruk               | [bar] xsd:float | Nee           |                                                                                                                                                                |
| Lokale verliezen bij appendages toevoegen | -                      | Energieverliescoefficient | [-]             | Nee           | Energieverlies coëfficiënten   voor lokale verliezen bestond nog niet als concept                                                                              |

## Persleidingincidenten
De XXX toegevoegde concepten zijn in Tabel 4.5 opgenomen
<!---https://data.gwsw.nl/1.5.1/Persleidingen -->

[STUIP rapport](https://www.riool.net/stuip-standaard-voor-uniforme-incidentenregistratie-persleidingen-2023-18-)

<img src="media/PersleidingincidentDiagram.svg" style="width:120%;height:120%" />

Deelnemers  
Taakverdeling, rol werkgroep, projectleider, RIONED  
Fasering in de tijd

# Handleiding, toepassen

## Risicogebied 

Help bij  
* opbouw datasets
* gebruik apps
