from flask import Flask
from flask import request
from gameState import GameState
import http.client

app = Flask(__name__)
gameState = GameState()

def run_game(game):
    gameState.shots = int(game['shots'])
    if game['style'] == 'on-off':
        run_on_off_game(game)

def run_on_off_game(game):
    for target in gameState.targets:
        turn_target_on(target)
    
def turn_target_on(target):
    conn = http.client.HTTPConnection(target.name, 5000)
    conn.set_debuglevel(1)
    conn.request("PUT", "/5/255")
    conn.close()
    target.isLit = True
    return

def turn_target_off(target):
    conn = http.client.HTTPConnection(target.name, 5000)
    conn.set_debuglevel(1)
    conn.request("PUT", "/5/0")
    conn.close()
    target.isLit = False
    target.isHit = False
    return

@app.route('/games', methods=['POST'])
def post_game():
    game = request.get_json()
    run_game(game)
    return game

@app.route('/<int:target>', methods=['POST'])
def record_hit(target):
    print("HIT!!! - " + str(target))
    gameState.set_hits(gameState.get_hits() + 1)
    print(gameState.shots, gameState.hits)
    t = gameState.targets[target]
    t.isHit = True
    t.isLit = False
    print(gameState.get_durration())
    print(gameState.isComplete)

    if gameState.isComplete:
        print("GAME OVER - ", gameState.get_durration())
    
    for t2 in gameState.targets:
        print(t2.name, t2.isHit, t2.isLit)
    
    return str(target)

app.run(host='0.0.0.0')
