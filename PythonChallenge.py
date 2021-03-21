def level_00() -> None:
    print(f"\033[31mLevel 00\033[0m")
    result = 2 ** 38
    print(result)


def level_01() -> None:
    print(f"\033[31mLevel 01\033[0m")
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\n" + \
           "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\n" + \
           "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    in_table = "abcdefghijklmnopqrstuvwxyz"
    out_table = "cdefghijklmnopqrstuvwxyzab"
    trans_table = str.maketrans(in_table, out_table)
    text = text.translate(trans_table)
    print(text)


def level_02() -> None:
    print(f"\033[31mLevel 02\033[0m")
    import re
    with open("level_02/data.txt", "r") as file:
        data = file.read()
    letters_list = re.findall(r"[a-z]", data)
    letters = ''.join(letters_list)
    print(letters)


def level_03() -> None:
    print(f"\033[31mLevel 03\033[0m")
    import re
    with open("level_03/data.txt", "r") as file:
        data = file.read()
    data = "\n" + data + "\n"
    pattern_0 = r"[A-Z]{3}([a-z])[A-Z]{3}"
    pattern_1 = r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"
    pattern_2 = r"[a-z][A-Z]{3}[a-z][A-Z]{3}\n"
    pattern_3 = r"\n[A-Z]{3}[a-z][A-Z]{3}[a-z]"
    letters_list = re.findall(rf"{pattern_1}|{pattern_2}|{pattern_3}", data)
    letters = '\n'.join(letters_list)
    letters_list = re.findall(rf"{pattern_0}", letters)
    letters = ''.join(letters_list)
    print(letters)


def level_04() -> None:
    print(f"\033[31mLevel 04\033[0m")
    from urllib import request

    # nothing = 12345 -> epochs = 86 , nothing = 16044
    # nothing = 8022  -> epochs = 165, nothing = 66831

    nothing = "12345"
    # nothing = "8022"

    epochs = 0
    while True:
        epochs += 1
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
        response = request.urlopen(url)
        text = response.read().decode()
        print(f"{epochs:3}\t{url}\n\t{text}")
        nothing = str(text.split(' ')[-1])


def level_05() -> None:
    print(f"\033[31mLevel 05\033[0m")
    import pickle
    with open("level_05/banner.p", "rb") as file:
        data_list = pickle.load(file)
    for line_list in data_list:
        for item_tuple in line_list:
            char, num = item_tuple
            print(char * num, end='')
        print()


def level_06() -> None:
    print(f"\033[31mLevel 06\033[0m")
    import zipfile
    epochs = 0
    nothing = "90052"
    comment_list = []
    zip_file = zipfile.ZipFile("level_06/channel.zip", 'r')
    while nothing != "comments.":
        epochs += 1
        filename = f"{nothing}.txt"
        file = zip_file.getinfo(filename)
        comment = file.comment
        text = zip_file.read(filename).decode()
        print(f"{epochs}\t{filename:10s}\t{comment}\t{text}")
        comment_list.append(comment.decode())
        nothing = str(text.split(' ')[-1])
    print()
    for comment in comment_list:
        print(comment, end='')


def level_07() -> None:
    print(f"\033[31mLevel 07\033[0m")
    from PIL import Image
    im = Image.open("level_07/oxygen.png")
    char_list = []
    for width in range(0, 608, 7):
        pixel = im.getpixel((width, im.height / 2))
        char = chr(pixel[0])
        char_list.append(char)
        print(f"{width:3d}\t{str(pixel):20s}\t{char}")
    print(''.join(char_list))

    key_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print(''.join([chr(key) for key in key_list]))


def level_08() -> None:
    print(f"\033[31mLevel 08\033[0m")
    import bz2
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    username = bz2.decompress(un).decode()
    password = bz2.decompress(pw).decode()
    print(f"username = {username}\npassword = {password}")


