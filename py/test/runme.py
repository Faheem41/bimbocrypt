
# runme.py
# run this module


import bimbocrypt

TEXT = "Bangalees have a rich literary heritage. The earliest available specimen of Bengali literature is about a " \
       "thousand years old. During the mediaeval period. Bengali Literature developed considerably with the patronage " \
       "of Muslim rulers. Chandi Das, Daulat Kazi and Alaol are some of the famous poets of the period. The era of " \
       "modern Bengali Literature began in the late nineteenth century Rabindranath Tagore, the Nobel Laureate is a " \
       "vital part of Bangalee culture. Kazi Nazrul Islam, Michael Madhusudan Datta. Sarat Chandra Chattopadhaya, " \
       "Bankim Chandra Chattopadhaya, Mir Mosharraf Hossain and Kazi Ahdul Wadud are the pioneers of modern Bengali " \
       "Literature. "
PASSWORD = "10"

print("Original Text: ", TEXT)
print("Password: ", PASSWORD)

encrypted_text = bimbocrypt.encrypt(TEXT, PASSWORD)
print("Encrypted Text: ", encrypted_text)

decrypted_text = bimbocrypt.decrypt(encrypted_text, PASSWORD)
print("Decrypted Text: ", decrypted_text)
print("Original Text == Decrypted Text ? >> ", TEXT == decrypted_text)
