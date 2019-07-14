using System;

namespace game_master.Controllers
{
    internal class GameStateFactory
    {
        public GameState CreateGameState(Game game)
        {
            switch (game.Kind)
            {
                case GameKind.OnOff:
                    return new OnOffGameState(game);
                
                case GameKind.Directional:
                    return new DirectionalGameState(game);
            }

            throw new ArgumentException("GameKind not supported");
        }
    }
}