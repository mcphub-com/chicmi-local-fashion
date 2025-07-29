import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/chicmi/api/chicmi-local-fashion'

mcp = FastMCP('chicmi-local-fashion')

@mcp.tool()
def get_fashion_events_in_city(city: Annotated[str, Field(description='The city to query. Values are currently "london", "glasgow", "edinburgh" or "manchester"')],
                               days: Annotated[Union[int, float, None], Field(description='Show events from today to X days in the future. Either this or a static date range is required. If a static date range is provided, days is ignored. Default: 5')] = None,
                               date_from: Annotated[Union[str, None], Field(description='If specifying a static date range, the from date, in "yyyy/mm/dd" format')] = None,
                               date_to: Annotated[Union[str, None], Field(description='If specifying a static date range, the to date, in "yyyy/mm/dd" format')] = None,
                               sectors: Annotated[Union[str, None], Field(description='Filter events by sectors. Values are "luxury", "designer", "high-street", "independent". Comma separated list. Leave blank for all sectors.')] = None,
                               types: Annotated[Union[str, None], Field(description='Filter events by event type. Values are "brand-sales" ,"sample-sales", "vintage-sales", "in-store-events", "exhibitions", "parties-and-awards", "talks-and-plays", "trade-shows", "bridal-sales". Comma separated list. Leave blank for all types.')] = None,
                               designers: Annotated[Union[str, None], Field(description='Filter events by designer, such as "chanel", "dior", "gucci". Check the designer URL on Chicmi.com for values. Comma separated list. Leave blank for all designers.')] = None,
                               stores: Annotated[Union[str, None], Field(description='Filter events by a particular store, such as "200" = Harrods. Check the store URL on Chicmi for values. Comma separated list. Leave blank for all stores.')] = None,
                               max_results: Annotated[Union[int, float, None], Field(description='The maximum number of results to return. Leaving this parameter off or providing 0 will return all results. Default: 3')] = None) -> dict: 
    '''Get all fashion events in a particular city'''
    url = 'https://chicmi.p.rapidapi.com/calendar_in_city/'
    headers = {'x-rapidapi-host': 'chicmi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'city': city,
        'days': days,
        'date_from': date_from,
        'date_to': date_to,
        'sectors': sectors,
        'types': types,
        'designers': designers,
        'stores': stores,
        'max_results': max_results,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
