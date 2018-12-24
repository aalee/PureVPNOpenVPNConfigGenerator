# -*- coding: utf-8 -*-
import scrapy

from spider.PureVPNSpider.items import PurevpnspiderItem


class PurevpnseverlistSpider(scrapy.Spider):
    name = 'purevpnseverlist'
    allowed_domains = ['support.purevpn.com']
    start_urls = ['https://support.purevpn.com/vpn-servers/']

    def parse(self, response):
        purevpn_data_list = []
        body = response.xpath('//tbody[@id="servers_data"]/tr')
        for index, tbody in enumerate(body):
            purevpn_data = PurevpnspiderItem()
            purevpn_data['region'] = tbody.xpath('td[1]/text()').extract()
            purevpn_data['country'] = tbody.xpath('td[2]/text()').extract()
            purevpn_data['city'] = tbody.xpath('td[3]/text()').extract()
            purevpn_data['address_pp2p'] = purevpn_data[
                'address_l2tp'] = purevpn_data['address_sstp'] = purevpn_data[
                'address_ikev2'] = tbody.xpath('td[4]/text()').extract()
            purevpn_data['address_openvpn_udp'] = tbody.xpath(
                'td[5]/text()').extract()
            purevpn_data['address_openvpn_tcp'] = tbody.xpath(
                'td[6]/text()').extract()
            purevpn_data_list.append(purevpn_data)
        return purevpn_data_list
