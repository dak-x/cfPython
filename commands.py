# Add new commands in this file
# Also modify `__init__.py` to expose the methods in the package
from utils import get


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

    pass


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


async def problem(tags):
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

    pass