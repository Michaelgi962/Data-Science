## Intro
files in this project: 
10 files: Rotating Proxy Crawler.ipynb,...,Rotating Proxy Crawler9.ipynb
1 file: Refactor.ipynb
1 file: break_ip_text_files_into_n_parts.ipynb
1 file: monsterScraper.ipynb
1 file: MonsterScraper_ForEveryState.ipynb
1 file: scrapeDataFromMonster.ipynb
2 files: HttpProxyList.txt, HttpsProxyList.txt
1 folder proxyLists:
-> 2 files: filtered_http_proxys.txt,filtered_https_proxys.txt
-> 10: files: http_proxys_part_0.txt,...,http_proxys_part_9.txt

## Process

Start with break_ip_text_files_onto_n_pats.ipynb:
-> this file will break the HttpProxyList.txt and HttpsProxyList.txt files into 10 parts and store them in proxyLists

Open Rotating Proxy Crawler.ipynb,...,Proxy Crawler9.ipynb and run all the codes simultaneously:
-> this file will delete all of the bad or slow-connecting proxies and append the filtered oned to the files filtered_http_proxys.txt and filtered_https_proxys.txt

Open MonsterScraper_forEveryState.ipynb:
-> randomly select one of the filtered proxies for each job posting request

-> MonsterScraper_forEveryState.ipynb will collect a dataframe of 1's and 0's for each skill listed in each job posting in each state, along with the job title
