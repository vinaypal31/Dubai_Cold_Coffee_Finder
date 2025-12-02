☕ Dubai Cold Coffee Finder

Dubai Cold Coffee Finder is a Python-based mini-project that helps users find the best cold coffee shops in Dubai using multiple smart filters such as:

- 📍 **Latitude**  
- 📍 **Longitude**  
- ⏰ **Opening Time**  
- ⏰ **Closing Time**

This project uses a simple CSV dataset and a Python script to return the most suitable coffee shops based on the user’s search input.

📂 Project Structure

dubai_project/
│── data.csv # Dataset of Dubai coffee shops
└── dubai.py # Main Python search script

📊 Dataset Information

Your dataset should include the following columns:

| name             | latitude | longitude | opening_time | closing_time |
|------------------|----------|-----------|---------------|----------------|
| Starbucks Marina | 25.080   | 55.140    | 08:00         | 23:00         |
| Costa JBR        | 25.080   | 55.130    | 09:00         | 00:00         |

Modify or expand based on your dataset.

🔍 Features

- Search coffee shops using **Latitude & Longitude**  
- Filter by **opening and closing time**  
- Fast and simple search system  
- Fully customizable Python script  
- Works with any CSV dataset  

🧠 Future Improvements

- Add distance calculation (**Haversine formula**)  
- Add real-time map display using **Folium**  
- Add **Streamlit UI** for better user experience  
- Add **ratings, menu, or price range** 
