from Alert import * # quick package to Email logs for long running programs
import math        # importing mathematical functions


class AffineCipher:  # declaring class
    def encryption(alphabet, avalue, bvalue, plaintext): # defining function
        # Preprocessing steps
        ciphertext = [] # input value
        plaintext = plaintext.lower()  #converts into lowercase
        # Checking the GCD condition
        # Encryption equation => ax+b mod len(alphabet) which is 26 should be equal to 1
        if math.gcd(avalue, len(alphabet)) == 1:
            for x in plaintext:
                xvalue = alphabet.find(x)
                cipher_number = ((avalue * xvalue) + bvalue) % len(alphabet) # ax+b (mod 26)
                ciphertext.append(alphabet[cipher_number])
            # array to string conversion
            cipher_text = ''.join(ciphertext)
            return cipher_text
        else:
            alert_popup("Affine Alert", "Invalid key for encryption process..!!..")

    def mod_inverse(input, mod_value):
        var = 0
        while (var < mod_value):
            mod_inverse_value = (input * var) % mod_value
            if mod_inverse_value == 1:
                return var
            var += 1

    def decryption(alphabet, avalue, bvalue, ciphertext):
        plaintext = [] # input value
        ciphertext = ciphertext.lower()
        # Decryption equation => (y-b)/a (mod len(alphabet)) which is(mod 26)
        if math.gcd(avalue, len(alphabet)) == 1:
            for y in ciphertext:
                yvalue = alphabet.find(y)
                mod_inverse = AffineCipher.mod_inverse(avalue, len(alphabet))
                # programmatic equation: [mod_inverse(a) * (yvalue - bvalue)] (mod (len(alphabet))
                dcipher_number = ((mod_inverse * yvalue) + (-(mod_inverse * bvalue) % len(alphabet))) % len(alphabet)
                plaintext.append(alphabet[dcipher_number])
            # array to string conversion
            plain_text = ''.join(plaintext)
            return plain_text

        else:
            alert_popup("Affine Alert", "Invalid key for decryption process..!!..")

# Code reference for testing
# alert_popup("Title goes here from backend..", "Hello World!", "A path or second message can go here..")
# print(AffineCipher.encryption("abcdefghijklmnopqrstuvwxyz", 5, 1, "Sravya"))
# print(AffineCipher.decryption("abcdefghijklmnopqrstuvwxyz", 5, 1, "RSAYVA")