#--- import modules ---
from hashlib import sha256

x = 5
y = 0

# --- while last digit in hashed product of x*y is not 0, increment y
while sha256(f"{x*y}".encode()).hexdigest()[-1] != "0":
    print(y,sha256(f"hash is {x*y}".encode()).hexdigest()[-1] )
    y +=1
    
# --- print solution ---
print(f"the solution is y = {y}")

