#include <iostream>
#include <fstream>
#include <string>
#include <dirent.h>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

#include "tree.h"

#define root "../"
#define data "data/"
#define freq "frequence/"
#define encode "fichier_code/"
#define decodage "fichier_decode/"

// Global variables list :

map <char, int> dico;
map <char, string> trad;

// Functions :

// Step 1 : create the dico

void printFile (string file = "freq_static.txt")
{
    string line;
    string temp = root;
    temp = temp + data + file;
    ifstream myfile (temp);
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            cout << line << '\n';
        }
        myfile.close();
    }

    else
        cout << "Unable to open file" << endl;
}

void printDico()
{
    cout << "Dico :" << endl;
    int countor = 0;
    // you want to print the content of the map dico:
    for(map <char, int>::iterator it = dico.begin(); it != dico.end(); it++)
    {
        cout << countor << " : " << it->first << " , " << it->second << endl;
        countor++;
    }
}

void readData () // V2, lire tous les fichiers de data/
{
    DIR * rep = opendir(root "data");
    if (rep != NULL)
    {
        struct dirent * ent;
        while ((ent = readdir(rep)) != NULL)
        {
            cout << string(ent->d_name) << endl;
            //printFile(data + string(ent->d_name));
        }
        closedir(rep);
    }
}

void createDico (string file)
{
    dico.clear();
    string line;
    string temp = root;
    temp = temp + data + file;
    ifstream myfile (temp);
    if (myfile.is_open())
    {
        while (getline(myfile,line))
        {
            for(unsigned int i = 0; i < line.size(); i++)
            {
                char letter = line[i];
                if (dico.count(letter) == 0)
                {
                    dico.insert(pair<char, int>(letter, 1));
                }
                else
                {
                    dico[letter]++;
                }
            }
        }
        myfile.close();
    }
    else
        cout << "Unable to open file" << endl;
        exit(1);
}

void impressionFreqences(string file)
{
    string temp = root;
    temp = temp + freq + "freq_" + file;
    ofstream myfile (temp);
    if (myfile.is_open())
    {
        myfile << dico.size() << "\n";
        for(map <char, int>::iterator it = dico.begin(); it != dico.end(); it++)
        {
            if (it->first != NULL)
            {
                myfile << it->first << "," << it->second << "\n";
            }
        }
    }
    myfile.close();
}

// Step 2 : create the Huffman tree

void printVector(vector<Noeud*> vec)
{
    int countor = 0;
    for(vector<Noeud*>::iterator it = vec.begin(); it != vec.end(); it++)
    {
        cout << countor << " : ";
        Noeud* temp = *it;
        cout << temp->letter << " " << temp->valeur << endl;
        cout << endl;
        countor++;
    }
}

int findMinKeyInVector (vector<Noeud*> tableau, vector<int> indexes)
{
    int theMin = -1;
    int key = -1;
    int countor = 0;
    Noeud* temp;
    for(vector<Noeud*>::iterator it = tableau.begin(); it != tableau.end(); it++)
    {
        if(indexes.empty() || countor != indexes.at(0))
        {
            temp = *it;
            if (theMin == -1)
            {
                theMin = temp->valeur;
                key = countor;
            }
            if (temp->valeur < theMin)
            {
                theMin = temp->valeur;
                key = countor;
            }
        }
        countor++;
    }
    return key;
}

vector<int> minCoupleTree (vector<Noeud*> tableau)
{
    vector<Noeud*> tab(tableau);
    vector<int> result;
    result.push_back(findMinKeyInVector(tab, result));
    result.push_back(findMinKeyInVector(tab, result));
    return result;
}

void manyToOneTree (vector<Noeud*> tableau)
{
    if (tableau.size() > 1)
    {
        vector<int> minCouple = minCoupleTree(tableau);
        if (tableau.size() == 2)
        {
            Ajouter(tableau.at(0), tableau.at(1));
        }
        else
        {
            Noeud* temp = creerSuperieur(tableau.at(minCouple.at(0)), tableau.at(minCouple.at(1)));
            tableau.push_back(temp);
            if (minCouple.at(0) > minCouple.at(1))
            {
                tableau.erase(tableau.begin() + minCouple.at(0));
                tableau.erase(tableau.begin() + minCouple.at(1));
            }
            else
            {
                tableau.erase(tableau.begin() + minCouple.at(1));
                tableau.erase(tableau.begin() + minCouple.at(0));
            }
            minCouple.clear();
            manyToOneTree(tableau);
        }
    }
}

