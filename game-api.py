from flask import Flask
from flask import request
from gameState import GameState
import http.client
import time

app = Flask(__name__)
gameState = GameState()

def run_game(game):
    gameState.reset()
    gameState.shots = int(game['shots'])
    print(gameState.shots)
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
    target.isHit = False
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
    gameState.hits = gameState.hits + 1
    print(gameState.hits, gameState.shots)
    t = gameState.targets[target]
    t.isHit = True
    t.isLit = False

    if gameState.isComplete:
        gameState.end = time.time()
        print("GAME OVER - ", gameState.get_durration())

    elif gameState.allTargetsHit:
        for t2 in gameState.targets:
            turn_target_on(t2)
            print(t2.name, t2.isHit, t2.isLit)
    
    return str(target)

app.run(host='0.0.0.0')
