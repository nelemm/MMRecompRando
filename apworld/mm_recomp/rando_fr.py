# Traduction française des réglages du randomizer (affichage uniquement).
# Les identifiants (clés YAML, valeurs des choix) ne sont JAMAIS modifiés :
# seuls le nom, la description et le libellé affichés sont remplacés.

GROUPS = {
    "Game Options": "Options de jeu",
    "Item & Location Options": "Objets et emplacements",
    "Moon Requirements": "Conditions pour la Lune",
    "Majora Requirements": "Conditions pour Majora",
    "Starting Item Shuffle": "Objets de départ mélangés",
    "Extensions": "Bourses",
    "Helpful Starting Items": "Aides au départ",
    "Dungeon Options": "Donjons",
    "Sanities": "Sanities (checks supplémentaires)",
    "Souls": "Âmes",
    "Entrance Randomization": "Entrées aléatoires",
    "options I want to remove in the future and are down here to get out of the way": "Divers",
}

# Libellés des choix, communs à toutes les options.
CHOICES = {
    "vanilla": "Original",
    "normal": "Normal",
    "disabled": "Désactivé",
    "enabled": "Activé",
    "advanced": "Avancé",
    "false": "Non",
    "true": "Oui",
    "true_include_majora": "Oui, avec Majora",
    "no_logic": "Sans logique",
    "nearly_no_logic": "Presque sans logique",
    "containers": "Réceptacles",
    "pieces": "Quarts de cœur",
    "starting": "Au départ",
    "anywhere": "N'importe où",
    "anything": "N'importe quoi",
    "bosses": "Entre boss",
    "ignore": "Ignorer",
    "free": "Gratuit",
    "cheap": "Bon marché",
    "expensive": "Cher",
    "offensive": "Abusif",
    "all": "Tous",
    "overworld_only": "Hors donjons",
    "dungeon_only": "Donjons seulement",
    "no_termina_field": "Sauf Plaine de Termina",
    "grotto_and_cave_only": "Grottes seulement",
    "half": "Moitié",
    "double": "Double",
    "quad": "Quadruple",
    "ohko": "Mort en un coup",
    "fast": "Rapide",
    "instant": "Instantané",
    "moon_crash": "Chute de la Lune",
    "full": "Complète",
    "minimal": "Minimale",
    "items": "Objets",
}

# Libellés de choix propres à une option, quand le libellé commun est trop long : le menu du jeu met tous
# les choix sur une seule ligne, sans retour à la ligne, et les libellés longs écrasent les autres.
OPTION_CHOICES = {
    "grasssanity": {
        "no_termina_field": "Hors Plaine",
        "grotto_and_cave_only": "Grottes",
        "dungeon_only": "Donjons",
    },
}

