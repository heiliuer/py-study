'''
Created on 2015年4月12日

@author: Administrator
'''
class Example(object):                     
                                           
    def Call(self, param1=None):           
        '''docstring'''                    
        return param1 + 10 * 10            
                                           
    def Call2(self):  # Comment              
        # Comment               
        result = self.Call(param1=10);
        print(result);            
        return result;   
ex = Example();
ex.Call2();   
