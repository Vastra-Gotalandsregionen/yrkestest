from flask_babel import lazy_gettext
questions = [
  [ lazy_gettext("Vad passar bäst in på dig?"),
    [
      lazy_gettext("Tuff & envis"),
      lazy_gettext("Omtänksam & konflikträdd"),
      lazy_gettext("Spontan & tanklös"),
      lazy_gettext("Ordningsam & kritisk")
    ]
  ],
  [ lazy_gettext("Du ska ut och campa ett par nätter med några vänner. Vad bidrar du med i gruppen?"),
    [
      lazy_gettext("Jag har koll på att vi ställer upp tältet på en bra plats och ser till att vi följer instruktionerna så det byggs upp på rätt sätt."),
      lazy_gettext("Jag har bestämt hur vi ska organisera allt och beslutat hur vi ska ta oss dit för att det ska gå snabbt och smidigt."),
      lazy_gettext("Jag tar med lite smått och gott som någon kan komma att behöva. T.ex. powerbanks till mobiler, värktabletter och plåster."),
      lazy_gettext("Jag fixar en spellista med skön musik. När vi kommer fram föreslår jag kul lekar och kommer på att vi ska nattbada.")
    ]
  ],
  [ lazy_gettext("Klassen har fått i uppgift att gruppvis göra förslag till en ny broschyr om er skola. Den broschyr som läraren gillar bäst kommer att delas ut vid öppet hus och liknande. Vad tänker du och vilken roll tar du i gruppen?"),
    [
      lazy_gettext("Älskar grupparbeten! Det är viktigt med en härlig känsla i broschyren så jag kommer med idéer om hur vi kan visa det. Det vore också kul om vi gjorde broschyren på något nytt sätt, kanske som en app"),
      lazy_gettext("Kan bli roligt även om jag helst jobbar själv i lugn och ro. Troligen ansvarar jag för att fakta i texterna stämmer och sådana saker."),
      lazy_gettext("Roligt! Jag har lätt för att komma överens med alla i grupparbeten. Jag hjälper till med det som behövs mest så att allt funkar bra och vi har trevligt."),
      lazy_gettext("Vore kul om vår grupp tar hem det! Jag ser till att få genomföra de idéer jag har och bestämmer strukturen för broschyren så att det blir ordentligt gjort.")
    ]
  ],
  [ lazy_gettext("Vad passar bäst in på dig?"),
    [
      lazy_gettext("Livlig & uppmärksamhetskrävande"),
      lazy_gettext("Korrekt & eftertänksam"),
      lazy_gettext("Snabb & bossig"),
      lazy_gettext("Vänlig & försiktig")
    ]
  ],
  [ lazy_gettext("En kompis nya cykel har blivit stulen. Trots att den var fastlåst vid cykelställen bakom skolan verkar någon ha hunnit kapa låset utan att ha blivit upptäckt. Hur reagerar du?"),
    [
      lazy_gettext("Jag blir upprörd och säger att jag tänker ta upp med elevrådet eller rektorn att cykelställen borde flyttas till en plats med bättre uppsikt så att inte fler drabbas. "),
      lazy_gettext("Jag berättar att jag alltid brukar använda två lås så att risken för denna typ av händelser minimeras."),
      lazy_gettext("Jag kommer på att vi kan anordna en fest och ta inträde för att samla in pengar till en ny cykel till vår kompis. Varför inte vända detta till något kul?"),
      lazy_gettext("Jag kramar om min kompis och tröstar hen, frågar hur det känns osv.")
    ]
  ],
  [ lazy_gettext("På vilket sätt vill du helst arbeta med människor?"),
    [
      lazy_gettext("Att praktiskt hjälpa och stötta människor"),
      lazy_gettext("Att utveckla idéer som förbättrar människors situation"),
      lazy_gettext("Att fördjupa mig i forskning om människor och använda den kunskapen"),
      lazy_gettext("Att inspirera och motivera människor")
    ]
  ],
  [ lazy_gettext("Du och några klasskompisar ska lösa en uppgift tillsammans. Hur ska det vara för att du ska trivas bäst?"),
    [
      lazy_gettext("Jag gillar när folk gör som jag säger"),
      lazy_gettext("Jag gillar när alla har koll på saker och inte fattar förhastade beslut"),
      lazy_gettext("Jag gillar när alla är överens"),
      lazy_gettext("Jag gillar när jag har kul och det händer nya saker under tiden")
    ]
  ],
  [ lazy_gettext("Vilket av följande skulle du helst göra i ett jobb?"),
    [
      lazy_gettext("Se till att andra mår bra och får bra service"),
      lazy_gettext("Bestämma vad vi ska göra för att uppnå resultat"),
      lazy_gettext("Ta fram fakta, analysera vad som är fel och sedan lösa det"),
      lazy_gettext("Hjälpa andra att bli motiverade")
    ]
  ],
  [ lazy_gettext("Vem i Bamse identifierar du dig mest med?"),
    [
      lazy_gettext("Spralliga Mini Hopp"),
      lazy_gettext("Modiga Nalle-Maja"),
      lazy_gettext("Finurliga Skalman"),
      lazy_gettext("Hjälpsamma Bamse")
    ]
  ],
  [ lazy_gettext("Vilken av dessa animerade karaktärer identifierar du dig mest med?"),
    [
      lazy_gettext("Partyglada Poppy i Trolls, som tar livet med en klackspark"),
      lazy_gettext("Drivna Vaiana, som går sin egen väg"),
      lazy_gettext("Skärpta Liza Simpson, som har ordning på allt"),
      lazy_gettext("Uthålliga Askungen, som aldrig blir arg på någon")
    ]
  ],
]

