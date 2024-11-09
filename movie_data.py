"""Movie and rating data management"""

class MovieDatabase:
    def __init__(self):
        # Sample movie data: id -> (title, genre)
        self.movies = {
            1: ("The Shawshank Redemption", "Drama"),
            2: ("The Godfather", "Crime"),
            3: ("The Dark Knight", "Action"),
            4: ("Pulp Fiction", "Crime"),
            5: ("Forrest Gump", "Drama"),
            6: ("Inception", "Sci-Fi"),
            7: ("The Matrix", "Sci-Fi"),
            8: ("Goodfellas", "Crime"),
            9: ("The Silence of the Lambs", "Thriller"),
            10: ("Fight Club", "Drama")
        }
        
        # Sample user ratings: user_id -> {movie_id: rating}
        self.ratings = {
            1: {1: 5, 2: 4, 3: 5, 4: 4, 7: 5},
            2: {1: 4, 2: 5, 4: 5, 5: 3, 8: 4},
            3: {1: 5, 2: 4, 3: 4, 6: 5, 7: 5},
            4: {2: 4, 4: 4, 5: 5, 6: 3, 8: 4},
            5: {1: 5, 3: 4, 5: 4, 7: 4, 9: 5}
        }
    
    def get_movie_title(self, movie_id):
        return self.movies[movie_id][0]
    
    def get_user_ratings(self, user_id):
        return self.ratings.get(user_id, {})