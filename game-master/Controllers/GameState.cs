using System;
using System.Collections.Generic;
using System.Threading.Tasks;

public abstract class GameState
{
    public GameState(Game game)
    {
        Shots = game.Shots;

        for (int i = 0; i < 5; i++)
        {
            var target = new Target(i);
            Targets.Add(target);
        }
    }

    public virtual async Task Start()
    {
        StartDateTime = DateTime.UtcNow;

        foreach (var target in Targets)
        {
            await target.Deactivate();
        }
    }

    public void RecordHit(int targetId)
    {
        Console.WriteLine($"\n\n\nHIT!!! - {targetId}\n\n\n");

        Targets[targetId].IsHit = true;
        Hits += 1;

        if (IsComplete)
        {
            EndDateTime = DateTime.UtcNow;
        }
    }

    public abstract Task LightNextTarget();

    public bool AllTargetsHit
    {
        get
        {
            var allTargetsHit = Targets.TrueForAll(t => t.IsHit);
            return allTargetsHit;
        }
    }

    public bool IsComplete 
    {
        get 
        {
            var isComplete = (Hits >= Shots);
            return isComplete;
        }
    }

    public DateTime StartDateTime {get; set;}

    public DateTime EndDateTime {get; set;}

    public TimeSpan TotalGameTime 
    {
        get
        {
            var totalGameTime = (EndDateTime - StartDateTime);
            return totalGameTime;
        }
    }

    public int Shots {get; set;}

    public int Hits {get; set;}

    public List<Target> Targets {get; set;} = new List<Target>();
}