answers = [
  ['d', 's', 'i', 'c'],
  ['c', 'd', 's', 'i'],
  ['i', 'c', 's', 'd'],
  ['i', 'c', 'd', 's'],
  ['d', 'c', 'i', 's'],
  ['s', 'd', 'c', 'i'],
  ['d', 'c', 's', 'i'],
  ['s', 'd', 'c', 'i'],
  ['i', 'd', 'c', 's'],
  ['i', 'd', 'c', 's'],
]

addextraquestions = [
  [ lazy_gettext("Du är på en stor invigningsfest för en ny ungdomsgård. Där är många du inte känner. Hur tänker och agerar du i början av festen?"),
    [
      lazy_gettext("Jag gillar inte stora grupper så försöker hitta någon jag har gemensamma intressen med. Det kan bli lite jobbigt eftersom jag då måste småprata först och jag inte är superbra på det. Men hittar jag rätt personer kan det bli trevligt med en intressant diskussion i lugn och ro i ett hörn."),
      lazy_gettext("Superkul! Jag minglar runt och snackar med alla. Tar kvällen som den kommer, skämtar, skrattar och har inget emot att stå i centrum om det skulle råka bli så."),
      lazy_gettext("Jag småpratar med andra om trevliga grejer, kollar om de som fixat festen behöver hjälp och går kanske fram till någon som verkar ensam så att hen inte känner sig utanför."),
      lazy_gettext("Jag gillar att prata med andra och berätta om något spännande eller kul jag sysslar med. Jag är inte heller rädd för att kasta mig in i hetsig diskussion som verkar intressant, även om de andra har en annan åsikt än vad jag har.")
    ]
  ],
  [ lazy_gettext("Vilken Astrid Lindgren-karaktär identifierar du dig mest med?"),
    [
      lazy_gettext("Orubbliga rövarhövdingen Mattis från Ronja"),
      lazy_gettext("Visa Skalle-Per från Ronja Rövardotter"),
      lazy_gettext("Fridsamma drängen Alfred från Emil i Lönneberga"),
      lazy_gettext("Impulsiva Emil i Lönneberga")
    ]
  ],
  [ lazy_gettext("Om du måste välja bara ett alternativ, hur vill du helst att andra uppfattar dig?"),
    [
      lazy_gettext("Som snäll"),
      lazy_gettext("Som smart"),
      lazy_gettext("Som korrekt"),
      lazy_gettext("Som kul")
    ]
  ],
  [
    lazy_gettext("Vilket skulle vara värst om någon trodde det om dig? Att du är…"),
    [
      lazy_gettext("…korkad"),
      lazy_gettext("…elak"),
      lazy_gettext("…tråkig"),
      lazy_gettext("…slarvig")
    ]
  ],
  [ lazy_gettext("Du har fått ett stipendium till en tvåveckors sommarkurs utomlands. Det finns ett stort urval av platser och kurser att välja på. Hur gör du valet?"),
    [
      lazy_gettext("Jag väljer en plats som erbjuder en kurs som jag kommer ha nytta av i framtiden."),
      lazy_gettext("Jag googlar och tittar på bilder från de olika platserna och väljer en kurs och en plats som känns kul och spännande."),
      lazy_gettext("Jag samlar fakta och läser på ordentligt om de olika kurserna och platserna innan jag fattar mitt beslut"),
      lazy_gettext("Jag frågar mina kompisar om råd och försöker hitta information om vilka kurser som ger mysigast gemenskap.")
    ]
  ],
  [ lazy_gettext("Några i klassen har fått i uppgift att hålla i en idrottslektion utan att läraren är med. När lektionen ska börja blir det tydligt att de inte gjort ett bra jobb, de har ingen plan och ingen vet vad ni ska göra. Vissa blir missnöjda och situationen börjar urarta. Vad gör du?"),
    [
      lazy_gettext("Jag försöker lugna de som blir upprörda, samtidigt som jag försöker stötta de som är ansvariga genom att försiktigt fråga om jag kan hjälpa till med något."),
      lazy_gettext("Jag försöker antingen styra upp hur vi bör göra för att få ut något av lektionen, eller har jag redan hittat något bättre att lägga min tid på."),
      lazy_gettext("Jag låter andra lösa kaoset på plats men erbjuder mig när läraren senare undrar om någon kan ta fram en checklista på hur detta bör göras för att undvika oreda nästa gång."),
      lazy_gettext("Jag tycker det kan vara kul med oväntade situationer och tar det som det kommer. Jag passar nog bara på att ta det lugnt och snacka med mina vänner.")
    ]
  ],
  [ lazy_gettext("Hur pluggar du helst inför stora prov?"),
    [
      lazy_gettext("Tillsammans med en eller ett par kompisar så kan vi hjälpa varandra och ha det trevligt under tiden."),
      lazy_gettext("Det beror lite på ämnet, men jag brukar läsa effektivt på slutet och så mycket som krävs för det betyg jag vill ha. Jag brukar ha koll!"),
      lazy_gettext("Det är lite olika hur jag känner mig inspirerad. Ibland pluggar jag själv, ibland med andra, det brukar lösa sig."),
      lazy_gettext("Jag pluggar bäst ostört och på egen hand. Är bra på att systematiskt plugga in saker, särskilt om ämnet intresserar mig.")
    ]
  ],
  [ lazy_gettext("Vad är viktigast av följande i ett jobb/grupparbete?"),
    [
      lazy_gettext("Att jag får hålla på med intressanta uppgifter och fördjupa mig i dem"),
      lazy_gettext("Att jag får ha idéer och skoja till det"),
      lazy_gettext("Att jag är tillsammans med trevliga personer och får visa att jag är en bra kompis"),
      lazy_gettext("Att jag får göra utvecklande uppgifter och visa vad jag kan")
    ]
  ],
  [ lazy_gettext("Om någon dissar din jättebra plan om hur något ska göras tycker du troligtvis att de är…"),
    [
      lazy_gettext("…för kritiska"),
      lazy_gettext("…korkade"),
      lazy_gettext("…oseriösa"),
      lazy_gettext("…taskiga")
    ]
  ],
  [ lazy_gettext("Vilken Mumin-karaktär identifierar du dig mest med?"),
    [
      lazy_gettext("Filosofiska Snusmumriken"),
      lazy_gettext("Omtänksamma Muminmamman"),
      lazy_gettext("Nyfikna Mumintrollet"),
      lazy_gettext("Viljestarka Lilla My")
    ]
  ],
]