void createTree ()
{
    vector <Noeud*> tableau;
    for(map <char, int>::iterator it = dico.begin(); it != dico.end(); it++)
    {
        tableau.push_back(creerFeuille(it->second, it->first));
    }
    cout << endl;
    manyToOneTree(tableau);
}

// Step 3 : Codage du texte

void printTrad()
{
    cout << "Trad :" << endl;
    int countor = 0;
    // you want to print the content of the map dico:
    for(map <char, string>::iterator it = trad.begin(); it != trad.end(); it++)
    {
        cout << countor << " : " << it->first << " , " << it->second << endl;
        countor++;
    }
}

void passage (Noeud* racine, string tra)
{
    if(racine->fils_gauche)
        passage(racine->fils_gauche, tra + string("0"));
    trad.insert(pair<char, string>(racine->letter, tra));
    if(racine->fils_droite)
        passage(racine->fils_droite, tra + string("1"));
}

void createTrad ()
{
    trad.clear();
    string encodage;
    passage(arbre, encodage);
}

void impressionFile(string file)
{
    // Starting file
    string lecture = root;
    lecture = lecture + data + file;
    ifstream myfileL (lecture);
    // Writing file
    string ecriture = root;
    ecriture = ecriture + encode + file;
    ofstream myfileE (ecriture);

    string line;
    if (myfileL.is_open() && myfileE.is_open())
    {
        while (getline(myfileL, line))
        {
            for(unsigned int i = 0; i < line.size(); i++)
            {
                char letter = line[i];
                myfileE << trad[letter];
            }
        }
        myfileE << "\n";
    }
    myfileE.close();
    myfileL.close();
}

void remplirDico(string nom_fichier)
{
    dico.clear();
    string line;
    string nom = root;
    nom = nom + freq + "freq_" + nom_fichier;
    ifstream fichier (nom.c_str(),ios::in);
    getline(fichier, line);
    while (getline(fichier, line))
        {
        char letter= line[0];
        char nombre=line[2];
        int nb=0;
        int i= 2;
        while (i<line.size())
        {
           nb=nb*10+(int)nombre - '0';
           i++;
           nombre=line[i];
        }
        dico.insert(pair<char, int>(letter, nb));
        }
}

void decode(Noeud* racine, string nom_fichier)
{
    string nom = root;
    nom = nom + encode + nom_fichier;
    string nom2 = root;
    nom2 = nom2 + decodage + nom_fichier;
    string line;
    ifstream fichier (nom);
    if (fichier.is_open())
    {
        ofstream message(nom2);
        if (message.is_open())
        {
            Noeud* fils;
            fils = racine;
            while (getline(fichier, line))
            {
                for(unsigned int i = 0; i < line.size(); i++)
                {
                    char letter = line[i];
                    fils = get_Fils((int) letter -'0', fils);
                    if (fils->letter != interdit)
                    {
                        message << fils->letter;
                        fils = racine;
                    }
                }
            }
            fichier.close();
            message.close();
        }
        else
        {
            exit(1);
        }
    }
    else
    {
        exit(1);
    }
}

int main ()
{
    string fileName = "alice.txt";

    createDico(fileName);
    //printDico();

    impressionFreqences(fileName);

    createTree();
    //Afficher(arbre);

    createTrad();
    //printTrad();

    impressionFile(fileName);

    cout << "fin codage" << endl;

    // Decodage
    // Initialisation
    arbre = NULL;

    remplirDico(fileName);
    //printDico();

    createTree();
    //Afficher(arbre);

    createTrad();
    //printTrad();

    decode(arbre, fileName);

    cout << "fin decodage" << endl;

    return 0;
}
