import hmac
# Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
# 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
message = b'hello,world'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

key2 = b'secret'
message2=b'hello'
h = hmac.new(key2,message2, digestmod='MD5')
h.update(b',world')
print(h.hexdigest())