addextraquestionsanswers = [
        ['c', 'i', 's', 'd'],
        ['d', 'c', 's', 'i'],
        ['s', 'd', 'c', 'i'],
        ['d', 's', 'i', 'c'],
        ['d', 'i', 'c', 's'],
        ['s', 'd', 'c', 'i'],
        ['s', 'd', 'i', 'c'],
        ['c', 'i', 's', 'd'],
        ['i', 'd', 'c', 's'],
        ['c', 's', 'i', 'd'],
]

extraquestion = {
        'question': lazy_gettext('Vad passar bäst in på dig?'),
        's': lazy_gettext('Hjälpsam'),
        'd': lazy_gettext('Orädd'),
        'c': lazy_gettext('Noggrann'),
        'i': lazy_gettext('Social'),
}

segmentQuestion = {
  'question': lazy_gettext('Hur ser du på att plugga vidare efter gymnasiet?'),
  'answers': {
    'a': lazy_gettext('Jag vill börja jobba direkt efter gymnasiet'),
    'b': lazy_gettext('Jag kan tänka mig en kortare utbildning, t.ex. yrkeshögskola (YH) på max två år'),
    'c': lazy_gettext('Jag kan tänka mig att läsa på högskola i cirka tre år'),
    'd': lazy_gettext('Jag kan tänka mig en längre utbildning på högskola på över fyra år')
  }
}

