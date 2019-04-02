#include <iostream>
#include <fstream>
#include <string>
#include <dirent.h>
#include <map>
#include <algorithm>
using namespace std;

#define root "../"
#define data "data/"

// Global variables list :

map <char, int> dico;

// Functions :

void printFile (string file = "freq_static.txt") {
    string line;
    string temp = root + file;
    ifstream myfile (temp);
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
          cout << line << '\n';
        }
        myfile.close();
    }

    else cout << "Unable to open file" << endl;
}

void readData () {
    DIR * rep = opendir(root "data");
    if (rep != NULL)
    {
        struct dirent * ent;
        while ((ent = readdir(rep)) != NULL)
        {
            printFile(data + string(ent->d_name));
        }
        closedir(rep);
    }
}

void createDico (string file) {
    string line;
    string temp = root + file;
    ifstream myfile (temp);
    if (myfile.is_open())
    {
        while (getline(myfile,line))
        {
            for(unsigned int i = 0; i < line.size(); i++) {
                char letter = line[i];
                cout << "letter : " << letter << endl;
                if (dico.count(letter) != 0) {
                    dico.insert(pair(letter, 1));
                }
                else {
                    dico[letter]++;
                }
            }
        }
        myfile.close();
    }
    else cout << "Unable to open file" << endl;
}

int main () {
    printFile();
    //readData();
    createDico("data/standard.txt");
    return 0;
}
