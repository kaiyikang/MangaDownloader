import chapter_parser

class MdMain(object):
    def __init__(self):
        self.chapterParser = chapter_parser.MDParser()

    def craw(self,root_url):
        get_list = self.chapterParser.get_all_chapter(root_url)

if __name__ == '__main__':

    download_url = "http://www.cartoonmad.com/comic/3376.html"
    jueAndGongcun = MdMain()
    jueAndGongcun.craw(download_url)