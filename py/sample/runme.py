from bimbocrypt import encrypt, decrypt

if __name__ == '__main__':
	TEXT = "The Sun is the star at the center of the Solar System. It is a nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion reactions in its core, radiating the energy mainly as visible light, ultraviolet light, and infrared radiation."
	PASSWORD = '250'
	print("Original text: ", TEXT)
	enc = encrypt(TEXT, PASSWORD)
	print("Encrypted text: ", enc)
	dec = decrypt(enc, PASSWORD)
	print("Decrypted text: ", dec)
	print("\nText == Decrypted_Text ?")
	print(">>> ", TEXT == dec)
	
