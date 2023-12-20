def rgb(r, g, b):

    hexCode = list("0123456789ABCDEF")
    
    def converterHex(n):
        #decimal values will result in a hexadecimal representation
        a, b = hexCode[(n//16)], hexCode[(n%16)]
        return f"{a}{b}"
    
    def minMax(x):
        #Any values that fall out of that range must be rounded
        y = 255 if x > 255 else 0 if x < 0 else x
        return y
    
    #main function
    r, g, b = minMax(r), minMax(g), minMax(b)
    result = f"{converterHex(r)}{converterHex(g)}{converterHex(b)}"
    return result