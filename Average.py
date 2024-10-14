numbers=[1,2,3,4,5]
def find_average(num):
    sum=0
    #læg alle tal sammenog divider medantal tal
    for nummer in num:
        sum=sum+nummer
    resultat=sum/len(num)
    return resultat
#Test find_average function
average=find_average (numbers)
print("Average:", average)
