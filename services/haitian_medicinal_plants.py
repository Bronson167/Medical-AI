# haitian_medicinal_plants.py

HAITIAN_MEDICINAL_PLANTS = {
    # ================================
    # Allium (ail, oignon, poireau)
    # ================================
    "Allium cepa": {
        "local_name": "Zonyon",
        "family": "Amaryllidaceae",
        "is_medicinal": True,
        "medicinal_uses": ["rhumes", "toux", "problèmes digestifs", "infections respiratoires"],
        "recommendations": "Consommé cru ou cuit dans les repas, décoction pour les maux respiratoires."
    },
    "Allium sativum": {
        "local_name": "Lay",
        "family": "Amaryllidaceae",
        "is_medicinal": True,
        "medicinal_uses": ["hypertension", "infection", "cholestérol", "immunité"],
        "recommendations": "Consommé cru ou dans les plats; infusion ou décoction pour infections."
    },
    "Allium fistulosum": {
        "local_name": "Poireau",
        "family": "Amaryllidaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestif léger", "tonique général", "antiseptique léger"],
        "recommendations": "Consommé dans les soupes ou bouillons; décoction légère pour usage antiseptique."
    },
    "Allium giganteum": {
        "local_name": "Piment de la reine",
        "family": "Amaryllidaceae",
        "is_medicinal": False,
        "medicinal_uses": [],
        "recommendations": ""
    },

    "Aloysia citrodora": {
    "local_name": "Vervein",
    "family": "Verbenaceae",
    "is_medicinal": True,
    "medicinal_uses": [
        "digestion",
        "stress",
        "insomnie",
        "fièvre légère",
        "rhumes"
    ],
    "recommendations": "Infusion des feuilles séchées ou fraîches pour calmer le stress et améliorer la digestion; peut être utilisée en bain relaxant."
},

    # ================================
    # Aloe
    # ================================
    "Aloe vera": {
        "local_name": "Aloès",
        "family": "Aloeaceae",
        "is_medicinal": True,
        "medicinal_uses": ["brûlures", "coupures", "soins de la peau", "digestion"],
        "recommendations": "Gel appliqué sur la peau; décoction ou jus pour digestion."
    },

    # ================================
    # Agrumes
    # ================================
    "Citrus aurantiifolia": {
        "local_name": "Sitwon vèt",
        "family": "Rutaceae",
        "is_medicinal": True,
        "medicinal_uses": ["rhumes", "fièvre", "digestion", "infections légères"],
        "recommendations": "Jus consommé dilué; infusion pour les maux de gorge."
    },

    # ================================
    # Plantes aromatiques
    # ================================
    "Cymbopogon citratus": {
        "local_name": "Sitwonèl",
        "family": "Poaceae",
        "is_medicinal": True,
        "medicinal_uses": ["stress", "digestion", "fièvre", "rhumes"],
        "recommendations": "Infusion des feuilles séchées; bain médicinal pour relaxant."
    },
    "Mentha nemorosa": {
        "local_name": "Mant",
        "family": "Lamiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "maux de tête", "rhumes"],
        "recommendations": "Infusion des feuilles; inhalation vapeur pour congestion nasale."
    },
    "Ocimum basilicum": {
        "local_name": "Basilik",
        "family": "Lamiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "stress", "rhume"],
        "recommendations": "Infusion ou ajout dans les repas; inhalation pour congestion."
    },

    # ================================
    # Plantes locales et médicinales
    # ================================
    "Phyllanthus niruri": {
        "local_name": "Ti pye bwa",
        "family": "Phyllanthaceae",
        "is_medicinal": True,
        "medicinal_uses": ["calculs rénaux", "foie", "digestion"],
        "recommendations": "Décoction des feuilles et tiges, à boire."
    },
    # ================================
    # Arbres Fruitiers et Médicinaux
    # ================================
    "Annona muricata": {
        "local_name": "Kowosòl",
        "family": "Annonaceae",
        "is_medicinal": True,
        "medicinal_uses": ["insomnie", "nervosité", "hypertension", "parasites intestinaux"],
        "recommendations": "Infusion des feuilles pour calmer les nerfs; fruit consommé pour les vitamines."
    },
    "Artocarpus altilis": {
        "local_name": "Veritab",
        "family": "Moraceae",
        "is_medicinal": True,
        "medicinal_uses": ["hypertension", "brûlures", "maux d'estomac"],
        "recommendations": "Décoction des feuilles jaunes (tombées) pour la tension; latex pour les brûlures légères."
    },
    "Mangifera indica": {
        "local_name": "Mango",
        "family": "Anacardiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diarrhée", "fièvre", "maux de gorge"],
        "recommendations": "Décoction de l'écorce ou des jeunes feuilles; fruit riche en vitamine A et C."
    },

    # ================================
    # Légumes et Racines (Vivres alimentaires)
    # ================================
    "Ipomoea batatas": {
        "local_name": "Patat",
        "family": "Convolvulaceae",
        "is_medicinal": True,
        "medicinal_uses": ["anémie", "constipation", "convalescence"],
        "recommendations": "Consommé bouilli ou au four; les feuilles (espina) sont riches en fer."
    },
    "Manihot esculenta": {
        "local_name": "Manyòk",
        "family": "Euphorbiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["problèmes de peau", "énergie", "digestion"],
        "recommendations": "Consommé après cuisson; la farine de manioc est utilisée en cataplasme pour certains abcès."
    },
    "Colocasia esculenta": {
        "local_name": "Malanga",
        "family": "Araceae",
        "is_medicinal": True,
        "medicinal_uses": ["gastrite", "digestion difficile"],
        "recommendations": "Râpé et cuit en acras ou bouilli; très doux pour l'estomac."
    },

    # ================================
    # Épices et Condiments
    # ================================
    "Capsicum chinense": {
        "local_name": "Piman bouk",
        "family": "Solanaceae",
        "is_medicinal": True,
        "medicinal_uses": ["rhumatisme", "digestion", "circulation sanguine"],
        "recommendations": "Consommé avec modération dans les plats; usage externe en friction (macéré dans l'alcool)."
    },
    "Cinnamomum verum": {
        "local_name": "Kanèl",
        "family": "Lauraceae",
        "is_medicinal": True,
        "medicinal_uses": ["grippe", "digestion", "douleurs menstruelles"],
        "recommendations": "Infusion de l'écorce; souvent mélangée au chocolat ou à l'avoine."
    },
    "Pimenta dioica": {
        "local_name": "Piman vèvèn",
        "family": "Myrtaceae",
        "is_medicinal": True,
        "medicinal_uses": ["douleurs musculaires", "rhumatisme", "gaz intestinaux"],
        "recommendations": "Décoction des feuilles ou des graines (poivre de la Jamaïque)."
    },

    # ================================
    # Autres Plantes Locales
    # ================================
    "Ricinus communis": {
        "local_name": "Maskriti",
        "family": "Euphorbiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["constipation sévère", "soins des cheveux", "douleurs musculaires"],
        "recommendations": "Huile extraite des graines (Lwil Maskriti) en application externe ou purgatif léger."
    },
    "Momordica charantia": {
        "local_name": "Asowosi",
        "family": "Cucurbitaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diabète", "infections cutanées", "purification du sang", "fièvre"],
        "recommendations": "Infusion des feuilles (très amer); bain pour les problèmes de peau."
    },
    "Catharanthus roseus": {
        "local_name": "Pervenche / Katran",
        "family": "Apocynaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diabète", "hypertension", "infections oculaires"],
        "recommendations": "Infusion légère des fleurs ou feuilles. Attention : toxique à forte dose."
    },
    "Stachytarpheta jamaicensis": {
        "local_name": "Vervein",
        "family": "Verbenaceae",
        "is_medicinal": True,
        "medicinal_uses": ["fièvre", "rhume", "infections"],
        "recommendations": "Infusion des feuilles pour les rhumes et fièvres."
    },
    "Zingiber officinale": {
        "local_name": "Jenjanm",
        "family": "Zingiberaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "nausées", "infections respiratoires", "inflammation"],
        "recommendations": "Décoction ou infusion du rhizome; ajout dans les repas."
    },
    "Pluchea carolinensis": {
        "local_name": "Djeritout",
        "family": "Asteraceae",
        "is_medicinal": True,
        "medicinal_uses": ["infections", "problèmes digestifs"],
        "recommendations": "Infusion des feuilles ou bain médicinal."
    },
    "Cissus verticillata": {
        "local_name": "Liann brilan",
        "family": "Vitaceae",
        "is_medicinal": True,
        "medicinal_uses": ["fractures", "douleurs articulaires", "inflammation"],
        "recommendations": "Cataplasme des feuilles; décoction à boire."
    },
    "Eupatorium odoratum": {
        "local_name": "Bwa fèy dantèl",
        "family": "Asteraceae",
        "is_medicinal": True,
        "medicinal_uses": ["fièvre", "infections", "douleurs légères"],
        "recommendations": "Infusion ou décoction des feuilles."
    },
    "Bidens pilosa": {
        "local_name": "Zèb zédjui",
        "family": "Asteraceae",
        "is_medicinal": True,
        "medicinal_uses": ["infections cutanées", "fièvre", "digestion"],
        "recommendations": "Cataplasme pour blessures; infusion pour fièvre."
    },


    # ============================================================
    # CATEGORIE : ARBRES FRUITIERS (ALIMENTAIRES ET MÉDICINAUX)
    # ============================================================
    "Anacardium occidentale": {
        "local_name": "Ponm kajou / Nwa kajou",
        "family": "Anacardiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["maux de gorge", "diarrhée", "verrues", "hypertension"],
        "recommendations": "Le jus du fruit frais pour la gorge; infusion de l'écorce pour la diarrhée; huile de la coque pour les verrues."
    },
    "Chrysophyllum cainito": {
        "local_name": "Kaymit",
        "family": "Sapotaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diarrhée", "diabète léger", "douleurs articulaires"],
        "recommendations": "Décoction des feuilles séchées pour le diabète; consommation du fruit pour ses antioxydants."
    },
    "Melicoccus bijugatus": {
        "local_name": "Kinep",
        "family": "Sapindaceae",
        "is_medicinal": True,
        "medicinal_uses": ["insomnie", "constipation", "parasites"],
        "recommendations": "Les graines grillées sont parfois utilisées contre la diarrhée; le fruit est riche en fibres."
    },
    "Tamarindus indica": {
        "local_name": "Tamarin",
        "family": "Fabaceae",
        "is_medicinal": True,
        "medicinal_uses": ["laxatif", "fièvre", "maux de tête", "digestion"],
        "recommendations": "Pulpe du fruit en boisson (rafraîchissant et laxatif); infusion des feuilles pour la fièvre."
    },
    "Persea americana": {
        "local_name": "Zaboka",
        "family": "Lauraceae",
        "is_medicinal": True,
        "medicinal_uses": ["hypertension", "cholestérol", "douleurs menstruelles", "soins capillaires"],
        "recommendations": "Infusion de la feuille pour la tension; noyau râpé en alcool pour frictionner les douleurs."
    },
    "Carica papaya": {
        "local_name": "Papay",
        "family": "Caricaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "vers intestinaux", "cicatrisation", "hypertension"],
        "recommendations": "Graines consommées pour les parasites; latex (lait papaye) pour les callosités; fruit pour la digestion."
    },
    "Spondias mombin": {
        "local_name": "Monben",
        "family": "Anacardiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["infections vaginales", "inflammation", "diarrhée"],
        "recommendations": "Décoction des feuilles en bain de siège ou à boire."
    },

    # ============================================================
    # CATEGORIE : PLANTES UTILISÉES POUR LE DIABÈTE (TRADITION)
    # ============================================================
    "Cucurbita moschata": {
        "local_name": "Jiraumon / Joumou",
        "family": "Cucurbitaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diabète", "prostate", "parasites"],
        "recommendations": "Les graines sont excellentes pour la prostate; la chair aide à réguler la glycémie."
    },
    "Bixa orellana": {
        "local_name": "Woucou",
        "family": "Bixaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diabète", "problèmes de peau", "hépatite"],
        "recommendations": "Infusion des feuilles pour abaisser le taux de sucre; graines utilisées comme colorant alimentaire sain."
    },
    "Opuntia ficus-indica": {
        "local_name": "Rakèt",
        "family": "Cactaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diabète", "cholestérol", "inflammation cutanée"],
        "recommendations": "La chair de la raquette (sans épines) est consommée en jus ou bouillie pour le sucre."
    },
    "Neurolaena lobata": {
        "local_name": "Zèb a pik",
        "family": "Asteraceae",
        "is_medicinal": True,
        "medicinal_uses": ["diabète", "paludisme", "grippe", "digestion"],
        "recommendations": "Infusion des feuilles (très amère). Très puissant pour nettoyer le système."
    },
    


    # ============================================================
    # CATEGORIE : LÉGUMES, CÉRÉALES ET VIVRES (ALIMENTATION DE BASE)
    # ============================================================
    "Oryza sativa": {
        "local_name": "Diri",
        "family": "Poaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diarrhée", "inflammation cutanée", "énergie"],
        "recommendations": "L'eau de riz (dlo diri) est utilisée contre la diarrhée; la poudre de riz pour apaiser les irritations de la peau."
    },
    "Zea mays": {
        "local_name": "Mayi",
        "family": "Poaceae",
        "is_medicinal": True,
        "medicinal_uses": ["rétention d'eau", "problèmes rénaux", "cystite"],
        "recommendations": "Décoction des 'cheveux de maïs' (barbe de maïs) comme puissant diurétique."
    },
    "Saccharum officinarum": {
        "local_name": "Kann",
        "family": "Poaceae",
        "is_medicinal": True,
        "medicinal_uses": ["ictère (jaunisse)", "énergie", "toux"],
        "recommendations": "Jus frais pour l'énergie; sirop de canne pour les remèdes contre la toux."
    },
    "Phaseolus vulgaris": {
        "local_name": "Pwa nwa / Pwa rouj",
        "family": "Fabaceae",
        "is_medicinal": True,
        "medicinal_uses": ["anémie", "convalescence", "santé cardiaque"],
        "recommendations": "Consommé en sauce (sòs pwa) pour sa haute teneur en fer et protéines."
    },
    "Cajanus cajan": {
        "local_name": "Pwa kongo",
        "family": "Fabaceae",
        "is_medicinal": True,
        "medicinal_uses": ["maux de gorge", "diarrhée", "hypertension"],
        "recommendations": "Infusion des feuilles pour les gargarismes; graines très nutritives."
    },
    "Dioscorea alata": {
        "local_name": "Yanm",
        "family": "Dioscoreaceae",
        "is_medicinal": True,
        "medicinal_uses": ["équilibre hormonal", "ménopause", "énergie"],
        "recommendations": "Consommé bouilli; contient de la diosgénine utile pour le système hormonal."
    },
    "Solanum melongena": {
        "local_name": "Berejèn",
        "family": "Solanaceae",
        "is_medicinal": True,
        "medicinal_uses": ["cholestérol", "perte de poids", "problèmes hépatiques"],
        "recommendations": "Eau de macération de la peau de l'aubergine pour aider à réduire le cholestérol."
    },

    # ============================================================
    # CATEGORIE : TONIQUES, IMMUNITÉ ET FORTIFIANTS
    # ============================================================
    "Petiveria alliacea": {
        "local_name": "Fey douvan / Koulyè",
        "family": "Petiveriaceae",
        "is_medicinal": True,
        "medicinal_uses": ["immunité", "rhumatisme", "sinusite", "grippe"],
        "recommendations": "Infusion ou macération dans l'alcool; très réputé pour 'renforcer le sang'."
    },
    "Justicia secunda": {
        "local_name": "San-m-ba-yo / Saint-Jean",
        "family": "Acanthaceae",
        "is_medicinal": True,
        "medicinal_uses": ["anémie", "règles douloureuses", "fatigue"],
        "recommendations": "Infusion des feuilles qui colore l'eau en rouge; utilisé pour fortifier le système sanguin."
    },
    "Quassia amara": {
        "local_name": "Bwa lamer / Kasi",
        "family": "Simaroubaceae",
        "is_medicinal": True,
        "medicinal_uses": ["fièvre", "manque d'appétit", "parasites", "digestion"],
        "recommendations": "Macération de petits morceaux de bois dans l'eau froide; tonique amer très puissant."
    },
    "Hamelia patens": {
        "local_name": "Koko chat",
        "family": "Rubiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["cicatrisation", "infections cutanées", "douleurs"],
        "recommendations": "Écraser les feuilles sur les plaies ou infuser pour laver les blessures."
    },
    "Hibiscus sabdariffa": {
        "local_name": "Asòl / Choublak wouj (Hibiscus)",
        "family": "Malvaceae",
        "is_medicinal": True,
        "medicinal_uses": ["hypertension", "vitamine C", "digestion"],
        "recommendations": "Infusion des calices séchés (Jus de Bissap/Asòl) pour faire baisser la tension."
    },
    "Plectranthus amboinicus": {
        "local_name": "Gwo bonm",
        "family": "Lamiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["toux grasse", "bronchite", "digestion"],
        "recommendations": "Infusion des feuilles charnues; très efficace contre les congestions pulmonaires."
    },

    # ============================================================
    # CATEGORIE : PLANTES SAUVAGES ET HERBES DES CHAMPS
    # ============================================================
    "Argemone mexicana": {
        "local_name": "Chardon béni / Chadon beni",
        "family": "Papaveraceae",
        "is_medicinal": True,
        "medicinal_uses": ["insomnie", "douleurs", "toux", "problèmes de peau"],
        "recommendations": "Infusion des feuilles avec précaution; le latex jaune est utilisé pour les verrues."
    },
    "Portulaca oleracea": {
        "local_name": "Pourpier / Pourpiye",
        "family": "Portulacaceae",
        "is_medicinal": True,
        "medicinal_uses": ["inflammation", "parasites", "vitamines", "brûlures"],
        "recommendations": "Consommé en salade ou bouilli; cataplasme de la plante écrasée pour apaiser la peau."
    },
    "Chenopodium ambrosioides": {
        "local_name": "Semèn kontra",
        "family": "Amaranthaceae",
        "is_medicinal": True,
        "medicinal_uses": ["vers intestinaux", "douleurs d'estomac", "grippe"],
        "recommendations": "Infusion des feuilles; très puissant vermifuge (ne pas abuser des doses)."
    },
    "Leonotis nepetifolia": {
        "local_name": "Gwo tèt / Chandi",
        "family": "Lamiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["fièvre", "rhumatisme", "toux", "problèmes de peau"],
        "recommendations": "Infusion de la tête florale ou des feuilles; utilisé aussi en bain médicinal."
    },
    "Mimosa pudica": {
        "local_name": "Honte / Manman pitit",
        "family": "Fabaceae",
        "is_medicinal": True,
        "medicinal_uses": ["insomnie", "nervosité", "infections urinaires"],
        "recommendations": "Décoction des racines ou infusion des feuilles pour calmer l'agitation."
    },

    # ============================================================
    # CATEGORIE : SANTÉ DES FEMMES (MATERNITÉ, RÈGLES, POST-PARTUM)
    # ============================================================
    "Gossypium barbadense": {
        "local_name": "Koton",
        "family": "Malvaceae",
        "is_medicinal": True,
        "medicinal_uses": ["hypertension", "règles irrégulières", "post-partum"],
        "recommendations": "Infusion des jeunes feuilles pour régulariser le cycle ou après l'accouchement."
    },
    "Leonurus sibiricus": {
        "local_name": "Gwo vèvèn / Agripa",
        "family": "Lamiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["règles douloureuses", "circulation", "ménopause"],
        "recommendations": "Infusion des feuilles pour calmer les douleurs utérines."
    },
    "Ruta graveolens": {
        "local_name": "Ri / Rue",
        "family": "Rutaceae",
        "is_medicinal": True,
        "medicinal_uses": ["règles retardées", "maux de tête", "parasites"],
        "recommendations": "Infusion très légère (plante forte); souvent macérée dans l'alcool pour les frictions."
    },
    "Artemisia vulgaris": {
        "local_name": "Armoise / Amwaz",
        "family": "Asteraceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "règles douloureuses", "tonique"],
        "recommendations": "Infusion des sommités fleuries pour stimuler l'appétit ou apaiser les crampes."
    },
    "Ricinus communis (Variété rouge)": {
        "local_name": "Maskriti wouj",
        "family": "Euphorbiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["massage post-partum", "douleurs musculaires", "cheveux"],
        "recommendations": "L'huile est chauffée et utilisée pour masser le ventre des nouvelles mères (pratique traditionnelle)."
    },

    # ============================================================
    # CATEGORIE : CONDIMENTS ET ÉPICES ADDITIONNELLES
    # ============================================================
    "Coriandrum sativum": {
        "local_name": "Koryand / Pèsi etranje",
        "family": "Apiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "gaz", "détoxification"],
        "recommendations": "Ajouté frais dans les repas ou infusion des graines."
    },
    "Pimpinella anisum": {
        "local_name": "Lanni / Anis étoilé",
        "family": "Apiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["coliques infantiles", "gaz", "toux"],
        "recommendations": "Infusion très légère pour les bébés ayant des gaz; utilisé dans le café en Haïti."
    },
    # ============================================================
    # CATEGORIE : BOIS MÉDICINAUX (POUR DÉCOCTIONS ET "TRANPE")
    # ============================================================
    "Guaiacum officinale": {
        "local_name": "Bwa gayak",
        "family": "Zygophyllaceae",
        "is_medicinal": True,
        "medicinal_uses": ["syphilis", "rhumatisme", "inflammation", "sudorifique"],
        "recommendations": "Utilisation de la résine ou copeaux de bois en décoction longue pour purifier le sang."
    },
    "Amyris balsamifera": {
        "local_name": "Bwa chandèl / Sandal",
        "family": "Rutaceae",
        "is_medicinal": True,
        "medicinal_uses": ["stress", "insomnie", "douleurs musculaires"],
        "recommendations": "L'huile essentielle ou le bois brûlé pour la relaxation; décoction légère pour le calme."
    },
    "Haematoxylum campechianum": {
        "local_name": "Bwa kanpèch",
        "family": "Fabaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diarrhée", "hémorragie", "anémie"],
        "recommendations": "Décoction du bois de cœur (donne une eau rouge/violette); utilisé comme astringent puissant."
    },
    "Simarouba glauca": {
        "local_name": "Frèn / Bwa blan",
        "family": "Simaroubaceae",
        "is_medicinal": True,
        "medicinal_uses": ["dysenterie", "paludisme", "fièvre"],
        "recommendations": "Décoction de l'écorce amère; réputé pour nettoyer les intestins."
    },
    "Cedrela odorata": {
        "local_name": "Sèd",
        "family": "Meliaceae",
        "is_medicinal": True,
        "medicinal_uses": ["douleurs articulaires", "fièvre", "problèmes respiratoires"],
        "recommendations": "Infusion de l'écorce ou des feuilles; utilisé aussi en bain de vapeur."
    },

    # ============================================================
    # CATEGORIE : ORNEMENTALES AUX VERTUS CACHÉES
    # ============================================================
    "Nerium oleander": {
        "local_name": "Lorye roz",
        "family": "Apocynaceae",
        "is_medicinal": True,
        "medicinal_uses": ["maladies de peau", "gale", "problèmes cardiaques (très risqué)"],
        "recommendations": "ATTENTION TOXIQUE. Usage externe uniquement en décoction pour laver les infections cutanées."
    },
    "Bougainvillea glabra": {
        "local_name": "Bugenvilye / Trinitè",
        "family": "Nyctaginaceae",
        "is_medicinal": True,
        "medicinal_uses": ["toux", "bronchite", "coqueluche"],
        "recommendations": "Infusion des bractées (les 'fleurs' colorées) pour apaiser les voies respiratoires."
    },
    "Catharanthus roseus (variété blanche)": {
        "local_name": "Katran blan",
        "family": "Apocynaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diabète", "hypertension", "nettoyage des yeux"],
        "recommendations": "Infusion des fleurs pour stabiliser le sucre dans le sang."
    },
    "Plumeria alba": {
        "local_name": "Franjipan / Pye frenn",
        "family": "Apocynaceae",
        "is_medicinal": True,
        "medicinal_uses": ["verrues", "douleurs dentaires", "rhumatisme"],
        "recommendations": "Le latex blanc est appliqué localement sur les verrues; infusion d'écorce pour les articulations."
    },
    "Mirabilis jalapa": {
        "local_name": "Bèl de nui",
        "family": "Nyctaginaceae",
        "is_medicinal": True,
        "medicinal_uses": ["purgatif", "inflammation", "cicatrisation"],
        "recommendations": "La racine est un purgatif fort; les feuilles écrasées s'utilisent sur les abcès."
    },

    # ============================================================
