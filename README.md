markdown
# Chicmi Local Fashion MCP Server

Welcome to the **Chicmi Local Fashion** MCP server! This server is designed to provide access to a unique set of fashion data, focusing on the vibrant fashion scenes in some of the world's most renowned fashion cities, including London, Glasgow, Edinburgh, and Manchester.

## What This Server Does

The Chicmi Local Fashion MCP server is your go-to resource for discovering the latest happenings in the fashion industry within these cities. Whether you're interested in fashion sales, sample sales, exhibitions, or events, this server has you covered. It offers a RESTful JSON API that does not require any authentication, making it easy to access and use.

### Key Data Types

The server provides data categorized into three main types:

- **Stores**: Information about fashion stores located at specific addresses.
- **Events**: Fashion-related events such as exhibitions, trade shows, or VIP events. These can occur at a store or any other location.
- **Sales**: Fashion sales taking place either at a specific store or address. As sales are a subset of events, they share many common properties.

## Tools and Usage

The Chicmi Local Fashion MCP server offers tools to help users acquire specific information about fashion events, sales, or stores in their desired city. Here's a brief overview of the available tool and its usage:

### Tool: Get Fashion Events in City

- **Function Name**: `get_fashion_events_in_city`
- **Description**: Retrieve all fashion events happening in a particular city.
- **Parameters**:
  - **city**: The city you want to query. Acceptable values are "london", "glasgow", "edinburgh", or "manchester".
  - **days**: (Optional) Number of days from today to show events. Either this or a static date range is required. Default is 5 days.
  - **date_from**: (Optional) Start date for a static date range, in "yyyy/mm/dd" format.
  - **date_to**: (Optional) End date for a static date range, in "yyyy/mm/dd" format.
  - **sectors**: (Optional) Filter events by sectors (e.g., "luxury", "designer"). Use a comma-separated list or leave blank for all sectors.
  - **types**: (Optional) Filter events by event type (e.g., "brand-sales", "exhibitions"). Use a comma-separated list or leave blank for all types.
  - **designers**: (Optional) Filter events by designer names (e.g., "chanel", "dior"). Use a comma-separated list or leave blank for all designers.
  - **stores**: (Optional) Filter events by store identifiers (e.g., "200" for Harrods). Use a comma-separated list or leave blank for all stores.
  - **max_results**: (Optional) Maximum number of results to return. Default is 3 results if not specified.

## Feedback

We welcome your feedback and suggestions to improve the Chicmi Local Fashion MCP server. Feel free to contact us at [team@chicmi.com](mailto:team@chicmi.com).