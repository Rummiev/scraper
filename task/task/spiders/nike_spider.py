import json

import scrapy


class NikeSpider(scrapy.Spider):
    name = "nike"
    allowed_domains = ["academy.com"]
    start_urls = ["https://www.academy.com/"]

    def parse(self, response):
        """Navigate to Women's Footwear"""
        shoes_href = "/c/womens/womens-footwear"
        yield response.follow(shoes_href, callback=self.parse_shoes)

    def parse_shoes(self, response):
        """Navigate to Women's Sneakers"""
        sneakers_href = "/c/womens/womens-footwear/womens-athletic-sneakers"
        yield response.follow(sneakers_href, callback=self.parse_sneakers)

    def parse_sneakers(self, response):
        """Navigate to Women's Lifestyle Sneakers"""
        lifestyle_href = (
            "/c/womens/womens-footwear/womens-athletic-sneakers/womens-lifestyle"
        )
        yield response.follow(lifestyle_href, callback=self.parse_lifestyle)

    def parse_lifestyle(self, response):
        """Navigate to a Specific Product"""
        product_href = "/p/nike-womens-court-legacy-next-nature-shoes"
        yield response.follow(product_href, callback=self.parse_product)

    def parse_product(self, response):
        """Extract product details and format JSON output"""
        data = json.loads(
            response.xpath(
                "//script[@type='application/ld+json'][contains(text(),'ProductGroup')]/text()"
            ).get()
        )

        yield {
            "name": data[0]["name"],
            "price": float(data[0]["hasVariant"][0]["offers"]["price"]),
            "defaultColour": data[0]["hasVariant"][0]["color"],
            "availableColours": [var["color"] for var in data[0]["hasVariant"]],
            "reviews_count": int(data[0]["aggregateRating"]["reviewCount"]),
            "reviews_score": float(data[0]["aggregateRating"]["ratingValue"]),
        }