# NOUVELLES PLANTES LOCALES HAÏTIENNES (exemple initial)
# ============================================================
"Ficus citrifolia": {
    "local_name": "Figi bwa",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "infections cutanées", "anti-inflammatoire"],
    "recommendations": "Décoction des feuilles pour apaiser les douleurs; cataplasme pour les plaies."
},
"Chrysobalanus icaco": {
    "local_name": "Prunier bò lanmè",
    "family": "Chrysobalanaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diarrhée", "infections intestinales"],
    "recommendations": "Infusion de l'écorce ou des fruits; consommation des fruits mûrs."
},
"Coccoloba diversifolia": {
    "local_name": "Rezen bwa",
    "family": "Polygonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "inflammation"],
    "recommendations": "Décoction des feuilles pour réduire la fièvre."
},
"Typha domingensis": {
    "local_name": "Roseau marécage",
    "family": "Typhaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diurétique", "soins cutanés"],
    "recommendations": "Infusion des feuilles pour faciliter la miction; cataplasme pour les irritations."
},
"Eichhornia crassipes": {
    "local_name": "Jacinthe d'eau",
    "family": "Pontederiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["purification sanguine", "inflammation"],
    "recommendations": "Infusion des feuilles pour nettoyer le système; usage externe pour inflammations."
},
"Psychotria poeppigiana": {
    "local_name": "Bois de fièvre",
    "family": "Rubiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "maladies respiratoires"],
    "recommendations": "Décoction des feuilles pour réduire la fièvre; inhalation pour les rhumes."
},
"Coffea arabica": {
    "local_name": "Kafe bwa",
    "family": "Rubiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fatigue", "stimulation", "antioxydant"],
    "recommendations": "Infusion des feuilles ou graines grillées; modération recommandée."
},
"Calotropis procera": {
    "local_name": "Bwa lanmò / Fèt bwa",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["douleurs articulaires", "problèmes de peau"],
    "recommendations": "Latex appliqué avec précaution sur les plaies; décoction des feuilles pour les douleurs."
},
"Hibiscus rosa-sinensis": {
    "local_name": "Hibiscus jòn",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "hypertension", "soins capillaires"],
    "recommendations": "Infusion des fleurs pour la tension; cataplasme pour le cuir chevelu."
},
"Xanthosoma sagittifolium": {
    "local_name": "Taro / Malanga",
    "family": "Araceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "constipation", "énergie"],
    "recommendations": "Racine bouillie ou écrasée en purée; feuilles cuites comme légume riche en fer."
},
# ============================================================
# NOUVELLES PLANTES LOCALES HAÏTIENNES (1–50)
# ============================================================
"Ficus citrifolia": {
    "local_name": "Figi bwa",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "infections cutanées", "anti-inflammatoire"],
    "recommendations": "Décoction des feuilles pour apaiser les douleurs; cataplasme pour les plaies."
},
"Chrysobalanus icaco": {
    "local_name": "Prunier bò lanmè",
    "family": "Chrysobalanaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diarrhée", "infections intestinales"],
    "recommendations": "Infusion de l'écorce ou des fruits; consommation des fruits mûrs."
},
"Coccoloba diversifolia": {
    "local_name": "Rezen bwa",
    "family": "Polygonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "inflammation"],
    "recommendations": "Décoction des feuilles pour réduire la fièvre."
},
"Typha domingensis": {
    "local_name": "Roseau marécage",
    "family": "Typhaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diurétique", "soins cutanés"],
    "recommendations": "Infusion des feuilles pour faciliter la miction; cataplasme pour les irritations."
},
"Eichhornia crassipes": {
    "local_name": "Jacinthe d'eau",
    "family": "Pontederiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["purification sanguine", "inflammation"],
    "recommendations": "Infusion des feuilles pour nettoyer le système; usage externe pour inflammations."
},
"Psychotria poeppigiana": {
    "local_name": "Bois de fièvre",
    "family": "Rubiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "maladies respiratoires"],
    "recommendations": "Décoction des feuilles pour réduire la fièvre; inhalation pour les rhumes."
},
"Coffea arabica": {
    "local_name": "Kafe bwa",
    "family": "Rubiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fatigue", "stimulation", "antioxydant"],
    "recommendations": "Infusion des feuilles ou graines grillées; modération recommandée."
},
"Calotropis procera": {
    "local_name": "Bwa lanmò / Fèt bwa",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["douleurs articulaires", "problèmes de peau"],
    "recommendations": "Latex appliqué avec précaution sur les plaies; décoction des feuilles pour les douleurs."
},
"Hibiscus rosa-sinensis": {
    "local_name": "Hibiscus jòn",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "hypertension", "soins capillaires"],
    "recommendations": "Infusion des fleurs pour la tension; cataplasme pour le cuir chevelu."
},
"Xanthosoma sagittifolium": {
    "local_name": "Taro / Malanga",
    "family": "Araceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "constipation", "énergie"],
    "recommendations": "Racine bouillie ou écrasée en purée; feuilles cuites comme légume riche en fer."
},
"Ficus citrifolia var. minor": {
    "local_name": "Figi bwa ti",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "soins cutanés"],
    "recommendations": "Décoction des jeunes feuilles; cataplasme pour blessures légères."
},
"Passiflora foetida": {
    "local_name": "Passiflò",
    "family": "Passifloraceae",
    "is_medicinal": True,
    "medicinal_uses": ["insomnie", "stress", "calmant nerveux"],
    "recommendations": "Infusion des feuilles et fleurs pour relaxer et dormir."
},
"Momordica charantia var. haitiensis": {
    "local_name": "Asowosi haïtien",
    "family": "Cucurbitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "purification du sang"],
    "recommendations": "Infusion des feuilles pour réguler la glycémie; très amer."
},
"Gymnema sylvestre": {
    "local_name": "Gimnema",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "appétit", "digestion"],
    "recommendations": "Infusion des feuilles pour réguler le sucre; prise modérée."
},
"Ficus elastica": {
    "local_name": "Figi kawotchou",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "cicatrisation"],
    "recommendations": "Latex appliqué localement sur petites blessures."
},
"Tabebuia rosea": {
    "local_name": "Bwa rouj",
    "family": "Bignoniaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "rhume"],
    "recommendations": "Décoction de l’écorce pour réduire la fièvre."
},
"Stachytarpheta jamaicensis var. minor": {
    "local_name": "Vervein ti",
    "family": "Verbenaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "rhume"],
    "recommendations": "Infusion des feuilles pour les symptômes de rhume."
},
"Chamaesyce hirta": {
    "local_name": "Ti zèb pikan",
    "family": "Euphorbiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections respiratoires", "fièvre"],
    "recommendations": "Infusion des feuilles; modération car plante forte."
},
"Annona reticulata": {
    "local_name": "Anona",
    "family": "Annonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["insomnie", "stress"],
    "recommendations": "Feuilles en infusion pour calmer le système nerveux."
},
"Zingiber zerumbet": {
    "local_name": "Jenjanm bwa",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "douleurs musculaires"],
    "recommendations": "Décoction du rhizome; application externe possible."
},
"Vernonia cinerea": {
    "local_name": "Zèb vènn",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "rhumatisme"],
    "recommendations": "Infusion des feuilles; usage traditionnel pour fièvre."
},
"Jatropha gossypiifolia": {
    "local_name": "Ti bwa gossipi",
    "family": "Euphorbiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections cutanées", "douleurs musculaires"],
    "recommendations": "Infusion des feuilles; application externe pour douleurs."
},
"Cestrum nocturnum": {
    "local_name": "Fleur nuit",
    "family": "Solanaceae",
    "is_medicinal": True,
    "medicinal_uses": ["insomnie", "relaxation"],
    "recommendations": "Infusion des fleurs pour calmer et faciliter le sommeil."
},
"Solanum torvum": {
    "local_name": "Ti piman solan",
    "family": "Solanaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hypertension", "digestion"],
    "recommendations": "Décoction des jeunes branches; utilisé en sauce ou infusion."
},
"Achyranthes aspera": {
    "local_name": "Zèb pwa",
    "family": "Amaranthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["douleurs articulaires", "inflammation"],
    "recommendations": "Infusion des racines ou feuilles pour douleurs musculaires."
},
"Hibiscus acetosella": {
    "local_name": "Asòl wouj",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hypertension", "digestion"],
    "recommendations": "Infusion des feuilles; consommé en salade pour effet doux."
},
"Piper aduncum": {
    "local_name": "Ti piman piper",
    "family": "Piperaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections respiratoires", "rhumatisme"],
    "recommendations": "Infusion des feuilles; inhalation pour congestion."
},
"Phyllanthus amarus": {
    "local_name": "Ti pye bwa fèy vèt",
    "family": "Phyllanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "diabète", "digestion"],
    "recommendations": "Décoction des feuilles pour soutien hépatique."
},
"Terminalia catappa": {
    "local_name": "Bwa mango bò lanmè",
    "family": "Combretaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections cutanées", "fièvre"],
    "recommendations": "Infusion des feuilles pour peau et fièvre."
},
"Solanum torvum var. minor": {
    "local_name": "Ti solan",
    "family": "Solanaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "hypertension"],
    "recommendations": "Jeunes branches en infusion; petites doses."
},
"Jasminum grandiflorum": {
    "local_name": "Jasmen",
    "family": "Oleaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "insomnie"],
    "recommendations": "Infusion des fleurs pour calmer et dormir."
},
"Phyllanthus niruri var. minor": {
    "local_name": "Ti pye bwa ti",
    "family": "Phyllanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["calculs rénaux", "digestion"],
    "recommendations": "Décoction légère des feuilles pour nettoyage des reins."
},
"Melastoma malabathricum": {
    "local_name": "Zèb wouj",
    "family": "Melastomataceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "plaies"],
    "recommendations": "Feuilles écrasées appliquées sur blessures; infusion pour inflammation."
},
"Alpinia galanga": {
    "local_name": "Galanga",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "inflammation"],
    "recommendations": "Décoction ou ajout aux repas; rhizome frais ou séché."
},
"Centella asiatica": {
    "local_name": "Zèb gerizon",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["cicatrisation", "circulation"],
    "recommendations": "Infusion des feuilles; cataplasme sur plaies."
},
"Clinopodium vulgare": {
    "local_name": "Zèb mant",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "rhumatisme"],
    "recommendations": "Infusion des feuilles; inhalation ou cataplasme."
},
"Thunbergia grandiflora": {
    "local_name": "Fleur bleu",
    "family": "Acanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "inflammation"],
    "recommendations": "Infusion des feuilles et fleurs; bain médicinal."
},
"Cissus quadrangularis": {
    "local_name": "Liann bwa",
    "family": "Vitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fractures", "douleurs articulaires"],
    "recommendations": "Cataplasme des tiges; décoction pour boire."
},
# ============================================================
# NOUVELLES PLANTES LOCALES HAÏTIENNES (51–100)
# ============================================================
"Terminalia arjuna": {
    "local_name": "Bwa arjuna",
    "family": "Combretaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hypertension", "problèmes cardiaques"],
    "recommendations": "Décoction de l’écorce pour le cœur et la tension."
},
"Alpinia officinarum": {
    "local_name": "Galanga officinale",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "anti-inflammatoire"],
    "recommendations": "Infusion du rhizome; utilisé dans les plats épicés."
},
"Ocimum gratissimum": {
    "local_name": "Basilik Afriken",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["rhume", "infections respiratoires"],
    "recommendations": "Infusion des feuilles; inhalation pour dégager les voies respiratoires."
},
"Plectranthus amboinicus var. minor": {
    "local_name": "Ti gwo bonm",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["toux", "bronchite"],
    "recommendations": "Infusion des petites feuilles; usage traditionnel pour congestion pulmonaire."
},
"Blighia sapida": {
    "local_name": "Ackee",
    "family": "Sapindaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "fatigue"],
    "recommendations": "Consommation des fruits mûrs; graines non comestibles."
},
"Fumaria officinalis": {
    "local_name": "Zèb la fumée",
    "family": "Papaveraceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "digestion"],
    "recommendations": "Infusion des feuilles; modération nécessaire."
},
"Centrosema pubescens": {
    "local_name": "Pois liane",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "anémie"],
    "recommendations": "Infusion des feuilles; utilisé en alimentation locale."
},
"Eleutherine bulbosa": {
    "local_name": "Zanmann",
    "family": "Iridaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infection urinaire", "digestion"],
    "recommendations": "Décoction du bulbe; modération pour usage interne."
},
"Passiflora incarnata": {
    "local_name": "Passiflò bleu",
    "family": "Passifloraceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "insomnie"],
    "recommendations": "Infusion des feuilles et fleurs pour relaxer."
},
"Annona squamosa": {
    "local_name": "Zaboka sukré",
    "family": "Annonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète léger", "stress"],
    "recommendations": "Infusion des feuilles; fruit consommé frais."
},
"Vernonia amygdalina": {
    "local_name": "Zèb amère",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "infections"],
    "recommendations": "Infusion des feuilles; goût très amer mais efficace."
},
"Guazuma ulmifolia": {
    "local_name": "Bwa kafe",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diarrhée", "digestion"],
    "recommendations": "Infusion de l’écorce ou feuilles pour digestion difficile."
},
"Scoparia dulcis": {
    "local_name": "Zèb ti dous",
    "family": "Plantaginaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "diabète"],
    "recommendations": "Infusion des feuilles; usage traditionnel."
},
"Achillea millefolium": {
    "local_name": "Acilè",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "fièvre", "cicatrisation"],
    "recommendations": "Infusion des feuilles; cataplasme sur petites blessures."
},
"Eleutherococcus senticosus": {
    "local_name": "Ginseng sibérien",
    "family": "Araliaceae",
    "is_medicinal": True,
    "medicinal_uses": ["immunité", "énergie"],
    "recommendations": "Infusion racinaire; tonique énergétique."
},
"Sesbania grandiflora": {
    "local_name": "Fleur arbre légume",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "infections"],
    "recommendations": "Infusion des feuilles et fleurs; bouilli pour légume nutritif."
},
"Lantana camara": {
    "local_name": "Zèb flè wòj",
    "family": "Verbenaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections cutanées", "fièvre"],
    "recommendations": "Infusion des feuilles; usage externe pour plaies."
},
"Azadirachta indica": {
    "local_name": "Neem / Margosa",
    "family": "Meliaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections", "diabète", "peau"],
    "recommendations": "Infusion des feuilles; pâte pour usage cutané."
},
"Vitex trifolia": {
    "local_name": "Gwo vèvèn bwa",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["règles douloureuses", "digestion"],
    "recommendations": "Infusion des feuilles pour douleurs menstruelles."
},
"Hibiscus tiliaceus": {
    "local_name": "Bwa hibiscus",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "fièvre"],
    "recommendations": "Infusion des feuilles; cataplasme pour douleurs locales."
},
"Alocasia macrorrhizos": {
    "local_name": "Gwo malanga",
    "family": "Araceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "énergie"],
    "recommendations": "Racine bouillie; feuilles cuites pour apport nutritionnel."
},
"Cymbopogon nardus": {
    "local_name": "Citronnelle bois",
    "family": "Poaceae",
    "is_medicinal": True,
    "medicinal_uses": ["insecticide naturel", "stress"],
    "recommendations": "Infusion des feuilles; huile essentielle pour répulsif."
},
"Ficus benjamina": {
    "local_name": "Figi bò kay",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "stress"],
    "recommendations": "Infusion des feuilles pour détente; cataplasme local."
},
"Clitoria ternatea": {
    "local_name": "Pois bleu",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "mémoire"],
    "recommendations": "Infusion des fleurs pour mémoire et relaxation."
},
"Piper nigrum": {
    "local_name": "Piman nwa",
    "family": "Piperaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "circulation"],
    "recommendations": "Graines ou poudre dans les repas; infusion des feuilles pour digestion."
},
"Tephrosia vogelii": {
    "local_name": "Zèb pike",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["insecticide naturel", "fièvre"],
    "recommendations": "Infusion des feuilles; usage traditionnel pour fièvre."
},
"Pluchea sagittalis": {
    "local_name": "Djeritout bò lanmè",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "fièvre"],
    "recommendations": "Infusion des feuilles; cataplasme possible."
},
"Adansonia digitata": {
    "local_name": "Baobab",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["vitamine C", "digestion"],
    "recommendations": "Pulpe des fruits; infusion des feuilles pour digestion."
},
"Rauvolfia serpentina": {
    "local_name": "Rauvolfia",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hypertension", "stress"],
    "recommendations": "Infusion des racines; usage strictement contrôlé."
},
"Crotalaria retusa": {
    "local_name": "Zèb pike koulè",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections", "digestion"],
    "recommendations": "Infusion des feuilles; usage local pour troubles digestifs."
},
"Barringtonia asiatica": {
    "local_name": "Fey lanmè",
    "family": "Lecythidaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections cutanées", "fièvre"],
    "recommendations": "Infusion des feuilles; cataplasme sur peau irritée."
},

