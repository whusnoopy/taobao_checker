# coding: utf8

from argparse import ArgumentParser

from actions import checker


def output_results(output_results, correct_price, output_full=False):
    def output_line(detail, promo, color=None):
        if not color:
            color = 37
        if output_full:
            line = detail + promo
        else:
            line = promo
        print '\033[%dm%s\033[m' % (color, line)

    detail_format = ' %-31s| %-15s| %-43s|'
    promo_format = ' %-11s| %-23s| %-s'

    detail_header = detail_format % ('detail server', 'origin price', 'detail resp via')
    promo_header = promo_format % ('price', 'promo resp via', 'promo resp _host')
    output_line(detail_header, promo_header)

    detail_hr = '-'*32 + '+' + '-'*16 + '+' + '-'*44 + '+'
    promo_hr = '-'*12 + '+' + '-'*24 + '+' + '-'*32
    output_line(detail_hr, promo_hr)

    last_price = ''
    for r in output_results:
        correct = True
        if correct_price:
            if r['promo_price'] == 'NULL' or float(r['promo_price']) != correct_price:
                correct = False
        else:
            if last_price:
                if r['promo_price'] != last_price:
                    correct = False
            else:
                last_price = r['promo_price']

        detail_output = detail_format % (r['detail_server'], r['origin_price'], r['detail_via'])
        promo_output = promo_format % (r['promo_price'], r['promo_via'], r['promo_host'])

        if correct:
            if correct_price:
                output_line(detail_output, promo_output, 32)
            else:
                output_line(detail_output, promo_output)
        else:
            output_line(detail_output, promo_output, 31)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('item_id', help="num_iid to check")
    parser.add_argument('-c', '--correct_price', help="correct price should be", type=float, default=0, required=False)
    parser.add_argument('-r', '--retry', help="retry times", type=int, default=16, required=False)
    parser.add_argument('-f', '--full', help="output all columns", action='store_true')

    args = parser.parse_args()

    item_url = checker.get_item_url(args.item_id)

    fetch_results = checker.fetch_taobao_price(item_url, args.retry)

    output_results(fetch_results, args.correct_price, args.full)
