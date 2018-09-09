# Filenaam: 01_create_git_hup_repos_oefen_bi_gui.sh
# Functie: create centrale remote git repository van de commandline
#          Tbv de Oefen_bi_gui sources scripts
#
# Opmerking: Relatie tussen de repositories cx1964ReposSsrsVS2010Branching02 en cx1964ReposDwhBranching wordt onderhouden met git tags obv releases aanduidingen.
#

# Tbv Ubuntu
# curl -u 'cx1964@gmail.com' https://api.github.com/user/repos -d '{"name":"cx1964ReposOefenBIGui"}'

# tbv mingw64 onder windows
# letop vul voor <PASSWORD> een password waarde in
curl -d '{"name":"cx1964ReposOefenBIGuiv012"}' -u cx1964@gmail.com:<PASSWORD> https://api.github.com/user/repos

