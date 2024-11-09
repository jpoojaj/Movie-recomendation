"""Main application entry point"""
from recommender import MovieRecommender

def main():
    recommender = MovieRecommender()
    
    print("\nMovie Recommendation System")
    print("-" * 30)
    
    # Get recommendations for user 1
    user_id = 1
    recommendations = recommender.get_recommendations(user_id)
    
    print(f"\nTop 5 Movie Recommendations for User {user_id}:")
    print("\nMovie Title                    | Predicted Rating")
    print("-" * 50)
    
    for movie_id, predicted_rating in recommendations:
        movie_title = recommender.db.get_movie_title(movie_id)
        print(f"{movie_title:<30} | {predicted_rating:.2f}")

if __name__ == "__main__":
    main()