def level_09() -> None:
    print(f"\033[31mLevel 09\033[0m")
    first = [146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170, 355, 169, 346, 167, 335, 170,
             329, 170, 320, 170, 310, 171, 301, 173, 290, 178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296,
             195, 305, 194, 307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346, 199, 352, 198,
             360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192, 389, 191, 392, 190, 396, 189, 400, 194, 401,
             201, 402, 208, 403, 213, 402, 216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
             365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311, 215, 306, 216, 296, 218, 290,
             221, 283, 225, 282, 233, 284, 238, 287, 243, 290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273,
             289, 278, 287, 279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294, 291, 296, 295,
             299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341, 306, 349, 303, 354, 301, 364, 301, 371, 297,
             375, 292, 384, 291, 386, 302, 393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
             336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346, 259, 346, 251, 349, 259, 349,
             264, 349, 273, 349, 280, 349, 288, 349, 295, 349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257,
             351, 249, 350, 234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137, 339, 132, 330,
             122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281, 122, 275, 128, 265, 129, 257, 131, 244, 133,
             239, 134, 228, 136, 221, 137, 214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
             134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108, 171, 111, 163, 115, 156, 116,
             149, 117, 142, 116, 136, 115, 129, 115, 124, 115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100,
             121, 95, 121, 89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108, 132, 110, 133, 110, 136,
             107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107,
             161, 111, 156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139, 276,
             143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153, 366, 149, 379, 147, 394, 146, 399]
    second = [156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186, 150, 179, 155, 175, 157, 168,
              157, 163, 157, 159, 157, 158, 164, 159, 175, 159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212,
              147, 215, 146, 218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172, 114, 167, 112,
              161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81, 162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141,
              110, 136, 111, 126, 113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157, 128, 156,
              134, 157, 136, 156, 136]
    from PIL import Image, ImageDraw
    im = Image.new("RGBA", (500, 500), "#FFFFFF")
    draw = ImageDraw.Draw(im)
    draw.line(first, fill="#000000")
    draw.line(second, fill="#000000")
    im.save()
    im.show()


def level_10() -> None:
    print(f"\033[31mLevel 10\033[0m")
    pre_string = "1"
    for k in range(31):
        print(f"{k}\t{len(pre_string):4d}\t{pre_string}")
        cnt_string = ""
        char = pre_string[0]
        pos = 0
        for i, c in enumerate(pre_string):
            if c == char:
                continue
            cnt_string += f"{i - pos}{char}"
            char = c
            pos = i
        cnt_string += f"{len(pre_string) - pos}{char}"
        pre_string = cnt_string


def level_11() -> None:
    print(f"\033[31mLevel 11\033[0m")
    import numpy as np
    from PIL import Image
    im0 = Image.open("level_11/cave.jpg")
    mat0 = np.asarray(im0)
    mat1 = np.zeros_like(mat0)
    for i, row in enumerate(mat0):
        j1, j2 = -1, 319
        for j, pixel in enumerate(row):
            if (i + j) % 2 == 0:
                j2 += 1
                mat1[i][j2] = mat0[i][j]
            else:
                j1 += 1
                mat1[i][j1] = mat0[i][j]
    im1 = Image.fromarray(mat1)
    im1.save("level_11/result.jpg")


def level_12() -> None:
    print(f"\033[31mLevel 12\033[0m")
    with open("level_12/evil2.gfx", "rb") as file:
        file_bytes = file.read()
    for i in range(5):
        piece_bytes = file_bytes[i::5]
        with open(f"level_12/{i}.jpeg", "wb") as file:
            file.write(piece_bytes)


def level_13() -> None:
    print(f"\033[31mLevel 13\033[0m")
    from xmlrpc.client import ServerProxy
    server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    response = server.phone("Bert")
    print(response)


def level_14() -> None:
    def next_pos(x, y, f):
        if f == 0:
            if y != 99 and mat1[x][y + 1] == 0:
                y += 1
            else:
                x, f = x + 1, 1
        elif f == 1:
            if x != 99 and mat1[x + 1][y] == 0:
                x += 1
            else:
                y, f = y - 1, 2
        elif f == 2:
            if y != 0 and mat1[x][y - 1] == 0:
                y -= 1
            else:
                x, f = x - 1, 3
        elif f == 3:
            if x != 0 and mat1[x - 1][y] == 0:
                x -= 1
            else:
                y, f = y + 1, 0
        mat1[x][y] = 1
        return x, y, f

    print(f"\033[31mLevel 14\033[0m")
    import numpy as np
    from PIL import Image
    im0 = Image.open("level_14/wire.png")
    im1 = Image.new("RGB", (100, 100), "#FFFFFF")
    mat1 = np.zeros((100, 100), dtype=np.int)
    i, j, d = 0, -1, 0
    for k in range(10000):
        i, j, d = next_pos(i, j, d)
        pixel = im0.getpixel((k, 0))
        im1.putpixel((i, j), pixel)
    im1 = im1.rotate(-90)
    im1.save("level_14/result.png")


