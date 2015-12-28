from ninfo import PluginBase
import requests, json
import ast

class riddler_plug(PluginBase):
    """"""
    name          = 'riddler'
    title         = 'Riddler'
    description   = 'riddler.io'
    cache_timeout = 60*60
    types         = ['ip','ip6', 'hostname']
    #local        = False
    #remote       = False

    def setup(self):
        import requests, json
        import ast
        self.token = self.GetAuthToken(self.plugin_config["username"], self.plugin_config["password"])

    def get_info(self, arg):
        results = self.Search(token=self.token, query="ip:"+arg, output="country_code,addr,host,keywords", limit=10)
        if len(results) > 0:
            return {
            "answers": results
            }
        else:
            return False

    def GetAuthToken(self, user, pwd):
        """
        Authenticates towards the API to retrive a valid authentication token.
        The token is required for all subsequent requests towards the API.
        """
        headers = {'Content-type': 'application/json'}
        post_data = {"email": user, "password": pwd}
        r = requests.post(self.plugin_config["base_url"]+"/auth/login", data=json.dumps(post_data), headers=headers)
        data_dict = json.loads(r.text)
        respones_code = data_dict["meta"]["code"]
        if respones_code == 400:
            print "Invalid login credentials"
            quit() #Exit program

        AuthToken = data_dict["response"]["user"]["authentication_token"]
        return AuthToken


    def Search(self, token, query, output, limit):
        """
        Query the riddler API for data using the authentication token header.
        """
        headers = {
            "Content-type": "application/json",
            "Authentication-Token": token
        }
        post_data = {
            "query": query,
            "output": output,
            "limit": limit,
        }
        r = requests.post(self.plugin_config["base_url"]+"/api/search", data=json.dumps(post_data), headers=headers)
        return json.loads(r.text)


plugin_class = riddler_plug