# ============================================================
# NOUVELLES PLANTES LOCALES HAÏTIENNES (101–150)
# ============================================================
"Momordica balsamina": {
    "local_name": "Asowosi bwa",
    "family": "Cucurbitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "infections cutanées"],
    "recommendations": "Infusion des feuilles; bain ou décoction pour usage cutané."
},
"Vitex agnus-castus": {
    "local_name": "Chasteberry",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["règles douloureuses", "hormonal"],
    "recommendations": "Infusion des feuilles ou baies; traditionnel pour réguler le cycle menstruel."
},
"Eclipta prostrata": {
    "local_name": "Zèb cheve",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["soins capillaires", "foie"],
    "recommendations": "Infusion des feuilles; huile pour cheveux."
},
"Phyllanthus amarus": {
    "local_name": "Ti pye bwa fèy dwat",
    "family": "Phyllanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "hépatite"],
    "recommendations": "Décoction des tiges et feuilles; consommation modérée."
},
"Artemisia absinthium": {
    "local_name": "Absinthe",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "tonique amer"],
    "recommendations": "Infusion très légère; usage interne limité."
},
"Crateva religiosa": {
    "local_name": "Bwa balanse",
    "family": "Capparaceae",
    "is_medicinal": True,
    "medicinal_uses": ["rein", "digestion"],
    "recommendations": "Infusion des feuilles ou racines pour usage traditionnel."
},
"Momordica dioica": {
    "local_name": "Asowosi liane",
    "family": "Cucurbitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "digestion"],
    "recommendations": "Infusion des feuilles ou jeunes fruits bouillis."
},
"Cassia alata": {
    "local_name": "Zèb kòk",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections cutanées", "mycoses"],
    "recommendations": "Cataplasme des feuilles écrasées; infusion possible."
},
"Tabernaemontana divaricata": {
    "local_name": "Crape Jasmine",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "infections"],
    "recommendations": "Infusion des fleurs et feuilles; usage externe pour plaies."
},
"Cissus quadrangularis": {
    "local_name": "Liann bwa",
    "family": "Vitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fractures", "douleurs articulaires"],
    "recommendations": "Décoction des tiges; cataplasme sur os et articulations."
},
"Talinum paniculatum": {
    "local_name": "Zèb koray",
    "family": "Talinaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "digestion"],
    "recommendations": "Infusion des feuilles; utilisé en cataplasme local."
},
"Clerodendrum inerme": {
    "local_name": "Bwa lanmè",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections", "inflammation cutanée"],
    "recommendations": "Infusion des feuilles; cataplasme sur plaies."
},
"Rauvolfia tetraphylla": {
    "local_name": "Rauvolfia rouge",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hypertension", "stress"],
    "recommendations": "Infusion des racines; usage strictement contrôlé."
},
"Peperomia pellucida": {
    "local_name": "Zèb vèt",
    "family": "Piperaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "douleurs articulaires"],
    "recommendations": "Infusion ou cataplasme des feuilles."
},
"Eleutherine americana": {
    "local_name": "Zanmann bwa",
    "family": "Iridaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infection urinaire", "digestion"],
    "recommendations": "Décoction du bulbe; usage interne avec modération."
},
"Phyllanthus debilis": {
    "local_name": "Ti pye bwa debilis",
    "family": "Phyllanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "diabète"],
    "recommendations": "Décoction des feuilles et tiges; consommation modérée."
},
"Vernonia cinerea": {
    "local_name": "Zèb ble",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "diabète"],
    "recommendations": "Infusion des feuilles; modération nécessaire."
},
"Solanum torvum": {
    "local_name": "Ti Piman Fwi",
    "family": "Solanaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hypertension", "digestion"],
    "recommendations": "Infusion des feuilles; fruit utilisé dans sauces traditionnelles."
},
"Achyranthes aspera": {
    "local_name": "Zèb aspera",
    "family": "Amaranthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["douleurs articulaires", "fièvre"],
    "recommendations": "Décoction des feuilles; cataplasme ou infusion."
},
"Ficus racemosa": {
    "local_name": "Figi bwa",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "infections"],
    "recommendations": "Infusion des feuilles; cataplasme possible."
},
"Adhatoda vasica": {
    "local_name": "Zèb tèt kè",
    "family": "Acanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["toux", "bronchite"],
    "recommendations": "Infusion des feuilles pour voies respiratoires."
},
"Bridelia micrantha": {
    "local_name": "Bwa micrantha",
    "family": "Phyllanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diarrhée", "digestion"],
    "recommendations": "Décoction de l’écorce ou feuilles; consommation modérée."
},
"Gymnema sylvestre": {
    "local_name": "Zèb dous",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "digestion"],
    "recommendations": "Infusion des feuilles; utilisé pour réguler la glycémie."
},
"Artocarpus heterophyllus": {
    "local_name": "Jakfruit",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "énergie"],
    "recommendations": "Fruit consommé frais; feuilles en décoction pour troubles digestifs."
},
"Erythrina variegata": {
    "local_name": "Bwa zoranj",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["douleurs musculaires", "stress"],
    "recommendations": "Infusion des feuilles ou cataplasme des fleurs."
},
"Calotropis procera": {
    "local_name": "Zèb katwop",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["cicatrisation", "douleurs"],
    "recommendations": "Usage externe uniquement; latex appliqué sur blessures."
},
"Coccinia grandis": {
    "local_name": "Zèb konkonm",
    "family": "Cucurbitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "digestion"],
    "recommendations": "Feuilles et jeunes fruits en décoction."
},
"Moringa stenopetala": {
    "local_name": "Moringa long feuille",
    "family": "Moringaceae",
    "is_medicinal": True,
    "medicinal_uses": ["nutrition", "immunité"],
    "recommendations": "Feuilles séchées ou fraîches en infusion."
},
"Curcuma zedoaria": {
    "local_name": "Zedoaria",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "inflammation"],
    "recommendations": "Infusion ou ajout dans les plats; rhizome frais ou sec."
},
# ============================================================
# NOUVELLES PLANTES LOCALES HAÏTIENNES (151–200)
# ============================================================
"Psidium cattleianum": {
    "local_name": "Goyave rouge",
    "family": "Myrtaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diarrhée", "infections", "digestion"],
    "recommendations": "Infusion des feuilles; consommation du fruit pour vitamines."
},
"Syzygium cumini": {
    "local_name": "Jambolan",
    "family": "Myrtaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "digestion"],
    "recommendations": "Infusion des feuilles et écorce; fruits consommés frais ou secs."
},
"Annona reticulata": {
    "local_name": "Kowosòl blan",
    "family": "Annonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["insomnie", "nervosité"],
    "recommendations": "Infusion des feuilles pour calmer le système nerveux."
},
"Ficus benghalensis": {
    "local_name": "Banyan",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "inflammation"],
    "recommendations": "Infusion des feuilles; cataplasme des racines pour blessures."
},
"Ocimum sanctum": {
    "local_name": "Tulsi / Basilic sacré",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "immunité", "respiration"],
    "recommendations": "Infusion des feuilles; inhalation vapeur."
},
"Terminalia catappa": {
    "local_name": "Amandier indien",
    "family": "Combretaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hépatite", "infections cutanées"],
    "recommendations": "Infusion des feuilles; bain ou cataplasme."
},
"Senna occidentalis": {
    "local_name": "Séné de l'Ouest",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["constipation", "digestion"],
    "recommendations": "Infusion des feuilles ou graines; usage modéré."
},
"Alstonia scholaris": {
    "local_name": "Bwa Alstonia",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "infections respiratoires"],
    "recommendations": "Décoction de l'écorce; usage interne modéré."
},
"Morinda citrifolia": {
    "local_name": "Noni",
    "family": "Rubiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["immunité", "digestion", "douleurs"],
    "recommendations": "Jus du fruit; infusion des feuilles."
},
"Piper betle": {
    "local_name": "Feuille de bétel",
    "family": "Piperaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "soins buccaux"],
    "recommendations": "Mâcher la feuille; infusion pour maux de gorge."
},
"Justicia gendarussa": {
    "local_name": "Justicia sauvage",
    "family": "Acanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "douleurs articulaires"],
    "recommendations": "Infusion des feuilles; cataplasme externe."
},
"Tropaeolum majus": {
    "local_name": "Capucine",
    "family": "Tropaeolaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections urinaires", "immunité"],
    "recommendations": "Infusion des fleurs et feuilles; usage interne modéré."
},
"Cynara scolymus": {
    "local_name": "Artichaut",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "digestion", "cholestérol"],
    "recommendations": "Décoction des feuilles; consommation des bourgeons."
},
"Alpinia galanga": {
    "local_name": "Galanga",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "inflammation", "respiration"],
    "recommendations": "Décoction ou infusion du rhizome; ajout aux plats."
},
"Artocarpus camansi": {
    "local_name": "Jakfruit sauvage",
    "family": "Moraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "énergie"],
    "recommendations": "Fruit bouilli ou en décoction; feuilles pour troubles digestifs."
},
"Annona squamosa": {
    "local_name": "Pomme cannelle",
    "family": "Annonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["insomnie", "nervosité"],
    "recommendations": "Infusion des feuilles; fruit consommé frais."
},
"Gymnema sylvestre var.": {
    "local_name": "Zèb dous variant",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diabète", "digestion"],
    "recommendations": "Feuilles en infusion; fruit parfois utilisé."
},
"Calotropis gigantea": {
    "local_name": "Zèb katwop géant",
    "family": "Apocynaceae",
    "is_medicinal": True,
    "medicinal_uses": ["cicatrisation", "douleurs"],
    "recommendations": "Usage externe uniquement; latex appliqué sur blessures."
},
"Heliotropium indicum": {
    "local_name": "Zèb solèy",
    "family": "Boraginaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections cutanées", "inflammation"],
    "recommendations": "Infusion ou cataplasme des feuilles."
},
"Abelmoschus moschatus": {
    "local_name": "Musk Lalo",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "stimulation lactation"],
    "recommendations": "Infusion des graines ou feuilles; usage interne modéré."
},
"Hydrocotyle asiatica": {
    "local_name": "Centella asiatica",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["cicatrisation", "mémoire", "stress"],
    "recommendations": "Infusion des feuilles; cataplasme pour plaies."
},
"Cleome gynandra": {
    "local_name": "Zèb cléo",
    "family": "Cleomaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "inflammation cutanée"],
    "recommendations": "Feuilles bouillies ou en infusion."
},
"Phyllanthus urinaria": {
    "local_name": "Ti pye bwa urinaria",
    "family": "Phyllanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections urinaires", "foie"],
    "recommendations": "Décoction des feuilles et tiges; consommation modérée."
},
"Melia azedarach": {
    "local_name": "Mélia",
    "family": "Meliaceae",
    "is_medicinal": True,
    "medicinal_uses": ["parasites", "digestion"],
    "recommendations": "Décoction des feuilles; usage modéré et contrôlé."
},
"Eclipta alba": {
    "local_name": "Zèb cheve blanc",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["soins capillaires", "foie"],
    "recommendations": "Infusion des feuilles; huile pour cheveux."
},
"Ocimum kilimandscharicum": {
    "local_name": "Basilic camphré",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "respiration"],
    "recommendations": "Infusion des feuilles; inhalation ou ajout aux plats."
},