def level_15() -> None:
    print(f"\033[31mLevel 15\033[0m")
    import calendar
    from datetime import date
    d = date(1006, 1, 1)
    while d.year < 2000:
        if d.isoweekday() == 4 and calendar.isleap(d.year):
            print(d.isoformat())
        d = d.replace(year=d.year + 10)


def level_16() -> None:
    print(f"\033[31mLevel 16\033[0m")
    from PIL import Image
    im0 = Image.open("level_16/mozart.gif")
    im1 = Image.new("P", (640, 480))
    im1.putpalette(im0.getpalette())
    for h in range(480):
        for w in range(4, 640):
            p1 = im0.getpixel((w - 4, h))
            p2 = im0.getpixel((w - 3, h))
            p3 = im0.getpixel((w - 2, h))
            p4 = im0.getpixel((w - 1, h))
            p5 = im0.getpixel((w, h))
            if p1 == p2 == p3 == p4 == p5 == 195:
                for ww in range(640):
                    pixel = im0.getpixel(((ww + w - 4) % 640, h))
                    im1.putpixel((ww, h), pixel)
                break
    im1.save("level_16/result.gif")


def level_17() -> None:
    from urllib import request, parse
    from http import cookiejar
    from xmlrpc.client import ServerProxy
    import bz2

    def crawl():
        # busynothing = 12345 -> epochs = 118 , busynothing = 83051
        epochs = 0
        busynothing = "12345"
        info = ""
        while str.isdigit(busynothing):
            epochs += 1
            url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={busynothing}"
            cookie = cookiejar.MozillaCookieJar()
            handler = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener(handler)
            response = opener.open(url)
            text = response.read().decode()
            print(f"{epochs:<3d}\tbusynothing = {busynothing}\n\t{text}")
            for c in cookie:
                print(f"\t{c.name} = {c.value}")
                if c.name == "info":
                    info += parse.unquote_plus(c.value)
            busynothing = str(text.split(' ')[-1])
        print(info)

    def decompress():
        info = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA" + \
               "%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS" + \
               "%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
        info = info.replace("+", "%20")
        info = parse.unquote_to_bytes(info)
        info = bz2.decompress(info).decode("utf-8")
        print(info)

    def phone():
        server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
        response = server.phone("Leopold")
        print(response)

    print(f"\033[31mLevel 17\033[0m")
    crawl()
    decompress()
    phone()


def level_18() -> None:
    print(f"\033[31mLevel 18\033[0m")
    import gzip
    import difflib
    from PIL import Image
    from io import BytesIO

    # decompress and split data
    data1_list, data2_list = [], []
    with gzip.open("level_18/deltas.gz", "rb") as file:
        for data in file:
            data = data.decode("utf-8")
            data1, data2 = data[:53].rstrip(' ') + "\n", data[56:]
            if data1 != "\n":
                data1_list.append(data1)
            if data2 != "\n":
                data2_list.append(data2)

    # Differ()
    d = difflib.Differ()
    diff = d.compare(data1_list, data2_list)
    print(''.join(list(diff)))

    # HtmlDiff()
    # d = difflib.HtmlDiff()
    # diff = d.make_file(data1_list, data2_list)
    # with open("level_18/HtmlDiff.html", "w") as f:
    #     f.write(diff)

    # group data
    space_bytes, plus_bytes, minus_bytes = b"", b"", b""
    for data in diff:
        data_list = data[2:].strip('\n').split(' ')
        byte = bytes([int(i, 16) for i in data_list])
        if data[0] == '+':
            plus_bytes += byte
        elif data[0] == '-':
            minus_bytes += byte
        elif data[0] == ' ':
            space_bytes += byte

    # save image
    stream = BytesIO(space_bytes)
    image_space = Image.open(stream)
    image_space.save("level_18/space.png")

    stream = BytesIO(plus_bytes)
    image_space = Image.open(stream)
    image_space.save("level_18/plus.png")

    stream = BytesIO(minus_bytes)
    image_space = Image.open(stream)
    image_space.save("level_18/minus.png")


