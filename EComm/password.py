
# SCRATCHPAD

from passlib.hash import pbkdf2_sha256


hashval = pbkdf2_sha256.hash("toomanysecrets")
print(hashval)

print(pbkdf2_sha256.verify("toomanysecrets", hashval))

print(pbkdf2_sha256.verify("joshua", hashval))