# ============================================================
# BASE MÉDICINALE GLOBALE – 500 PLANTES (format dictionnaire)
# ============================================================

"Adhatoda vasica": {
    "local_name": "Zèb bronchi",
    "family": "Acanthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["toux", "bronchite", "asthme"],
    "recommendations": "Infusion des feuilles pour soulager les voies respiratoires."
},
"Agave americana": {
    "local_name": "Agave",
    "family": "Asparagaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "soins de la peau"],
    "recommendations": "Gel appliqué sur brûlures; décoction des feuilles pour la digestion."
},
"Alisma plantago-aquatica": {
    "local_name": "Alisma",
    "family": "Alismataceae",
    "is_medicinal": True,
    "medicinal_uses": ["diurétique", "détox du foie"],
    "recommendations": "Infusion des racines; usage interne modéré."
},
"Allium ursinum": {
    "local_name": "Ail des ours",
    "family": "Amaryllidaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hypertension", "digestion"],
    "recommendations": "Feuilles en infusion ou ajout aux repas."
},
"Alnus glutinosa": {
    "local_name": "Aulne noir",
    "family": "Betulaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "soins cutanés"],
    "recommendations": "Décoction de l'écorce pour bains ou lotions."
},
"Alpinia officinarum": {
    "local_name": "Galanga officinal",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "anti‑inflammatoire"],
    "recommendations": "Infusion ou décoction du rhizome."
},
"Amaranthus cruentus": {
    "local_name": "Amarante",
    "family": "Amaranthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["anémie", "digestion"],
    "recommendations": "Feuilles bouillies ou en infusion."
},
"Ammi visnaga": {
    "local_name": "Ammi",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["respiration", "anti‑spasmodique"],
    "recommendations": "Infusion des graines pour spasmes musculaires."
},
"Angelica archangelica": {
    "local_name": "Angélique",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "stress"],
    "recommendations": "Infusion des racines ou feuilles."
},
"Anredera cordifolia": {
    "local_name": "Mazamorra",
    "family": "Basellaceae",
    "is_medicinal": True,
    "medicinal_uses": ["soins cutanés", "anti‑inflammatoire"],
    "recommendations": "Cataplasme des feuilles sur peaux irritées."
},
"Arbutus unedo": {
    "local_name": "Arbousier",
    "family": "Ericaceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections urinaires", "antioxydant"],
    "recommendations": "Infusion des feuilles; fruits consommés frais."
},
"Arctium lappa": {
    "local_name": "Bardane",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["peau", "nettoyage du sang"],
    "recommendations": "Infusion des racines ou feuilles."
},
"Arenaria serpyllifolia": {
    "local_name": "Arenaire",
    "family": "Caryophyllaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "anti‑inflammatoire"],
    "recommendations": "Infusion des feuilles; usage interne léger."
},
"Artemisia absinthium": {
    "local_name": "Absinthe",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "amélioration appétit"],
    "recommendations": "Infusion très légère; usage interne limité."
},
"Artemisia annua": {
    "local_name": "Armoise douce",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["fièvre", "maladies infectieuses"],
    "recommendations": "Infusion des feuilles."
},
"Asparagus officinalis": {
    "local_name": "Asperge",
    "family": "Asparagaceae",
    "is_medicinal": True,
    "medicinal_uses": ["diurétique", "digestion"],
    "recommendations": "Jus ou décoction des jeunes tiges."
},
"Atriplex halimus": {
    "local_name": "Atriplex",
    "family": "Amaranthaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "soins de la peau"],
    "recommendations": "Infusion des feuilles."
},
"Avena sativa": {
    "local_name": "Avoine",
    "family": "Poaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "nutrition"],
    "recommendations": "Infusion des grains ou flocons."
},
"Azolla filiculoides": {
    "local_name": "Azolle",
    "family": "Salviniaceae",
    "is_medicinal": True,
    "medicinal_uses": ["nettoyage du sang"],
    "recommendations": "Utilisation traditionnelle en décoction."
},
"Ballota nigra": {
    "local_name": "Ballote",
    "family": "Lamiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["anxiété", "digestion"],
    "recommendations": "Infusion des feuilles."
},
"Berberis vulgaris": {
    "local_name": "Épine‑vinette",
    "family": "Berberidaceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "digestion", "infections"],
    "recommendations": "Infusion des racines ou écorce."
},
"Borago officinalis": {
    "local_name": "Bourrache",
    "family": "Boraginaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "respiration"],
    "recommendations": "Infusion des feuilles et fleurs."
},
"Botrychium lunaria": {
    "local_name": "Fougère lune",
    "family": "Ophioglossaceae",
    "is_medicinal": True,
    "medicinal_uses": ["soins des plaies"],
    "recommendations": "Infusion traditionnelle des feuilles."
},

