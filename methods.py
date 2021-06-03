import requests


def GET(req):
   
   r = requests.get(req)
   statusCode = r.status_code
   return r.json(), statusCode

def GETD(req):
   time = requests.get(req).elapsed.total_seconds()
   r = requests.get(req)
   statusCode = r.status_code
   return r.json(), statusCode,time


def POST(req,data):
   
   r = requests.post(req,data)
   statusCode = r.status_code
   return r.json(), statusCode


def PUT(req,data):
   
   r = requests.put(req,data)
   statusCode = r.status_code
   return r.json(), statusCode


def DELETE(req):
   
   r = requests.delete(req)
   statusCode = r.status_code
   return statusCode


def PATCH(req,data):
   
   r = requests.patch(req,data)
   statusCode = r.status_code
   return r.json(), statusCode
