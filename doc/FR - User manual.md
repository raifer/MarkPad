% Manuel Utilisateur du module MarkPad
% Mathieu Barbe
% 21 janvier 2017

# Introduction

MarkPad est une extension dédiée à l'édition de langage à balisage léger permettant une prise de note rapide.
Ces nouvelles fonctionnalités viennent prendre place dans l'éditeur spécialisé "6pad++" développé par Quentin C. et dont vous pouvez suivre son projet sur github [à cette adresse](https://github.com/qtnc/6pad2 "Projet de 6pad++ sur Github").

## Fonctionnalités

- Détection automatique du langage en fonction du fichier en cour d'édition;
- utilisation d'un langage par défaut pour les nouveaux fichiers ou fichier sans extension;
- déplacement vers le titre suivant ou précédent avec annonce de son niveau hiérarchique;
- déplacement vers le titre suivant ou précédent en spécifiant son niveau hiérarchique;;
- déplacement vers le lien suivant ou précédent;
- Langues : Anglais et Français.

# Installation

Deux solutions s'offre à vous pour l'installation de MarkPad :
    
1. Le pack complet : tester facilement MarkPad en téléchargeant une archive pré à l'emploi.
2. L'extension seul : pour ajouter MarkPad à votre environnement existant.

## Pack 6pad++ et MarkPad

Ce pack prêt à l'emploi vous permet de tester rapidement 6padd++ et MarkPad et de partir sur de bonne base. Il contient :

- 6pad++ Apha 10.1;
- MarkPad 0.1 alpha;
- les configuration nécessaire pour lancer MarkPad au démarrage de 6pad++.

1. Télécharger l'archive disponible ici : [Pack MarkPad 0.1 alpha](http://sandbox.raifer.fr/markpad/pack-markpad-stable.zip "Lien vers le pack MarkPad");
2. Extraire l'archive dans votre dossier utilisateur, disque dur  ou sur une clé USB;
3. 6padd++ ne nécessitant pas pas d'installation, vous pouvez lancer directement 6pad++.exe;
4. Ouvrer un fichier à balisage légé compatible, par exemple, Markdown, pour lancer MarkPad;
5. Si vous voulez que MarkPad soit utilisé pour les nouveaux documents ou pour les fichiers sans extension, référez vous à la section configuration de ce manuel.

## MarkPad seul

