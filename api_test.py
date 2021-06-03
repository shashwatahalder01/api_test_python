from tests.test import *
import requests
from Utils.requestlink import*
from Utils.patchdata import *
from Utils.putdata import *
from Utils.postdata import *
from Utils.getdata import *
from methods import *
 
import json




        


def api_test():

   
        res,ges= GET(get_SingleUser)
        print("\nGET Single User test \n")
        print(test_status_code_200(ges) +'\n')
        for key, value in res.items():
                for k in value:
                        # print(res[key][k])
                        if res[key][k] == singleuser[key][k] : print("PASS "+k+"test" +"\n")
                # print(key, value)

      
        res,ges= GET(get_AllUsers)
        print("\nGET ALL user test \n")
        print(test_status_code_200(ges) +'\n')



        if res['page'] ==                    allusers['page']               :  print("PASS page test" + "\n") 
        if res['per_page'] ==                allusers['per_page']          :  print("PASS per-page test" + "\n")
        if res['total'] ==                   allusers['total']              :  print("PASS total test" + "\n") 
        if res['total_pages'] ==             allusers['total_pages']        :  print("PASS total-pages test" + "\n")
        if res['support']['url']        ==   allusers['support']['url']       :  print("PASS url test" + "\n")
        if res['support']['text']       ==   allusers['support']['text']      :  print("PASS text test" + "\n")

        a=0
        for item, item1 in zip(res['data'], allusers['data']):
                for (key,value), (key1,value1) in zip( item.items(),item1.items()):
                        if value == value1 : print("PASS user_no "+str(a)+ " "+key+"test" +"\n")
                a=a+1;

     

        
      

        res,ges= GET(get_ListResource)
        print("\nGET ALL user test \n")
        print(test_status_code_200(ges) +'\n')



        if res['page'] ==                    listresource['page']               :  print("PASS page test" + "\n") 
        if res['per_page'] ==                listresource['per_page']          :  print("PASS per-page test" + "\n")
        if res['total'] ==                   listresource['total']              :  print("PASS total test" + "\n") 
        if res['total_pages'] ==             listresource['total_pages']        :  print("PASS total-pages test" + "\n")
        if res['support']['url']        ==   listresource['support']['url']       :  print("PASS url test" + "\n")
        if res['support']['text']       ==   listresource['support']['text']      :  print("PASS text test" + "\n")

        a=0
        for item, item1 in zip(res['data'], listresource['data']):
                for (key,value), (key1,value1) in zip( item.items(),item1.items()):
                        if value == value1 : print("PASS user_no "+str(a)+ " "+key+"test" +"\n")
                a=a+1;

        
        res,ges=GET(get_SingleUsernotfound)
        print( res, ges)
        print("\nGET Single user  test \n")
        print(test_status_code_404(ges) +'\n')
        if not res :  print("PASS NO User found check" + "\n")
        
        res,ges= GET(get_SingleResource)
        print("\nGET Single Resource test \n")
        print(test_status_code_200(ges) +'\n')
        for key, value in res.items():
                for k in value:
                        # print(res[key][k])
                        if res[key][k] == singleresource[key][k] : print("PASS "+k+" test " +"\n")

        
  
       
        
        res,ges= GET(get_SingleResourceNotfound)
        print( res, ges)
        print("\nGET Single Resource existence test \n")
        print(test_status_code_404(ges) +'\n')
        if not res :  print("PASS NO resource check" + "\n")

        
        res,ges,time=GETD(get_delayedResponse)
        # print(time)
        print("\nGET Delayed responce test \n")
        print(test_status_code_200(ges) +'\n')
        if time >3 : print("Response time is greater than 3s" +'\n')



        

        res,pos=POST(post_Create,create)
        # print(create, res, pos)
        print("\n POST user create test \n" )
        print(test_status_code_201(pos) +'\n')
        if res['name'] == create['name']:  print("PASS user name exists" + "\n") 
        if res['job'] == create['job']:  print("PASS job details exists" + "\n")
        if 'id' in res:  print("PASS user id created" + "\n")  
        if 'createdAt' in res:  print("PASS JSON has createdAt" + "\n") 
        
        
        res,pos=POST(post_RegisterSuccessful,registerSuccess)
        print(registerSuccess, res, pos)
        print("\nPOST register test \n" )
        print(test_status_code_200(pos) +'\n')
        if 'id' in res:  print("PASS user id created" + "\n")  
        if 'token' in res:  print("PASS JSON has token" + "\n") 
       

        res,pos= POST(post_RegisterUnuccessful,registerUnsuccess)
        print(registerUnsuccess, res, pos)
        print("\nPOST test \n" )
        print(test_status_code_400(pos)+"\n")
        if res['error'] == "Missing password":  print("user password missing registrationunsuccess" + "\n") 

      
        res,pos=POST(post_LoginSuccessful,loginSuccess)
        print(loginSuccess, res, pos)
        print("\nPOST register test \n" )
        print(test_status_code_200(pos) +'\n') 
        if 'token' in res:  print("PASS JSON has token" + "\n") 
        
        res,pos= POST(post_LoginUnsuccessful,loginUnsuccess)
        print(loginUnsuccess, res, pos)
        print("\nPOST test \n" )
        print(test_status_code_400(pos)+"\n")
        if res['error'] == "Missing password":  print("user password missing login unsuccess" + "\n") 

        

        r,pat= PUT(put_update,putdata)
        print("\nPUT test \n" )
        print(test_status_code_200(pat) + "\n")
        if r['name'] == patchdata['name']:  print("PASS user name updated" + "\n") 
        if r['job'] == patchdata['job']:  print("PASS job details updated" + "\n") 
        if 'updatedAt' in r:  print("PASS JSON has updatedAt" + "\n") 
        
        r,pat= PATCH(pathch_update,patchdata)
        print("\nPATCH test \n" )
        print(test_status_code_200(pat) + "\n")
        if r['name'] == patchdata['name']:  print("PASS user name updated" + "\n") 
        if r['job'] == patchdata['job']:  print("PASS job details updated" + "\n") 
        if 'updatedAt' in r:  print("PASS JSON has updatedAt" + "\n") 

        dele = DELETE(delete_delete)
        print("\nDELETE test \n" )
        print(test_status_code_204(dele)+ "\n")

        

if __name__ == '__main__':
    api_test()