#include <iostream>
using namespace std;

#include "tree.h"

Noeud* arbre = NULL;
char interdit = '|';

Noeud* creerFeuille(int valeur, char letter)
{
    Noeud* nouveau = new Noeud;
    nouveau->valeur = valeur;
    nouveau->letter = letter;
    nouveau->fils_droite = NULL;
    nouveau->fils_gauche = NULL;
    return nouveau;
}

Noeud* creerSuperieur(Noeud* N1, Noeud* N2)
{
    Noeud* nouveau = new Noeud;
    nouveau->valeur = N1->valeur + N2->valeur;
    nouveau->letter = interdit;
    nouveau->fils_droite = N1;
    nouveau->fils_gauche = N2;
    return nouveau;
}

void Ajouter(Noeud* N1, Noeud* N2)
{
    Noeud* nouveau = new Noeud;
    nouveau->valeur = N1->valeur + N2->valeur;
    nouveau->letter = interdit;
    nouveau->fils_droite = N1;
    nouveau->fils_gauche = N2;
    arbre = nouveau;
}

bool isFeuille (Noeud* node)
{
    return (node->fils_droite == NULL && node->fils_gauche == NULL);
}

Noeud* get_Fils(int i, Noeud* fils)
{
    if (i == 0)
    {
        return fils->fils_gauche;
    }
    else
    {
        return fils->fils_droite;
    }
}

void aff (Noeud* racine, int iter)
{
    if(racine->fils_gauche)
        aff(racine->fils_gauche, iter + 1);
    cout << iter << " : " << racine->letter << " , " << racine->valeur << endl;
    if(racine->fils_droite)
        aff(racine->fils_droite, iter + 1);
}

void Afficher(Noeud* racine)
{
    if(racine->fils_gauche)
        Afficher(racine->fils_gauche);
    if (racine->letter != interdit)
        cout << racine->letter << " , " << racine->valeur << endl;
    if(racine->fils_droite)
        Afficher(racine->fils_droite);
}
