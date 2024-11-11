from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the clustered stock data
data = pd.read_csv('stock_flask.csv') 

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user-selected risk level from the form
    risk_level = request.form.get('risk_level')

    category_data = data[data['Risk_Label'] == risk_level]

    avg_vector = category_data[['Volatility_14d', 'beta', 'BB_Upper', 'BB_Lower']].median().values

    stock_features = data[['Volatility_14d', 'beta', 'BB_Upper', 'BB_Lower']].values

    similarity_scores = cosine_similarity(stock_features, [avg_vector]).flatten()

    data['similarity'] = similarity_scores

    category_data = data[data['Risk_Label'] == risk_level]
    
    # Filter the data based on the selected risk level
    unique_stocks = (
        category_data.groupby('symbol')
        .agg({'similarity': 'mean'})
        .reset_index()
        .sort_values(by='similarity', ascending=False)
        .head(5)  # Limit to the top 5 recommendations
    )

    recommended_stocks = unique_stocks.merge(data, on='symbol').drop_duplicates(subset='symbol')
    
    # Send the filtered list to the results page
    return render_template('recommend.html', stocks=recommended_stocks.to_dict(orient='records'), risk_level=risk_level)

if __name__ == '__main__':
    app.run(debug=True)