# ============================================================
# BASE MÉDICINALE GLOBALE – PLANTES 51–200
# ============================================================

"Ceratonia siliqua": {
    "local_name": "Caroube",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "cholestérol"],
    "recommendations": "Infusion des graines; poudre des gousses."
},
"Cichorium intybus": {
    "local_name": "Chicorée",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "digestion"],
    "recommendations": "Infusion des racines torréfiées."
},
"Cirsium vulgare": {
    "local_name": "Chardon vulgaire",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "inflammation"],
    "recommendations": "Infusion des feuilles."
},
"Commiphora myrrha": {
    "local_name": "Myrrhe",
    "family": "Burseraceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections", "anti‑inflammatoire"],
    "recommendations": "Résine en décoction ou usage externe."
},
"Convallaria majalis": {
    "local_name": "Muguet",
    "family": "Asparagaceae",
    "is_medicinal": True,
    "medicinal_uses": ["cardiotonique"],
    "recommendations": "Usage en décoction contrôlée (plante forte)."
},
"Corchorus olitorius": {
    "local_name": "Jute",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "nutritive"],
    "recommendations": "Feuilles bouillies ou infusion."
},
"Coriandrum sativum": {
    "local_name": "Coriandre",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "anti‑spasmodique"],
    "recommendations": "Infusion des graines; herbe fraîche en cuisine."
},
"Cornus mas": {
    "local_name": "Cornouiller",
    "family": "Cornaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "infections"],
    "recommendations": "Infusion des fruits pour troubles digestifs."
},
"Cucumis sativus": {
    "local_name": "Concombre",
    "family": "Cucurbitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "hydratation"],
    "recommendations": "Jus frais; applications cutanées pour peau."
},
"Curcuma longa": {
    "local_name": "Curcuma",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "digestion"],
    "recommendations": "Décortiqué ou infusion du rhizome."
},
"Cyclamen hederifolium": {
    "local_name": "Cyclamen",
    "family": "Primulaceae",
    "is_medicinal": True,
    "medicinal_uses": ["respiration", "digestion"],
    "recommendations": "Usage traditionnel en décoction modérée."
},
"Daphne mezereum": {
    "local_name": "Laurier des bois",
    "family": "Thymelaeaceae",
    "is_medicinal": True,
    "medicinal_uses": ["soins cutanés"],
    "recommendations": "Usage externe uniquement — toxique interne."
},
"Daucus carota": {
    "local_name": "Carotte",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "vitamines"],
    "recommendations": "Infusion des graines; consommation du légume."
},
"Dioscorea villosa": {
    "local_name": "Igname sauvage",
    "family": "Dioscoreaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hormonal", "digestion"],
    "recommendations": "Décotion des tubercules."
},
"Ephedra sinica": {
    "local_name": "Ephedra",
    "family": "Ephedraceae",
    "is_medicinal": True,
    "medicinal_uses": ["respiration", "stimulant"],
    "recommendations": "Infusion des tiges; usage strictement contrôlé."
},
"Eschscholzia californica": {
    "local_name": "Pavot de Californie",
    "family": "Papaveraceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "douleurs légères"],
    "recommendations": "Infusion des feuilles."
},
"Eucalyptus globulus": {
    "local_name": "Eucalyptus",
    "family": "Myrtaceae",
    "is_medicinal": True,
    "medicinal_uses": ["respiration", "antiseptique"],
    "recommendations": "Infusion des feuilles; inhalation vapeur."
},
"Euphrasia officinalis": {
    "local_name": "Euphraise",
    "family": "Orobanchaceae",
    "is_medicinal": True,
    "medicinal_uses": ["yeux", "inflammation"],
    "recommendations": "Infusion légère utilisée en compresses oculaires."
},
"Fagopyrum esculentum": {
    "local_name": "Sarrasin",
    "family": "Polygonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "nutritive"],
    "recommendations": "Graines bouillies; infusion des graines."
},
"Festuca arundinacea": {
    "local_name": "Fétuque",
    "family": "Poaceae",
    "is_medicinal": False,
    "medicinal_uses": [],
    "recommendations": ""
},
"Foeniculum vulgare": {
    "local_name": "Fenouil",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "gaz"],
    "recommendations": "Infusion des graines."
},
"Fragaria vesca": {
    "local_name": "Fraisier des bois",
    "family": "Rosaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "vitamines"],
    "recommendations": "Infusion des feuilles; fruits consommés frais."
},
"Galium odoratum": {
    "local_name": "Aspérule odorante",
    "family": "Rubiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "relaxation"],
    "recommendations": "Infusion des feuilles."
},
"Ginkgo biloba": {
    "local_name": "Ginkgo",
    "family": "Ginkgoaceae",
    "is_medicinal": True,
    "medicinal_uses": ["mémoire", "circulation"],
    "recommendations": "Extrait en infusion ou capsules."
},
"Glycyrrhiza glabra": {
    "local_name": "Réglisse",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "soins de la gorge"],
    "recommendations": "Infusion de racines."
},
"Helianthus annuus": {
    "local_name": "Tournesol",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "peau"],
    "recommendations": "Graines et pétales en infusion."
},
"Humulus lupulus": {
    "local_name": "Houblon",
    "family": "Cannabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "insomnie"],
    "recommendations": "Infusion des cônes."
},
"Ilex paraguariensis": {
    "local_name": "Yerba mate",
    "family": "Aquifoliaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stimulation", "digestion"],
    "recommendations": "Infusion des feuilles."
},
"Iris germanica": {
    "local_name": "Iris",
    "family": "Iridaceae",
    "is_medicinal": True,
    "medicinal_uses": ["peau", "soins cutanés"],
    "recommendations": "Usage externe de décoctions florales."
},
"Brassica juncea": {
    "local_name": "Moutarde brune",
    "family": "Brassicaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "respiration"],
    "recommendations": "Graines en infusion ou ajout alimentaire."
},
"Bryonia alba": {
    "local_name": "Bryone",
    "family": "Cucurbitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["douleurs articulaires"],
    "recommendations": "Décoction des racines; usage interne léger."
},
"Buddleja davidii": {
    "local_name": "Arbre aux papillons",
    "family": "Scrophulariaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "respiration"],
    "recommendations": "Infusion des feuilles."
},
"Calendula officinalis": {
    "local_name": "Souci",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["soins cutanés", "anti‑inflammatoire"],
    "recommendations": "Infusion des fleurs ou usage externe."
},
"Camellia sinensis": {
    "local_name": "Thé",
    "family": "Theaceae",
    "is_medicinal": True,
    "medicinal_uses": ["antioxydant", "immunité"],
    "recommendations": "Infusion des feuilles."
},
"Capsella bursa-pastoris": {
    "local_name": "Bourse‑à‑pasteur",
    "family": "Brassicaceae",
    "is_medicinal": True,
    "medicinal_uses": ["saignements légers"],
    "recommendations": "Infusion des feuilles."
},
"Carya illinoinensis": {
    "local_name": "Pacane",
    "family": "Juglandaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "antioxydant"],
    "recommendations": "Infusion des feuilles."
},
# ============================================================
# BASE MÉDICINALE GLOBALE – PLANTES 51–200
# ============================================================

