from flask import Flask, request, render_template, send_file
from Rekomendacje import get_recommendation, Rekomendacje, get_example_moviescore


app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

rekomendacje = get_recommendation('Rekomendacje.pkl')
movies = rekomendacje.movies


user_score = get_example_moviescore()
user_movies = movies.get_movies_by_ids(user_score.index)

@app.route('/')
def main():
    return render_template('index.html',
                           user_score=user_score['rating'].to_dict(),
                           user_movies=user_movies.to_dict(orient='items'))


@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    import json
    data = json.loads(request.data)
    print(type(data))
    recommended = rekomendacje.get_recommendation(data)

    print(recommended)
    return recommended.to_dict(orient='items')


app.run(debug=True, use_reloader=True, host='0.0.0.0', port=80)

