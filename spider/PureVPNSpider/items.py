# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PurevpnspiderItem(scrapy.Item):
    # define the fields for your item here like:

    region = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    address_pp2p = scrapy.Field()
    address_l2tp = scrapy.Field()
    address_sstp = scrapy.Field()
    address_ikev2 = scrapy.Field()
    address_openvpn_udp = scrapy.Field()
    address_openvpn_tcp = scrapy.Field()
    # pass