Si vous avez déjà 6pad++ installé sur votre système et que vous voulez ajouter le module MarkPad a votre installation, veuillez suvre ces différentes étapes :

        1. Télécharger la dernière version de MarkPad : [MarkPad version 0.1 alpha](http://sandbox.raifer.fr/markpad/markpad-stable.zip "Lien vers l’extension de MarkPad stable");
        2. Extraire l'archive dans le dossier "plugin" de 6pad++ (pour information, l'archive contient un dossier markpad à sa racine qui regroupe les fichiers, il est donc possible d'utiliser sans risque la fonctionnalité "extraire ici");
        3. Ajouter le plugin markpad dans votre fichier de configuration 6pad++.ini :  
    plugin=markpad
    4. Si vous voulez que MarkPad soit utilisé pour les nouveaux documents ou pour les fichiers sans extension, référez vous à la section configuration de ce manuel.

# Utilisation

À l'ouverture d'un fichier, quand une extension correspond à un langage à balisage léger connu, MarkPad est chargé automatiquement.
Le module se lance dans l'onglet courant et sera configuré en fonction des balises propre à ce langage.

MarkPad et le type de langage utilisé sont liés a l'onglet courant.
Il est donc possible d'avoir plusieurs onglets ouverts, et pour chacun d'entre eux, une configuration spécifique.
Mais cela reste transparent à l'usage.


Si MarkPad n'est pas disponible dans l'onglet courant, c'est que l'extension du fichier ne correspond à aucun langage connu. Il est possible d'associer un langage à des nouveau fichiers ou à des fichiers sans extension, vous référer à la section configuration.

Quand l'extension est disponible, un menu MarkPad spécifique à ce document sera créé. Il contiendra l'ensemble des fonctionnalités disponible.
    
## Menu de déplacement

Dans ce menu sont regroupées les fonctions de déplacement, en voici la liste :

- Titre de niveau suivant / précédent;  
Lors du déplacement, le niveau hiérarchique  du titre sera annoncé suivi du nom.
- Titre de niveau 1;
- titre de niveau 2;
- titre de niveau 3;
- lien hypertexte.

Note : Il est également possible de se déplacer au titre de niveau 4 et 5, mais ces items n'ont pas été ajoutés ici pour ne pas surcharger le menu déplacement. Veuillez vous référer à la section raccourci clavier de ce document pour voir comment les utiliser.

## Raccourcis Clavier

| Fonctionnalité | Raccourci | Détail |
|----|----|----|
| Se déplacer au titre suivant | CTRL + R | Va au titre suivant et annonce son niveau puis son nom |
| Se déplacer au titre précédent | CTRL + SHIFT + R | Va au titre précédent et annonce son niveau puis son nom |
| Se déplacer au prochain titre de niveau hiérarchique 1 à 5 | CTRL + 1 à 5 | Va au prochain titre de niveau corespondant et le li |
| Se déplacer au précédent titre de niveau hiérarchique 1 à 5 | CTRL + SHIFT + 1 à 5 | Va au précédent titre de niveau corespondant et le li |
# Configuration

Dans le dossier "markup language" se trouve la configuration des langages utilisable avec MarkPad. 
Ces fichiers ont pour extension ".mul".

On retrouve pour chaque fichier de configuration :

- La liste des extensions compatible avec ce langage;
- Les regex utiles pour retrouver les niveaux de titres et les liens.

## Choix des extensions

Voici à quoi ressemble la ligne de configuration des extensions pour le langage markdown:  
extension='markdown', 'md', 'txt', 'noext'

On indique ici, que l'on désir utiliser le langage Markdown pour les extensions "md", "markdown", "txt" et l'extension spéciale "noext". 

L'extension spéciale "noext" permet d'utiliser MarkPad dans les nouveaux documents ou les fichiers sans extension.

## Utiliser MarkPad pour les nouveaux documents et les fichiers sans extension

Pour utiliser MarkPad avec des documents non enregistrés ou des fichiers sans extension. Il suffit d'ajouter "noext" à la liste des extensions dans la configuration du langage de votre choix.

## Regex

Pour retrouver les titres ou les liens dans un document, MarkPad a besoin d'une définition précise de chacun de ces objets.
Pour chacun d'entre eux, une regex devra être défini.

### Sélection du texte énoncé grâce aux parenthèses capturantes 

Pour optimiser le déplacement d'élément en élément, il est possible de préciser ce qui devra être lu par Markpad une fois l'objet trouvé.  
Par exemple : Lors d'un déplacement au titre de niveau 4 suivant, il n'est pas forcement nécessaire d'énoncer les quatre dièses en plus du titre.

Il est donc possible de délimiter le texste qui sera prononcé grâce au mécanisme des parenthèses capturantes.

Syntaxe : regex entre parenthèse suivi d'un dollar,  
exemple : "(le texte à énoncer)$"

### Liste des objets Markpad

- HEAD : Tout les titres de niveaux;
- HEAD1 : Titre de niveau 1;
- HEAD2 : Titre de niveau 2;
- HEAD3 : Titre de niveau 3;
- HEAD4 : Titre de niveau 4;
- HEAD5 : Titre de niveau 5;
- LINK : Lien

### exemple de regex

Voici pour exemple, HEAD et HEAD1 pour le langage Markdown : 

HEAD='^#+ (.+)$'  
On recherche ici un ou plusieurs dièze en début de ligne, suivit par un espace, puis d'un texte.
Comme le texte est entouré de parenthèse capturante, c'est seulement cette parti qui sera lu lors du déplacement.

HEAD1='^# (.+)$'  
On recherche ici un dièze en début de ligne, suivi d'un espace puis d'un texte.

## Ajouter son langage à balisage léger

Il est possible d'ajouter votre langage dans la liste des langage compatible avec MarkPad. Pour ce faire :

1. Rendez-vous dans le dossier "markup language";
2. Copier le fichier template.mul vers mon_langage.mul;  
Attention, seul les fichier .mul seront pris en compte dans ce dossier.
3. Renseigner les champs :
    * extension,
    * Les regex qui vous intéresse.  
Référez-vous à la section regex pour en étudier la liste.


Pensez à partager vos nouveaux fichiers MUL avec la communauté.