import xml.sax
import math

class R2Handler( xml.sax.ContentHandler ):
    def __init__(self):
        self.title = ""
        self.bpm = []
        self.bgm = ""
        self.offset = 0.0
        self.pumian = []
    
    # 元素开始事件处理
    def startElement(self, tag, attributes):
        # self.CurrentData = tag
        if tag == "TITLE":
            self.title = attributes["Name"]
        elif tag == "BPM":
            # 一个Coord=48分音
            self.bpm.append(str(int(attributes["Frame"]) / 48.0) + '=' + attributes["BPM"])
        elif tag == "BGM":
            self.bgm = attributes["Name"]
        elif tag == "DELAY":
            # R2Beat里的1秒=60帧
            self.offset = int(attributes["Value"]) / 60.0
        elif tag == "LENGTH":
            self.pumian = ["00000"] * (int(attributes["Value"]) + 1)
        elif tag == "AREA":
            coord = int(attributes["Coord"])
            kind = int(attributes["Kind"])
            level = int(attributes["Level"])
            # 左上 1 看成是 上
            # 左下 0 看成是 左
            # 右上 3 看成是 右
            # 右下 4 看成是 下
            pumianslice = "00000"
            if (kind == 16):
                # 上：　Kind=“16” Level=“3”
                pumianslice = "01000"
            elif (kind == 17):
                # 下：　Kind=“17” Level=“3”
                pumianslice = "00001"
            elif (kind == 18):
                # 左：　Kind=“18” Level=“2”
                pumianslice = "10000"
            elif (kind == 19):
                # 右：　Kind=“19” Level=“2”
                pumianslice = "00010"
            elif (kind == 20):
                # 左上：Kind=“20” Level=“5”
                pumianslice = "01100"
            elif (kind == 21):
                # 右上：Kind=“21” Level=“5”
                pumianslice = "00110"
            elif (kind == 22):
                # 左下：Kind=“22” Level=“4”
                pumianslice = "10100"
            elif (kind == 23):
                # 右下：Kind=“23” Level=“4”
                pumianslice = "00101"
            elif (kind == 24):
                # 跳台：Kind=“24” Level=“4”
                pumianslice = "00100"
            elif (kind == 26):
                # 左星：Kind=“26” Level=“1”
                pumianslice = "11100"
            elif (kind == 27):
                # 右星：Kind=“27” Level=“1”
                pumianslice = "00111"
            elif (kind == 128):
                # 长左上：起始Kind=“128”
                pumianslice = "02200"
            elif (kind == 130):
                # 长左上：结束Kind=“130”
                pumianslice = "03300"
            elif (kind == 131):
                # 长右上：起始Kind=“131”
                pumianslice = "00220"
            elif (kind == 133):
                # 长右上：结束Kind=“133”
                pumianslice = "00330"
            elif (kind == 134):
                # 长上：　起始Kind=“134”
                pumianslice = "02000"
            elif (kind == 136):
                # 长上：　结束Kind=“136”
                pumianslice = "03000"
            elif (kind == 137):
                # 长下：　起始Kind=“137”
                pumianslice = "00002"
            elif (kind == 139):
                # 长下：　结束Kind=“139”
                pumianslice = "00003"
            elif (kind == 140):
                # 长左：　起始Kind=“140”
                pumianslice = "20000"
            elif (kind == 142):
                # 长左：　结束Kind=“142”
                pumianslice = "30000"
            elif (kind == 143):
                # 长右：　起始Kind=“143”
                pumianslice = "00020"
            elif (kind == 145):
                # 长右：　结束Kind=“145”
                pumianslice = "00030"

            self.pumian[coord] = pumianslice
 
    # 元素结束事件处理
    def endElement(self, tag):
        pass
 
    # 内容事件处理
    def characters(self, content):
        pass

def output_sm(out, handler):
    with open(out, 'w') as f:
        output_head(f, handler)
        output_content(f, handler)

def output_head(f, handler):
    f.write('#TITLE:' + handler.title + ';\n')
    f.write('#SUBTITLE:;\n')
    f.write('#ARTIST:Unknown artist;\n')
    f.write('#TITLETRANSLIT:;\n')
    f.write('#SUBTITLETRANSLIT:;\n')
    f.write('#ARTISTTRANSLIT:;\n')
    f.write('#MUSIC:' + handler.bgm + ';\n')
    f.write('#BACKGROUND:;\n')
    f.write('#BANNER:;\n')
    f.write('#OFFSET:' + str(handler.offset) +';\n')
    f.write('#SAMPLESTART:0.000;\n')
    f.write('#SAMPLELENGTH:12.000;\n')
    f.write('#BPMS:'+','.join(handler.bpm)+';\n')

def output_content(f, handler):
    f.write('#NOTES:\n')
    f.write('     pump-single:\n')
    f.write('     Crazy:\n')
    f.write('     Hard:\n')
    f.write('     7:\n')
    f.write('     1:\n')    
    num_measure = math.ceil(len(handler.pumian) / 48)
    current_line = 0
    for i in range(num_measure):
        for j in range(48):
            if (current_line < len(handler.pumian)):
                f.write(handler.pumian[current_line]+'\n')
            else:
                f.write('00000\n')
            current_line += 1
        f.write(',\n')

if ( __name__ == "__main__"):
   
    fromdir = "n_song4423.xml"
    todir = "xiaye.sm"

    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = R2Handler()
    parser.setContentHandler( Handler )

    parser.parse(fromdir)

    output_sm(todir, Handler)