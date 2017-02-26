% Manuel Utilisateur du module MarkPad
 % Mathieu Barbe
% 21 janvier 2017

# Introduction
## Fonctionnalités

- Détection du language markUP utilisé en fonction de l'extension du fichier chargé;
- utilisation d'un language par défaut pour les nouveaux fichiers ou fichier sans extension;
- déplacement vers le titre suivant ou précédent avec annonce de son niveau hiérachique;
- déplacement vers le titre de niveau 1 à 5 suivant ou précédent;
- déplacement vers le lien suivant ou précédent;

# Installation

Deux solutions s'offre à vous pour l'installation de MarkPad. Vous pouvez le tester facillement en téléchargeant une archive pré à l'emplois contenant 6pad++, MarkPad et les configurations nécessaire.
Vous avez également la possibilité d'ajouter le modul MarkPad à votre installation de 6pad++.

## Pack 6pad++ et MarkPad

Ce pack prêt à l'emploi vous permêt de tester rapidement 6padd++ et MarkPad et de partir sur de bonne base. Il contient :

- 6pad++ Apha 10.1;
- MarkPad 0.1 alpha;
- les configuration de nécessaire pour lancer MarkPad.

1. Télécharger l'archive disponnible ici : [Pack MarkPad 0.1 alpha ()];
2. Extraire l'archive où vous le voulez, dans votre dossier utilisateur ou sur une clé USB;
3. 6padd++ ne nécessite pas d'installation, vous pouvez lancer directement 6pad++.exe;
4. Si vous voulez que MarkPad soit utilisé pour les nouveaux documents ou pour les fichiers sans extension, référez vous à la section configuration de ce manuel.

## MarkPad seul

Si vous avez déjà 6pad++ installé sur votre système et que vous voulez ajouter le module MarkPad, veuillez suvre ces différentes étapes :

  1. Télécharger la dernière version de MarkPad ici : [MarkPad version 0.1 alpha ()];
  2. Extraire l'archive dans le dossier plugin de votre installation de 6pad++ (pour information, l'archive contient un dossier markpad regroupant les fichiers, vous pouvez faire un extraire ici);
  3. Ajouter le plugin markpad dans votre fichier de configuration 6pad++.ini :  
 plugin=markpad
 4. Si vous voulez que MarkPad soit utilisé pour les nouveaux documents ou pour les fichiers sans extension, référez vous à la section configuration de ce manuel.

# Utilisation

Quand une extension corespond à un langage défini dans MarkPad, celui-ci est chargé automatiquement pour ce document.
Un menu MarkPad spécifique à ce document sera créé et contiendra l'ensemble des fonctionnalités.
 
## Déplacement

Dans ce menu, vous pouvez déplacer d'élément en éléments, en voici la liste :

- Titre de niveau, le niveau hiérachique sera annoncé lors du déplacement. 
- Titre de niveau 1;
- titre de niveau 2;
- titre de niveau 3;
- lien hypertexte.

Note : Il est également possible de se déplacer au titre de niveau 4 et 5, mais ces items n'ont pas été ajoutés pour ne pas surcharger le menu déplacement. Veuillez vous référer à la section raccourci clavier de ce document.

## Racourcis Clavier

| Fonctionnalité | Raccourci | Détail |
|----|----|----|
| Se déplacer au titre suivant | CTRL + R | Va au titre suivant et annonce son niveau puis son nom |
| Se déplacer au titre précédent | CTRL + SHIFT + R | Va au titre suivant et annonce son niveau puis son nom |
| Se déplacer au titre ne niveau 1 à 5  suivant | CTRL + 1 à 5 | Va au titre de niveau corespondant au chiffre utilisé et le li |

# Configuration
## Choix des extensions

# Ajouter son language MarkUp

