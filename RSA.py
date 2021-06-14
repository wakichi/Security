def word2ascii(word):
    word = str(word)
    num_lis = []
    for s in word:
        num_lis.append(ord(s))
    return num_lis


def make_encript(asciied_word_lis):
    p = 17
    q = 19
    n = p * q
    k_1 = 5
    k_2 = 173
    enc_lis = []
    for s in asciied_word_lis:
        enc = pow(s, k_1, n)
        enc_lis.append(enc)
    return enc_lis


def make_plane_text(enc_lis, k, n):
    plane_lis = []
    for e in enc_lis:
        plane = chr(pow(e, k, n))
        plane_lis.append(plane)
    return plane_lis


if __name__ == "__main__":
    asciied_word = word2ascii("cat")
    print(asciied_word)
    enc = make_encript(asciied_word)
    print(enc)
    print(make_plane_text(enc, 173, 17 * 19))
