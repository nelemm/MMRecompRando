# MMRecompRando — French & fixes fork

> **This is a fork** of [RecompRando/MMRecompRando](https://github.com/RecompRando/MMRecompRando), based on its development branch `python-glue` (October 2026). It enables the pot, grass, crate and other "sanity" checks that are not in an official release yet, and adds the fixes below. The upstream README follows after this section.

[English](#about-this-fork) · [Français](#à-propos-de-ce-fork)

## About this fork

### Security fixes (online / Archipelago)
- **Save file name**: built with a bounded copy instead of `sprintf` into a 72-byte buffer, and path separators / invalid characters from the slot or seed name (sent by the server) are replaced. Prevents a stack overflow and writing a save outside the save folder.
- **In-game messages**: the 53 `EZTR_MsgSContent_Sprintf` calls that insert item / player names are now `EZTR_MsgSContent_Snprintf` bounded to the message buffer.
- **`sanitizeRandoText`**: index widened from `u8` to `u32`. Names of 256+ bytes made the loop wrap forever and froze the game.
- **Solo menu labels**: bounded formatting of the session date and seed name.

### Bug fixes
- **Containers that are not checks** (crates, barrels, rocks, trees, signs, snowballs, webs, hit spots, soft soil…) no longer drop *nothing*: the 53 conditions now check `rando_location_exists()`, like pots and grass already did, and fall back to the vanilla drop.
- **Logic (apworld, `NormalRules.py`)**:
  - Without owlsanity, `can_use_owl` always returned false, making the inside of Gorman Racetrack unreachable in some settings (generation failure). The Clock Town owl now counts (Song of Soaring + sword / Goron / Zora).
  - With NPC souls and without shopsanity, `can_get_red_potion` queried a shop location that doesn't exist (`KeyError`, generation crash). The Trading Post now sells its Red Potion vanilla-style.
- **Compatibility**: builds against the released *Better Double SoT 1.0.0* (unused debug `dsot_set_time` call and `dsot_on_whitelist_check` callback removed) and no longer patches `EnFall_LodMoon_Draw`, which conflicted with *Disable Draw Distance*.
- **Frog moon buffer**: the object buffer is only allocated in frog mode, freed with its moon actor, and the moon falls back to normal mode if allocation fails (it used to load to a NULL address).
- **Better Double SoT in the final hours**: choosing an hour between 0:00 and 6:00 on day 3 crashes the game; the hour cursor is locked during the final hours (Better Double SoT itself is not modified).
- **Solo menu**: the *Start* button label was invisible (`DISPLAY_FLEX` on a button with a bare text node); it is now shown and right-aligned.

### Additions
- **French interface**: menus, buttons and the 83 randomizer options (names, descriptions, choices, groups). Only displayed text changes: option ids and values written to the YAML are untouched. Translations live in `apworld/mm_recomp/rando_fr.py`.
- **Mod settings**: *Lune* (normal moon or the dev branch's frog moon, normal by default) and *Couleur de l'herbe* (grass colouring follows the container setting, never coloured, or gold until collected).

### Building and dependencies

This branch builds with `modbuild.py`, which downloads its own MIPS toolchain:

```bash
git clone --recurse-submodules -b fr-fixes https://github.com/nelemm/MMRecompRando
cd MMRecompRando
python modbuild.py build -n debug   # build/mm_recomp_rando.nrm
python modbuild.py apworld          # build/mm_recomp.apworld
```

Python 3.12+ is required (`modbuild.py` uses `Path.relative_to(..., walk_up=True)`), plus `make`.
The mod needs these mods in the same folder:
- [RecompExternalPython_API](https://github.com/LT-Schmiddy/zelda64recomp-python-extlibs-mod/releases) 2.0.0+ (`RecompExternalPython_for_Zelda64Recompiled` package);
- [REPY_PopularPythonPackages](https://github.com/LT-Schmiddy/repy_popular_python_packages) 1.0.0, which has no published release: build it with `python modbuild.py build -n zelda_debug`;
- [MM_EZ_Text_Replacer_API](https://thunderstore.io/c/zelda-64-recompiled/) 2.3.0+.

The release only contains the apworld: the `.nrm` embeds code from repositories without a license, so it is not redistributed here.

Generation was tested with 60+ seeds (normal logic, every new sanity alone and combined, souls, entrance rando, swordless / ocarinaless, nearly-no-logic).

## À propos de ce fork

Fork de [RecompRando/MMRecompRando](https://github.com/RecompRando/MMRecompRando), basé sur la branche de développement `python-glue` (octobre 2026), qui active les checks de jarres, d'herbe, de caisses et les autres « sanities » pas encore publiés officiellement.

- **Sécurité (jeu en ligne)** : nom de fichier de sauvegarde borné et nettoyé (noms envoyés par le serveur), messages en jeu bornés, boucle de `sanitizeRandoText` corrigée (gel du jeu avec des noms de 256 octets ou plus), libellés du menu solo bornés.
- **Bugs** : les conteneurs qui ne sont pas des checks redonnent leur contenu normal ; tampon de la lune grenouille sécurisé ; curseur de Better Double SoT bloqué pendant les dernières heures (choisir une heure y fait crasher le jeu) ; deux erreurs de logique de l'apworld corrigées (hiboux sans owlsanity, potion rouge sans shopsanity) ; compatibilité avec *Better Double SoT 1.0.0* et *Disable Draw Distance* ; bouton *Lancer* du menu solo visible.
- **Ajouts** : interface et réglages du randomizer en français, réglages *Lune* et *Couleur de l'herbe* dans le menu Mods.

---

# MMRecompRando

This is an Archipelago randomizer mod for Majora's Mask: Recompiled with both Singleplayer and Multiworld support.

## Disclaimer

This randomizer is still under development in the beta phase but is considered stable for playing. You may encounter features that are not finished yet or errors. Be sure to check the Issues page and report anything you encounter there.

## Setup

### Mod Installation
1. Download the latest [Visual Studio C++ Redist](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-microsoft-visual-c-redistributable-version).
2. Download [Zelda64Recomp](https://github.com/Zelda64Recomp/Zelda64Recomp/releases/latest).
3. Download [MMRecompRando.zip](https://github.com/RecompRando/MMRecompRando/releases/latest).
4. Optionally download any additional mods or texture packs you'd like from [Thunderstore](https://thunderstore.io/c/zelda-64-recompiled/).
    - You only need to drag and drop mod zips from GitHub or Thunderstore onto the game window to install them.
5. You can also download [poptracker](https://github.com/black-sliver/PopTracker/releases/latest) along with [G4M3RL1F3's fork of Seto's pack](https://github.com/G4M3RL1F3/Majoras-Mask-AP-PopTracker-Pack/releases/latest)
6. Open `Zelda64Recompiled`.
    1. Select your ROM file.
    2. Install MMRecompRando and any additional mods.
    3. Select Start Game.
7. Go nuts.

### Solo Setup
1. Launch the game with the randomizer mod enabled.
2. Select `Solo` in the randomizer menu.
3. Create a new session and choose which settings you'd like.
    - Details about these settings are currently not available through the mod only, you will have to look at the [multiworld's example YAML](https://github.com/RecompRando/Archipelago-MM/blob/master/worlds/mm_recomp/EXAMPLE_YAML.yaml) for more information on what each setting does.
4. Hit `Generate` and select your seed.
5. Profit.

### Multiworld Archipelago Setup
1. Know [Archipelago](https://archipelago.gg/tutorial/Archipelago/setup/en).
2. Download the [apworld](https://github.com/RecompRando/MMRecompRando/releases/latest).
3. **MAKE SURE** to clear out _any_ apworlds named `mm-recomp.apworld` or `mm_recomp.apworld` from your `Archipelago/lib/worlds` folder and your `Archipelago/custom_worlds` folder.
4. Place the apworld into `Archipelago/custom_worlds/`.
5. Generate a multiworld, and host the game either locally or on the website.

## FAQ

### I launched this mod and my save is gone? Did rando delete my save?

Don't worry, your vanilla saves are intact. When playing this mod, a per-session savefile will be created. Your normal save file will not be touched.

### I got Letter to Kafei and now I can't use the Pendant of Memories! Is it just gone?

Try moving your cursor to the Letter to Kafei and pressing the N64's L button. That should cycle through all quest items in that slot. That's true for the Moon's Tear item slot and the Room Key item slot as well.

### I opened a chest/got a check and it always shows a grey Archipelago item, what's wrong with you?

The phantom AP item means the check is not yet implemented. Please use a text client or Seto's/G4M3RL1F3's amazing poptracker pack from step 5 to see checks that you can definitely get (though some implemented checks may be missing until the tracker is updated).

If you picked up a phantom on a check that should be implemented, you can open an issue on this repo letting us know!

## Known Issues

- Kotake sometimes does not show the price of her shopsanity item in the second dialogue.

## Credit for additional mods included

Thank you to the original authors of some of the other recomp mods used!

- ThatHypedPerson (Color Mods)
- danielryb (Better SoDT, Z-Target Fix, Song Utils)

## Contributing

> [!WARNING]
> The developers and maintainers of this randomizer, along with the N64 Recompiled community as a whole, disallow any "vibe-coded" contributions to this repository. Any contributions or extra features for this randomizer which are primarily AI generated are not endorsed by us.
>
> For more information see [CONTRIBUTING.md](CONTRIBUTING.md).

## Writing mods
See [this document](https://hackmd.io/fMDiGEJ9TBSjomuZZOgzNg) for an explanation of the modding framework, including how to write function patches and perform interop between different mods.

## Tools
You'll need to install `clang` and `make` to build rando.
* On Windows, using [chocolatey](https://chocolatey.org/) to install both is recommended. The packages are `llvm` and `make` respectively.
* On MacOS, these can both be installed using Homebrew, as well as `zip`. Apple clang won't work, as you need a mips target for building the mod code.
* On Linux, install the above packages, and some additional ones: `clang`, `make`, `llvm`, `lld`, `zip`, using your distro's package manager.

You'll also need to build [N64Recomp](https://github.com/N64Recomp/N64Recomp) for the `RecompModTool` utility, and copy it into your clone of rando (or put it on your PATH).

## Building
* First, make sure you've cloned the repo recursively `git clone https://github.com/RecompRando/MMRecompRando --recurse-submodules` or you can update the submodules afterwards `git submodule update --init --recursive`.
* Then, run `make` (with an optional job count) to build the mod code itself.
