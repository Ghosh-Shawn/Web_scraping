# web_scraping
Web scraping projects

The website `https://www.fifaindex.com/players/fifa20/` is scraped in this project,  to collect information about players. 



First , `fifa-player.py` collects the urls of the single player pages and saves them as a csv file names `url.csv`.

Then `info.py` crawls through each of the urls in `url.csv` and stores the player's information in a file called `info.csv`. In this version only Player's name and Height is collected. You can edit this file to collect other information about the player. 



To run the the project, download `fifa_player.py` and `info.py`. Then first run `fifa_player.py` and then `info.py`. 

>>In order to collect a different set of information from each player, you can edit `info.py`. 
