import pandas as pd
import random

import display


def launch():
    # TODO: Read and choose a random item from the 'auction_item.csv' file
    auction_items = readfile()

    # TODO: Event closes after a random number of items have been auctioned.
    event = random.choice(range(1, len(auction_items)))
    event_open = True
    auction_log = {}

    # TODO: Execute event until the event closes.
    while event_open:
        auction_item = random.choice(list(auction_items))
        print(f'\nAuction Item: {auction_item["Auction Item"]}')
        auction_log[auction_item["Auction Item"]] = (execute_bidding(auction_item["Auction Item"], auction_item["Cost"]))
        event -= 1
        if event == 0:
            event_open = False
            # TODO: Close the event and print out the event log.
            print(display.logo)
            print("\nAuction is closed for the day. Thank you for participating.")
            print(f"Today's Auction Log: ")
            for k, v in auction_log.items():
                print("\t", k)
                for key, val in v.items():
                    print("\t\t", key, val)
        else:
            print('Next item on the Auction is: ')


def execute_bidding(auction_item, actual_cost):
    bid_again = True
    auction_participants = {}
    while bid_again:
        if len(auction_participants) < 1 and input("\nWould anyone like to start the bid? Type 'yes' or 'no': ") == 'no':
            print(f'No bids for {auction_item}. We will move on to the next item.')
            bid_again = False
        else:
            name = input("What is your name?: ")
            bid = int(input("what is your bid?: $"))
            auction_participants[name] = bid
            if input(f"\nAre there any other bidders for {auction_item}? Type 'yes' or 'no': ") == 'no':
                bid_again = False

    if len(auction_participants) == 0:
        return {"Winner": "N/A", "Bid": "N/A", "Actual Value": f'${actual_cost}'}
    else:
        winner = ''
        largest_bid = 0
        for participant in auction_participants:
            if auction_participants[participant] > largest_bid:
                largest_bid = auction_participants[participant]
                winner = participant
        print(display.logo)
        print(f'\t{auction_item} Sold! \nThe winner for this round is {winner}, with a bid of ${largest_bid}.')
        return {"Winner": winner, "Bid": f'${largest_bid}', "Actual Value": f'${actual_cost}'}


def readfile():
    file = pd.read_csv("auction_item.csv")
    return file.to_dict("records")
