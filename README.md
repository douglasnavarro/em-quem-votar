# em-quem-votar
🔎 Web scraping to aid brazilian voters make well-informed decisions

## The idea:
- The idea is to find stories on politicians that will run for the 2018 brazil election
  - and give each story a rating based on how strongly it may indicate that this politician is involved with anything ilegal
  - and present this 'dossier' as clearly as possible for a regular citizen that wants to catch up on that politician's activity
## The implementation:
- **The scraper**
  - Write scrapy spiders for each trust-worthy news website (i.e a site that wont publish fake news)
  - Run each spider with a candidate name as input
    - Each spider will produce a candidate_newspaper.json file with the scraped material
- **How to rate stories as positive or negative?**
  - This is where it gets tricky. When scraping for stories on a candidate, how can we be sure that:
    1. This story is actually about that candidate and the candidate is not just mentioned.
    2. This story tells something good about that candidate.
    3. This story tells something bad about that candidate.
  - It is possible that a solution for this is feasible through NLP.
- **The presentation**
  - A web interface will be used to present the data as clearly as possible.
  - I am not sure whether an MVC framework is necessary. Even though a large amount of data must be presented, it is not going to be created or modified by the viewer.
  