"Ceratonia siliqua": {
    "local_name": "Caroube",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "cholestérol"],
    "recommendations": "Infusion des graines; poudre des gousses."
},
"Cichorium intybus": {
    "local_name": "Chicorée",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["foie", "digestion"],
    "recommendations": "Infusion des racines torréfiées."
},
"Cirsium vulgare": {
    "local_name": "Chardon vulgaire",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "inflammation"],
    "recommendations": "Infusion des feuilles."
},
"Commiphora myrrha": {
    "local_name": "Myrrhe",
    "family": "Burseraceae",
    "is_medicinal": True,
    "medicinal_uses": ["infections", "anti‑inflammatoire"],
    "recommendations": "Résine en décoction ou usage externe."
},
"Convallaria majalis": {
    "local_name": "Muguet",
    "family": "Asparagaceae",
    "is_medicinal": True,
    "medicinal_uses": ["cardiotonique"],
    "recommendations": "Usage en décoction contrôlée (plante forte)."
},
"Corchorus olitorius": {
    "local_name": "Jute",
    "family": "Malvaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "nutritive"],
    "recommendations": "Feuilles bouillies ou infusion."
},
"Coriandrum sativum": {
    "local_name": "Coriandre",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "anti‑spasmodique"],
    "recommendations": "Infusion des graines; herbe fraîche en cuisine."
},
"Cornus mas": {
    "local_name": "Cornouiller",
    "family": "Cornaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "infections"],
    "recommendations": "Infusion des fruits pour troubles digestifs."
},
"Cucumis sativus": {
    "local_name": "Concombre",
    "family": "Cucurbitaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "hydratation"],
    "recommendations": "Jus frais; applications cutanées pour peau."
},
"Curcuma longa": {
    "local_name": "Curcuma",
    "family": "Zingiberaceae",
    "is_medicinal": True,
    "medicinal_uses": ["inflammation", "digestion"],
    "recommendations": "Décortiqué ou infusion du rhizome."
},
"Cyclamen hederifolium": {
    "local_name": "Cyclamen",
    "family": "Primulaceae",
    "is_medicinal": True,
    "medicinal_uses": ["respiration", "digestion"],
    "recommendations": "Usage traditionnel en décoction modérée."
},
"Daphne mezereum": {
    "local_name": "Laurier des bois",
    "family": "Thymelaeaceae",
    "is_medicinal": True,
    "medicinal_uses": ["soins cutanés"],
    "recommendations": "Usage externe uniquement — toxique interne."
},
"Daucus carota": {
    "local_name": "Carotte",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "vitamines"],
    "recommendations": "Infusion des graines; consommation du légume."
},
"Dioscorea villosa": {
    "local_name": "Igname sauvage",
    "family": "Dioscoreaceae",
    "is_medicinal": True,
    "medicinal_uses": ["hormonal", "digestion"],
    "recommendations": "Décotion des tubercules."
},
"Ephedra sinica": {
    "local_name": "Ephedra",
    "family": "Ephedraceae",
    "is_medicinal": True,
    "medicinal_uses": ["respiration", "stimulant"],
    "recommendations": "Infusion des tiges; usage strictement contrôlé."
},
"Eschscholzia californica": {
    "local_name": "Pavot de Californie",
    "family": "Papaveraceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "douleurs légères"],
    "recommendations": "Infusion des feuilles."
},
"Eucalyptus globulus": {
    "local_name": "Eucalyptus",
    "family": "Myrtaceae",
    "is_medicinal": True,
    "medicinal_uses": ["respiration", "antiseptique"],
    "recommendations": "Infusion des feuilles; inhalation vapeur."
},
"Euphrasia officinalis": {
    "local_name": "Euphraise",
    "family": "Orobanchaceae",
    "is_medicinal": True,
    "medicinal_uses": ["yeux", "inflammation"],
    "recommendations": "Infusion légère utilisée en compresses oculaires."
},
"Fagopyrum esculentum": {
    "local_name": "Sarrasin",
    "family": "Polygonaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "nutritive"],
    "recommendations": "Graines bouillies; infusion des graines."
},
"Festuca arundinacea": {
    "local_name": "Fétuque",
    "family": "Poaceae",
    "is_medicinal": False,
    "medicinal_uses": [],
    "recommendations": ""
},
"Foeniculum vulgare": {
    "local_name": "Fenouil",
    "family": "Apiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "gaz"],
    "recommendations": "Infusion des graines."
},
"Fragaria vesca": {
    "local_name": "Fraisier des bois",
    "family": "Rosaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "vitamines"],
    "recommendations": "Infusion des feuilles; fruits consommés frais."
},
"Galium odoratum": {
    "local_name": "Aspérule odorante",
    "family": "Rubiaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "relaxation"],
    "recommendations": "Infusion des feuilles."
},
"Ginkgo biloba": {
    "local_name": "Ginkgo",
    "family": "Ginkgoaceae",
    "is_medicinal": True,
    "medicinal_uses": ["mémoire", "circulation"],
    "recommendations": "Extrait en infusion ou capsules."
},
"Glycyrrhiza glabra": {
    "local_name": "Réglisse",
    "family": "Fabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "soins de la gorge"],
    "recommendations": "Infusion de racines."
},
"Helianthus annuus": {
    "local_name": "Tournesol",
    "family": "Asteraceae",
    "is_medicinal": True,
    "medicinal_uses": ["digestion", "peau"],
    "recommendations": "Graines et pétales en infusion."
},
"Humulus lupulus": {
    "local_name": "Houblon",
    "family": "Cannabaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stress", "insomnie"],
    "recommendations": "Infusion des cônes."
},
"Ilex paraguariensis": {
    "local_name": "Yerba mate",
    "family": "Aquifoliaceae",
    "is_medicinal": True,
    "medicinal_uses": ["stimulation", "digestion"],
    "recommendations": "Infusion des feuilles."
},
"Iris germanica": {
    "local_name": "Iris",
    "family": "Iridaceae",
    "is_medicinal": True,
    "medicinal_uses": ["peau", "soins cutanés"],
    "recommendations": "Usage externe de décoctions florales."
},

    # ============================================================
    # CATEGORIE : LÉGUMES ET ÉPICES COMPLÉMENTAIRES
    # ============================================================
    "Abelmoschus esculentus": {
        "local_name": "Lalo / Kalalou",
        "family": "Malvaceae",
        "is_medicinal": True,
        "medicinal_uses": ["gastrite", "constipation", "cholestérol"],
        "recommendations": "Consommé bouilli; sa texture mucilagineuse protège les parois de l'estomac."
    },
    "Brassica oleracea var. capitata": {
        "local_name": "Chou",
        "family": "Brassicaceae",
        "is_medicinal": True,
        "medicinal_uses": ["ulcères d'estomac", "inflammation", "engorgement mammaire"],
        "recommendations": "Le jus de chou frais pour l'estomac; feuilles chauffées en cataplasme pour les douleurs."
    },
    "Apium graveolens": {
        "local_name": "Seleri",
        "family": "Apiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["hypertension", "rétention d'eau", "rhumatisme"],
        "recommendations": "Jus frais ou décoction des tiges et racines pour éliminer les toxines."
    },
    # ============================================================
    # CATEGORIE : VARIÉTÉS DE MANGUES (MANGIFERA INDICA VAR.)
    # Note : Bien que l'espèce soit la même, les propriétés diffèrent.
    # ============================================================
    "Mangifera indica (Francisque)": {
        "local_name": "Mango Fransik",
        "family": "Anacardiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "vitamine A", "laxatif léger"],
        "recommendations": "La variété la plus exportée; excellente pour la peau et la vision."
    },
    "Mangifera indica (Baptiste)": {
        "local_name": "Mango Batis",
        "family": "Anacardiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["énergie", "convalescence"],
        "recommendations": "Chair très charnue et sucrée, idéale pour reprendre des forces."
    },
    "Mangifera indica (Muscat)": {
        "local_name": "Mango Miska",
        "family": "Anacardiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["digestion", "hydratation"],
        "recommendations": "Petite mangue très fibreuse; les fibres aident au transit intestinal."
    },

    # ============================================================
    # CATEGORIE : BANANES ET VIVRES (MUSA SPP.)
    # ============================================================
    "Musa x paradisiaca (Plantain)": {
        "local_name": "Bannann miske / Bannann kochon",
        "family": "Musaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diarrhée", "gastrite", "anémie"],
        "recommendations": "La banane bouillie est douce pour l'estomac; riche en potassium pour le cœur."
    },
    "Musa sapientum (Figue)": {
        "local_name": "Fig mi",
        "family": "Musaceae",
        "is_medicinal": True,
        "medicinal_uses": ["dépression légère", "énergie rapide", "brûlures d'estomac"],
        "recommendations": "Consommé mûr; contient du tryptophane qui aide à la relaxation."
    },

    # ============================================================
    # CATEGORIE : PLANTES DU LITTORAL ET DE LA MER
    # ============================================================
    "Coccoloba uvifera": {
        "local_name": "Rezen bòdmè",
        "family": "Polygonaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diarrhée", "infections intestinales", "hémorragies"],
        "recommendations": "Décoction de l'écorce ou des racines; le fruit est comestible et astringent."
    },
    "Rhizophora mangle": {
        "local_name": "Mang wouj (Palétuvier)",
        "family": "Rhizophoraceae",
        "is_medicinal": True,
        "medicinal_uses": ["angines", "infections de la gorge", "cicatrisation"],
        "recommendations": "Décoction de l'écorce riche en tanins pour les gargarismes."
    },
    "Canavalia rosea": {
        "local_name": "Pwa bòdmè",
        "family": "Fabaceae",
        "is_medicinal": True,
        "medicinal_uses": ["douleurs", "rhumatisme (en bain)"],
        "recommendations": "Utilisé principalement en bain médicinal pour soulager les courbatures."
    },
    "Hippomane mancinella": {
        "local_name": "Mansiniye (Mançanillier)",
        "family": "Euphorbiaceae",
        "is_medicinal": False,
        "medicinal_uses": [],
        "recommendations": "DANGER EXTRÊME : Plante hautement toxique. Ne pas toucher, ne pas s'abriter dessous quand il pleut."
    },

    # ============================================================
    # CATEGORIE : ÉPICES ET RACINES ADDITIONNELLES
    # ============================================================
    "Plectranthus verticillatus": {
        "local_name": "Ti bonm",
        "family": "Lamiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["grippe", "maux de tête", "digestion"],
        "recommendations": "Infusion des petites feuilles; souvent planté près des maisons pour l'odeur et l'usage rapide."
    },
    "Anethum graveolens": {
        "local_name": "Ladi",
        "family": "Apiaceae",
        "is_medicinal": True,
        "medicinal_uses": ["gaz chez les enfants", "insomnie", "coliques"],
        "recommendations": "Infusion très légère des graines."
    },
    "Sesamum indicum": {
        "local_name": "Zenga / Sisam",
        "family": "Pedaliaceae",
        "is_medicinal": True,
        "medicinal_uses": ["mémoire", "constipation", "lactation"],
        "recommendations": "Graines grillées ou huile; excellent pour fortifier le système nerveux."
    },

    # ================================
    # Autres plantes mondiales utilisées
    # ================================
    "Curcuma longa": {
        "local_name": "Curcuma",
        "family": "Zingiberaceae",
        "is_medicinal": True,
        "medicinal_uses": ["inflammation", "digestion", "immunité"],
        "recommendations": "Ajout dans les repas; infusion ou décoction du rhizome."
    },
    "Psidium guajava": {
        "local_name": "Goyav",
        "family": "Myrtaceae",
        "is_medicinal": True,
        "medicinal_uses": ["diarrhée", "infection", "fièvre"],
        "recommendations": "Infusion des feuilles; consommation des fruits."
    },
    "Moringa oleifera": {
        "local_name": "Moringa",
        "family": "Moringaceae",
        "is_medicinal": True,
        "medicinal_uses": ["nutrition", "immunité", "digestion"],
        "recommendations": "Feuilles séchées en infusion; ajout dans les repas."
    }
}