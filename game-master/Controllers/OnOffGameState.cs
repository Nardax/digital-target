using System;
using System.Threading.Tasks;

namespace game_master.Controllers
{
    public class OnOffGameState : GameState
    {
        public OnOffGameState(Game game) : base(game)
        { }

        public override async Task Start()
        {
            StartDateTime = DateTime.UtcNow;
            await ActivateAllTargets();
        }

        public override async Task LightNextTarget()
        {
            if (AllTargetsHit)
            {
                await ActivateAllTargets();
            }
        }

        private async Task ActivateAllTargets()
        {
            foreach (var target in Targets)
            {
                await target.Activate();
            }
        }
    }
}