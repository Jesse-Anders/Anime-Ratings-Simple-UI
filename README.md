Simple UI For Anime Ratings Lineaer Regression Model

( Complete Set of Anime Rating Models Can Be Run in Jupyter Notebook: AnimeRating.ipynb )

Documentation:

Install Docker Desktop App - https://www.docker.com
Create Environment in VS Studio with included Files (file structure)

From Terminal in VS Code Run:
docker build -t anime_image_name .

From Terminal in VS Code Run:
docker run --name new_anime_container_name -p 8001:8001 anime_image_name

In Web Browser Navigate to:
http://localhost:8001/docs

To test model, enter into Post Prediction Request Body on the FastAPI Page:
{"features": [64, 8.0, 1, 0, 1, 103707.0, 14351, 25810, 2656, 86547, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1, 2]}

The “features” represent an encoded set of 40 features from the anime data set as used by the linear regression model. The table figure below is a sample of what each encoded value represents

<img width="1021" alt="Screenshot 2024-11-06 at 12 13 13 AM" src="https://github.com/user-attachments/assets/22449116-a1cf-4e1e-87aa-b5b55528c94b">
