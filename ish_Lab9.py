def encode(password):
    encoded = ''
    for i in password:
        i = int(i)
        encoded += str(i+3)
    
    return encoded

def decode(password):
    decoded = ''
    for i in password:
        i = int(i)
        decoded += str(i-3)
    return decoded



