constants_for_generate_key = ((70, 151, 177, 186, 163, 183, 16, 10, 197, 55, 179, 201, 90, 40, 172, 100),
                              (236, 171, 170, 198, 103, 149, 88, 13, 248, 154, 246, 110, 102, 220, 5, 61),
                              (138, 195, 216, 137, 106, 233, 54, 73, 67, 191, 235, 212, 150, 155, 104, 160),
                              (93, 87, 146, 31, 213, 113, 92, 187, 34, 193, 190, 123, 188, 153, 99, 148),
                              (42, 97, 184, 52, 50, 25, 253, 251, 23, 64, 230, 81, 29, 65, 68, 143),
                              (221, 4, 128, 222, 231, 49, 214, 127, 1, 162, 247, 57, 218, 111, 35, 202),
                              (58, 208, 28, 209, 48, 62, 18, 161, 205, 15, 224, 168, 175, 130, 89, 44),
                              (125, 173, 178, 239, 194, 135, 206, 117, 6, 19, 2, 144, 79, 46, 114, 51),
                              (192, 141, 207, 169, 129, 226, 196, 39, 47, 108, 122, 159, 82, 225, 21, 56),
                              (252, 32, 66, 199, 8, 228, 9, 85, 94, 140, 20, 118, 96, 255, 223, 215),
                              (250, 11, 33, 0, 26, 249, 166, 185, 232, 158, 98, 76, 217, 145, 80, 210),
                              (24, 180, 7, 132, 234, 91, 164, 200, 14, 203, 72, 105, 75, 78, 156, 53),
                              (69, 77, 84, 229, 37, 60, 12, 74, 139, 63, 204, 167, 219, 107, 174, 244),
                              (45, 243, 124, 109, 157, 181, 38, 116, 242, 147, 83, 176, 240, 17, 237, 131),
                              (182, 3, 22, 115, 59, 30, 142, 112, 189, 134, 27, 71, 126, 36, 86, 241),
                              (136, 70, 151, 177, 186, 163, 183, 16, 10, 197, 55, 179, 201, 90, 40, 172),
                              (220, 134, 119, 215, 166, 17, 251, 244, 186, 146, 145, 100, 131, 241, 51, 239),
                              (44, 181, 178, 43, 136, 209, 153, 203, 140, 132, 29, 20, 129, 151, 113, 202),
                              (163, 139, 87, 60, 130, 196, 82, 92, 28, 232, 160, 4, 180, 133, 74, 246),
                              (84, 182, 223, 12, 26, 142, 222, 224, 57, 252, 32, 155, 36, 78, 169, 152),
                              (171, 242, 96, 208, 108, 234, 250, 199, 217, 0, 212, 31, 110, 67, 188, 236),
                              (137, 254, 122, 93, 73, 201, 50, 194, 249, 154, 248, 109, 22, 219, 89, 150),
                              (233, 205, 230, 70, 66, 143, 10, 193, 204, 185, 101, 176, 210, 198, 172, 30),
                              (98, 41, 46, 14, 116, 80, 2, 90, 195, 37, 123, 138, 42, 91, 240, 6),
                              (71, 111, 112, 157, 126, 16, 206, 18, 39, 213, 76, 79, 214, 121, 48, 104),
                              (117, 125, 228, 237, 128, 106, 144, 55, 162, 94, 118, 170, 197, 127, 61, 175),
                              (229, 25, 97, 253, 77, 124, 183, 11, 238, 173, 75, 34, 245, 231, 115, 35),
                              (200, 5, 225, 102, 221, 179, 88, 105, 99, 86, 15, 161, 49, 149, 23, 7),
                              (40, 1, 45, 226, 147, 190, 69, 21, 174, 120, 3, 135, 164, 184, 56, 207),
                              (8, 103, 9, 148, 235, 38, 168, 107, 189, 24, 52, 27, 187, 191, 114, 247),
                              (53, 72, 156, 81, 47, 59, 85, 227, 192, 159, 216, 211, 243, 141, 177, 255),
                              (62, 220, 134, 119, 215, 166, 17, 251, 244, 186, 146, 145, 100, 131, 241, 51))

