#!/usr/bin/env python
# coding: utf-8

# In[ ]:


message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "?!',. "
decoding_offset = 10

def decoder(message, offset):
  decoded_message = ""
  for i in message:
    if not i in punctuation:
      letter_value = alphabet.find(i)
      decoded_message += alphabet[(letter_value + offset) % len(alphabet)] 
    else:
      decoded_message += i
  return decoded_message
print(decoder(message, decoding_offset))

message_to_vish = "Hey heres an encrypted message!, did you get it alright?"
encoding_offset = -(10)
encoded_message = ""

def encoder(message, offset):
  encoded_message = ""
  for i in message_to_vish:
    if not i in punctuation:
      letter_value = alphabet.find(i)
      encoded_message += alphabet[(letter_value + offset) % len(alphabet)]
    else:
      encoded_message += i
  return encoded_message
print(encoder(message_to_vish, encoding_offset))

st_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(decoder(st_message, decoding_offset))

decoding_offset2 = 14
message2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
print(decoder(message2, decoding_offset2))

message3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx"

for i in range(0,len(alphabet)):
  print("Offset: ", i)
  print(decoder(message3, i))

message_4 = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"

def vin_decipher(message, keyword):
  keyword_index = ""
  letter_int = 0
  for i in range(0, len(message)):
    if message[i] in punctuation:
      keyword_index += message[i]
    else:
      keyword_index += keyword[letter_int]
      letter_int = (letter_int+1) % len(keyword)
  ciphered_message = ""
  print(keyword_index)
  for i in range(0, len(message)):
    if not keyword_index[i] in punctuation:
      letter_value = alphabet.find(message[i]) + alphabet.find(keyword_index[i])
      ciphered_message += alphabet[letter_value % len(alphabet)]
    else:
      ciphered_message += message[i]
  return ciphered_message

print(vin_decipher(message_4, keyword))

def vin_cipher(message, keyword):
  keyword_index = ""
  letter_int = 0
  for i in range(0, len(message)):
    if message[i] in punctuation:
      keyword_index += message[i]
    else:
      keyword_index += keyword[letter_int]
      letter_int = (letter_int+1) % len(keyword)
  deciphered_message = ""
  for i in range(0, len(message)):
    if not keyword_index[i] in punctuation:
      letter_value = alphabet.find(message[i]) - alphabet.find(keyword_index[i])
      deciphered_message += alphabet[letter_value % len(alphabet)]
    else:
      deciphered_message += message[i]
  return deciphered_message

keyword2 = "doggo"
message_5 = "this is a coded message"

encrypted_message = print(vin_cipher(message_5, keyword2))
print(vin_decipher(encrypted_message, keyword2))

