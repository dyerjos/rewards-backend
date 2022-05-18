class should be called Transaction
- payer -> string
- available_points -> integer
- (redeemed_points -> integer)
- timestamp -> date
- (user -> foreign key)

class called User
- created_by -> date
- last_updated -> date
- (total_point_balance -> integer) or make this a property of the model
have a one-to-many relationship with payers

User can earn and spend points

When spending:
- oldest transaction points get spent first
- payer points can never go below zero

make a spend_points endpoint, earn_points endpoint, and points balance route

earn_points route:
- POST
- must provide payer, points, timestamp fields
{ "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" }
- the back end updates balances for each payer for the user if the date is validated (won't bring balance below zero)
- return a response to the front end

spend_points route:
- PUT
- must provide points field
{ "points": 5000 }
- return payer and and points for each transaction redeemed
[
    { "payer": "DANNON", "points": -100 },
    { "payer": "UNILEVER", "points": -200 },
    { "payer": "MILLER COORS", "points": -4,700 }
]

points_balance route:
- GET
- return balance for each payer
{
    "DANNON": 1000,
    "UNILEVER": 0,
    "MILLER COORS": 5300
}
