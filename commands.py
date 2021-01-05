# Add new commands in this file
# Also modify `__init__.py` to expose the methods in the package
from utils import get
import json
from config import Config


async def getUserInfo(handles):
    """
    Refer: https://codeforces.com/apiHelp/methods#user.info

    Fetches the user info of the given handles

    Parameters
    ----------
    handles: list<str>
        List of handles of all users

    Returns
    -------
    list
        List of json objects contating user info for the handles
    """
    method_name = 'user.info'
    handle_params = 'handles=' + ';'.join(handles)
    return await get(method_name, handle_params)


async def contestList():
    """
    Refer: https://codeforces.com/apiHelp/methods#contest.list

    Fetches information about all available contests

    Returns
    -------
    Returns a list of Contest objects.

    See Also: https://codeforces.com/apiHelp/objects#Contest
    """
    pass


async def problem(tags, counts=2):
    """
    Refer: https://codeforces.com/apiHelp/methods#problemset.problems

    Fetches a list of all problems filtered by tags

    Parameters
    ----------
    tags: str
        semicolor `;` seperated list of tags

    Returns
    -------
    List of Problem objects

    See Also: https://codeforces.com/apiHelp/objects#Problem
    """
    methodName = "problemset.problems"
    methodParams = "tags=" + tags

    problems = await get(methodName, methodParams)
    counts = min(counts, Config['MAX_PROBLEMS'])
    splitProblems = problems['result']['problems'][:counts]

    return splitProblems
    pass


# For Testing 
async def test(): 
    # Add debug/testing code here 
    resp = await getUserInfo(['sam6134'])
    print(json.dumps(resp,indent=3))
    return 

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
