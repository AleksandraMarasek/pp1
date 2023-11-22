movie_titles=['HG: Ballad of songbirds and snakes','Barbie','Black swan','Nun']

file=open("movies.txt","w")

for title in movie_titles:
    file.write(title+'\n')

file.close()

print('your movies should be added to the movie.txt file')