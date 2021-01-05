import json
import aiohttp


# Feels like a seperate class wont be neccesary
# Directly create specific functions

# from abc import ABC, abstractmethod

# REQ_PREFIX = 'https://codeforces.com/api/'

# # Inherit this class to any new method added
# class Method(ABC):
#     """
#     An Abstract class which represents method of the cf-api.
#     Refer: "https://codeforces.com/apiHelp/methods"
#     """
#     @abstractmethod
#     def name(self) -> str:
#         """ 
#         Return the name of the method
#         """
#         pass

#     @abstractmethod
#     def params(self) -> str:
#         """
#         Return all the params in the request url for the cf-api.
#         Refer: "https://codeforces.com/apiHelp/methods:
#         """
#         pass
    
#     @abstractmethod
#     def request(self) -> str:
#         """
#         Return the  
#         """
#     pass
