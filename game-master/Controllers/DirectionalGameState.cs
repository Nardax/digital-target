using System;
using System.Threading.Tasks;

namespace game_master.Controllers
{
    public class DirectionalGameState : GameState
    {
        private Direction _direction;
        private int _currentTarget;

        public DirectionalGameState(Game game) : base(game)
        { 
            _direction = game.Direction;
        }

        public override async Task Start()
        {
            await base.Start();

            switch (_direction)
            {
                case Direction.LeftToRight:
                    _currentTarget = 4;
                    break;
                case Direction.RightToLeft:
                    _currentTarget = 0;
                    break;
            }
            
            await LightNextTarget();
        }

        public override async Task LightNextTarget()
        {
            switch (_direction)
            {
                case Direction.LeftToRight:
                    _currentTarget = (_currentTarget >= 4) ? 0 : (_currentTarget + 1);
                    break;
                case Direction.RightToLeft:
                    _currentTarget = (_currentTarget <= 0) ? 4 : (_currentTarget - 1);
                    break;
            }

            await Targets[_currentTarget].Activate();
        }
    }
}