def level_19() -> None:
    print(f"\033[31mLevel 19\033[0m")
    import base64
    import wave
    with open("level_19/indian.dat", "r") as file:
        text = file.read().replace("\n", "")
    stream = base64.b64decode(text.encode())
    with open("level_19/indian.wav", "wb") as file:
        file.write(stream)

    with wave.open("level_19/indian.wav", "rb") as f1:
        with wave.open("level_19/reverse.wav", "wb") as f2:
            f2.setparams(f1.getparams())
            for _ in range(f1.getnframes()):
                f2.writeframes(f1.readframes(1)[::-1])


def level_20() -> None:
    print(f"\033[31mLevel 20\033[0m")
    from urllib import request, error
    url = "http://www.pythonchallenge.com/pc/hex/unreal.jpg"
    user = "butter"
    password = "fly"
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, url, user, password)
    handler = request.HTTPBasicAuthHandler(password_mgr)
    opener = request.build_opener(handler)

    with open("level_20/invader.zip", "wb") as file:
        opener.addheaders = [("range", f"bytes=1152983631-"), ]
        response = opener.open(url)
        data = response.read()
        file.write(data)

    # start = -1
    # start = 2123456790
    start = 1152983632
    while True:
        # start += 1
        start -= 1
        print(f"{start}", end="\t")
        opener.addheaders = [("range", f"bytes={start}-"), ]
        try:
            response = opener.open(url)
        except error.HTTPError:
            print("HTTP Error 416")
        else:
            data = response.read()
            headers = dict(response.info())
            content_range = str(headers['Content-Range'])
            print(f"\033[31m{content_range}\t{data}\033[0m")
            # start = int(content_range.split('-')[1].split('/')[0])
            start = int(content_range.split(' ')[1].split('-')[0])


def level_21() -> None:
    print(f"\033[31mLevel 21\033[0m")
    import bz2
    import zlib
    with open("level_20/package.pack", "rb") as file:
        data = file.read()
    while data != b"sgol ruoy ta kool":
        if data.startswith(b"x\x9c"):
            data = zlib.decompress(data)
            print(' ', end='')
        elif data.startswith(b"BZ"):
            data = bz2.decompress(data)
            print('B', end='')
        elif data.endswith(b"\x9cx"):
            data = data[::-1]
            print()
    print(data[::-1])


def level_22() -> None:
    print(f"\033[31mLevel 22\033[0m")
    from PIL import Image, ImageSequence
    im0 = Image.open("level_22/white.gif")
    im1 = Image.new("1", (400, 100))
    index = 1
    x, y = 50, 50
    for frame in ImageSequence.Iterator(im0):
        i, j = 98, 98
        while i <= 102:
            if frame.getpixel((i, j)) != 0:
                break
            if j == 102:
                i, j = i + 1, 98
            else:
                j += 1
        dx, dy = i - 100, j - 100
        if dx == dy == 0:
            index += 1
            x, y = index * 50, 50
        else:
            x, y = x + dx, y + dy
            im1.putpixel((x, y), 1)
    im1.save("level_22/result.png")


def level_23() -> None:
    print(f"\033[31mLevel 23\033[0m")
    import this
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    text = "va gur snpr bs jung?"
    for offset in range(26):
        new_aplhabets = alphabets[offset:] + alphabets[:offset]
        trans = str.maketrans(alphabets, new_aplhabets)
        new_text = text.translate(trans)
        print(new_text)


