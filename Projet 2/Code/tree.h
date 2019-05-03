#ifndef TREE_H_INCLUDED
#define TREE_H_INCLUDED

struct Noeud
{
   int valeur;
   char letter;
   Noeud* fils_droite;
   Noeud* fils_gauche;
};

extern Noeud* arbre;
extern char interdit;

Noeud* creerFeuille(int valeur, char letter);
Noeud* creerSuperieur(Noeud* N1, Noeud* N2);
void Ajouter(Noeud* N1, Noeud* N2);
bool isFeuille (Noeud* node);
Noeud* get_Fils(int i, Noeud* fils);
void aff (Noeud* racine, int iter);
void Afficher(Noeud* racine);

#endif // TREE_H_INCLUDED
