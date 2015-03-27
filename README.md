# Python-TweetNaCl

Note: you probably don't want to use this. Use [pynacl](https://github.com/pyca/pynacl) instead, which has more features and is better-maintained.

This is a python binding to the "[tweetnacl](http://tweetnacl.cr.yp.to/)" cryptography library, by djb and others. The binding was originally written by Jan Mojžíš, downloaded from http://mojzis.com/software/python-tweetnacl/index.html . It was further modified by Brian Warner.

## Exposed Functions

* Public-Key Authenticated Encryption (Curve25519+XSalsa20+Poly1305)

 * `pk,sk = crypto_box_keypair()`
 * encryption:
 * `c = crypto_box(msg, nonce, pk_B, sk_A)`
 * encryption pre-computation:
 * `k = crypto_box_beforenm(pk_B, sk_A)`
 * `c = crypto_box_afternm(msg, nonce, k)`
 * decryption:
 * `msg = crypto_box_open(c, nonce, pk_A, sk_B)`
 * decryption pre-computation:
 * `msg = crypto_box_open_afternm(c, nonce, k)`

* Symmetric-Key Authenticated Encryption (XSalsa20+Poly1305)

  * `c = crypto_secretbox(msg, nonce, key)`
  * `msg = crypto_secretbox_open(c, nonce, key)`

* Public-Key Signatures (Ed25519)

  * `pk,sk = crypto_sign_keypair()`
  * `signedmsg = crypto_sign(msg, sk)`
  * `msg = crypto_sign_open(signedmsg, pk)`

* Hashing (SHA512)

  * `h = crypto_hash(msg)`

* constant-time comparison

  * `crypto_verify_16(x,y)`
  * `crypto_verify_32(x,y)`

* Scalar Multiplication (Curve25519)

  * `p2 = crypto_scalarmult(n, p1)`
  * `p2 = crypto_scalarmult_base(n)`

* Pseudo-Random Stream Generator (XSalsa20)

  * `c = crypto_stream(len, nonce, key)`
  * unauthenticated stream-cipher encryption:
  * `c = crypto_stream_xor(msg, nonce, key)`

* One-Time Authentication (Poly1305)

  * `auth = crypto_onetimeauth(msg, key)`
  * `crypto_onetimeauth_verify(auth, msg, key)`

## Installation

* `python setup.py build`
* `python setup.py test`: run unit tests
* `python setup.py speed`: run performance benchmarks
