"""
Using Tf-IDF to find similarities between movie descriptions.
This will be used as a content-based recommender system.

Dataset Link:
http://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz


Useful links:
https://stackoverflow.com/questions/46875469/where-can-i-find-a-movie-dataset-with-plots-and-genres
http://www.cs.cmu.edu/~ark/personas/


Intructions - Downloading and Loading the data
----------------------------------------------
1. Create a function to download and untar a file.
   The function should have the following inputs:
   - url
   - download path
   - extract path
2. Use the function in step 1 to download the following:
   http://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz
3. Define another function that reads reads in the metadata and plot summaries,
   joins the two datasets together on the ID, and returns the results in a
   pandas dataframe.
4. Package up your functions so they can be reused. The user should be able to
   get the dataframe in step 3 be calling a function. The function signature 
   can be something like:
   <module_name>.get_movie_summaries(download_path, extract_path=None)


Instructions - Building a Basic Recommender System
--------------------------------------------------
1. Use the movies summary dataset along with TF-IDF to create a basic 
   recommender system. Your recommender system should take in the name of a
   movie and output the names of similar movies.
2. Recommendations:
   - Clean text before applying TF-TDF.
   - Use TF-IDF to represent each movie as a vector.
   - Find similarities between movies by using the cosine similarity metric.
   - Be creative. You can combine similarities based on plot summaries or
     genres. Experiment to see what gives you decent results.

"""
