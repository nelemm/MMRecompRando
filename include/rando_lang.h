#ifndef RANDO_LANG_H
#define RANDO_LANG_H

#include "recompconfig.h"

// Menu language, from the "language" mod setting (0 = English, 1 = French).
// Menus read it when they are built: a change applies after restarting the game.
static inline int rando_lang_fr(void) {
    return recomp_get_config_u32("language") == 1;
}

#define TR(en, fr) (rando_lang_fr() ? (fr) : (en))

#endif
