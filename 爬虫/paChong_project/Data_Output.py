# coding:utf-8
import codecs
class DataOutput():
    def __init__(self):
        self.datas=[]
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout=open('baike.txt','w',encoding='utf-8')
        for data in self.datas:
            fout.write(data['url'])
            fout.write(data['title'])
            fout.write(data['summary'])
        fout.close()

    ''' 
   def output_html(self):
        fout=codecs.open('baike.html','w',encoding='utf-8')
        fout.writer("<html>")
        fout.writer("<head><meta charset='utf-8'/></head>")
        fout.writer("<body>")
        fout.writer("<table>")
        for data in self.datas:
            fout.writer("<tr>")
            fout.writer("<td>%s</td>"%data['url'])
            fout.writer("<td>%s</td>"%data['title'])
            fout.writer("<td>%s</td>"%data['summary'])
            fout.writer("</tr>")
            self.datas.remove(data)
        fout.writer("</table>")
        fout.writer("</body>")
        fout.writer("</html>")
        fout.close()
        '''


