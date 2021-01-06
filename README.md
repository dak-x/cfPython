# cf-python
Python wrapper for the codeforces web api.
Refer to <a href="https://codeforces.com/apiHelp"> CodeForces-API </a> for the detailed explanation of each method.
It currently supports only public api methods.
# Usage:
1. Move to the directory of your folder where you wish to use this API.
2. Clone this repo inside your folder 
        
    git clone https://github.com/dak-x/cfPython
3. Import the package directly into your project:

    <!-- language: lang-python -->
        from cfPython import * 
        
4. Check the `__init__.py` to look at the available functions. All neccessary documentation is provided in the function definitions.
\
You can also use `__doc__` attribute for the `docstring` for a function or use `help(cfPython.<Method Name>)` to view inside the `python3` shell
## Examples:

<!-- language: lang-python -->
    import cfPython
    import asyncio

    # Return the CF Profile of tourist
    async def test(): 
        resp = await cfPython.getUserInfo(['tourist'])
        print(json.dumps(resp,indent=3))

    # Get the asyncio event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
    
This return the following json:

    {
       "status": "OK",
       "result": [
          {
             "lastName": "Korotkevich",
             "country": "Belarus",
             "lastOnlineTimeSeconds": 1609910994,
             "city": "Gomel",
             "rating": 3778,
             "friendOfCount": 31596,
             "titlePhoto": "//userpic.codeforces.com/422/title/50a270ed4a722867.jpg",
             "handle": "tourist",
             "avatar": "//userpic.codeforces.com/422/avatar/2b5dbe87f0d859a2.jpg",
             "firstName": "Gennady",
             "contribution": 155,
             "organization": "ITMO University",
             "rank": "legendary grandmaster",
             "maxRating": 3783,
             "registrationTimeSeconds": 1265987288,
             "maxRank": "legendary grandmaster"
          }
       ]
    }




