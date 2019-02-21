#Import cssutils and webcolors as required
import cssutils as cu
import webcolors as wc

#Found this online, it suppresses the ridiculous level of error logging from cssutils
import logging
cu.log.setLevel(logging.CRITICAL)

#Giving a shorter name to the name-to-hex dictionary
nth = wc.CSS2_NAMES_TO_HEX

#I'll keep the next few lines in for now, shows how I figured out how to only
#convert a color value to hex if there's a hex representation for that value
# blue = 'blue'
# blurb = 'blurb'
# if blue in nth:
#     print(nth[blue])
# if blurb in nth:
#     print(nth[blurb])

#Read from the css file provided
inbound_file = cu.parseFile('main.css')

#For each rule in our file...
for rule in inbound_file.cssRules:
    #If it's a style rule...
    if rule.type == rule.STYLE_RULE:
        #Then check out the properties it has
        for property in rule.style:
            #And if it's either color or background-color and has a name-to-hex value
            if (property.name == 'color' or property.name == 'background-color') and property.value in nth:
                #Then change it's value to the hex value
                property.value = nth[property.value]

#Get a new file ready to write to
outbound_file = open("new_main.css","w")
#Decode the bytestring values of the outbound file and encode as UTF-8
outbound_file.write(inbound_file.cssText.decode("utf-8"))
#Finally, close the file
outbound_file.close()
