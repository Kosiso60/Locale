# LOCALE

Welcome to the Locale API documentation. Locale is a developer tool that provides information about Nigeria's regions, states, and local government areas (LGAs). This API allows developers to access metadata and search for information based on regions, states, and LGAs.

## Authentication and Authorization

All requests to the Locale API must be authenticated.

### API Key

To authenticate your requests, include the following header in your HTTP requests:

Authorization: Bearer {API_KEY}


## Endpoints

### Search Regions

Get information about regions in Nigeria.

# GET /api/regions


### Search States

Get information about states in Nigeria.

## GET /api/states


### Search LGAs

Get information about local government areas (LGAs) in Nigeria.

* GET /api/lgas


### Get All Regions

Get all regions in Nigeria.

** GET /api/regions/all
