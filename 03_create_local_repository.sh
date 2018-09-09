# Filenaam: 03_create_local_repository.sh
# Functie: create local git repository vanuit Visual Studio
# Opmerking:
#
#

# Voor SSRS obv VS2010 maak de local repository aan vanuit Visual studio ipv van het git init commando
Het aanmaken van local repository vanuit VS2010 gaat mbv de volgende stappen:
1. Start Visual Studio op
2. Zorg dat er een solution is aangemaakt of een bestaande solution met een project is geopend
3. selecteer in de solution Explorer van VS2010 het project
4. Kies met de rechter muisoptie de optie "Create Git Repository" 
(zie ook het artikel https://blog.discountasp.net/using-git-with-visual-studio-2010-an-introduction-2/)

Als alles goed is gegaan zie je in de directory van het VS2010 project (in de directory met de sln en de suo files)
een hidden directory .git en de files .gitignore en .tfignore aangemaakt worden.

In de solution explorer van VS2010 zie je achter de projectnaam de tekst (master) verschijnen

# Voor text files gebruik het git init commando
# git init
