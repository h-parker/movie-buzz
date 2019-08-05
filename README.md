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
We defined a 'good' movie to be a movie that has a Rotten Tomatoes Critic rating of over 75%. When we plotted the budgets of movies fitting this description, calculated a five number summary, and found the mean, we saw that the middle 50% of budgets fell between $20 and $100 million, with a median of $38 million and an average of $69 million. This leads us to believe that Microsoft should expect to invest around $38 million, perhaps more, on their movies.

<img src=https://github.com/h-parker/movie-buzz/blob/master/wise_budget.png alt="budget box plot" width="450"/>


### Are budget and revenue correlated?
The relationship seemed somewhat positively correlated, but there are too many confounding variables to say with any confidence that an increased budget will lead to an increase in revenue. We recommend sticking with the range indicated above. 

<img src=https://github.com/h-parker/movie-buzz/blob/master/wise_budget.png alt="budget vs revenue scatter plot" width="450"/>



### Which movie genres are crowd favorites? 
The movie genres with the highest ratings on both IMDB and Rotten Tomatoes were 'documentary' and 'history'. However, upon looking at the distributions of ratings (pictured below), it became clear that perhaps there were fewer movies falling in these categories. We surmised that these movies might tend to get reviewed by fans of these somewhat niche genres, and therefore would tend to get higher ratings from these fans, whereas movies from more popular genres, like drama and comedy (distributions of votes also pictured below), get reviewed by the more general movie audience that may be more stingy with their ratings. Therefore, we looked at what could be considered a more objective voting board -- wins and nominations for awards. We found that drama had secured far and away more wins and nominations than any other genre, however, we did not control for the fact that it also has more movies. As a result, in the future we would like to create a weighted score based on wins, nominations, _and_ number of movies in the genre that would help level the playing field.

<img src=https://github.com/h-parker/movie-buzz/blob/master/ratings_by_genre.png alt="crowd favorites" width="450"/>
<img src=https://github.com/h-parker/movie-buzz/blob/master/documentary_ratings.png alt="documentary ratings distribution" width="450"/>
<img src=https://github.com/h-parker/movie-buzz/blob/master/history_ratings.png alt="history ratings distribution" width="450"/>
<img src=https://github.com/h-parker/movie-buzz/blob/master/drama_ratings.png alt="drama ratings distribution" width="450"/>
<img src=https://github.com/h-parker/movie-buzz/blob/master/comedy_ratings.png alt="comedy ratings distribution" width="450"/>
<img src=https://github.com/h-parker/movie-buzz/blob/master/awards_by_genre.png alt="awards across genre bar chart" width="450"/>

### Which actors will generate the most revenue?
<img src=https://github.com/h-parker/movie-buzz/blob/master/profitability_by_actor.png alt="actor profitability table" width="450"/>


## Final Recommendations
Based on our findings, we would recommend that Microsoft look to spend somewhere between $20MM and $100MM, most likely around $38MM based on our budget data. Furthermore, it looks as though documentaries consistently get high ratings among the documentary fanbase, and that it may be that dramas recieve many awards and nominations, but more research needs to be done with respect to the effect of the sheer quantity of drama movies and whether that contributed to the overwhelming number of nominations and wins in that genre. Finally, based on the revenue that James McAvoy has been associated with in the past, he may be a good actor to hire, but again, this may just be correlation, _not_ causation. 
