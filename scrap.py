import requests
from bs4 import BeautifulSoup


for i in range(1, 22):
    r = requests.get(
        'https://www.ivoox.com/podcast-contrahistoria_sq_f1298566_'+str(i)+'.html')

    soup = BeautifulSoup(r.content, 'html.parser')
    episodios = soup.find_all('img', 'main lozad radius-sm img-hover')

    for episodio in episodios:
        titulo = episodio.get('alt')
        link = episodio.parent.get('href')
        n = link.split("_1.html")[0][-8:]

        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'html.parser')
        descripcion = soup.find('p', 'description').text.split(
            '· “La ContraHistoria de España')[0].split('Apoya La Contra en:')[0]
        fecha = soup.find('span', 'icon-date').text

        with open(titulo+".md", "w") as file:
            file.write("# "+titulo+'\n')
            file.write('<iframe id=\'audio_88903085\' frameborder=\'0\' allowfullscreen=\'\' scrolling=\'no\' height=\'200\' style=\'width:100%;\' src=\'https://www.ivoox.com/player_ej_' +
                       n + '_6_1.html\' loading=\'lazy\'></iframe>')
            file.write(fecha+"\n\n")
            file.write(descripcion.replace('\r', '\n\n')+'\n\n')
            file.write(link+'\n')