def level_24() -> None:
    print(f"\033[31mLevel 24\033[0m")
    import numpy as np
    from PIL import Image
    im0 = Image.open("level_24/maze.png")
    rgba_array = np.asarray(im0, dtype=np.uint8).copy()
    im0 = im0.convert(mode="1")
    maze_array = np.asarray(im0, dtype=np.uint8).copy()
    maze_array = 1 - maze_array

    n, m = maze_array.shape
    queue_list = [(0, m - 2)]
    path_array = np.zeros((n, m, 2), dtype=np.int)
    dx_tuple, dy_tuple = (0, 0, 1, -1), (1, -1, 0, 0)
    while queue_list:
        x, y = queue_list.pop(0)
        maze_array[x, y] = 0
        if x == n - 1:
            break
        for dx, dy in zip(dx_tuple, dy_tuple):
            xx, yy = x + dx, y + dy
            if 0 <= xx < n and 0 <= yy < m and maze_array[xx, yy]:
                maze_array[xx, yy] = False
                path_array[xx, yy] = [x, y]
                queue_list.append((xx, yy))

    im1 = Image.new(mode="1", size=(n, m), color=1)
    r_list = []
    x, y = n - 1, 1
    while x != 0 or y != 0:
        im1.putpixel((x, y), 0)
        r_list.append(rgba_array[x, y, 0])
        x, y = path_array[x, y]
    im1.save("level_24/path.png")

    r_list = r_list[-2::-2]
    r_bytes = bytes(r_list)
    with open("level_24/red.rar", "wb") as file:
        file.write(r_bytes)


def level_25() -> None:
    print(f"\033[31mLevel 25\033[0m")
    from urllib import request, error
    import wave
    from PIL import Image
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, "http://www.pythonchallenge.com/", "butter", "fly")
    handler = request.HTTPBasicAuthHandler(password_mgr)
    opener = request.build_opener(handler)

    for i in range(1, 0):
        print(f"Processing {i:2d}...", end='\t')
        url = f"http://www.pythonchallenge.com/pc/hex/lake{i}.wav"
        try:
            response = opener.open(url)
        except error.HTTPError:
            print("HTTP ERROR 404")
        else:
            with open(f"level_25/lake{i}.wav", "wb") as file:
                data = response.read()
                file.write(data)
                print("Successfully Saved.")

    im = Image.new("RGB", (300, 300))
    for i in range(1, 26):
        with wave.open(f"level_25/lake{i}.wav", "rb") as file:
            data = file.readframes(file.getnframes())
            block_im = Image.frombytes("RGB", (60, 60), data)
            x, y = (i - 1) % 5 * 60, (i - 1) // 5 * 60
            im.paste(block_im, (x, y))
    im.save("level_25/result.jpg")


def level_26() -> None:
    print(f"\033[31mLevel 26\033[0m")
    import hashlib
    with open("level_26/mybroken.zip", "rb") as file:
        broken_data = file.read()
    correct_digest = "bbb8b499a0eef99b52c7f13f4e78c24b"
    for pos in range(len(broken_data)):
        print(f"Trying position {pos} ...")
        for k in range(256):
            data = broken_data[:pos] + bytes([k]) + broken_data[pos + 1:]
            digest = hashlib.md5(data).hexdigest()
            if digest == correct_digest:
                print(f"Successfully insert {k} at position {pos}")
                with open("level_26/mycorrect.zip", "wb") as file:
                    file.write(data)
                    return


def level_27() -> None:
    print(f"\033[31mLevel 27\033[0m")
    from PIL import Image
    import bz2
    import keyword
    im0 = Image.open("level_27/zigzag.gif")
    palette = im0.getpalette()[::3]
    data = im0.tobytes()
    palette_bytes = bytes(palette)
    index_bytes = bytes([i for i in range(256)])
    trans = bytes.maketrans(index_bytes, palette_bytes)
    new_data = data.translate(trans)

    print(data)
    print(new_data)

    diff_bytes = b''.join([bytes([b1]) if b1 != b2 else b'' for b1, b2 in zip(data[1:], new_data[:-1])])
    text = bz2.decompress(diff_bytes).decode()
    content = set(s if not keyword.iskeyword(s) else '' for s in text.split(' '))
    print(content)


def level_28() -> None:
    print(f"\033[31mLevel 28\033[0m")
    from PIL import Image
    im = Image.open("level_28/bell.png")
    green = list(im.split()[1].getdata())
    diff = [abs(p1 - p2) for p1, p2 in zip(green[0::2], green[1::2])]
    diff_filter = list(filter(lambda x: x != 42, diff))
    text = bytes(diff_filter).decode()
    print(text)


def level_29() -> None:
    print(f"\033[31mLevel 29\033[0m")
    import bz2
    with open("level_29/silence!.html", "r") as file:
        data = file.read()
    space_list = data.split('\n')[12:]
    count_list = [len(line) for line in space_list]
    count_bytes = bytes(count_list)
    text = bz2.decompress(count_bytes).decode()
    print(text)


