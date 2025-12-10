from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin) : 
    # def process_request(self , request) : 
    #     print(request)
    #     print ("---------------------------------------")
    #     return 
    
    def process_response(self , request , response) : 
        print ("++++++++++++++++++++++++++++++++++++")
        print (response)
        return response