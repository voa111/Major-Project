from flask import Blueprint, render_template, request, redirect
from app.models import db, Player
import pandas as pd

ui_bp = Blueprint(
    'ui_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@ui_bp.route('/')
def home():
    return render_template("home.html")


@ui_bp.route('/players', methods=['GET', 'POST'])
def players_list():
    # first = request.form.get('first')
    # last = request.form.get('last')
    # height = request.form.get('height')
    # weight = request.form.get('weight')
    # threepoint = request.form.get('threepoint')
    # freethrow = request.form.get('freethrow')
    # avgscore = request.form.get('avgscore')
    # player1 = Player(
    # short_name=short_name,
    # overall=overall,
    # age=age,
    # height_cm=height_cm,
    # wight_kg=wight_kg,
    # club_name=club_name
    # club_position=club_position,
    # nationality_name=nationality,
    # skill_moves=skill_moves
    # international_reputation=international_reputation,
    # pace=pace,
    # shooting=shooting,
    # passing=passing,
    # dribbling=dribbling,
    # defending=defending,
    # physic=physic,
    # attacking_finishing=attacking_finishing,
    # attacking_heading_accuracy=attacking_heading_accuracy,
    # skill_dribbling=skill_dribbling,
    #
    # )
    # db.session.add(player1)
    # db.session.commit()
    return render_template('players.html', players=players)


@ui_bp.route('/players/add_player')
def add_player():
    title = 'Create New Player'
    return render_template('add_player.html', title=title)


@ui_bp.route('/players/import/upload_file', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        parse_csv_players(uploaded_file.filename)
    return redirect('/players/import')


@ui_bp.route('/players/import', methods=['GET', 'POST'])
def import_players():
    return render_template('upload_players.html')


def parse_csv_players(file_path):
    # Use Pandas to parse the CSV file
    csv_data = pd.read_csv(file_path)
    # Loop through the rows and create a Student object for each row
    for i, row in csv_data.iterrows():
        player = Player(
            short_name=row['short_name'],
            overall=row['overall'],
            age=row['age'],
            height_cm=row['height_cm'],
            weight_kg=row['weight_kg'],
            club_name=row['club_name'],
            club_position=row['club_position'],
            nationality_name=row['nationality_name'],
            skill_moves=row['skill_moves'],
            international_reputation=row['international_reputation'],
            pace=row['pace'],
            shooting=row['shooting'],
            passing=row['passing'],
            dribbling=row['dribbling'],
            defending=row['defending'],
            physic=row['physic'],
            attacking_finishing=row['attacking_finishing'],
            attacking_heading_accuracy=row['attacking_heading_accuracy'],
            skill_dribbling=row['skill_dribbling']
        )
        db.session.add(player)
    db.session.commit()


@ui_bp.route('/api/players')
def players():
    return {'data': [player.to_dict() for player in Player.query]}


@ui_bp.route('/selectplayers')
def select_players():
    # need to get list from database column (names and ids)
    dropdown_list = ['Air', 'Land', 'Sea']
    player_list = [r.short_name for r in db.session.query(Player.short_name)]
    return render_template('select_players.html', dropdown_list=player_list)


@ui_bp.route('/game')
def game():
    p1 = Player.query.filter_by(short_name='L. Messi').first()
    p2 = Player.query.filter_by(short_name='Cristiano Ronaldo').first()
    return render_template("game.html", p1=p1, p2=p2)