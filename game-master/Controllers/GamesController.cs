using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace game_master.Controllers
{
    [ApiController]
    public class GamesController : ControllerBase
    {
        private static GameState _gameState;

        [Route("/games")]
        [HttpPost]
        public void Post([FromBody] Game game)
        {
            Console.Write(game.Kind);
            var factory = new GameStateFactory();
            _gameState = factory.CreateGameState(game);
            _gameState.Start();
        }

        [Route("/games/{targetId}")]
        [HttpPost]
        public void RecordHit(int targetId)
        {
            _gameState.RecordHit(targetId);

            if (_gameState.IsComplete)
            {
                Console.WriteLine($"GAME OVER - {_gameState.TotalGameTime}");
                return;
            }

            _gameState.LightNextTarget();
        }
    }
}
