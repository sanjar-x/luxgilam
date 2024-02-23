def format_price(narx):
    rounded_narx = round(narx)
    narx_str = str(rounded_narx)
    
    if rounded_narx >= 1000:
        parts = []
        while len(narx_str) > 3:
            parts.append(narx_str[-3:])
            narx_str = narx_str[:-3]
        parts.append(narx_str)
        
        formatted_narx = ','.join(parts[::-1])
    else:
        formatted_narx = narx_str
    
    return formatted_narx
