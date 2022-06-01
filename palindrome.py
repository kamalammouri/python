list=["mayoresses","kinematical","acervulus","gaol","speises","zigzaggers","carrefours",
 "ethnohistorical","hornists","refitted","diphthonging","cetanes","flagellins",
 "quaintly","keelhaling","acetonitriles","likewise","foamflower","appointed",
 "marchlike","miniscule","argus","softish","creatines","nicols","fluorides","fatally",
 "walker","odist", "Able was I ere I saw Elba", "radar", "level", "rotor"]


def is_palindrome(mots):
   for x in mots:
       reverce = x[::-1]
       if (x.lower()==reverce.lower()):
           print(x)
            
is_palindrome(list)