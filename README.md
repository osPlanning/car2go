car2go
======

Scripts for interfacing with Car2Go's API.

This script downloads all available (un-rented) Car2Go vehicles for user-specified regions and a given time interval. 

To run the script, users must first register for a Car2Go API account: https://code.google.com/p/car2go/wiki/index_v2_1. 

Car2Go restricts data collection for "tracking" purposes, so please follow the legal guidelines and beware that
Car2Go could reject your access request if it believes you may be using the data for overly-intrusive purposes. 

Our purposes are not specifically to track vehicles, but to understand aggregate fleet usage and vehicle availability 
over time and space in context of other transportation options. Car2Go provides a dimension of mobility that we hope to
measure and possibly integrate within our regional modeling and planning efforts.

Potential uses:

This data could help us infer trip tables for car-sharing. These trips are rarely captured at statistically significant rates from basic travel surveys, but this approach allows us to gather numerous trips at different times of day, for long periods of time. Trip origins and destinations can be inferred from where vehicles dissapear and reappear from the dataset. At finer collection intervals, travel times could be estimated as well.

Data might also tell us how Car2Go coverage affects mobility and accessibility for certain neighborhoods at different times of day. Are vehicles being used as a replacement to existing transit service (and thus competing) or is the service fostering more zero-car (by choice) households? Single-point data collection or stated-preference surveys do not provide the depth that this data provides for these kinds of analyses. 

What other interesting applications can we try? Please comment on potential uses!
