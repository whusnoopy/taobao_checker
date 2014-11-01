# coding: utf8

import urllib2
from argparse import ArgumentParser


def get_item_url(url):
    if url.find('?') < 0:
        num_iid = url
    else:
        num_iid = 0
        for para in url.split('?')[1].split('&'):
            k, v = para.split('=')
            if k == 'id':
                num_iid = v

    return 'http://item.taobao.com/item.htm?id=' + num_iid


def get_sib_url(item_url):
    request = urllib2.urlopen(item_url)
    content = request.read()

    pos = content.find('http://detailskip.taobao.com/json/sib.htm')
    if pos < 0:
        # tmall
        pos = content.find('http://mdskip.taobao.com/core/initItemDetail.htm')
        sib_url = content[pos:content.find("'", pos)]
    else:
        sib_url = content[pos:content.find('"', pos)]

    return sib_url


def fetch_taobao_price(detail_url, item_url, retry_times=16):
    tmall = False
    if detail_url.find('sib.htm') < 0:
        tmall = True

    opener = urllib2.build_opener()
    fetch_rets = []
    for i in xrange(retry_times):
        request = urllib2.Request(detail_url)
        request.add_header('Referer', item_url)

        response = opener.open(request)

        content = response.read()
        if tmall:
            promotion_pos = content.find('promotionList')
            if content[promotion_pos+15:promotion_pos+19] == 'null':
                pos = -1
            else:
                pos = content.find('price":', promotion_pos)
        else:
            promotion_pos = content.find('g_config.PromoData=')
            pos = content.find('price:"', promotion_pos)
        if pos < 0:
            page_price = 'NULL'
        else:
            start_pos = content.find(':', pos) + 2
            end_pos = content.find('"', start_pos)
            page_price = content[start_pos:end_pos]

        via = 'NULL'
        host = 'NULL'
        headers = response.info().headers
        for header in headers:
            k, v = header[:-2].split(': ', 1)
            if k == 'Via':
                via = v
            elif k == '_Host':
                host = v

        fetch_rets.append((page_price, via, host))

    return fetch_rets


def output_results(output_results, correct_price):
    format_str = '%-8s| %-23s| %-s'

    print format_str % ('price', 'response header via', 'response header _host')
    print '-'*8 + '+' + '-'*24 + '+' + '-'*32

    for r in output_results:
        correct = True
        if float(r[0]) != correct_price:
            correct = False

        output = format_str % r

        if correct:
            print '\033[32m%s\033[m' % output
        else:
            print '\033[31m%s\033[m' % output


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('item_id', help="num_iid to check")
    parser.add_argument('-c', '--correct_price', help="correct price should be", type=float, default=0, required=False)
    parser.add_argument('-r', '--retry', help="retry times", type=int, default=16, required=False)

    args = parser.parse_args()

    item_url = get_item_url(args.item_id)
    sib_url = get_sib_url(item_url)

    fetch_results = fetch_taobao_price(sib_url, item_url, args.retry)

    output_results(fetch_results, args.correct_price)