# option_id -> (nom affiché, description)
OPTIONS = {
    # --- Options communes d'Archipelago ---
    "progression_balancing": ("Équilibrage de progression",
        "Plus la valeur est haute, plus les objets de progression sont placés tôt dans les autres mondes."),
    "accessibility": ("Accessibilité",
        "Ce que la génération garantit.\n\n"
        "Complète : tu pourras ouvrir tous les checks de la partie, sans exception.\n\n"
        "Minimale : tu pourras finir la partie, mais certains checks peuvent rester "
        "impossibles à atteindre (ils ne contiendront alors rien d'indispensable)."),
    "death_link": ("Death Link",
        "Quand tu meurs, tous les joueurs avec Death Link meurent aussi, et inversement."),

    # --- Logique ---
    "logic_difficulty": ("Difficulté de la logique",
        "Normal : faisable sans glitch.\n\n"
        "Presque sans logique : seuls les accès aux temples et à la Lune sont vérifiés. "
        "Peut demander des glitchs.\n\n"
        "Sans logique : aucune vérification, peut être impossible.\n\n"
        "Hors Normal, mets Accessibilité sur Minimale."),

    # --- Lune ---
    "moon_remains_required": ("Restes de boss requis (Lune)",
        "Nombre de restes de boss nécessaires pour aller sur la Lune après avoir joué l'Ode de l'Appel (Oath to Order)."),
    "moon_masks_required": ("Masques requis (Lune)",
        "Nombre de masques nécessaires pour aller sur la Lune après avoir joué l'Ode de l'Appel (Oath to Order)."),
    "moon_star_fox": ("Star Fox (Lune)",
        "Exige les masques Keaton, Parfumé, de Brême, Capuche de lapin et Don Gero pour aller sur la Lune."),
    "moon_owls_required": ("Statues de hibou requises (Lune)",
        "Nombre de statues de hibou nécessaires pour aller sur la Lune."),
    "moon_scarecrows_required": ("Épouvantails requis (Lune)",
        "Nombre d'épouvantails nécessaires pour aller sur la Lune."),
    "moon_frogs_required": ("Grenouilles requises (Lune)",
        "Nombre de grenouilles nécessaires pour aller sur la Lune."),
    "moon_items_required": ("Objets d'échange requis (Lune)",
        "Nombre d'objets d'échange nécessaires pour aller sur la Lune."),

    # --- Majora ---
    "majora_remains_required": ("Restes de boss requis (Majora)",
        "Nombre de restes de boss nécessaires pour affronter Majora."),
    "majora_masks_required": ("Masques requis (Majora)",
        "Nombre de masques nécessaires pour affronter Majora."),
    "majora_star_fox": ("Star Fox (Majora)",
        "Exige les masques Keaton, Parfumé, de Brême, Capuche de lapin et Don Gero pour affronter Majora."),
    "majora_owls_required": ("Statues de hibou requises (Majora)",
        "Nombre de statues de hibou nécessaires pour affronter Majora."),
    "majora_scarecrows_required": ("Épouvantails requis (Majora)",
        "Nombre d'épouvantails nécessaires pour affronter Majora."),
    "majora_frogs_required": ("Grenouilles requises (Majora)",
        "Nombre de grenouilles nécessaires pour affronter Majora."),
    "majora_items_required": ("Objets d'échange requis (Majora)",
        "Nombre d'objets d'échange nécessaires pour affronter Majora."),

    # --- Divers / objectif ---
    "completion_goal": ("Objectif 100 %",
        "Ajoute un objectif de complétion : il faut récupérer 100 % des objets à collectionner."),
    "camc": ("Coffres assortis au contenu (CAMC)",
        "L'apparence des coffres correspond à leur contenu."),

    # --- Entrées ---
    "dungeon_entrance_rando": ("Entrées de donjons aléatoires",
        "Les donjons sont mélangés entre eux."),
    "boss_entrance_rando": ("Entrées de boss aléatoires",
        "Les salles de boss sont mélangées entre elles."),
    "dungeon_chaining": ("Enchaînement de donjons",
        "Si les entrées de donjons et de boss sont aléatoires, un donjon peut mener à un autre donjon, "
        "ou ne contenir qu'un boss."),

    # --- Objets de départ ---
    "ocarinaless": ("Sans ocarina",
        "Commence sans l'ocarina, qui devient un objet à trouver. Le temps s'écoule alors plus vite."),
    "timeless": ("Sans Chant du Temps",
        "Commence sans le Chant du Temps, qui devient un objet à trouver."),
    "swordless": ("Sans épée",
        "Commence sans épée, et ajoute une Épée progressive de plus parmi les objets à trouver."),
    "shieldless": ("Sans bouclier",
        "Commence sans bouclier, et ajoute un Bouclier progressif de plus parmi les objets à trouver."),
    "starting_hearts": ("Cœurs de départ",
        "Nombre de quarts de cœur au départ.\n"
        "En dessous de 12, des cœurs supplémentaires sont ajoutés aux objets à trouver pour compenser."),
    "starting_hearts_are_containers_or_pieces": ("Cœurs de départ : réceptacles ou quarts",
        "Les cœurs de départ manquants sont ajoutés aux objets à trouver sous forme de réceptacles (plus le reste en quarts) "
        "ou uniquement en quarts de cœur."),
    "shuffle_regional_maps": ("Cartes de Tingle",
        "Où placer les cartes régionales vendues par Tingle."),
    "child_wallet": ("Mélanger la bourse d'enfant",
        "Commence sans la bourse de 99 rubis : une Bourse progressive de plus est ajoutée aux objets à trouver."),
    "deity_wallet": ("Ajouter la bourse divine",
        "Ajoute une Bourse progressive de plus, qui contient jusqu'à 999 rubis.\n\n"
        "Les prix Abusifs des boutiques peuvent alors monter jusqu'à cette capacité."),

    # --- Aides au départ ---
    "start_with_soaring": ("Commencer avec le Chant de l'Envol",
        "Commence la partie avec le Chant de l'Envol."),
    "start_with_consumables": ("Commencer avec des consommables",
        "Commence avec 99 rubis, 10 bâtons Mojo et 20 noix Mojo."),
    "permanent_chateau_romani": ("Lait Chateau Romani permanent",
        "Les effets du Lait Chateau Romani restent après un retour dans le temps."),
    "start_with_inverted_time": ("Temps inversé au retour",
        "Le temps est inversé dès le premier jour, même après un retour dans le temps."),
    "receive_filled_wallets": ("Bourses déjà remplies",
        "Les bourses reçues arrivent pleines (hors bourse de départ)."),
    "magic_is_a_trap": ("La magie est un piège",
        "Garde le bug d'origine qui permet d'utiliser certains objets magiques sans magie.\n"
        "Une fois la magie obtenue, ces objets consomment de la magie normalement.\n\n"
        "(Aucun effet sur la logique)"),

    # --- Donjons ---
    "shuffle_boss_remains": ("Mélanger les restes de boss",
        "Original : les restes sont donnés par leur boss habituel.\n"
        "N'importe où : n'importe quel objet peut remplacer un reste, et les restes peuvent être n'importe où, "
        "dans n'importe quel monde.\n"
        "Entre boss : les restes sont mélangés entre les boss."),
    "remains_allow_boss_warps": ("Téléportation vers les boss avec les restes",
        "Garde la possibilité d'origine de se téléporter au boss d'un donjon quand on a ses restes.\n"
        "Obtenir le check des restes d'un donjon ouvre sa téléportation dans tous les cas."),
    "keysanity": ("Petites clés mélangées",
        "Les petites clés peuvent se trouver n'importe où, au lieu de rester à leur place d'origine."),
    "bosskeysanity": ("Clés du boss mélangées",
        "Les clés du boss peuvent se trouver n'importe où, au lieu de rester à leur place d'origine."),

    # --- Sanities ---
    "skullsanity": ("Skulltulas d'or (Skullsanity)",
        "Ce que peuvent donner les Skulltulas d'or.\n\n"
        "Original : seulement des jetons, dans les Maisons des Skulltulas.\n"
        "N'importe quoi : n'importe quel objet, et les jetons peuvent être n'importe où.\n"
        "Ignorer : les Maisons des Skulltulas sont retirées de la génération."),
    "required_skull_tokens": ("Jetons de Skulltula requis",
        "Nombre de jetons de Skulltula d'or nécessaires pour la récompense de chaque Maison des Skulltulas (0 à 30).\n"
        "Les 30 jetons de chaque maison restent à trouver quel que soit le réglage."),
    "shuffle_spiderhouse_reward": ("Récompenses des Maisons des Skulltulas",
        "Mélange le Masque de Vérité (Maison du Marais) et l'agrandissement de bourse (Maison Océane)."),
    "shopsanity": ("Boutiques (Shopsanity)",
        "Mélange les objets des boutiques (Bazar, bombes, Goron, Zora, Gorman, Bar Latte).\n\n"
        "Original : rien n'est mélangé.\n"
        "Activé : les boutiques de nuit et de printemps partagent les objets du jour.\n"
        "Avancé : elles ont chacune leurs propres objets."),
    "scrubsanity": ("Pestes Mojo marchandes",
        "Mélange les achats auprès des Pestes Mojo marchandes."),
    "shop_prices": ("Prix des boutiques",
        "Prix des boutiques (seulement avec Shopsanity).\n\n"
        "Original : prix normaux.\n"
        "Gratuit : 0 rubis.\n"
        "Bon marché : bourse de départ suffit.\n"
        "Cher : jusqu'à la Bourse d'adulte.\n"
        "Abusif : jusqu'à la Bourse de géant."),
    "cowsanity": ("Vaches (Cowsanity)",
        "Les vaches donnent un objet mélangé."),
    "shuffle_great_fairy_rewards": ("Récompenses des Grandes Fées",
        "Mélange les récompenses des Grandes Fées."),
    "required_stray_fairies": ("Fées égarées requises",
        "Nombre de fées égarées nécessaires pour la récompense de chaque Grande Fée de donjon (0 à 15).\n"
        "Les 15 fées de chaque donjon restent à trouver quel que soit le réglage."),
    "fairysanity": ("Fées égarées (Fairysanity)",
        "Les fées égarées deviennent des checks : elles peuvent contenir n'importe quel objet."),
    "curiostity_shop_trades": ("Échanges de la Boutique de curiosités",
        "Mélange les rubis donnés en échange d'objets en bouteille à la Boutique de curiosités."),
    "intro_checks": ("Checks de l'introduction",
        "Mélange les checks situés avant l'entrée dans la Tour de l'Horloge.\n\n"
        "Un passage retour a été ajouté par la porte en pierre en bas de l'intérieur de la Tour de l'Horloge."),
    "grasssanity": ("Herbe (Grasssanity)",
        "Quelle herbe donne un objet mélangé.\n\n"
        "Normal : toute l'herbe du jeu.\n"
        "Hors Plaine : tout sauf la Plaine de Termina et ses grottes.\n"
        "Grottes : seulement l'herbe des grottes et cavernes.\n"
        "Donjons : seulement l'herbe des donjons."),
    "potsanity": ("Jarres (Potsanity)",
        "Quelles jarres donnent un objet mélangé.\n\n"
        "Tous : toutes les jarres du jeu.\n"
        "Hors donjons : seulement celles hors des donjons.\n"
        "Donjons seulement : seulement celles des donjons."),
    "hitsanity": ("Points d'impact (Hitsanity)",
        "Les endroits cachés qui lâchent un objet quand on les frappe donnent un objet mélangé."),
    "rocksanity": ("Rochers (Rocksanity)",
        "Les rochers donnent un objet mélangé."),
    "soilsanity": ("Terre meuble (Soilsanity)",
        "Les zones de terre meuble donnent un objet mélangé."),
    "rupeesanity": ("Rubis posés (Rupeesanity)",
        "Les rubis posés au sol deviennent des checks : ils peuvent contenir n'importe quel objet."),
    "invisisanity": ("Rubis invisibles (Invisisanity)",
        "Les rubis invisibles deviennent des checks : ils peuvent contenir n'importe quel objet."),
    "snowsanity": ("Boules de neige (Snowsanity)",
        "Les boules de neige donnent un objet mélangé."),
    "woodsanity": ("Caisses et tonneaux (Woodsanity)",
        "Les caisses et tonneaux en bois donnent un objet mélangé."),
    "realfairysanity": ("Fées libres (Realfairysanity)",
        "Les fées des Pierres à potins, des papillons et celles en liberté sont mélangées."),
    "iciclesanity": ("Stalactites de glace (Iciclesanity)",
        "Les stalactites de glace donnent un objet mélangé."),
    "scarecrowsanity": ("Épouvantails (Scarecrowsanity)",
        "L'épouvantail donne un objet quand il apparaît."),
    "hivesanity": ("Ruches (Hivesanity)",
        "Les ruches donnent un objet mélangé."),
    "notebooksanity": ("Carnet des Bombers (Notebooksanity)",
        "Les entrées du Carnet des Bombers donnent un objet mélangé."),
    "owlsanity": ("Statues de hibou (Owlsanity)",
        "Activer une statue de hibou donne un objet mélangé."),
    "frogsanity": ("Grenouilles (Frogsanity)",
        "Les quatre grenouilles donnent un objet mélangé."),
    "treesanity": ("Arbres et buissons (Treesanity)",
        "Les arbres et buissons lâchent un objet mélangé."),
    "flowersanity": ("Fleurs Mojo (Flowersanity)",
        "Entrer dans une Fleur Mojo donne un objet mélangé."),
    "signsanity": ("Panneaux (Signsanity)",
        "Couper un panneau carré donne un objet mélangé."),
    "websanity": ("Toiles d'araignée (Websanity)",
        "Brûler une toile d'araignée donne un objet mélangé."),
    "oneoffs": ("Checks uniques (Oneoffs)",
        "Les emplacements uniques, comme les photos de Skull Kid ou les murs à exploser, donnent un objet mélangé."),

    # --- Âmes ---
    "boss_souls": ("Âmes des boss",
        "Ajoute les âmes des boss principaux : un boss n'apparaît pas tant que son âme n'est pas obtenue.\n\n"
        "Concerne Odolwa, Goht, Gyorg, Twinmold et, en option, Majora."),
    "npc_souls": ("Âmes des personnages",
        "Ajoute les âmes des personnages (Anju, Romani, Kamaro, etc.) : "
        "ils n'apparaissent pas tant que leur âme n'est pas obtenue.\n\n"
        "Attention : chaque âme ajoute un objet à trouver. Avec beaucoup d'âmes, active aussi des sanities, sinon la génération échoue faute d'emplacements."),
    "enemy_souls": ("Âmes des ennemis",
        "Ajoute les âmes des ennemis de base (Wolfos, Peahat, etc.) : "
        "ils n'apparaissent pas tant que leur âme n'est pas obtenue.\n\n"
        "Attention : chaque âme ajoute un objet à trouver. Avec beaucoup d'âmes, active aussi des sanities, sinon la génération échoue faute d'emplacements."),
    "misc_souls": ("Âmes diverses",
        "Ajoute les âmes des vaches, des Skulltulas d'or et de Keaton : "
        "ils n'apparaissent pas tant que leur âme n'est pas obtenue."),
    "utility_souls": ("Âmes utilitaires",
        "Ajoute les âmes des éléments utilitaires comme les boîtes aux lettres : "
        "ils n'apparaissent pas tant que leur âme n'est pas obtenue."),
    "absurd_souls": ("Âmes absurdes",
        "Ajoute les âmes d'éléments absurdes comme les rochers, les murs de chant ou l'herbe : "
        "ils n'apparaissent pas tant que leur âme n'est pas obtenue.\n\n"
        "Attention : chaque âme ajoute un objet à trouver. Avec beaucoup d'âmes, active aussi des sanities, sinon la génération échoue faute d'emplacements."),

    # --- Indices, dégâts, mort ---
    "hint_percentage": ("Pourcentage d'indices utiles",
        "Pourcentage de Pierres à potins qui donnent un indice utile sur les objets du multiworld."),
    "damage_multiplier": ("Multiplicateur de dégâts",
        "Ajuste les dégâts reçus."),
    "death_behavior": ("Comportement à la mort",
        "Ce qui se passe quand tu meurs.\n\n"
        "Original : la cinématique de mort normale.\n"
        "Rapide : la cinématique de mort est très accélérée.\n"
        "Instantané : pas de cinématique.\n"
        "Chute de la Lune : déclenche la chute de la Lune et recommence le cycle."),
    "link_tunic_color": ("Couleur de la tunique",
        "Choisis la couleur de la tunique de Link."),
}


def _choice_label(text):
    # Le jeu affiche les choix en majuscules (text-transform: uppercase), qui ne gère
    # que l'ASCII : les lettres accentuées restent minuscules et la largeur est mal
    # calculée (les libellés se chevauchent). On fournit donc des majuscules ASCII.
    import unicodedata
    text = text.replace("œ", "oe").replace("Œ", "OE").replace("’", "'")
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return text.upper()


def translate_options(options):
    """Remplace en place les textes affichés de recomp_data.options."""
    for group_name, group in options.items():
        for option_id, info in group.items():
            fr = OPTIONS.get(option_id)
            if fr:
                info["name"], info["description"] = fr
            if "choices" in info:
                own = OPTION_CHOICES.get(option_id, {})
                info["choice_names"] = {c: _choice_label(own.get(c) or CHOICES[c]) for c in info["choices"] if c in own or c in CHOICES}
    return {g: GROUPS.get(g, g) for g in options}
