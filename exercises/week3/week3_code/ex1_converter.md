# Excercise 2 - Converter

#### Intro
link to write up:  https://blog.pspaul.de/posts/pwn-ctf-2018-converter/
* webapp that converts stuff from format a to b
* it sets a cookie (has something to do with data you entered)
* according to write up: 

This is hex encoded data with high entropy. Its length is related to the length of the content you submitted and the length (in bytes) is always a multiple of 16. When we change the last byte, we see an error: ValueError: Invalid padding bytes. When we change the first byte, we see another error: JSONDecodeError: Expecting value: line 1 column 1 (char 0). This suggests that the cookie contains AES-CBC-encrypted JSON data, in a pad-then-encrypt scheme, which is vulnerable to the Padding Oracle Attack

* length is always a multiple of 16: that means be have 16 byte blocks here 
* and since the content you enter is probably not always a multiple of 16 bytes, there must be a padding that is used

* when we test, if a padding is used (which we do by changing the last byte in the cookie), we get the padding error
    * that confirms a padding is used 
    * and we know now that the software has a vulneability because it tells us if there is an error with the padding at all 

* we can use the padding error to find out the unencrypted string behind the cookie 

#### Strategy: Paddig Oracle Attack 
* we must flip the byte in a way, that the next block has a 1 at the end
* and then we flip the bytes in a way, that the next block has the byte \x01 at the end
* so we must try out hella lotta bytes: maybe use python app for that
* if the blocks are all 16 bytes then we must start with flipping the -17th byte from the end (so the last byte of the second last block)
* also: does our input matter?
    * but we only know what we input 
    * we do not know what is actually standing in the string also 
    * it might be something like: secretinformtaion:##hello usw. 
* example with 2 blocks: 

Block 1: SECRET_INFORMATI (16 chars = 16 bytes)
Block 2: ROFLCOPTER (10 chars)
Block 2 mit Padding: ROFLCOPTER\x03\x03\x03 (23 chars, 16 bytes weil \x entspricht einem byte )



