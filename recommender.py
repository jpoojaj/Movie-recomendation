"""Recommendation engine implementation"""
import math
from movie_data import MovieDatabase

class MovieRecommender:
    def __init__(self):
        self.db = MovieDatabase()
    
    def calculate_similarity(self, user1_ratings, user2_ratings):
        """Calculate similarity between two users using Pearson correlation"""
        common_movies = set(user1_ratings.keys()) & set(user2_ratings.keys())
        if not common_movies:
            return 0
        
        n = len(common_movies)
        
        # Calculate means
        sum1 = sum(user1_ratings[movie] for movie in common_movies)
        sum2 = sum(user2_ratings[movie] for movie in common_movies)
        
        mean1 = sum1 / n
        mean2 = sum2 / n
        
        # Calculate correlation components
        numerator = sum((user1_ratings[movie] - mean1) * (user2_ratings[movie] - mean2) 
                       for movie in common_movies)
        
        sum1_sq = sum((user1_ratings[movie] - mean1) ** 2 for movie in common_movies)
        sum2_sq = sum((user2_ratings[movie] - mean2) ** 2 for movie in common_movies)
        
        denominator = math.sqrt(sum1_sq * sum2_sq)
        
        if denominator == 0:
            return 0
            
        return numerator / denominator
    
    def get_recommendations(self, user_id, n_recommendations=5):
        """Get movie recommendations for a user"""
        user_ratings = self.db.get_user_ratings(user_id)
        if not user_ratings:
            return []
        
        # Calculate similarities with other users
        similarities = {}
        for other_id in self.db.ratings:
            if other_id != user_id:
                similarity = self.calculate_similarity(
                    user_ratings,
                    self.db.get_user_ratings(other_id)
                )
                similarities[other_id] = similarity
        
        # Get weighted ratings for unseen movies
        weighted_ratings = {}
        for other_id, similarity in similarities.items():
            if similarity <= 0:
                continue
                
            other_ratings = self.db.get_user_ratings(other_id)
            
            for movie_id, rating in other_ratings.items():
                if movie_id not in user_ratings:
                    weighted_ratings.setdefault(movie_id, [0, 0])
                    weighted_ratings[movie_id][0] += similarity * rating
                    weighted_ratings[movie_id][1] += similarity
        
        # Calculate predicted ratings
        recommendations = []
        for movie_id, (rating_sum, similarity_sum) in weighted_ratings.items():
            if similarity_sum > 0:
                predicted_rating = rating_sum / similarity_sum
                recommendations.append((movie_id, predicted_rating))
        
        # Sort and return top N recommendations
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:n_recommendations]