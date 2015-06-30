import webapp2
import logging
import json
import utils
import re
import advanced

class show_search_results(utils.BaseHandler):
        def post(self):
            #get info about slack post
            token = self.request.get('token')
            channel = self.request.get('channel')
            text = self.request.get('text')
            user = self.request.get('user_name')
            user_id = self.request.get('user_id')

            #verify that the call to app is being made by an authorized slack slash command
            if token == 'your_token':
                
                #extract the search term from the command and build the resulting search link
                query_name = re.match("[^\s]+", text)

                if query_name is not None:
                    query_name = image_name.group(0)
                    query_link = "<https://google.com/q?={}".format(query_name)
                    self.response.out.write("".format(query_link))

                    #call the Slack incoming webhook
                    url = "your_incoming_webhooks_url"
                    payload = json.dumps(
                            {"channel":channel, "username":"Highfive", "text":"".format(query_link)})
                    result = urlfetch.fetch(url=url, 
                            method=urlfetch.POST,
                            payload=payload)

app = webapp2.WSGIApplication([
    ('/slack-five', query_link, debug=True)])                    
