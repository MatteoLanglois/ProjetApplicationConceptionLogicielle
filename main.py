from random import randint

import puissanceQuatre as ps4
import grid as gr


def main(**argv):
    grille = gr.pq_init_grille(6, 7)
    for I in range(0, 20):
        ps4.pq_ajout_piece(grille, randint(0, 6), I % 2 + 1)
    gr.pq_print_grille(grille)


if __name__ == '__main__':
    main()