rec_text = {
  'd': lazy_gettext('Du gillar att utveckla och förbättra saker och har inte något emot att bestämma. Du vill nå snabba resultat och har inget till övers för ineffektivitet. Inom hälso- och sjukvården finns flera områden där du kan få användning för dessa egenskaper. Om du även besitter andra goda egenskaper som empati, analysförmåga och kreativitet kan dina drivkrafter passa bra i exempelvis en ledarskapsroll.'),
  'i': lazy_gettext('Du är en social person som gillar att bli inspirerad och att inspirera andra. Du är spontan, kreativ och har oftast inget större behov av att överväga något länge innan du fattar beslut. Du skulle trivas i roller där du får komma med idéer, sprida god stämning och motivera andra.'),
  's': lazy_gettext('Du är en empatisk person som gillar att vara till hjälp. Du är omtänksam, bra på att kompromissa och gillar när alla är överens. Du har inget behov av att bossa över andra och trivs i roller där du får fixa, stötta och känna att du gör skillnad.'),
  'c': lazy_gettext('Du är en ordningsam och analyserande person som gillar att ha koll på läget. Du föredrar att tänka igenom saker så att resultaten blir så bra som möjligt. Du är seriös, har höga krav på dig själv och ogillar slarv. Du skulle trivas i roller där du får möjlighet att fördjupa dig och där det är viktigt att allt blir korrekt.'),
}

rec_jobs = {
  'd': {
    'a': [],
    'b': [],
    'c': [],
    'd': []
  },
  'i': {
    'a': [
      lazy_gettext('Kock'),
      lazy_gettext('Patientvaktmästare')
    ],
    'b': [
      lazy_gettext('Kock')
    ],
    'c': [
      lazy_gettext('Arbetsterapeut'),
      lazy_gettext('Dietist'),
      lazy_gettext('Fysioterapeut')
    ],
    'd': [
      lazy_gettext('Arbetsterapeut'),
      lazy_gettext('Dietist'),
      lazy_gettext('Fysioterapeut')
    ]
  },
  's': {
    'a': [
      lazy_gettext('Undersköterska'),
      lazy_gettext('Patientvaktmästare'),
      lazy_gettext('Lokalvårdare')
    ],
    'b': [
      lazy_gettext('Tandsköterska'),
      lazy_gettext('Undersköterska')
    ],
    'c': [
      lazy_gettext('Tandhygienist'),
      lazy_gettext('Sjuksköterska')
    ],
    'd': [
      lazy_gettext('Barnmorska'),
      lazy_gettext('Läkare'),
      lazy_gettext('Tandläkare'),
      lazy_gettext('Psykolog')
    ]
  },
  'c': {
    'a': [
      lazy_gettext('Lagerarbetare'),
      lazy_gettext('Transportarbetare'),
      lazy_gettext('Tvättoperatör')
    ],
    'b': [
      lazy_gettext('Medicinsk sekreterare')
    ],
    'c': [
      lazy_gettext('Biomedicinsk analytiker')
    ],
    'd': [
      lazy_gettext('Medicinteknisk ingenjör'),
      lazy_gettext('Läkare'),
      lazy_gettext('Tandläkare'),
      lazy_gettext('Psykolog')
    ]
  }
}

how_many_questions = 10