def level_30() -> None:
    print(f"\033[31mLevel 30\033[0m")
    import re
    import numpy as np
    from PIL import Image

    with open("level_30/yankeedoodle.csv", "r") as file:
        data = file.read()
    data = re.findall(r"(0.\d*)", data)

    img_data = np.array(data, dtype=np.float).reshape(139, 53)
    im = Image.fromarray(256 * img_data)
    im = im.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
    im.save("level_30/formula.bmp")

    info_list = [int(x1[5] + x2[5] + x3[6]) for x1, x2, x3 in zip(data[::3], data[1::3], data[2::3])]
    info = bytes(info_list).decode()
    print(info)


def level_31() -> None:
    print(f"\033[31mLevel 31\033[0m")
    from PIL import Image

    left, top, width, height = 0.34, 0.57, 0.036, 0.027
    im0 = Image.open("level_31/mandelbrot.gif")
    im1 = Image.new("P", (640, 480))
    im1.putpalette(im0.getpalette())
    for w in range(640):
        for h in range(480):
            z = complex(0, 0)
            c = complex(left + w * width / 640, top + (479 - h) * height / 480)
            for i in range(128):
                z = z ** 2 + c
                if abs(z) > 2:
                    im1.putpixel((w, h), i)
                    break
            else:
                im1.putpixel((w, h), 127)
    im1.save("level_31/mandelbrot_1.gif")

    data0, data1 = list(im0.getdata()), list(im1.getdata())
    diff = [255 * (p0 < p1) for p0, p1 in zip(data0, data1) if p0 != p1]
    im2 = Image.new("L", (23, 73))
    im2.putdata(diff)
    im2.save("level_31/result.jpg")


