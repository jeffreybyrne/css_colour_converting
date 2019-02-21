import cssutils as cu
import webcolors as wc

import logging
cu.log.setLevel(logging.CRITICAL)

# print(css_file)


blue = 'blue'
blurb = 'blurb'
nth = wc.CSS2_NAMES_TO_HEX

# if blue in nth:
#     print(nth[blue])
# if blurb in nth:
#     print(nth[blurb])


sheet = cu.parseFile('main.css')

# for rule in sheet:
#     print(rule.cssText)

for rule in sheet:
    if rule.type == rule.STYLE_RULE:
        # find property
        for property in rule.style:
            if property.name == 'color' and property.value in nth:
                # print(property.value)
                property.value = nth[property.value]
                # property.priority = 'IMPORTANT'
                break
        # or simply:
        # rule.style['margin'] = '01.0eM' # or: ('1em', 'important')

# for rule in sheet:
#     print(rule.cssText)

print('hi')
# print(sheet.ru)
    # if 'color' in rule.:
    #     rule.color = nth[rule.color]
output_file = open("output.css","w")
# print(str(sheet.cssText))
output_file.write(sheet.cssText.decode("utf-8"))
output_file.close()




# print(rule)
# print(rule.style)
# rule.style.width = '90%'
# print(rule)
# sheet = cssutils.parseString('@import url(main.css)')
# print('hello!')
# print(sheet)
