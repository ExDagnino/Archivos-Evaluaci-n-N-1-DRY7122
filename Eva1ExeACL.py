aclNum = int(input("Cual es el numero de la ACL Ipv4? "))
if aclNum >= 1 and aclNum <= 99:
    print("Esta es una ACL Ipv4 estandar.")
elif aclNum >=100 and aclNum <= 199:
    print("Esta es una ACL Ipv4 Extendida")
else:
    print("Este numero de ACL no existe")