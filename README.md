# movie-buzz

Group Members: Brendan Gilroy, Kristina Barounis, and Hannah Parker


## Big question: What movies should Microsoft invest in producing as part of its new streaming service venture?
- How are box office revenue, awards, and ratings influenced by budget, genre, and actors?
- Hypotheses: 
  - Positive correlation between top actors and revenue
  - At some point, a higher budget will no longer contribute to an increase in revenue

## Process & Tools Used
1. Researched what factors might go into movie success, possible variables, etc.
2. Scraped Box Office Mojo, used OMDB's API to gather data:
    - Independent variables: Budget, genre, actors
    - Dependent variables: Box office revenue, awards (wins and nominations), ratings (Rotten Tomatoes and IMDB)
3. Created an Amazon RDB instance, with a main table containing the movie titles (Box Office Mojo and OMDB had different titles), budget, box office revenue, release date, award wins, award nominations, Rotten Tomato ratings, and IMDB ratings. Created separate tables for genres and actors, and then created join tables for genres and movies and for actors and movies. 
4. Queried data and created visuals using Matplotlib to gain insight into any interesting relationships. 

## Findings

### What can you expect to spend on a _good_ movie?
We defined a 'good' movie to be a movie that has a Rotten Tomatoes Critic rating of over 75%. When we plotted this, calculated a five number summary, and found the mean, we saw that []

![budget](https://github.com/h-parker/movie-buzz/blob/master/wise_budget.png)


### Are budget and revenue correlated?
[]

### Which movie genres are crowd favorites? 
-----> we realize that drama has more movies than other categories but [insert defense or contrition here], and in the future, we would like to [               ]

### Which actors will generate the most revenue?
[]


## Final Recommendations
Based on our findings, we would recommend that Microsoft look to spend somewhere between $20MM and $100MM, most likely around $69MM based on our budget data. Furthermore, it looks as though documentaries 
