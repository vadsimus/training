def bmp_gif(bmp):
    gif = f'Internal converting ({bmp}) to gif'
    return gif


class BigUsefilLib:
    def jpg_bmp(self, jpg):
        bmp = f'Internal converting ({jpg}) to bmp'
        return bmp

    def png_bmp(self, png):
        pass

    def png_jpg(self, png):
        pass


class FacdeBigUsefulLib:
    def jpg_gif(self, jpg):
        bibl = BigUsefilLib()
        return bmp_gif(bibl.jpg_bmp(jpg))


facade = FacdeBigUsefulLib()
print(facade.jpg_gif('jpg_pic'))

