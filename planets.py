#
#Name: Brandon Chan
#Student ID:bchan24
#Date: 9/24/18
#
#Lab 0
#Section 15
#Purpose of Lab: Learning Python syntax and unit testing
#
#This function will a print statement that states what someone would weigh on mars and jupiter based on his/her weight on earth
def weight_on_planets():
   #earth is a number, representing the number of pounds someone weighs on earth
   earth = int(input('What do you weigh on earth? '))
   #mars is a number, representing the number of pounds someone weighs on mars by multiplying earth pounds by 0.38
   mars = earth*0.38
   #jupiter is a number, representing the number of pounds someone weighs on jupiter by multiplying earth pounds by 2.34
   jupiter = earth*2.34
   print('\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds.' %(mars, jupiter))
      
if __name__ == '__main__':
   weight_on_planets()