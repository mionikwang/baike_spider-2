# 爬虫数据输出器
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]

    # 用于收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 用于将收集好的数据生成html页面
    def output_html(self):
        fout=open('output.html', 'w', encoding="utf-8")
        fout.write("<html>")
        fout.write('<head><meta charset="utf-8"></head>')  # 告诉浏览器使用什么编码，解决了输出乱码
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("<tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
