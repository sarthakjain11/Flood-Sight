# Flood-Sight

## Overview

Welcome to the FloodSight a Real-Time Flood Detection project repository! This project focuses on leveraging machine learning models and real-time weather data to enhance flood preparedness through accurate detection and prediction of flood-prone conditions.

## Project Structure

- **`app.py`**: Python flask web app.
- **`Flood modelling.ipynb`**: Jupyter Notebook containing data preprocessing,visualization,building and training model.
- **`fetch_data.py`**: Python script to fetch and preprocess daily weather data from visualcrossing.com to send it to model for classification.
- **`requirements.txt`**: List of Python packages required for the project.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/FloodSight.git
   cd FloodSight

2. **Install Dependencies:**
    pip install -r requirements.txt

3. **Run Jupyter Notebook:**
    save model in pickel file

4. **Get API KEY from visual crosssing weather APIs**
    set API_KEY = "YOUR_API_KEY" in fetch_data.py

5. **Run Application:**
    python app.py

    

License
This project is licensed under the MIT License.

Feel free to reach out if you have any questions or suggestions. Happy coding!