matrix_for_encrypt = ((2, 2, 1, 1, 16, 8, 2, 1, 4, 2, 4, 2, 1, 1, 4, 4),
                      (1, 1, 1, 1, 8, 4, 2, 1, 2, 1, 4, 2, 1, 1, 2, 2),
                      (1, 1, 4, 4, 2, 1, 4, 2, 4, 2, 16, 8, 2, 2, 1, 1),
                      (1, 1, 2, 2, 2, 1, 2, 1, 4, 2, 8, 4, 1, 1, 1, 1),
                      (4, 4, 2, 1, 4, 2, 4, 2, 16, 8, 1, 1, 1, 1, 2, 2),
                      (2, 2, 2, 1, 2, 1, 4, 2, 8, 4, 1, 1, 1, 1, 1, 1),
                      (1, 1, 4, 2, 4, 2, 16, 8, 2, 1, 2, 2, 4, 4, 1, 1),
                      (1, 1, 2, 1, 4, 2, 8, 4, 2, 1, 1, 1, 2, 2, 1, 1),
                      (2, 1, 16, 8, 1, 1, 2, 2, 1, 1, 4, 4, 4, 2, 4, 2),
                      (2, 1, 8, 4, 1, 1, 1, 1, 1, 1, 2, 2, 4, 2, 2, 1),
                      (4, 2, 4, 2, 4, 4, 1, 1, 2, 2, 1, 1, 16, 8, 2, 1),
                      (2, 1, 4, 2, 2, 2, 1, 1, 1, 1, 1, 1, 8, 4, 2, 1),
                      (4, 2, 2, 2, 1, 1, 4, 4, 1, 1, 4, 2, 2, 1, 16, 8),
                      (4, 2, 1, 1, 1, 1, 2, 2, 1, 1, 2, 1, 2, 1, 8, 4),
                      (16, 8, 1, 1, 2, 2, 1, 1, 4, 4, 2, 1, 4, 2, 4, 2),
                      (8, 4, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 4, 2))

matrix_for_decrypt = ((2, -2, 1, -2, 1, -1, 4, -8, 2, -4, 1, -1, 1, -2, 1, -1),
                      (-4, 4, -2, 4, -2, 2, -8, 16, -2, 4, -1, 1, -1, 2, -1, 1),
                      (1, -2, 1, -1, 2, -4, 1, -1, 1, -1, 1, -2, 2, -2, 4, -8),
                      (-2, 4, -2, 2, -2, 4, -1, 1, -1, 1, -1, 2, -4, 4, -8, 16),
                      (1, -1, 2, -4, 1, -1, 1, -2, 1, -2, 1, -1, 4, -8, 2, -2),
                      (-1, 1, -2, 4, -1, 1, -1, 2, -2, 4, -2, 2, -8, 16, -4, 4),
                      (2, -4, 1, -1, 1, -2, 1, -1, 2, -2, 4, -8, 1, -1, 1, -2),
                      (-2, 4, -1, 1, -1, 2, -1, 1, -4, 4, -8, 16, -2, 2, -2, 4),
                      (1, -1, 1, -2, 1, -1, 2, -4, 4, -8, 2, -2, 1, -2, 1, -1),
                      (-1, 1, -1, 2, -1, 1, -2, 4, -8, 16, -4, 4, -2, 4, -2, 2),
                      (1, -2, 1, -1, 4, -8, 2, -2, 1, -1, 1, -2, 1, -1, 2, -4),
                      (-1, 2, -1, 1, -8, 16, -4, 4, -2, 2, -2, 4, -1, 1, -2, 4),
                      (4, -8, 2, -2, 1, -2, 1, -1, 1, -2, 1, -1, 2, -4, 1, -1),
                      (-8, 16, -4, 4, -2, 4, -2, 2, -1, 2, -1, 1, -2, 4, -1, 1),
                      (1, -1, 4, -8, 2, -2, 1, -2, 1, -1, 2, -4, 1, -1, 1, -2),
                      (-2, 2, -8, 16, -4, 4, -2, 4, -1, 1, -2, 4, -1, 1, -1, 2))

arrE = (99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254, 215, 171, 118,
        202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 162, 175, 156, 164, 114, 192,
        183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229, 241, 113, 216, 49, 21,
        4, 199, 35, 195, 24, 150, 5, 154, 7, 18, 128, 226, 235, 39, 178, 117,
        9, 131, 44, 26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47, 132,
        83, 209, 0, 237, 32, 252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207,
        208, 239, 170, 251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168,
        81, 163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210,
        205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 115,
        96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94, 11, 219,
        224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 149, 228, 121,
        231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174, 8,
        186, 120, 37, 46, 28, 166, 180, 198, 232, 221, 116, 31, 75, 189, 139, 138,
        112, 62, 181, 102, 72, 3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158,
        225, 248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233, 206, 85, 40, 223,
        140, 161, 137, 13, 191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22)

arrL = (82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 215, 251,
        124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 233, 203,
        84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 78,
        8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37,
        114, 248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146,
        108, 112, 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132,
        144, 216, 171, 0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6,
        208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107,
        58, 145, 17, 65, 79, 103, 220, 234, 151, 242, 207, 206, 240, 180, 230, 115,
        150, 172, 116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28, 117, 223, 110,
        71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98, 14, 170, 24, 190, 27,
        252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90, 244,
        31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 95,
        96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239,
        160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97,
        23, 43, 4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125)
