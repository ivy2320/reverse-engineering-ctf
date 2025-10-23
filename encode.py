import base64
flag = "flag{#mu@lt!_k3y_x0R_Solv3Rr!#}"
reversed_flag = flag[::-1]
b64_encoded = base64.b64encode(reversed_flag.encode())
with open("challenge.bin", "wb") as f:
    f.write(b64_encoded)

print("[+] challenge.bin generated successfully!")
