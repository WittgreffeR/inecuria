# Failed Imports Service

A web service for visualizing failed data imports across all the ESG Data APIs.

## High Level Requirements

- API Endpoint that Import Processes can call to notify that a "asset" has failed to import & why
- Dashboard to display all failed imports across our Data APIs
- An asset that fails to import for the same reason will only appear ONCE in the results, we just update the date/time
- Track this over a certain period of time - failed imports older 7* days, we don't care about
- Authenticated with Gatekeeper
- OPTIONAL: Every 24 hours* we want to send an email report to a list of people detailing the failed imports and why

## Technical Implementation

- Django for the database interaction & website
- Django REST Framework for the API endpoint
- PostgreSQL for the database engine
- Terraform to provision infrastructure
- Helm charts to run the deployment
- GitLab to perform the deployment

## API Request

### What We Want

`PUT` `/api/failed-imports/`
``` json
{
    "id": "{id goes here}",
    "name": "{human readable 'name' goes here}",
    "reason": "{reason for failure goes here}"
}
```

### Example Request

`PUT` `/api/failed-imports/`
``` json
{
    "id": "asi-chain-of-custody-standard-a33efa63",
    "name": "ASI Chain of Custody Standard",
    "reason": "ASI Chain of Custody Standard: Scheme Holder"
}
```

# Notes
- The styling for the email table is separate to the styling for the site. If changes are made to the site, make sure to update the table styling so the two are consistent.
