# vigenere-cipher
Program with graphic interface for encryption and decryption of vigenere

The Vigenère cipher is a polyalphabetic substitution cipher system in which the same letter of the plain message can, depending on its position in it, be replaced by different letters, unlike a mono alphabetic cipher system like the Caesar cipher. (which it however uses as a component). This method is thus resistant to frequency analysis, which is a decisive advantage over mono-alphabetic ciphers. However, the Vigenère cipher was pierced by the Prussian major Friedrich Kasiski who published his method in 1863. Since that time, it no longer offers any security.

For each letter in clear, we select the corresponding column and for a letter of the key we select the appropriate line, then at the intersection of the line and the column we find the encrypted letter. The letter of the key is to be taken in the order in which it occurs and the key is repeated in a loop as much as necessary.
Exemple:
     Key: musique
     Text: I love listening to the radio all day
     Key repeated: M USIQU EMUSIQU EM USIQU EMUSI QU EMUSIQU
     
 The ciphertext is then: V'UVWHY IOIMBUL PM LSLYI XAOLM BU NAOJVUY
     
   If we want to decipher this text, we look for each letter of the repeated key in the corresponding line and we search there for the encrypted letter. The first letter of the column found in this way is the deciphered letter.
   
   Mathematically, we identify the letters of the alphabet with the numbers from 0 to 25 (A=0, B=1...). The encryption and decryption operations are, for each letter, those of the Caesar cipher. By designating the ith letter of the plain text by Text[i], the ith of the encrypted by Ciphered[i], and the ith letter of the key, repeated enough times, by Keys[i], it is formalized by:

  Cipher[i] = (Text[i] + Keys[i]) modulo 26
  Text[i] = (Encrypted[i] - Keys[i]) modulo 26

where x modulo 26 designates the remainder of the integer division of x by 26. For encryption, simply add the two letters then subtract 26 if the result exceeds 26. For decryption, simply perform the subtraction and add 26 if the result is negative. Decryption is also an operation identical to that of encryption for the key obtained by Key'[i] = 26 - Key[i]. A disk to encrypt (en), which uses a circular representation of the alphabet (after Z we have A), makes it possible to carry out this operation directly.

The cipher of a sufficiently long text consisting only of A gives the key ( 0 + x = x, that is A + Keys[i] = Keys[i] ).
