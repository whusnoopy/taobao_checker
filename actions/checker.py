# coding: utf8

import urllib2


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


def fetch_taobao_price(detail_url, retry_times=16):
    opener = urllib2.build_opener()
    fetch_results = []
    for i in xrange(retry_times):
        tmall = False

        # detail page
        detail_request = urllib2.Request(detail_url)
        detail_response = opener.open(detail_request)
        detail_content = detail_response.read()

        detail_server_pos = detail_content.find('<div id="server-num">')
        if detail_server_pos < 0:
            detail_server = 'NULL'
        else:
            start_pos = detail_content.find('>', detail_server_pos) + 1
            end_pos = detail_content.find('<', start_pos)
            detail_server = detail_content[start_pos:end_pos]

        detail_via = 'NULL'
        detail_host = 'NULL'
        detail_headers = detail_response.info().headers
        for header in detail_headers:
            k, v = header[:-2].split(': ', 1)
            if k == 'Via':
                detail_via = v
            elif k == '_Host':
                detail_host = v

        sib_pos = detail_content.find('http://detailskip.taobao.com/json/sib.htm')
        if sib_pos < 0:
            # tmall
            sib_pos = detail_content.find('http://mdskip.taobao.com/core/initItemDetail.htm')
            sib_url = detail_content[sib_pos:detail_content.find("'", sib_pos)]
            tmall = True
        else:
            sib_url = detail_content[sib_pos:detail_content.find('"', sib_pos)]

        if tmall:
            origin_price_pos = detail_content.find('<span class="originPrice"')
            if origin_price_pos < 0:
                origin_price = 'NULL'
            else:
                start_pos = detail_content.find(';', origin_price_pos) + 1
                end_pos = detail_content.find('<', start_pos)
                origin_price = detail_content[start_pos:end_pos]
        else:
            origin_price_pos = detail_content.find('<strong id="J_StrPrice"')
            if origin_price_pos < 0:
                origin_price = 'NULL'
            else:
                start_pos = detail_content.find('class="tb-rmb-num">', origin_price_pos) + 19
                end_pos = detail_content.find('<', start_pos)
                origin_price = detail_content[start_pos:end_pos]

        # promo data request
        sib_request = urllib2.Request(sib_url)
        sib_request.add_header('Referer', detail_url)

        sib_response = opener.open(sib_request)

        sib_content = sib_response.read()
        if tmall:
            promotion_pos = sib_content.find('promotionList')
            if sib_content[promotion_pos+15:promotion_pos+19] == 'null':
                pos = -1
            else:
                pos = sib_content.find('price":', promotion_pos)
        else:
            promotion_pos = sib_content.find('g_config.PromoData=')
            pos = sib_content.find('price:"', promotion_pos)
        if pos < 0:
            page_price = 'NULL'
        else:
            start_pos = sib_content.find(':', pos) + 2
            end_pos = sib_content.find('"', start_pos)
            page_price = sib_content[start_pos:end_pos]

        promo_via = 'NULL'
        promo_host = 'NULL'
        promo_headers = sib_response.info().headers
        for header in promo_headers:
            k, v = header[:-2].split(': ', 1)
            if k == 'Via':
                promo_via = v
            elif k == '_Host':
                promo_host = v

        fetch_results.append(dict(detail_server=detail_server, origin_price=origin_price,
                                  detail_via=detail_via, detail_host=detail_host,
                                  promo_price=page_price, promo_via=promo_via, promo_host=promo_host))

    return fetch_results
