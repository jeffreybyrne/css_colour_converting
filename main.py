import cssutils as cu
import webcolors as wc

import logging
cu.log.setLevel(logging.CRITICAL)

# print(css_file)
# output_file = open("output.css","w")
# output_file.write("Hello")
# output_file.close()

blue = 'blue'
blurb = 'blurb'
nth = wc.CSS2_NAMES_TO_HEX

# if blue in nth:
#     print(nth[blue])
# if blurb in nth:
#     print(nth[blurb])


sheet = cu.parseFile('main.css', 'ascii')

# for rule in sheet:
#     print(rule)

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        # find property
        for property in rule.style:
            if property.name == 'color':
                property.value = nth[property.value]
                property.priority = 'IMPORTANT'
                # break
        # or simply:
        # rule.style['margin'] = '01.0eM' # or: ('1em', 'important')

# for rule in sheet:
#     print(rule)
    # if 'color' in rule.:
    #     rule.color = nth[rule.color]



# print(rule)
# print(rule.style)
# rule.style.width = '90%'
# print(rule)
# sheet = cssutils.parseString('@import url(main.css)')
# print('hello!')
# print(sheet)
