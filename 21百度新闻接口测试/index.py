import requests

if __name__ == "__main__":
    q1 = '智商'
    r = requests.get(
        (
            'http://news.baidu.com/ns?from=news&cl=2&bt=1499011200&y0=2017&m0=7&d0=3&y1=2017&m1=7&d1=3&et=1499097599&q1=' + q1 + '&submit=&q3=&q4=&mt=0&lm=&s=2&begin_date=2017-7-3&end_date=2017-7-3&tn=newsdy&ct1=1&ct=1&rn=20&q6='))
    file = open('result.html', 'wb')

    file.write(r.content)
    pass
