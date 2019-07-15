using System;
using System.Net.Http;
using System.Threading.Tasks;

public class Target
{
    private HttpClient _httpClient;

    public Target(int number)
    {
        _httpClient = new HttpClient();

        Name = $"t{number}";
    }

    internal async Task Activate()
    {
        IsHit = false;
        var response = await _httpClient.PutAsync($"http://{Name}:5000/5/255", null);
        if (!response.IsSuccessStatusCode)
        {
            Console.WriteLine("\n\n\nActivation request failed.\n\n\n");
        }
    }

    internal async Task Deactivate()
    {
        IsHit = false;
        var response = await _httpClient.PutAsync($"http://{Name}:5000/5/0", null);
        if (!response.IsSuccessStatusCode)
        {
            Console.WriteLine("\n\n\nDeactivation request failed.\n\n\n");
        }
    }

    public string Name {get; set;}

    public bool IsHit {get; set;}
}
