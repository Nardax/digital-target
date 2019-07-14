using System.Threading.Tasks;

namespace game_master.Controllers
{
    public class DirectionalGameState : GameState
    {
        private Game game;

        public DirectionalGameState(Game game) : base(game)
        {
            this.game = game;
        }

        public override async Task LightNextTarget()
        {
            throw new System.NotImplementedException();
        }

        public override Task Start()
        {
            throw new System.NotImplementedException();
        }
    }
}