def level_32() -> None:
    print(f"\033[31mLevel 32\033[0m")
    import numpy as np
    from PIL import Image

    is_solved = False
    ans_points = np.zeros(1)

    n = 9
    horizontal = [[2, 1, 2], [1, 3, 1], [5], [7], [9], [3], [2, 3, 2], [2, 3, 2], [2, 3, 2]]
    vertical = [[2, 1, 3], [1, 2, 3], [3], [8], [9], [8], [3], [1, 2, 3], [2, 1, 3]]

    n = 32
    horizontal = [[3, 2], [8], [10], [3, 1, 1],
                  [5, 2, 1], [5, 2, 1], [4, 1, 1], [15],
                  [19], [6, 14], [6, 1, 12], [6, 1, 10],
                  [7, 2, 1, 8], [6, 1, 1, 2, 1, 1, 1, 1], [5, 1, 4, 1], [5, 4, 1, 4, 1, 1, 1],
                  [5, 1, 1, 8], [5, 2, 1, 8], [6, 1, 2, 1, 3], [6, 3, 2, 1],
                  [6, 1, 5], [1, 6, 3], [2, 7, 2], [3, 3, 10, 4],
                  [9, 12, 1], [22, 1], [21, 4], [1, 17, 1],
                  [2, 8, 5, 1], [2, 2, 4], [5, 2, 1, 1], [5]]
    vertical = [[5], [5], [5], [3, 1],
                [3, 1], [5], [5], [6],
                [5, 6], [9, 5], [11, 5, 1], [13, 6, 1],
                [14, 6, 1], [7, 12, 1], [6, 1, 11, 1], [3, 1, 1, 1, 9, 1],
                [3, 4, 10], [8, 1, 1, 2, 8, 1], [10, 1, 1, 1, 7, 1], [10, 4, 1, 1, 7, 1],
                [3, 2, 5, 2, 1, 2, 6, 2], [3, 2, 4, 2, 1, 1, 4, 1], [2, 6, 3, 1, 1, 1, 1, 1], [12, 3, 1, 2, 1, 1, 1],
                [3, 2, 7, 3, 1, 2, 1, 2], [2, 6, 3, 1, 1, 1, 1], [12, 3, 1, 5], [6, 3, 1],
                [6, 4, 1], [5, 4], [4, 1, 1], [5]]

    def print_points(points: np.array) -> None:
        # print array in console
        if points[0, 0] == -2:
            print("ERROR\n")
            return
        for i in range(n):
            for j in range(n):
                if points[i, j] >= 1:
                    print('█', end='')
                elif points[i, j] == 1:
                    print('■', end='')
                elif points[i, j] == 0:
                    print('.', end='')
                elif points[i, j] == -1:
                    print('×', end='')
            print()
        print()

    def horizontal_put(points: np.array, x: int, y0: int, y1: int) -> np.array:
        # the next position of current array is already occupied
        if y1 + 1 < n and np.min(points[x, y0:y1 + 1]) >= 1:
            points[0, 0] = -3
            return points
        # some positions of current array are inaccessible
        if np.min(points[x, y0:y1]) == -1 or (y1 < n and points[x, y1] > 0):
            points[0, 0] = -2
            return points
        # set all positions of current array occupied
        points[x, y0:y1] = 1
        # set the next position of current array inaccessible
        if y1 < n:
            points[x, y1] = -1
        return points

    def vertical_put(points: np.array) -> np.array:
        for y in range(n):
            x = 0
            # this column is already finished
            if points[n - 1, y] != 0:
                continue
            for i, nums in enumerate(vertical[y]):
                # find next begin position of this column
                while x < n and points[x, y] <= 0:
                    x += 1
                # at the end of this column
                if x == n:
                    break
                # goto the end position of current array
                if points[x, y] == 2:
                    x += nums
                # not enough positions to put current array
                elif points[x, y] == 1 and x + nums - 1 >= n:
                    points[0, 0] = -2
                    return points
                # set positions of current array occupied
                elif points[x, y] == 1:
                    points[x, y] = 2
                    points[x + 1:x + nums, y] = 1
                    # set the next position of current array inaccessible
                    if x + nums < n:
                        points[x + nums, y] = -1
                    # this is the last array and set all rest positions inaccessible
                    if i + 1 == len(vertical[y]) and x + nums < n:
                        points[x + nums:, y] = -1
                    break
        return points

    def search(points: np.array, x: int, y: int, k: int) -> None:
        nonlocal is_solved, ans_points
        # solution is found
        if x == n:
            print_points(points)
            ans_points = points.copy()
            is_solved = True
            return

        # the last position of this row can start this array
        j_end = n - sum(horizontal[x][k:]) - (len(horizontal[x]) - k - 1)

        for j in range(y, j_end + 1):
            # the previous position of current array is occupied
            if j >= 1 and points[x, j - 1] > 0:
                break

            # create a copy
            j1 = j + horizontal[x][k]
            new_points = points.copy()

            # try to put current array into positions row[x] column[j-j1]
            new_points = horizontal_put(new_points, x, j, j1)
            # error code -2
            if new_points[0, 0] == -2:
                continue
            # error code -3
            elif new_points[0, 0] == -3:
                break

            # check and put arrays in columns
            new_points = vertical_put(new_points)
            if new_points[0, 0] == -2:
                continue

            # this is the last array of this row, but some rest positions of this row are still occupied
            if k + 1 == len(horizontal[x]) and j1 < n and np.max(new_points[x, j1:]) > 0:
                continue

            # recur to next
            if k + 1 == len(horizontal[x]):
                search(new_points, x + 1, 0, 0)
            else:
                search(new_points, x, j1 + 1, k + 1)

            # solution is already found
            if is_solved:
                return

    search(np.zeros((n, n), dtype=np.int), 0, 0, 0)

    ans_points[ans_points > 0] = 255
    ans_points[ans_points <= 0] = 0
    im = Image.fromarray(ans_points.astype(np.uint8), "L")
    im.save("level_32/python.jpg")


def level_33() -> None:
    print(f"\033[31mLevel 33\033[0m")
    from PIL import Image
    import numpy as np

    im = Image.open("level_33/beer2.png")
    data_list = list(im.getdata())
    data_set = set(data_list)
    while data_set:
        c0 = max(data_set)
        data_set.remove(c0)
        c1 = max(data_set)
        data_set.remove(c1)
        c0, c1 = max(c0, c1), min(c0, c1)

        n = int(len(data_list) ** 0.5)
        data_np = np.array(data_list, dtype=np.uint8).reshape(n, n)
        data_np[data_np >= c1] = 255
        data_np[data_np < c1] = 0
        data_list = [c for c in data_list if c < c1]

        im = Image.fromarray(data_np, "L")
        im.save(f"level_33/{n}.png")


if __name__ == "__main__":
    level_12()
