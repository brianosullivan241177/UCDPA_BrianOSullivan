# *********************** Brian O'Sullivan ***********************
# ******************* Fifa Prep - Golden Boy *********************
# *** Add the year the player won the Golden Boy award to name ***
# * https://github.com/brianosullivan241177/UCDPA_BrianOSullivan *

text = open("/users/brian/documents/FIFA_Project_Final/Modified/FIFAAllplayersM.csv", "r")
text = ''.join([i for i in text]) \
    .replace("M. Balotelli","GB Winner 2010 M. Balotelli").\
    replace("M. Götze", "GB Winner 2011 M. Götze").replace("Isco", "GB Winner 2012 Isco").\
    replace("P. Pogba", "GB Winner 2013 P. Pogba").replace("R. Sterling", "GB Winner 2014 R. Sterling")

x = open("/users/brian/documents/FIFA_Project_Final/Modified/FIFAAllplayers_GB.csv","w")
x.writelines(text)
x.close()