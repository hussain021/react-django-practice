import requests
import json
from best_buy_scrapper.constants import headers, params, cookies


class MenuLink:
    def __init__(self):
        response = requests.get(
            "https://www.bestbuy.com/api/tcfb/model.json",
            headers=headers,
            params=params,
            cookies=cookies,
        )
        js = json.loads(response.text)
        self.list_of_links = []
        js = js["jsonGraph"]["shop"]["scds"]["v2"]["page"]["byView"]["tenants"][
            "bbypres"
        ]["pages"]["globalnavigationv5sv"]["view"]["large"]["header"]["value"]
        for global_nav in js["globalNavigation"]:
            for link in global_nav["childNodes"]:
                if len(link["childNodes"]) > 0:
                    for inner_link in link["childNodes"]:
                        if inner_link["link"].get("url"):
                            self.list_of_links.append(
                                "https://bestbuy.com" + inner_link["link"]["url"]
                            )
                else:
                    if link["link"].get("url"):
                        self.list_of_links.append(
                            "https://bestbuy.com" + link["link"]["url"]
                        )
