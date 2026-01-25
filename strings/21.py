#placeholder can include a modifier to format the value
#a modifier is included by adding a colon (:) followed by a legal formatting type, like .2f which means fixed point number with 2 decimals
price=59
txt=f"The price is {price:.2f} dollar " #59.00
print(txt)