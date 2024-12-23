import csv
import json
import random

# Define the input and output file paths
csv_file_path = r'C:\Users\hp\projects\apps\app_christmasMovies\assets\scripts\data\christmas_movies.csv'
json_file_path = r'C:\Users\hp\projects\apps\app_christmasMovies\assets\scripts\data\christmas_movies.json'

# Initialize an empty list to hold movie data
movies = []

# Function to safely convert a string to an integer
def safe_int_conversion(value, default=None):
    try:
        return int(value)
    except ValueError:
        return default

# Open and read the CSV file
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Read all rows into a list
    all_movies = list(csv_reader)
    # Randomly sample 20 movies
    # sampled_movies = random.sample(all_movies, 20)
    for row in all_movies:
        # Create a dictionary for each movie with the desired structure
        movie = {
            'title': row['title'],
            'thumbnail': {
                'trending': {
                    'small': None,  # Placeholder; adjust as needed
                    'large': None   # Placeholder; adjust as needed
                },
                'regular': {
                    'small': None,   # Placeholder; adjust as needed
                    'medium': row['img_src'],  # Use the image source from CSV
                    'large': None    # Placeholder; adjust as needed
                }
            },
            'year': safe_int_conversion(row['release_year']),
            'category': 'Movie',  # Set category to 'Movie'
            'rating': row['rating'],
            'isBookmarked': False,  # Default value; adjust as needed
            'isTrending': False     # Default value; will set some to True below
        }
        # Append the movie dictionary to the list
        movies.append(movie)

# Randomly select a few movies to mark as trending
trending_count = random.randint(1, 5)  # Number of trending movies
trending_indices = random.sample(range(20), trending_count)
for index in trending_indices:
    movies[index]['isTrending'] = True

# Write the list of movies to a JSON file
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(movies, json_file, indent=4)

print(f"Test data successfully created at {json_file_path}")
